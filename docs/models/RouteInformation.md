# openapi_client.model.route_information.RouteInformation

At least one of the \"ipv4Addr\" attribute and the \"ipv6Addr\" attribute shall be included in the \"RouteInformation\" data type.  

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | At least one of the \&quot;ipv4Addr\&quot; attribute and the \&quot;ipv6Addr\&quot; attribute shall be included in the \&quot;RouteInformation\&quot; data type.   | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**portNumber** | [**Uinteger**](Uinteger.md) | [**Uinteger**](Uinteger.md) |  | 
**ipv4Addr** | [**Ipv4Addr1**](Ipv4Addr1.md) | [**Ipv4Addr1**](Ipv4Addr1.md) |  | [optional] 
**ipv6Addr** | [**Ipv6Addr1**](Ipv6Addr1.md) | [**Ipv6Addr1**](Ipv6Addr1.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

