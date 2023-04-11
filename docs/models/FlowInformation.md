# openapi_client.model.flow_information.FlowInformation

Contains the flow information.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains the flow information. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**flowDescription** | str,  | str,  | Defines a packet filter for an IP flow. | [optional] 
**ethFlowDescription** | [**EthFlowDescription**](EthFlowDescription.md) | [**EthFlowDescription**](EthFlowDescription.md) |  | [optional] 
**packFiltId** | str,  | str,  | An identifier of packet filter. | [optional] 
**packetFilterUsage** | bool,  | BoolClass,  | The packet shall be sent to the UE. | [optional] 
**tosTrafficClass** | None, str,  | NoneClass, str,  | Contains the Ipv4 Type-of-Service and mask field or the Ipv6 Traffic-Class field and mask field. | [optional] 
**spi** | None, str,  | NoneClass, str,  | the security parameter index of the IPSec packet. | [optional] 
**flowLabel** | None, str,  | NoneClass, str,  | the Ipv6 flow label header field. | [optional] 
**flowDirection** | [**FlowDirectionRm**](FlowDirectionRm.md) | [**FlowDirectionRm**](FlowDirectionRm.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

