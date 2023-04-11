# openapi_client.model.cn_slice_subnet_profile.CNSliceSubnetProfile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxNumberofUEs** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**dLLatency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**uLLatency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**dLThptPerSliceSubnet** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**dLThptPerUE** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uLThptPerSliceSubnet** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uLThptPerUE** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**maxNumberOfPDUSessions** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**coverageAreaTAList** | [**NrTacList**](NrTacList.md) | [**NrTacList**](NrTacList.md) |  | [optional] 
**resourceSharingLevel** | [**SharingLevel**](SharingLevel.md) | [**SharingLevel**](SharingLevel.md) |  | [optional] 
**dLMaxPktSize** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**uLMaxPktSize** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**delayTolerance** | [**DelayTolerance**](DelayTolerance.md) | [**DelayTolerance**](DelayTolerance.md) |  | [optional] 
**synchronicity** | [**SynchronicityRANSubnet**](SynchronicityRANSubnet.md) | [**SynchronicityRANSubnet**](SynchronicityRANSubnet.md) |  | [optional] 
**sliceSimultaneousUse** | [**SliceSimultaneousUse**](SliceSimultaneousUse.md) | [**SliceSimultaneousUse**](SliceSimultaneousUse.md) |  | [optional] 
**reliability** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**energyEfficiency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**dLDeterministicComm** | [**DeterministicComm**](DeterministicComm.md) | [**DeterministicComm**](DeterministicComm.md) |  | [optional] 
**uLDeterministicComm** | [**DeterministicComm**](DeterministicComm.md) | [**DeterministicComm**](DeterministicComm.md) |  | [optional] 
**survivalTime** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**nssaaSupport** | [**NSSAASupport**](NSSAASupport.md) | [**NSSAASupport**](NSSAASupport.md) |  | [optional] 
**n6Protection** | [**N6Protection**](N6Protection.md) | [**N6Protection**](N6Protection.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

