# openapi_client.model.service_profile.ServiceProfile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**serviceProfileId** | str,  | str,  |  | [optional] 
**plmnInfoList** | [**PlmnInfoList**](PlmnInfoList.md) | [**PlmnInfoList**](PlmnInfoList.md) |  | [optional] 
**maxNumberofUEs** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**dLLatency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**uLLatency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**uEMobilityLevel** | [**MobilityLevel**](MobilityLevel.md) | [**MobilityLevel**](MobilityLevel.md) |  | [optional] 
**sst** | [**Sst**](Sst.md) | [**Sst**](Sst.md) |  | [optional] 
**networkSliceSharingIndicator** | [**NetworkSliceSharingIndicator**](NetworkSliceSharingIndicator.md) | [**NetworkSliceSharingIndicator**](NetworkSliceSharingIndicator.md) |  | [optional] 
**availability** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**delayTolerance** | [**DelayTolerance**](DelayTolerance.md) | [**DelayTolerance**](DelayTolerance.md) |  | [optional] 
**dLDeterministicComm** | [**DeterministicComm**](DeterministicComm.md) | [**DeterministicComm**](DeterministicComm.md) |  | [optional] 
**uLDeterministicComm** | [**DeterministicComm**](DeterministicComm.md) | [**DeterministicComm**](DeterministicComm.md) |  | [optional] 
**dLThptPerSlice** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**dLThptPerUE** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uLThptPerSlice** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**uLThptPerUE** | [**XLThpt**](XLThpt.md) | [**XLThpt**](XLThpt.md) |  | [optional] 
**dLMaxPktSize** | [**MaxPktSize**](MaxPktSize.md) | [**MaxPktSize**](MaxPktSize.md) |  | [optional] 
**uLMaxPktSize** | [**MaxPktSize**](MaxPktSize.md) | [**MaxPktSize**](MaxPktSize.md) |  | [optional] 
**maxNumberofPDUSessions** | [**MaxNumberofPDUSessions**](MaxNumberofPDUSessions.md) | [**MaxNumberofPDUSessions**](MaxNumberofPDUSessions.md) |  | [optional] 
**kPIMonitoring** | [**KPIMonitoring**](KPIMonitoring.md) | [**KPIMonitoring**](KPIMonitoring.md) |  | [optional] 
**nBIoT** | [**NBIoT**](NBIoT.md) | [**NBIoT**](NBIoT.md) |  | [optional] 
**radioSpectrum** | [**RadioSpectrum**](RadioSpectrum.md) | [**RadioSpectrum**](RadioSpectrum.md) |  | [optional] 
**synchronicity** | [**Synchronicity**](Synchronicity.md) | [**Synchronicity**](Synchronicity.md) |  | [optional] 
**positioning** | [**Positioning**](Positioning.md) | [**Positioning**](Positioning.md) |  | [optional] 
**userMgmtOpen** | [**UserMgmtOpen**](UserMgmtOpen.md) | [**UserMgmtOpen**](UserMgmtOpen.md) |  | [optional] 
**v2XCommModels** | [**V2XCommModels**](V2XCommModels.md) | [**V2XCommModels**](V2XCommModels.md) |  | [optional] 
**coverageArea** | str,  | str,  |  | [optional] 
**termDensity** | [**TermDensity**](TermDensity.md) | [**TermDensity**](TermDensity.md) |  | [optional] 
**activityFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**uESpeed** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**jitter** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**survivalTime** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**reliability** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**maxDLDataVolume** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**maxULDataVolume** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**sliceSimultaneousUse** | [**SliceSimultaneousUse**](SliceSimultaneousUse.md) | [**SliceSimultaneousUse**](SliceSimultaneousUse.md) |  | [optional] 
**energyEfficiency** | [**EnergyEfficiency**](EnergyEfficiency.md) | [**EnergyEfficiency**](EnergyEfficiency.md) |  | [optional] 
**nssaaSupport** | [**NSSAASupport**](NSSAASupport.md) | [**NSSAASupport**](NSSAASupport.md) |  | [optional] 
**n6Protection** | [**N6Protection**](N6Protection.md) | [**N6Protection**](N6Protection.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

