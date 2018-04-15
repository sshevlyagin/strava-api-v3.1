# strava_api_v3.RoutesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_route_by_id**](RoutesApi.md#get_route_by_id) | **GET** /routes/{id} | Get Route
[**get_routes_by_athlete_id**](RoutesApi.md#get_routes_by_athlete_id) | **GET** /athletes/{id}/routes | List Athlete Routes


# **get_route_by_id**
> Route get_route_by_id(id)

Get Route

Returns a route using its identifier.

### Example
```python
from __future__ import print_function
import time
import strava_api_v3
from strava_api_v3.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = strava_api_v3.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = strava_api_v3.RoutesApi(strava_api_v3.ApiClient(configuration))
id = 56 # int | The identifier of the route.

try:
    # Get Route
    api_response = api_instance.get_route_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->get_route_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the route. | 

### Return type

[**Route**](Route.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routes_by_athlete_id**
> list[Route] get_routes_by_athlete_id(id, page=page, per_page=per_page)

List Athlete Routes

Returns a list of the routes created by the authenticated athlete using their athlete ID.

### Example
```python
from __future__ import print_function
import time
import strava_api_v3
from strava_api_v3.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: strava_oauth
configuration = strava_api_v3.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = strava_api_v3.RoutesApi(strava_api_v3.ApiClient(configuration))
id = 56 # int | The identifier of the athlete.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Athlete Routes
    api_response = api_instance.get_routes_by_athlete_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->get_routes_by_athlete_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the athlete. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[Route]**](Route.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

