# openapi_client.model.redirect_information.RedirectInformation

Contains the redirect information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains the redirect information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**redirectEnabled** | bool,  | BoolClass,  | Indicates the redirect is enable. | [optional] 
**redirectAddressType** | [**RedirectAddressType**](RedirectAddressType.md) | [**RedirectAddressType**](RedirectAddressType.md) |  | [optional] 
**redirectServerAddress** | str,  | str,  | Indicates the address of the redirect server. If \&quot;redirectAddressType\&quot; attribute indicates the IPV4_ADDR, the encoding is the same as the Ipv4Addr data type defined in 3GPP TS 29.571.If \&quot;redirectAddressType\&quot; attribute indicates the IPV6_ADDR, the encoding is the same as the Ipv6Addr data type defined in 3GPP TS 29.571.If \&quot;redirectAddressType\&quot; attribute indicates the URL or SIP_URI, the encoding is the same as the Uri data type defined in 3GPP TS 29.571.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

