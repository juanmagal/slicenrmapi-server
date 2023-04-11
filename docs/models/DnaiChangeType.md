# openapi_client.model.dnai_change_type.DnaiChangeType

Possible values are: - EARLY: Early notification of UP path reconfiguration. - EARLY_LATE: Early and late notification of UP path reconfiguration. This value shall   only be present in the subscription to the DNAI change event. - LATE: Late notification of UP path reconfiguration.  

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Possible values are: - EARLY: Early notification of UP path reconfiguration. - EARLY_LATE: Early and late notification of UP path reconfiguration. This value shall   only be present in the subscription to the DNAI change event. - LATE: Late notification of UP path reconfiguration.   | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["EARLY", "EARLY_LATE", "LATE", ] 
[any_of_1](#any_of_1) | str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode  content defined in the present version of this API.   | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["EARLY", "EARLY_LATE", "LATE", ] 

# any_of_1

This string provides forward-compatibility with future extensions to the enumeration but is not used to encode  content defined in the present version of this API.  

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode  content defined in the present version of this API.   | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

