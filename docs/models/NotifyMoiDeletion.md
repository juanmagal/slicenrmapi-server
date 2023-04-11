# openapi_client.model.notify_moi_deletion.NotifyMoiDeletion

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[NotificationHeader](NotificationHeader.md) | [**NotificationHeader**](NotificationHeader.md) | [**NotificationHeader**](NotificationHeader.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[correlatedNotifications](#correlatedNotifications)** | list, tuple,  | tuple,  |  | [optional] 
**additionalText** | str,  | str,  |  | [optional] 
**sourceIndicator** | [**SourceIndicator**](SourceIndicator.md) | [**SourceIndicator**](SourceIndicator.md) |  | [optional] 
**attributeList** | [**AttributeNameValuePairSet**](AttributeNameValuePairSet.md) | [**AttributeNameValuePairSet**](AttributeNameValuePairSet.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# correlatedNotifications

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CorrelatedNotification**](CorrelatedNotification.md) | [**CorrelatedNotification**](CorrelatedNotification.md) | [**CorrelatedNotification**](CorrelatedNotification.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

