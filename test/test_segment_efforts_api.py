# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import strava_api_v3
from strava_api_v3.api.segment_efforts_api import SegmentEffortsApi  # noqa: E501
from strava_api_v3.rest import ApiException


class TestSegmentEffortsApi(unittest.TestCase):
    """SegmentEffortsApi unit test stubs"""

    def setUp(self):
        self.api = strava_api_v3.api.segment_efforts_api.SegmentEffortsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_efforts_by_segment_id(self):
        """Test case for get_efforts_by_segment_id

        List Segment Efforts  # noqa: E501
        """
        pass

    def test_get_segment_effort_by_id(self):
        """Test case for get_segment_effort_by_id

        Get Segment Effort  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
