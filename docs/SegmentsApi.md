# strava_api_v3.SegmentsApi

All URIs are relative to *https://www.strava.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**explore_segments**](SegmentsApi.md#explore_segments) | **GET** /segments/explore | Explore segments
[**get_leaderboard_by_segment_id**](SegmentsApi.md#get_leaderboard_by_segment_id) | **GET** /segments/{id}/leaderboard | Get Segment Leaderboard
[**get_logged_in_athlete_starred_segments**](SegmentsApi.md#get_logged_in_athlete_starred_segments) | **GET** /segments/starred | List Starred Segments
[**get_segment_by_id**](SegmentsApi.md#get_segment_by_id) | **GET** /segments/{id} | Get Segment
[**star_segment**](SegmentsApi.md#star_segment) | **PUT** /segments/{id}/starred | Star Segment


# **explore_segments**
> ExplorerResponse explore_segments(bounds, activity_type=activity_type, min_cat=min_cat, max_cat=max_cat)

Explore segments

Returns the segments matching a specified query.

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
api_instance = strava_api_v3.SegmentsApi(strava_api_v3.ApiClient(configuration))
bounds = [3.4] # list[float] | The geographical boundaries of the search.
activity_type = 'activity_type_example' # str | Desired activity type. (optional)
min_cat = 56 # int | The minimum climbing category. (optional)
max_cat = 56 # int | The maximum climbing category. (optional)

try:
    # Explore segments
    api_response = api_instance.explore_segments(bounds, activity_type=activity_type, min_cat=min_cat, max_cat=max_cat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->explore_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bounds** | [**list[float]**](float.md)| The geographical boundaries of the search. | 
 **activity_type** | **str**| Desired activity type. | [optional] 
 **min_cat** | **int**| The minimum climbing category. | [optional] 
 **max_cat** | **int**| The maximum climbing category. | [optional] 

### Return type

[**ExplorerResponse**](ExplorerResponse.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboard_by_segment_id**
> SegmentLeaderboard get_leaderboard_by_segment_id(id, gender=gender, age_group=age_group, weight_class=weight_class, following=following, club_id=club_id, date_range=date_range, context_entries=context_entries, page=page, per_page=per_page)

Get Segment Leaderboard

Returns the specified segment leaderboard.

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
api_instance = strava_api_v3.SegmentsApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the segment leaderboard.
gender = 'gender_example' # str | Filter by gender. (optional)
age_group = 'age_group_example' # str | Premium Feature. Filter by age group. (optional)
weight_class = 'weight_class_example' # str | Premium Feature. Filter by weight class. (optional)
following = true # bool | Filter by friends of the authenticated athlete. (optional)
club_id = 789 # int | Filter by club. (optional)
date_range = 'date_range_example' # str | Filter by date range. (optional)
context_entries = 56 # int |  (optional)
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # Get Segment Leaderboard
    api_response = api_instance.get_leaderboard_by_segment_id(id, gender=gender, age_group=age_group, weight_class=weight_class, following=following, club_id=club_id, date_range=date_range, context_entries=context_entries, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_leaderboard_by_segment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment leaderboard. | 
 **gender** | **str**| Filter by gender. | [optional] 
 **age_group** | **str**| Premium Feature. Filter by age group. | [optional] 
 **weight_class** | **str**| Premium Feature. Filter by weight class. | [optional] 
 **following** | **bool**| Filter by friends of the authenticated athlete. | [optional] 
 **club_id** | **int**| Filter by club. | [optional] 
 **date_range** | **str**| Filter by date range. | [optional] 
 **context_entries** | **int**|  | [optional] 
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**SegmentLeaderboard**](SegmentLeaderboard.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logged_in_athlete_starred_segments**
> list[SummarySegment] get_logged_in_athlete_starred_segments(page=page, per_page=per_page)

List Starred Segments

List of the authenticated athlete's starred segments.

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
api_instance = strava_api_v3.SegmentsApi(strava_api_v3.ApiClient(configuration))
page = 56 # int | Page number. (optional)
per_page = 30 # int | Number of items per page. Defaults to 30. (optional) (default to 30)

try:
    # List Starred Segments
    api_response = api_instance.get_logged_in_athlete_starred_segments(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_logged_in_athlete_starred_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number. | [optional] 
 **per_page** | **int**| Number of items per page. Defaults to 30. | [optional] [default to 30]

### Return type

[**list[SummarySegment]**](SummarySegment.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_segment_by_id**
> DetailedSegment get_segment_by_id(id)

Get Segment

Returns the specified segment.

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
api_instance = strava_api_v3.SegmentsApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the segment.

try:
    # Get Segment
    api_response = api_instance.get_segment_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_segment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment. | 

### Return type

[**DetailedSegment**](DetailedSegment.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **star_segment**
> DetailedSegment star_segment(id)

Star Segment

Stars the given segment for the authenticated athlete.

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
api_instance = strava_api_v3.SegmentsApi(strava_api_v3.ApiClient(configuration))
id = 789 # int | The identifier of the segment to star.

try:
    # Star Segment
    api_response = api_instance.star_segment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->star_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the segment to star. | 

### Return type

[**DetailedSegment**](DetailedSegment.md)

### Authorization

[strava_oauth](../README.md#strava_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

