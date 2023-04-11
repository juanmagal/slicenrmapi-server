# openapi_client.model.redirect_address_type.RedirectAddressType

Possible values are - IPV4_ADDR: Indicates that the address type is in the form of \"dotted-decimal\" IPv4 address. - IPV6_ADDR: Indicates that the address type is in the form of IPv6 address. - URL: Indicates that the address type is in the form of Uniform Resource Locator. - SIP_URI: Indicates that the address type is in the form of SIP Uniform Resource Identifier. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Possible values are - IPV4_ADDR: Indicates that the address type is in the form of \&quot;dotted-decimal\&quot; IPv4 address. - IPV6_ADDR: Indicates that the address type is in the form of IPv6 address. - URL: Indicates that the address type is in the form of Uniform Resource Locator. - SIP_URI: Indicates that the address type is in the form of SIP Uniform Resource Identifier.  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["IPV4_ADDR", "IPV6_ADDR", "URL", "SIP_URI", ] 
[any_of_1](#any_of_1) | str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["IPV4_ADDR", "IPV6_ADDR", "URL", "SIP_URI", ] 

# any_of_1

This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | This string provides forward-compatibility with future extensions to the enumeration but is not used to encode content defined in the present version of this API.  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

