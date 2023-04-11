# openapi_client.model.qos_data.QosData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**qosId** | str,  | str,  |  | [optional] 
**fiveQIValue** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**maxbrUl** | [**BitRateRm**](BitRateRm.md) | [**BitRateRm**](BitRateRm.md) |  | [optional] 
**maxbrDl** | [**BitRateRm**](BitRateRm.md) | [**BitRateRm**](BitRateRm.md) |  | [optional] 
**gbrUl** | [**BitRateRm**](BitRateRm.md) | [**BitRateRm**](BitRateRm.md) |  | [optional] 
**gbrDl** | [**BitRateRm**](BitRateRm.md) | [**BitRateRm**](BitRateRm.md) |  | [optional] 
**arp** | [**Arp**](Arp.md) | [**Arp**](Arp.md) |  | [optional] 
**qosNotificationControl** | bool,  | BoolClass,  |  | [optional] 
**reflectiveQos** | bool,  | BoolClass,  |  | [optional] 
**sharingKeyDl** | str,  | str,  |  | [optional] 
**sharingKeyUl** | str,  | str,  |  | [optional] 
**maxPacketLossRateDl** | [**PacketLossRateRm**](PacketLossRateRm.md) | [**PacketLossRateRm**](PacketLossRateRm.md) |  | [optional] 
**maxPacketLossRateUl** | [**PacketLossRateRm**](PacketLossRateRm.md) | [**PacketLossRateRm**](PacketLossRateRm.md) |  | [optional] 
**extMaxDataBurstVol** | [**ExtMaxDataBurstVolRm**](ExtMaxDataBurstVolRm.md) | [**ExtMaxDataBurstVolRm**](ExtMaxDataBurstVolRm.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

