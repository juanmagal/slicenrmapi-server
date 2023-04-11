# openapi_client.model.ces_management_function_single.CESManagementFunctionSingle

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

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attributes](#attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cesSwitch** | bool,  | BoolClass,  |  | [optional] 
**intraRatEsActivationOriginalCellLoadParameters** | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) |  | [optional] 
**intraRatEsActivationCandidateCellsLoadParameters** | [**IntraRatEsActivationCandidateCellsLoadParameters**](IntraRatEsActivationCandidateCellsLoadParameters.md) | [**IntraRatEsActivationCandidateCellsLoadParameters**](IntraRatEsActivationCandidateCellsLoadParameters.md) |  | [optional] 
**intraRatEsDeactivationCandidateCellsLoadParameters** | [**IntraRatEsDeactivationCandidateCellsLoadParameters**](IntraRatEsDeactivationCandidateCellsLoadParameters.md) | [**IntraRatEsDeactivationCandidateCellsLoadParameters**](IntraRatEsDeactivationCandidateCellsLoadParameters.md) |  | [optional] 
**esNotAllowedTimePeriod** | [**EsNotAllowedTimePeriod**](EsNotAllowedTimePeriod.md) | [**EsNotAllowedTimePeriod**](EsNotAllowedTimePeriod.md) |  | [optional] 
**interRatEsActivationOriginalCellParameters** | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) |  | [optional] 
**interRatEsActivationCandidateCellParameters** | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) |  | [optional] 
**interRatEsDeactivationCandidateCellParameters** | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) | [**IntraRatEsActivationOriginalCellLoadParameters**](IntraRatEsActivationOriginalCellLoadParameters.md) |  | [optional] 
**energySavingControl** | str,  | str,  |  | [optional] must be one of ["toBeEnergySaving", "toBeNotEnergySaving", ] 
**energySavingState** | str,  | str,  |  | [optional] must be one of ["isNotEnergySaving", "isEnergySaving", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

