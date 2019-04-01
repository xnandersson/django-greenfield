from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import pytest
import requests


class TestLiveServer(StaticLiveServerTestCase):

    def test_can_create_widget(self):
        data = {
            "display_name": "niklas",
        }
        ret_val = requests.post(self.live_server_url+"/api/v1/widgets/", json=data)
        assert ret_val.status_code == status.HTTP_201_CREATED
