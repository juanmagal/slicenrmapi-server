# openapi_client.model.gnb_cu_cp_function_single.GnbCuCpFunctionSingle

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
[ManagedFunctionNcO](ManagedFunctionNcO.md) | [**ManagedFunctionNcO**](ManagedFunctionNcO.md) | [**ManagedFunctionNcO**](ManagedFunctionNcO.md) |  | 
[all_of_3](#all_of_3) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attributes](#attributes)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ManagedFunctionAttr](ManagedFunctionAttr.md) | [**ManagedFunctionAttr**](ManagedFunctionAttr.md) | [**ManagedFunctionAttr**](ManagedFunctionAttr.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gnbId** | str,  | str,  |  | [optional] 
**gnbIdLength** | [**GnbIdLength**](GnbIdLength.md) | [**GnbIdLength**](GnbIdLength.md) |  | [optional] 
**gnbCuName** | [**GnbName**](GnbName.md) | [**GnbName**](GnbName.md) |  | [optional] 
**plmnId** | [**PlmnId**](PlmnId.md) | [**PlmnId**](PlmnId.md) |  | [optional] 
**x2BlockList** | [**GGnbIdList**](GGnbIdList.md) | [**GGnbIdList**](GGnbIdList.md) |  | [optional] 
**xnBlockList** | [**GGnbIdList**](GGnbIdList.md) | [**GGnbIdList**](GGnbIdList.md) |  | [optional] 
**x2AllowList** | [**GGnbIdList**](GGnbIdList.md) | [**GGnbIdList**](GGnbIdList.md) |  | [optional] 
**xnAllowList** | [**GGnbIdList**](GGnbIdList.md) | [**GGnbIdList**](GGnbIdList.md) |  | [optional] 
**x2HOBlackList** | [**GEnbIdList**](GEnbIdList.md) | [**GEnbIdList**](GEnbIdList.md) |  | [optional] 
**xnHOBlackList** | [**GGnbIdList**](GGnbIdList.md) | [**GGnbIdList**](GGnbIdList.md) |  | [optional] 
**mappingSetIDBackhaulAddress** | [**MappingSetIDBackhaulAddress**](MappingSetIDBackhaulAddress.md) | [**MappingSetIDBackhaulAddress**](MappingSetIDBackhaulAddress.md) |  | [optional] 
**tceMappingInfoList** | [**TceMappingInfoList**](TceMappingInfoList.md) | [**TceMappingInfoList**](TceMappingInfoList.md) |  | [optional] 
**configurable5QISetRef** | str,  | str,  |  | [optional] 
**dynamic5QISetRef** | str,  | str,  |  | [optional] 
**dCHOControl** | bool,  | BoolClass,  |  | [optional] 
**dDAPSHOControl** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**RRMPolicyRatio** | [**RRMPolicyRatioMultiple**](RRMPolicyRatioMultiple.md) | [**RRMPolicyRatioMultiple**](RRMPolicyRatioMultiple.md) |  | [optional] 
**NrCellCu** | [**NrCellCuMultiple**](NrCellCuMultiple.md) | [**NrCellCuMultiple**](NrCellCuMultiple.md) |  | [optional] 
**EP_XnC** | [**EPXnCMultiple**](EPXnCMultiple.md) | [**EPXnCMultiple**](EPXnCMultiple.md) |  | [optional] 
**EP_E1** | [**EPE1Multiple**](EPE1Multiple.md) | [**EPE1Multiple**](EPE1Multiple.md) |  | [optional] 
**EP_F1C** | [**EPF1CMultiple**](EPF1CMultiple.md) | [**EPF1CMultiple**](EPF1CMultiple.md) |  | [optional] 
**EP_NgC** | [**EPNgCMultiple**](EPNgCMultiple.md) | [**EPNgCMultiple**](EPNgCMultiple.md) |  | [optional] 
**EP_X2C** | [**EPX2CMultiple**](EPX2CMultiple.md) | [**EPX2CMultiple**](EPX2CMultiple.md) |  | [optional] 
**DANRManagementFunction** | [**DANRManagementFunctionSingle**](DANRManagementFunctionSingle.md) | [**DANRManagementFunctionSingle**](DANRManagementFunctionSingle.md) |  | [optional] 
**DESManagementFunction** | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) |  | [optional] 
**DMROFunction** | [**DMROFunctionSingle**](DMROFunctionSingle.md) | [**DMROFunctionSingle**](DMROFunctionSingle.md) |  | [optional] 
**DLBOFunction** | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

