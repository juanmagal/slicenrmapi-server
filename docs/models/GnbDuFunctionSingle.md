# openapi_client.model.gnb_du_function_single.GnbDuFunctionSingle

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
**gnbDuId** | [**GnbDuId**](GnbDuId.md) | [**GnbDuId**](GnbDuId.md) |  | [optional] 
**gnbDuName** | [**GnbName**](GnbName.md) | [**GnbName**](GnbName.md) |  | [optional] 
**gnbId** | str,  | str,  |  | [optional] 
**gnbIdLength** | [**GnbIdLength**](GnbIdLength.md) | [**GnbIdLength**](GnbIdLength.md) |  | [optional] 
**rimRSReportConf** | [**RimRSReportConf**](RimRSReportConf.md) | [**RimRSReportConf**](RimRSReportConf.md) |  | [optional] 
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
**NrCellDu** | [**NrCellDuMultiple**](NrCellDuMultiple.md) | [**NrCellDuMultiple**](NrCellDuMultiple.md) |  | [optional] 
**Bwp-Multiple** | [**BwpMultiple**](BwpMultiple.md) | [**BwpMultiple**](BwpMultiple.md) |  | [optional] 
**NrSectorCarrier-Multiple** | [**NrSectorCarrierMultiple**](NrSectorCarrierMultiple.md) | [**NrSectorCarrierMultiple**](NrSectorCarrierMultiple.md) |  | [optional] 
**EP_F1C** | [**EPF1CSingle**](EPF1CSingle.md) | [**EPF1CSingle**](EPF1CSingle.md) |  | [optional] 
**EP_F1U** | [**EPF1UMultiple**](EPF1UMultiple.md) | [**EPF1UMultiple**](EPF1UMultiple.md) |  | [optional] 
**DRACHOptimizationFunction** | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) |  | [optional] 
**OperatorDU** | [**OperatorDuMultiple**](OperatorDuMultiple.md) | [**OperatorDuMultiple**](OperatorDuMultiple.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

