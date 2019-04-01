from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import pytest
import requests

class TestLiveServer(StaticLiveServerTestCase):

    def test_server_is_reachable(self):
        r = requests.get(self.live_server_url+"/api/v1")
        assert r.status_code == 200
