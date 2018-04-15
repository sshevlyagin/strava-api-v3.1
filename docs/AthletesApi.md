# strava_api_v3.AthletesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logged_in_athlete**](AthletesApi.md#get_logged_in_athlete) | **GET** /athlete | Get Authenticated Athlete
[**get_logged_in_athlete_zones**](AthletesApi.md#get_logged_in_athlete_zones) | **GET** /athlete/zones | Get Zones
[**get_stats**](AthletesApi.md#get_stats) | **GET** /athletes/{id}/stats | Get Athlete Stats
[**update_logged_in_athlete**](AthletesApi.md#update_logged_in_athlete) | **PUT** /athlete | Update Athlete


# **get_logged_in_athlete**
> DetailedAthlete get_logged_in_athlete()

Get Authenticated Athlete

Returns the currently authenticated athlete.

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
api_instance = strava_api_v3.AthletesApi(strava_api_v3.ApiClient(configuration))

try:
    # Get Authenticated Athlete
    api_response = api_instance.get_logged_in_athlete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->get_logged_in_athlete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DetailedAthlete**](DetailedAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_zones**
> Zones get_logged_in_athlete_zones()

Get Zones

Returns the the authenticated athlete's heart rate and power zones.

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
api_instance = strava_api_v3.AthletesApi(strava_api_v3.ApiClient(configuration))

try:
    # Get Zones
    api_response = api_instance.get_logged_in_athlete_zones()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->get_logged_in_athlete_zones: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Zones**](Zones.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> ActivityStats get_stats(id, page=page, per_page=per_page)

Get Athlete Stats

Returns the activity stats of an athlete.

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
api_instance = strava_api_v3.AthletesApi(strava_api_v3.ApiClient(configuration))
id = 56 # int | The identifier of the athlete.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # Get Athlete Stats
    api_response = api_instance.get_stats(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the athlete. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**ActivityStats**](ActivityStats.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_logged_in_athlete**
> DetailedAthlete update_logged_in_athlete(body)

Update Athlete

Update the currently authenticated athlete.

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
api_instance = strava_api_v3.AthletesApi(strava_api_v3.ApiClient(configuration))
body = strava_api_v3.DetailedAthlete() # DetailedAthlete | The athlete entity to update.

try:
    # Update Athlete
    api_response = api_instance.update_logged_in_athlete(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AthletesApi->update_logged_in_athlete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DetailedAthlete**](DetailedAthlete.md)| The athlete entity to update. | 

### Return type

[**DetailedAthlete**](DetailedAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

