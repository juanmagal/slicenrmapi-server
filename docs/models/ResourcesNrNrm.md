# openapi_client.model.resources_nr_nrm.ResourcesNrNrm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[MnS](MnS.md) | [**MnS**](MnS.md) | [**MnS**](MnS.md) |  | 
[SubNetworkSingle](SubNetworkSingle.md) | [**SubNetworkSingle**](SubNetworkSingle.md) | [**SubNetworkSingle**](SubNetworkSingle.md) |  | 
[ManagedElementSingle](ManagedElementSingle.md) | [**ManagedElementSingle**](ManagedElementSingle.md) | [**ManagedElementSingle**](ManagedElementSingle.md) |  | 
[GnbDuFunctionSingle](GnbDuFunctionSingle.md) | [**GnbDuFunctionSingle**](GnbDuFunctionSingle.md) | [**GnbDuFunctionSingle**](GnbDuFunctionSingle.md) |  | 
[GnbCuUpFunctionSingle](GnbCuUpFunctionSingle.md) | [**GnbCuUpFunctionSingle**](GnbCuUpFunctionSingle.md) | [**GnbCuUpFunctionSingle**](GnbCuUpFunctionSingle.md) |  | 
[GnbCuCpFunctionSingle](GnbCuCpFunctionSingle.md) | [**GnbCuCpFunctionSingle**](GnbCuCpFunctionSingle.md) | [**GnbCuCpFunctionSingle**](GnbCuCpFunctionSingle.md) |  | 
[OperatorDuSingle](OperatorDuSingle.md) | [**OperatorDuSingle**](OperatorDuSingle.md) | [**OperatorDuSingle**](OperatorDuSingle.md) |  | 
[NrCellCuSingle](NrCellCuSingle.md) | [**NrCellCuSingle**](NrCellCuSingle.md) | [**NrCellCuSingle**](NrCellCuSingle.md) |  | 
[NrCellDuSingle](NrCellDuSingle.md) | [**NrCellDuSingle**](NrCellDuSingle.md) | [**NrCellDuSingle**](NrCellDuSingle.md) |  | 
[NrOperatorCellDuSingle](NrOperatorCellDuSingle.md) | [**NrOperatorCellDuSingle**](NrOperatorCellDuSingle.md) | [**NrOperatorCellDuSingle**](NrOperatorCellDuSingle.md) |  | 
[NRFrequencySingle](NRFrequencySingle.md) | [**NRFrequencySingle**](NRFrequencySingle.md) | [**NRFrequencySingle**](NRFrequencySingle.md) |  | 
[EUtranFrequencySingle](EUtranFrequencySingle.md) | [**EUtranFrequencySingle**](EUtranFrequencySingle.md) | [**EUtranFrequencySingle**](EUtranFrequencySingle.md) |  | 
[NrSectorCarrierSingle](NrSectorCarrierSingle.md) | [**NrSectorCarrierSingle**](NrSectorCarrierSingle.md) | [**NrSectorCarrierSingle**](NrSectorCarrierSingle.md) |  | 
[BwpSingle](BwpSingle.md) | [**BwpSingle**](BwpSingle.md) | [**BwpSingle**](BwpSingle.md) |  | 
[CommonBeamformingFunctionSingle](CommonBeamformingFunctionSingle.md) | [**CommonBeamformingFunctionSingle**](CommonBeamformingFunctionSingle.md) | [**CommonBeamformingFunctionSingle**](CommonBeamformingFunctionSingle.md) |  | 
[BeamSingle](BeamSingle.md) | [**BeamSingle**](BeamSingle.md) | [**BeamSingle**](BeamSingle.md) |  | 
[RRMPolicyRatioSingle](RRMPolicyRatioSingle.md) | [**RRMPolicyRatioSingle**](RRMPolicyRatioSingle.md) | [**RRMPolicyRatioSingle**](RRMPolicyRatioSingle.md) |  | 
[NRCellRelationSingle](NRCellRelationSingle.md) | [**NRCellRelationSingle**](NRCellRelationSingle.md) | [**NRCellRelationSingle**](NRCellRelationSingle.md) |  | 
[EUtranCellRelationSingle](EUtranCellRelationSingle.md) | [**EUtranCellRelationSingle**](EUtranCellRelationSingle.md) | [**EUtranCellRelationSingle**](EUtranCellRelationSingle.md) |  | 
[NRFreqRelationSingle](NRFreqRelationSingle.md) | [**NRFreqRelationSingle**](NRFreqRelationSingle.md) | [**NRFreqRelationSingle**](NRFreqRelationSingle.md) |  | 
[EUtranFreqRelationSingle](EUtranFreqRelationSingle.md) | [**EUtranFreqRelationSingle**](EUtranFreqRelationSingle.md) | [**EUtranFreqRelationSingle**](EUtranFreqRelationSingle.md) |  | 
[DANRManagementFunctionSingle](DANRManagementFunctionSingle.md) | [**DANRManagementFunctionSingle**](DANRManagementFunctionSingle.md) | [**DANRManagementFunctionSingle**](DANRManagementFunctionSingle.md) |  | 
[DESManagementFunctionSingle](DESManagementFunctionSingle.md) | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) | [**DESManagementFunctionSingle**](DESManagementFunctionSingle.md) |  | 
[DRACHOptimizationFunctionSingle](DRACHOptimizationFunctionSingle.md) | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) | [**DRACHOptimizationFunctionSingle**](DRACHOptimizationFunctionSingle.md) |  | 
[DMROFunctionSingle](DMROFunctionSingle.md) | [**DMROFunctionSingle**](DMROFunctionSingle.md) | [**DMROFunctionSingle**](DMROFunctionSingle.md) |  | 
[DLBOFunctionSingle](DLBOFunctionSingle.md) | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) | [**DLBOFunctionSingle**](DLBOFunctionSingle.md) |  | 
[DPCIConfigurationFunctionSingle](DPCIConfigurationFunctionSingle.md) | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) | [**DPCIConfigurationFunctionSingle**](DPCIConfigurationFunctionSingle.md) |  | 
[CPCIConfigurationFunctionSingle](CPCIConfigurationFunctionSingle.md) | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) | [**CPCIConfigurationFunctionSingle**](CPCIConfigurationFunctionSingle.md) |  | 
[CESManagementFunctionSingle](CESManagementFunctionSingle.md) | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) | [**CESManagementFunctionSingle**](CESManagementFunctionSingle.md) |  | 
[RimRSGlobalSingle](RimRSGlobalSingle.md) | [**RimRSGlobalSingle**](RimRSGlobalSingle.md) | [**RimRSGlobalSingle**](RimRSGlobalSingle.md) |  | 
[RimRSSetSingle](RimRSSetSingle.md) | [**RimRSSetSingle**](RimRSSetSingle.md) | [**RimRSSetSingle**](RimRSSetSingle.md) |  | 
[ExternalGnbDuFunctionSingle](ExternalGnbDuFunctionSingle.md) | [**ExternalGnbDuFunctionSingle**](ExternalGnbDuFunctionSingle.md) | [**ExternalGnbDuFunctionSingle**](ExternalGnbDuFunctionSingle.md) |  | 
[ExternalGnbCuUpFunctionSingle](ExternalGnbCuUpFunctionSingle.md) | [**ExternalGnbCuUpFunctionSingle**](ExternalGnbCuUpFunctionSingle.md) | [**ExternalGnbCuUpFunctionSingle**](ExternalGnbCuUpFunctionSingle.md) |  | 
[ExternalGnbCuCpFunctionSingle](ExternalGnbCuCpFunctionSingle.md) | [**ExternalGnbCuCpFunctionSingle**](ExternalGnbCuCpFunctionSingle.md) | [**ExternalGnbCuCpFunctionSingle**](ExternalGnbCuCpFunctionSingle.md) |  | 
[ExternalNrCellCuSingle](ExternalNrCellCuSingle.md) | [**ExternalNrCellCuSingle**](ExternalNrCellCuSingle.md) | [**ExternalNrCellCuSingle**](ExternalNrCellCuSingle.md) |  | 
[ExternalENBFunctionSingle](ExternalENBFunctionSingle.md) | [**ExternalENBFunctionSingle**](ExternalENBFunctionSingle.md) | [**ExternalENBFunctionSingle**](ExternalENBFunctionSingle.md) |  | 
[ExternalEUTranCellSingle](ExternalEUTranCellSingle.md) | [**ExternalEUTranCellSingle**](ExternalEUTranCellSingle.md) | [**ExternalEUTranCellSingle**](ExternalEUTranCellSingle.md) |  | 
[EPXnCSingle](EPXnCSingle.md) | [**EPXnCSingle**](EPXnCSingle.md) | [**EPXnCSingle**](EPXnCSingle.md) |  | 
[EPE1Single](EPE1Single.md) | [**EPE1Single**](EPE1Single.md) | [**EPE1Single**](EPE1Single.md) |  | 
[EPF1CSingle](EPF1CSingle.md) | [**EPF1CSingle**](EPF1CSingle.md) | [**EPF1CSingle**](EPF1CSingle.md) |  | 
[EPNgCSingle](EPNgCSingle.md) | [**EPNgCSingle**](EPNgCSingle.md) | [**EPNgCSingle**](EPNgCSingle.md) |  | 
[EPX2CSingle](EPX2CSingle.md) | [**EPX2CSingle**](EPX2CSingle.md) | [**EPX2CSingle**](EPX2CSingle.md) |  | 
[EPXnUSingle](EPXnUSingle.md) | [**EPXnUSingle**](EPXnUSingle.md) | [**EPXnUSingle**](EPXnUSingle.md) |  | 
[EPF1USingle](EPF1USingle.md) | [**EPF1USingle**](EPF1USingle.md) | [**EPF1USingle**](EPF1USingle.md) |  | 
[EPNgUSingle](EPNgUSingle.md) | [**EPNgUSingle**](EPNgUSingle.md) | [**EPNgUSingle**](EPNgUSingle.md) |  | 
[EPX2USingle](EPX2USingle.md) | [**EPX2USingle**](EPX2USingle.md) | [**EPX2USingle**](EPX2USingle.md) |  | 
[EPS1USingle](EPS1USingle.md) | [**EPS1USingle**](EPS1USingle.md) | [**EPS1USingle**](EPS1USingle.md) |  | 
[CCOFunctionSingle](CCOFunctionSingle.md) | [**CCOFunctionSingle**](CCOFunctionSingle.md) | [**CCOFunctionSingle**](CCOFunctionSingle.md) |  | 
[CCOWeakCoverageParametersSingle](CCOWeakCoverageParametersSingle.md) | [**CCOWeakCoverageParametersSingle**](CCOWeakCoverageParametersSingle.md) | [**CCOWeakCoverageParametersSingle**](CCOWeakCoverageParametersSingle.md) |  | 
[CCOPilotPollutionParametersSingle](CCOPilotPollutionParametersSingle.md) | [**CCOPilotPollutionParametersSingle**](CCOPilotPollutionParametersSingle.md) | [**CCOPilotPollutionParametersSingle**](CCOPilotPollutionParametersSingle.md) |  | 
[CCOOvershootCoverageParametersSingle](CCOOvershootCoverageParametersSingle.md) | [**CCOOvershootCoverageParametersSingle**](CCOOvershootCoverageParametersSingle.md) | [**CCOOvershootCoverageParametersSingle**](CCOOvershootCoverageParametersSingle.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

