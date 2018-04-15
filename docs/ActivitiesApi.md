# strava_api_v3.ActivitiesApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity**](ActivitiesApi.md#create_activity) | **POST** /activities | Create an Activity
[**get_activity_by_id**](ActivitiesApi.md#get_activity_by_id) | **GET** /activities/{id} | Get Activity
[**get_comments_by_activity_id**](ActivitiesApi.md#get_comments_by_activity_id) | **GET** /activities/{id}/comments | List Activity Comments
[**get_kudoers_by_activity_id**](ActivitiesApi.md#get_kudoers_by_activity_id) | **GET** /activities/{id}/kudos | List Activity Kudoers
[**get_laps_by_activity_id**](ActivitiesApi.md#get_laps_by_activity_id) | **GET** /activities/{id}/laps | List Activity Laps
[**get_logged_in_athlete_activities**](ActivitiesApi.md#get_logged_in_athlete_activities) | **GET** /athlete/activities | List Athlete Activities
[**get_zones_by_activity_id**](ActivitiesApi.md#get_zones_by_activity_id) | **GET** /activities/{id}/zones | Get Activity Zones
[**update_activity_by_id**](ActivitiesApi.md#update_activity_by_id) | **PUT** /activities/{id} | Update Activity


# **create_activity**
> DetailedActivity create_activity(name, type, start_date_local, elapsed_time, description=description, distance=distance, private=private, trainer=trainer, photo_ids=photo_ids, commute=commute)

Create an Activity

Creates a manual activity for an athlete. Requires write permissions, as requested during the authorization process.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
name = 'name_example' # str | The name of the activity.
type = 'type_example' # str | Type of activity. For example - Run, Ride etc.
start_date_local = 'start_date_local_example' # str | ISO 8601 formatted date time.
elapsed_time = 56 # int | In seconds.
description = 'description_example' # str | Description of the activity. (optional)
distance = 'distance_example' # str | In meters. (optional)
private = 56 # int | set to 1 to mark the resulting activity as private, ‘view_private’ permissions will be necessary to view the activity. If not specified, set according to the athlete’s privacy setting (recommended). (optional)
trainer = 56 # int | Set to 1 to mark as a trainer activity. (optional)
photo_ids = 'photo_ids_example' # str | List of native photo ids to attach to the activity. (optional)
commute = 56 # int | Set to 1 to mark as commute. (optional)

try:
    # Create an Activity
    api_response = api_instance.create_activity(name, type, start_date_local, elapsed_time, description=description, distance=distance, private=private, trainer=trainer, photo_ids=photo_ids, commute=commute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->create_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the activity. | 
 **type** | **str**| Type of activity. For example - Run, Ride etc. | 
 **start_date_local** | **str**| ISO 8601 formatted date time. | 
 **elapsed_time** | **int**| In seconds. | 
 **description** | **str**| Description of the activity. | [optional] 
 **distance** | **str**| In meters. | [optional] 
 **private** | **int**| set to 1 to mark the resulting activity as private, ‘view_private’ permissions will be necessary to view the activity. If not specified, set according to the athlete’s privacy setting (recommended). | [optional] 
 **trainer** | **int**| Set to 1 to mark as a trainer activity. | [optional] 
 **photo_ids** | **str**| List of native photo ids to attach to the activity. | [optional] 
 **commute** | **int**| Set to 1 to mark as commute. | [optional] 

### Return type

[**DetailedActivity**](DetailedActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity_by_id**
> DetailedActivity get_activity_by_id(id, include_all_efforts=include_all_efforts)

Get Activity

Returns the given activity that is owned by the authenticated athlete.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the activity.
include_all_efforts = true # bool | To include all segments efforts. (optional)

try:
    # Get Activity
    api_response = api_instance.get_activity_by_id(id, include_all_efforts=include_all_efforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **include_all_efforts** | **bool**| To include all segments efforts. | [optional] 

### Return type

[**DetailedActivity**](DetailedActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comments_by_activity_id**
> list[Comment] get_comments_by_activity_id(id, page=page, per_page=per_page)

List Activity Comments

Returns the comments on the given activity.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the activity.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Activity Comments
    api_response = api_instance.get_comments_by_activity_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_comments_by_activity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[Comment]**](Comment.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kudoers_by_activity_id**
> list[SummaryAthlete] get_kudoers_by_activity_id(id, page=page, per_page=per_page)

List Activity Kudoers

Returns the athletes who kudoed an activity identified by an identifier.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 56 # int | The identifier of the activity.
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Activity Kudoers
    api_response = api_instance.get_kudoers_by_activity_id(id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_kudoers_by_activity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummaryAthlete]**](SummaryAthlete.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_laps_by_activity_id**
> list[Lap] get_laps_by_activity_id(id)

List Activity Laps

Returns the laps of an activity identified by an identifier.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the activity.

try:
    # List Activity Laps
    api_response = api_instance.get_laps_by_activity_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_laps_by_activity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 

### Return type

[**list[Lap]**](Lap.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_activities**
> list[SummaryActivity] get_logged_in_athlete_activities(before=before, after=after, page=page, per_page=per_page)

List Athlete Activities

Returns the activities of an athlete for a specific identifier.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
before = 56 # int | An epoch timestamp to use for filtering activities that have taken place before a certain time. (optional)
after = 56 # int | An epoch timestamp to use for filtering activities that have taken place after a certain time. (optional)
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Athlete Activities
    api_response = api_instance.get_logged_in_athlete_activities(before=before, after=after, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_logged_in_athlete_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| An epoch timestamp to use for filtering activities that have taken place before a certain time. | [optional] 
 **after** | **int**| An epoch timestamp to use for filtering activities that have taken place after a certain time. | [optional] 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummaryActivity]**](SummaryActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones_by_activity_id**
> list[ActivityZone] get_zones_by_activity_id(id)

Get Activity Zones

Premium Feature. Returns the zones of a given activity.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 56 # int | The identifier of the activity.

try:
    # Get Activity Zones
    api_response = api_instance.get_zones_by_activity_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->get_zones_by_activity_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 

### Return type

[**list[ActivityZone]**](ActivityZone.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity_by_id**
> DetailedActivity update_activity_by_id(id, body=body)

Update Activity

Updates the given activity that is owned by the authenticated athlete.

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
api_instance = strava_api_v3.ActivitiesApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the activity.
body = strava_api_v3.UpdatableActivity() # UpdatableActivity |  (optional)

try:
    # Update Activity
    api_response = api_instance.update_activity_by_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->update_activity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the activity. | 
 **body** | [**UpdatableActivity**](UpdatableActivity.md)|  | [optional] 

### Return type

[**DetailedActivity**](DetailedActivity.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

