# openapi_client.model.sub_network_single.SubNetworkSingle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Top](Top.md) | [**Top**](Top.md) | [**Top**](Top.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[SubNetworkNcO](SubNetworkNcO.md) | [**SubNetworkNcO**](SubNetworkNcO.md) | [**SubNetworkNcO**](SubNetworkNcO.md) |  | 
[all_of_3](#all_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**attributes** | [**SubNetworkAttr**](SubNetworkAttr.md) | [**SubNetworkAttr**](SubNetworkAttr.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SubNetwork** | [**SubNetworkMultiple**](SubNetworkMultiple.md) | [**SubNetworkMultiple**](SubNetworkMultiple.md) |  | [optional] 
**ManagedElement** | [**ManagedElementMultiple**](ManagedElementMultiple.md) | [**ManagedElementMultiple**](ManagedElementMultiple.md) |  | [optional] 
**NRFrequency** | [**NRFrequencyMultiple**](NRFrequencyMultiple.md) | [**NRFrequencyMultiple**](NRFrequencyMultiple.md) |  | [optional] 
**ExternalGnbCuCpFunction** | [**ExternalGnbCuCpFunctionMultiple**](ExternalGnbCuCpFunctionMultiple.md) | [**ExternalGnbCuCpFunctionMultiple**](ExternalGnbCuCpFunctionMultiple.md) |  | [optional] 
**ExternalENBFunction** | [**ExternalENBFunctionMultiple**](ExternalENBFunctionMultiple.md) | [**ExternalENBFunctionMultiple**](ExternalENBFunctionMultiple.md) |  | [optional] 
**EUtranFrequency** | [**EUtranFrequencyMultiple**](EUtranFrequencyMultiple.md) | [**EUtranFrequencyMultiple**](EUtranFrequencyMultiple.md) |  | [optional] 
**DESManagementFunction** | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) |  | [optional] 
**DRACHOptimizationFunction** | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) |  | [optional] 
**DMROFunction** | [**DMROFunctionSingle**](DMROFunctionSingle.md) | [**DMROFunctionSingle**](DMROFunctionSingle.md) |  | [optional] 
**DLBOFunction** | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) |  | [optional] 
**DPCIConfigurationFunction** | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) |  | [optional] 
**CPCIConfigurationFunction** | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) |  | [optional] 
**CESManagementFunction** | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) |  | [optional] 
**Configurable5QISet** | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) |  | [optional] 
**RimRSGlobal** | [**RimRSGlobalSingle**](RimRSGlobalSingle.md) | [**RimRSGlobalSingle**](RimRSGlobalSingle.md) |  | [optional] 
**Dynamic5QISet** | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) |  | [optional] 
**CCOFunction** | [**CCOFunctionSingle**](CCOFunctionSingle.md) | [**CCOFunctionSingle**](CCOFunctionSingle.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

