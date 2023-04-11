# openapi_client.model.traffic_control_data.TrafficControlData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**tcId** | str,  | str,  |  | [optional] 
**flowStatus** | [**FlowStatus**](FlowStatus.md) | [**FlowStatus**](FlowStatus.md) |  | [optional] 
**redirectInfo** | [**RedirectInformation**](RedirectInformation.md) | [**RedirectInformation**](RedirectInformation.md) |  | [optional] 
**[addRedirectInfo](#addRedirectInfo)** | list, tuple,  | tuple,  |  | [optional] 
**muteNotif** | bool,  | BoolClass,  |  | [optional] 
**trafficSteeringPolIdDl** | None, str,  | NoneClass, str,  |  | [optional] 
**trafficSteeringPolIdUl** | None, str,  | NoneClass, str,  |  | [optional] 
**[routeToLocs](#routeToLocs)** | list, tuple,  | tuple,  |  | [optional] 
**traffCorreInd** | bool,  | BoolClass,  |  | [optional] 
**upPathChgEvent** | [**UpPathChgEvent**](UpPathChgEvent.md) | [**UpPathChgEvent**](UpPathChgEvent.md) |  | [optional] 
**steerFun** | [**SteeringFunctionality**](SteeringFunctionality.md) | [**SteeringFunctionality**](SteeringFunctionality.md) |  | [optional] 
**steerModeDl** | [**SteeringMode**](SteeringMode.md) | [**SteeringMode**](SteeringMode.md) |  | [optional] 
**steerModeUl** | [**SteeringMode**](SteeringMode.md) | [**SteeringMode**](SteeringMode.md) |  | [optional] 
**mulAccCtrl** | [**MulticastAccessControl**](MulticastAccessControl.md) | [**MulticastAccessControl**](MulticastAccessControl.md) |  | [optional] 
**snssaiList** | [**SnssaiList**](SnssaiList.md) | [**SnssaiList**](SnssaiList.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# addRedirectInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RedirectInformation**](RedirectInformation.md) | [**RedirectInformation**](RedirectInformation.md) | [**RedirectInformation**](RedirectInformation.md) |  | 

# routeToLocs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RouteToLocation**](RouteToLocation.md) | [**RouteToLocation**](RouteToLocation.md) | [**RouteToLocation**](RouteToLocation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

