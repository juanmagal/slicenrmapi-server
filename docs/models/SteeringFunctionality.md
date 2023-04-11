# openapi_client.model.steering_functionality.SteeringFunctionality

Possible values are   - MPTCP: Indicates that PCF authorizes the MPTCP functionality to support traffic steering, switching and splitting.   - ATSSS_LL: Indicates that PCF authorizes the ATSSS-LL functionality to support traffic steering, switching and splitting. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Possible values are   - MPTCP: Indicates that PCF authorizes the MPTCP functionality to support traffic steering, switching and splitting.   - ATSSS_LL: Indicates that PCF authorizes the ATSSS-LL functionality to support traffic steering, switching and splitting.  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["MPTCP", "ATSSS_LL", ] 
[any_of_1](#any_of_1) | str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["MPTCP", "ATSSS_LL", ] 

# any_of_1

This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

