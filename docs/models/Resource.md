# openapi_client.model.resource.Resource

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[one_of_1](#one_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | 
**objectClass** | str,  | str,  |  | [optional] 
**objectInstance** | str,  | str,  |  | [optional] 
**[attributes](#attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[any_string_name](#any_string_name)** | list, tuple,  | tuple,  | any string name can be used but the value must be the correct type | [optional] 

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ResourcesGenericNrm](ResourcesGenericNrm.md) | [**ResourcesGenericNrm**](ResourcesGenericNrm.md) | [**ResourcesGenericNrm**](ResourcesGenericNrm.md) |  | 
[ResourcesNrNrm](ResourcesNrNrm.md) | [**ResourcesNrNrm**](ResourcesNrNrm.md) | [**ResourcesNrNrm**](ResourcesNrNrm.md) |  | 
[Resources5gcNrm](Resources5gcNrm.md) | [**Resources5gcNrm**](Resources5gcNrm.md) | [**Resources5gcNrm**](Resources5gcNrm.md) |  | 
[ResourcesSliceNrm](ResourcesSliceNrm.md) | [**ResourcesSliceNrm**](ResourcesSliceNrm.md) | [**ResourcesSliceNrm**](ResourcesSliceNrm.md) |  | 
[ResourcesCoslaNrm](ResourcesCoslaNrm.md) | [**ResourcesCoslaNrm**](ResourcesCoslaNrm.md) | [**ResourcesCoslaNrm**](ResourcesCoslaNrm.md) |  | 
[ResourcesIntentNrm](ResourcesIntentNrm.md) | [**ResourcesIntentNrm**](ResourcesIntentNrm.md) | [**ResourcesIntentNrm**](ResourcesIntentNrm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

