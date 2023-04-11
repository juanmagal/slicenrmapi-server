# openapi_client.model.af_sig_protocol.AfSigProtocol

Possible values are - NO_INFORMATION: Indicate that no information about the AF signalling protocol is being provided.  - SIP: Indicate that the signalling protocol is Session Initiation Protocol. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Possible values are - NO_INFORMATION: Indicate that no information about the AF signalling protocol is being provided.  - SIP: Indicate that the signalling protocol is Session Initiation Protocol.  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["NO_INFORMATION", "SIP", ] 
[NullValue](NullValue.md) | [**NullValue**](NullValue.md) | [**NullValue**](NullValue.md) |  | 
[any_of_2](#any_of_2) | str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NO_INFORMATION", "SIP", ] 

# any_of_2

This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

