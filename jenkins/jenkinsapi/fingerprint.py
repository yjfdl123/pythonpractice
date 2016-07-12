from jenkinsapi.jenkinsbase import JenkinsBase
from jenkinsapi.exceptions import ArtifactBroken

import urllib2
import re

import logging

log = logging.getLogger( __name__ )

class Fingerprint(JenkinsBase):
    """
    Represents a jenkins fingerprint on a single artifact file ??
    """
    RE_MD5 = re.compile("^([0-9a-z]{32})$")

    def __init__(self, baseurl, id, jenkins_obj):
        logging.basicConfig()
        self.jenkins_obj = jenkins_obj
        assert self.RE_MD5.search( id ), "%s does not look like a valid id" % id
        url =  "%s/fingerprint/%s/" % ( baseurl, id  )
        JenkinsBase.__init__( self, url, poll=False )
        self.id = id

    def get_jenkins_obj(self):
        return self.jenkins_obj

    def __str__(self):
        return self.id

    def valid(self):
        """
        Return True / False if valid
        """
        try:
            self.poll()
        except urllib2.HTTPError:
            return False
        return True

    def validate_for_build(self, filename, job, build):
        if not self.valid():
            log.info("Unknown to jenkins.")
            return False
        if not self._data["original"] is None:
            if self._data["original"]["name"] == job:
                if self._data["original"]["number"] == build:
                    return True
        if self._data["fileName"] != filename:
            log.info("Filename from jenkins (%s) did not match provided (%s)" % ( self._data["fileName"], filename ) )
            return False
        for usage_item in self._data["usage"]:
            if usage_item["name"] == job:
                for range in usage_item["ranges"]["ranges"]:
                    if range["start"] <= build <= range["end"]:
                        log.info("This artifact was generated by %s between build %i and %i" % ( job, range["start"],  range["end"] ) )
                        return True
        return False

    def validate(self):
        try:
            assert self.valid()
        except AssertionError:
            raise ArtifactBroken( "Artifact %s seems to be broken, check %s" % ( self.id, self.baseurl ) )
        except urllib2.HTTPError:
            raise ArtifactBroken( "Unable to validate artifact id %s using %s" % ( self.id, self.baseurl ) )
        return True

    def get_info( self ):
        """
        Returns a tuple of build-name, build# and artifiact filename for a good build.
        """
        self.poll()
        return self._data["original"]["name"], self._data["original"]["number"], self._data["fileName"]
