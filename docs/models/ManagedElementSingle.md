# openapi_client.model.managed_element_single.ManagedElementSingle

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
[ManagedElementNcO](ManagedElementNcO.md) | [**ManagedElementNcO**](ManagedElementNcO.md) | [**ManagedElementNcO**](ManagedElementNcO.md) |  | 
[all_of_3](#all_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**attributes** | [**ManagedElementAttr**](ManagedElementAttr.md) | [**ManagedElementAttr**](ManagedElementAttr.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**GnbDuFunction** | [**GnbDuFunctionMultiple**](GnbDuFunctionMultiple.md) | [**GnbDuFunctionMultiple**](GnbDuFunctionMultiple.md) |  | [optional] 
**GnbCuUpFunction** | [**GnbCuUpFunctionMultiple**](GnbCuUpFunctionMultiple.md) | [**GnbCuUpFunctionMultiple**](GnbCuUpFunctionMultiple.md) |  | [optional] 
**GnbCuCpFunction** | [**GnbCuCpFunctionMultiple**](GnbCuCpFunctionMultiple.md) | [**GnbCuCpFunctionMultiple**](GnbCuCpFunctionMultiple.md) |  | [optional] 
**DESManagementFunction** | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) |  | [optional] 
**DRACHOptimizationFunction** | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) |  | [optional] 
**DMROFunction** | [**DMROFunctionSingle**](DMROFunctionSingle.md) | [**DMROFunctionSingle**](DMROFunctionSingle.md) |  | [optional] 
**DLBOFunction** | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) |  | [optional] 
**DPCIConfigurationFunction** | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) |  | [optional] 
**CPCIConfigurationFunction** | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) |  | [optional] 
**CESManagementFunction** | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) |  | [optional] 
**Configurable5QISet** | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) | [**Configurable5QISetMultiple**](Configurable5QISetMultiple.md) |  | [optional] 
**Dynamic5QISet** | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) | [**Dynamic5QISetMultiple**](Dynamic5QISetMultiple.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

