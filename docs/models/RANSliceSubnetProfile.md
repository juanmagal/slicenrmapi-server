# openapi_client.model.ran_slice_subnet_profile.RANSliceSubnetProfile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**coverageAreaTAList** | [**NrTacList**](NrTacList.md) | [**NrTacList**](NrTacList.md) |  | [optional] 
**dLLatency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**uLLatency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**uEMobilityLevel** | [**MobilityLevel**](MobilityLevel.md) | [**MobilityLevel**](MobilityLevel.md) |  | [optional] 
**resourceSharingLevel** | [**SharingLevel**](SharingLevel.md) | [**SharingLevel**](SharingLevel.md) |  | [optional] 
**maxNumberofUEs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**activityFactor** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**dLThptPerSliceSubnet** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**dLThptPerUE** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uLThptPerSliceSubnet** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uLThptPerUE** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uESpeed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**reliability** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**sST** | [**Sst**](Sst.md) | [**Sst**](Sst.md) |  | [optional] 
**dLMaxPktSize** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**uLMaxPktSize** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**nROperatingBands** | str,  | str,  |  | [optional] 
**delayTolerance** | [**DelayTolerance**](DelayTolerance.md) | [**DelayTolerance**](DelayTolerance.md) |  | [optional] 
**positioning** | [**PositioningRANSubnet**](PositioningRANSubnet.md) | [**PositioningRANSubnet**](PositioningRANSubnet.md) |  | [optional] 
**sliceSimultaneousUse** | [**SliceSimultaneousUse**](SliceSimultaneousUse.md) | [**SliceSimultaneousUse**](SliceSimultaneousUse.md) |  | [optional] 
**energyEfficiency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**termDensity** | [**TermDensity**](TermDensity.md) | [**TermDensity**](TermDensity.md) |  | [optional] 
**survivalTime** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**synchronicity** | [**SynchronicityRANSubnet**](SynchronicityRANSubnet.md) | [**SynchronicityRANSubnet**](SynchronicityRANSubnet.md) |  | [optional] 
**dLDeterministicComm** | [**DeterministicComm**](DeterministicComm.md) | [**DeterministicComm**](DeterministicComm.md) |  | [optional] 
**uLDeterministicComm** | [**DeterministicComm**](DeterministicComm.md) | [**DeterministicComm**](DeterministicComm.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

