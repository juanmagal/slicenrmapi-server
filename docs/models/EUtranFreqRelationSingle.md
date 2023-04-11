# openapi_client.model.e_utran_freq_relation_single.EUtranFreqRelationSingle

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
**cellIndividualOffset** | [**CellIndividualOffset**](CellIndividualOffset.md) | [**CellIndividualOffset**](CellIndividualOffset.md) |  | [optional] 
**[blackListEntry](#blackListEntry)** | list, tuple,  | tuple,  |  | [optional] 
**blackListEntryIdleMode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cellReselectionPriority** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cellReselectionSubPriority** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**pMax** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**qOffsetFreq** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**qQualMin** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**qRxLevMin** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**threshXHighP** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**threshXHighQ** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**threshXLowP** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**threshXLowQ** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tReselectionEutran** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**tReselectionNRSfHigh** | [**TReselectionNRSf**](TReselectionNRSf.md) | [**TReselectionNRSf**](TReselectionNRSf.md) |  | [optional] 
**tReselectionNRSfMedium** | [**TReselectionNRSf**](TReselectionNRSf.md) | [**TReselectionNRSf**](TReselectionNRSf.md) |  | [optional] 
**eUTranFrequencyRef** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# blackListEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

