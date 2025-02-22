# coding: utf-8

"""
    Endpoints

    Oyster uses OAuth2 to enable customers to grant access to their data to third party applications. Customers also need to use this API to authenticate themselves when making API requests.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import oyster_python_sdk
from oyster_python_sdk.paths.v1_time_off_entitlements import get
from oyster_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1TimeOffEntitlements(ApiTestMixin, unittest.TestCase):
    """
    V1TimeOffEntitlements unit test stubs
        Retrieve entitlements
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
