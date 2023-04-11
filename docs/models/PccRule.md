# openapi_client.model.pcc_rule.PccRule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pccRuleId** | str,  | str,  | Univocally identifies the PCC rule within a PDU session. | [optional] 
**[flowInfoList](#flowInfoList)** | list, tuple,  | tuple,  |  | [optional] 
**applicationId** | str,  | str,  |  | [optional] 
**appDescriptor** | str,  | str,  | string with format &#x27;bytes&#x27; as defined in OpenAPI | [optional] 
**contentVersion** | decimal.Decimal, int,  | decimal.Decimal,  | Represents the content version of some content. | [optional] 
**precedence** | [**Uinteger**](Uinteger.md) | [**Uinteger**](Uinteger.md) |  | [optional] 
**afSigProtocol** | [**AfSigProtocol**](AfSigProtocol.md) | [**AfSigProtocol**](AfSigProtocol.md) |  | [optional] 
**isAppRelocatable** | bool,  | BoolClass,  |  | [optional] 
**isUeAddrPreserved** | bool,  | BoolClass,  |  | [optional] 
**[qosData](#qosData)** | list, tuple,  | tuple,  |  | [optional] 
**[altQosParams](#altQosParams)** | list, tuple,  | tuple,  |  | [optional] 
**[trafficControlData](#trafficControlData)** | list, tuple,  | tuple,  |  | [optional] 
**conditionData** | [**ConditionData**](ConditionData.md) | [**ConditionData**](ConditionData.md) |  | [optional] 
**tscaiInputDl** | [**TscaiInputContainer**](TscaiInputContainer.md) | [**TscaiInputContainer**](TscaiInputContainer.md) |  | [optional] 
**tscaiInputUl** | [**TscaiInputContainer**](TscaiInputContainer.md) | [**TscaiInputContainer**](TscaiInputContainer.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# flowInfoList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FlowInformation**](FlowInformation.md) | [**FlowInformation**](FlowInformation.md) | [**FlowInformation**](FlowInformation.md) |  | 

# qosData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**QosDataList**](QosDataList.md) | [**QosDataList**](QosDataList.md) | [**QosDataList**](QosDataList.md) |  | 

# altQosParams

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**QosDataList**](QosDataList.md) | [**QosDataList**](QosDataList.md) | [**QosDataList**](QosDataList.md) |  | 

# trafficControlData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TrafficControlDataList**](TrafficControlDataList.md) | [**TrafficControlDataList**](TrafficControlDataList.md) | [**TrafficControlDataList**](TrafficControlDataList.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

