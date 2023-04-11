# openapi_client.model.nr_cell_du_single.NrCellDuSingle

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
**administrativeState** | [**AdministrativeState**](AdministrativeState.md) | [**AdministrativeState**](AdministrativeState.md) |  | [optional] 
**operationalState** | [**OperationalState**](OperationalState.md) | [**OperationalState**](OperationalState.md) |  | [optional] 
**cellLocalId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**cellState** | [**CellState**](CellState.md) | [**CellState**](CellState.md) |  | [optional] 
**plmnInfoList** | [**PlmnInfoList**](PlmnInfoList.md) | [**PlmnInfoList**](PlmnInfoList.md) |  | [optional] 
**npnIdentityList** | [**NpnIdentityList**](NpnIdentityList.md) | [**NpnIdentityList**](NpnIdentityList.md) |  | [optional] 
**nrPci** | [**NrPci**](NrPci.md) | [**NrPci**](NrPci.md) |  | [optional] 
**nrTac** | [**NrTac**](NrTac.md) | [**NrTac**](NrTac.md) |  | [optional] 
**arfcnDL** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**arfcnUL** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**arfcnSUL** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bSChannelBwDL** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bSChannelBwUL** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**bSChannelBwSUL** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ssbFrequency** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ssbPeriodicity** | [**SsbPeriodicity**](SsbPeriodicity.md) | [**SsbPeriodicity**](SsbPeriodicity.md) |  | [optional] 
**ssbSubCarrierSpacing** | [**SsbSubCarrierSpacing**](SsbSubCarrierSpacing.md) | [**SsbSubCarrierSpacing**](SsbSubCarrierSpacing.md) |  | [optional] 
**ssbOffset** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**ssbDuration** | [**SsbDuration**](SsbDuration.md) | [**SsbDuration**](SsbDuration.md) |  | [optional] 
**[nrSectorCarrierRef](#nrSectorCarrierRef)** | list, tuple,  | tuple,  |  | [optional] 
**[bwpRef](#bwpRef)** | list, tuple,  | tuple,  |  | [optional] 
**rimRSMonitoringStartTime** | str,  | str,  |  | [optional] 
**rimRSMonitoringStopTime** | str,  | str,  |  | [optional] 
**rimRSMonitoringWindowDuration** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**rimRSMonitoringWindowStartingOffset** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**rimRSMonitoringWindowPeriodicity** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**rimRSMonitoringOccasionInterval** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**rimRSMonitoringOccasionStartingOffset** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**nRFrequencyRef** | str,  | str,  |  | [optional] 
**victimSetRef** | str,  | str,  |  | [optional] 
**aggressorSetRef** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nrSectorCarrierRef

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# bwpRef

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# all_of_3

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**RRMPolicyRatio** | [**RRMPolicyRatioMultiple**](RRMPolicyRatioMultiple.md) | [**RRMPolicyRatioMultiple**](RRMPolicyRatioMultiple.md) |  | [optional] 
**CPCIConfigurationFunction** | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) |  | [optional] 
**DRACHOptimizationFunction** | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) |  | [optional] 
**NrOperatorCellDu** | [**NrOperatorCellDuMultiple**](NrOperatorCellDuMultiple.md) | [**NrOperatorCellDuMultiple**](NrOperatorCellDuMultiple.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

