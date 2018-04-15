# coding: utf-8

"""
    Strava API v3

    Strava API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from strava_api_v3.api_client import ApiClient


class AthletesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_logged_in_athlete(self, **kwargs):  # noqa: E501
        """Get Authenticated Athlete  # noqa: E501

        Returns the currently authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DetailedAthlete
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_logged_in_athlete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_logged_in_athlete_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_logged_in_athlete_with_http_info(self, **kwargs):  # noqa: E501
        """Get Authenticated Athlete  # noqa: E501

        Returns the currently authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: DetailedAthlete
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_logged_in_athlete" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/athlete', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedAthlete',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_logged_in_athlete_zones(self, **kwargs):  # noqa: E501
        """Get Zones  # noqa: E501

        Returns the the authenticated athlete's heart rate and power zones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_zones(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Zones
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_logged_in_athlete_zones_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_logged_in_athlete_zones_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_logged_in_athlete_zones_with_http_info(self, **kwargs):  # noqa: E501
        """Get Zones  # noqa: E501

        Returns the the authenticated athlete's heart rate and power zones.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_zones_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: Zones
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_logged_in_athlete_zones" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/athlete/zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Zones',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stats(self, id, **kwargs):  # noqa: E501
        """Get Athlete Stats  # noqa: E501

        Returns the activity stats of an athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stats(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the athlete. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: ActivityStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_stats_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_stats_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Athlete Stats  # noqa: E501

        Returns the activity stats of an athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stats_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the athlete. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: ActivityStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/athletes/{id}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActivityStats',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_logged_in_athlete(self, body, **kwargs):  # noqa: E501
        """Update Athlete  # noqa: E501

        Update the currently authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_logged_in_athlete(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DetailedAthlete body: The athlete entity to update. (required)
        :return: DetailedAthlete
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_logged_in_athlete_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_logged_in_athlete_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_logged_in_athlete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update Athlete  # noqa: E501

        Update the currently authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_logged_in_athlete_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param DetailedAthlete body: The athlete entity to update. (required)
        :return: DetailedAthlete
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_logged_in_athlete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_logged_in_athlete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/athlete', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedAthlete',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)