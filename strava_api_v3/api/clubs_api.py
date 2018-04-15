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


class ClubsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_club_activities_by_id(self, id, **kwargs):  # noqa: E501
        """List Club Activities  # noqa: E501

        Retrieve recent activities from members of a specific club. The authenticated athlete must belong to the requested club in order to hit this endpoint. Pagination is supported. Enhanced Privacy Mode is respected for all activities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_activities_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryActivity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_club_activities_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_club_activities_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_club_activities_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Club Activities  # noqa: E501

        Retrieve recent activities from members of a specific club. The authenticated athlete must belong to the requested club in order to hit this endpoint. Pagination is supported. Enhanced Privacy Mode is respected for all activities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_activities_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryActivity]
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
                    " to method get_club_activities_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_club_activities_by_id`")  # noqa: E501

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
            '/clubs/{id}/activities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummaryActivity]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_club_admins_by_id(self, id, **kwargs):  # noqa: E501
        """List Club Administrators.  # noqa: E501

        Returns a list of the administrators of a given club.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_admins_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryAthlete]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_club_admins_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_club_admins_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_club_admins_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Club Administrators.  # noqa: E501

        Returns a list of the administrators of a given club.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_admins_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryAthlete]
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
                    " to method get_club_admins_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_club_admins_by_id`")  # noqa: E501

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
            '/clubs/{id}/admins', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummaryAthlete]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_club_by_id(self, id, **kwargs):  # noqa: E501
        """Get Club  # noqa: E501

        Returns a given club using its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :return: DetailedClub
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_club_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_club_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_club_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Club  # noqa: E501

        Returns a given club using its identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :return: DetailedClub
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_club_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_club_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/clubs/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedClub',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_club_members_by_id(self, id, **kwargs):  # noqa: E501
        """List Club Members  # noqa: E501

        Returns a list of the athletes who are members of a given club.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_members_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryAthlete]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_club_members_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_club_members_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_club_members_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Club Members  # noqa: E501

        Returns a list of the athletes who are members of a given club.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_club_members_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryAthlete]
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
                    " to method get_club_members_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_club_members_by_id`")  # noqa: E501

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
            '/clubs/{id}/members', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummaryAthlete]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_logged_in_athlete_clubs(self, **kwargs):  # noqa: E501
        """List Athlete Clubs  # noqa: E501

        Returns a list of the clubs whose membership includes the authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_clubs(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryClub]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_logged_in_athlete_clubs_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_logged_in_athlete_clubs_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_logged_in_athlete_clubs_with_http_info(self, **kwargs):  # noqa: E501
        """List Athlete Clubs  # noqa: E501

        Returns a list of the clubs whose membership includes the authenticated athlete.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_logged_in_athlete_clubs_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[SummaryClub]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_logged_in_athlete_clubs" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/athlete/clubs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SummaryClub]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def join_club_by_id(self, id, **kwargs):  # noqa: E501
        """Join Club  # noqa: E501

        Adds the authenticated athlete to the club's membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.join_club_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :return: MembershipApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.join_club_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.join_club_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def join_club_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Join Club  # noqa: E501

        Adds the authenticated athlete to the club's membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.join_club_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :return: MembershipApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method join_club_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `join_club_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/clubs/{id}/join', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MembershipApplication',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def leave_club_by_id(self, id, **kwargs):  # noqa: E501
        """Leave Club  # noqa: E501

        Removes the authenticated athlete from the club's membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.leave_club_by_id(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :return: MembershipApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.leave_club_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.leave_club_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def leave_club_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Leave Club  # noqa: E501

        Removes the authenticated athlete from the club's membership.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.leave_club_by_id_with_http_info(id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int id: The identifier of the club. (required)
        :return: MembershipApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method leave_club_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `leave_club_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/clubs/{id}/leave', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MembershipApplication',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
