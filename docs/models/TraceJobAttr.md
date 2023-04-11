# openapi_client.model.trace_job_attr.TraceJobAttr

abstract class used as a container of all TraceJob attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | abstract class used as a container of all TraceJob attributes | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**jobType** | [**JobTypeType**](JobTypeType.md) | [**JobTypeType**](JobTypeType.md) |  | [optional] 
**listOfInterfaces** | [**ListOfInterfacesType**](ListOfInterfacesType.md) | [**ListOfInterfacesType**](ListOfInterfacesType.md) |  | [optional] 
**listOfNETypes** | [**ListOfNETypesType**](ListOfNETypesType.md) | [**ListOfNETypesType**](ListOfNETypesType.md) |  | [optional] 
**pLMNTarget** | [**PLMNTargetType**](PLMNTargetType.md) | [**PLMNTargetType**](PLMNTargetType.md) |  | [optional] 
**traceReportingConsumerUri** | str,  | str,  |  | [optional] 
**traceCollectionEntityIPAddress** | [**IpAddr**](IpAddr.md) | [**IpAddr**](IpAddr.md) |  | [optional] 
**traceDepth** | [**TraceDepthType**](TraceDepthType.md) | [**TraceDepthType**](TraceDepthType.md) |  | [optional] 
**traceReference** | [**TraceReferenceType**](TraceReferenceType.md) | [**TraceReferenceType**](TraceReferenceType.md) |  | [optional] 
**traceRecordingSessionReference** | str,  | str,  |  | [optional] 
**jobId** | str,  | str,  |  | [optional] 
**traceReportingFormat** | [**TraceReportingFormatType**](TraceReportingFormatType.md) | [**TraceReportingFormatType**](TraceReportingFormatType.md) |  | [optional] 
**traceTarget** | [**TraceTargetType**](TraceTargetType.md) | [**TraceTargetType**](TraceTargetType.md) |  | [optional] 
**triggeringEvents** | [**TriggeringEventsType**](TriggeringEventsType.md) | [**TriggeringEventsType**](TriggeringEventsType.md) |  | [optional] 
**anonymizationOfMDTData** | [**AnonymizationOfMDTDataType**](AnonymizationOfMDTDataType.md) | [**AnonymizationOfMDTDataType**](AnonymizationOfMDTDataType.md) |  | [optional] 
**areaConfigurationForNeighCell** | [**AreaConfig**](AreaConfig.md) | [**AreaConfig**](AreaConfig.md) |  | [optional] 
**[areaScope](#areaScope)** | list, tuple,  | tuple,  |  | [optional] 
**beamLevelMeasurement** | bool,  | BoolClass,  | Determines whether beam level measurements shall be included in case of immediate MDT M1 measurement in NR. For additional details see 3GPP TS 32.422 clause 5.10.40. | [optional] 
**collectionPeriodRRMLTE** | [**CollectionPeriodRRMLTEType**](CollectionPeriodRRMLTEType.md) | [**CollectionPeriodRRMLTEType**](CollectionPeriodRRMLTEType.md) |  | [optional] 
**collectionPeriodM6LTE** | [**CollectionPeriodM6LTEType**](CollectionPeriodM6LTEType.md) | [**CollectionPeriodM6LTEType**](CollectionPeriodM6LTEType.md) |  | [optional] 
**collectionPeriodM7LTE** | [**CollectionPeriodM7LTEType**](CollectionPeriodM7LTEType.md) | [**CollectionPeriodM7LTEType**](CollectionPeriodM7LTEType.md) |  | [optional] 
**collectionPeriodRRMUMTS** | [**CollectionPeriodRRMUMTSType**](CollectionPeriodRRMUMTSType.md) | [**CollectionPeriodRRMUMTSType**](CollectionPeriodRRMUMTSType.md) |  | [optional] 
**collectionPeriodRRMNR** | [**CollectionPeriodRRMNRType**](CollectionPeriodRRMNRType.md) | [**CollectionPeriodRRMNRType**](CollectionPeriodRRMNRType.md) |  | [optional] 
**collectionPeriodM6NR** | [**CollectionPeriodM6NRType**](CollectionPeriodM6NRType.md) | [**CollectionPeriodM6NRType**](CollectionPeriodM6NRType.md) |  | [optional] 
**collectionPeriodM7NR** | [**CollectionPeriodM7NRType**](CollectionPeriodM7NRType.md) | [**CollectionPeriodM7NRType**](CollectionPeriodM7NRType.md) |  | [optional] 
**eventListForEventTriggeredMeasurement** | [**EventListForEventTriggeredMeasurementType**](EventListForEventTriggeredMeasurementType.md) | [**EventListForEventTriggeredMeasurementType**](EventListForEventTriggeredMeasurementType.md) |  | [optional] 
**eventThreshold** | [**EventThresholdType**](EventThresholdType.md) | [**EventThresholdType**](EventThresholdType.md) |  | [optional] 
**listOfMeasurements** | [**ListOfMeasurementsType**](ListOfMeasurementsType.md) | [**ListOfMeasurementsType**](ListOfMeasurementsType.md) |  | [optional] 
**loggingDuration** | [**LoggingDurationType**](LoggingDurationType.md) | [**LoggingDurationType**](LoggingDurationType.md) |  | [optional] 
**loggingInterval** | [**LoggingIntervalType**](LoggingIntervalType.md) | [**LoggingIntervalType**](LoggingIntervalType.md) |  | [optional] 
**eventThresholdL1** | [**EventThresholdL1Type**](EventThresholdL1Type.md) | [**EventThresholdL1Type**](EventThresholdL1Type.md) |  | [optional] 
**hysteresisL1** | [**HysteresisL1Type**](HysteresisL1Type.md) | [**HysteresisL1Type**](HysteresisL1Type.md) |  | [optional] 
**timeToTriggerL1** | [**TimeToTriggerL1Type**](TimeToTriggerL1Type.md) | [**TimeToTriggerL1Type**](TimeToTriggerL1Type.md) |  | [optional] 
**[mBSFNAreaList](#mBSFNAreaList)** | list, tuple,  | tuple,  |  | [optional] 
**measurementPeriodLTE** | [**MeasurementPeriodLTEType**](MeasurementPeriodLTEType.md) | [**MeasurementPeriodLTEType**](MeasurementPeriodLTEType.md) |  | [optional] 
**measurementPeriodUMTS** | [**MeasurementPeriodUMTSType**](MeasurementPeriodUMTSType.md) | [**MeasurementPeriodUMTSType**](MeasurementPeriodUMTSType.md) |  | [optional] 
**measurementQuantity** | [**MeasurementQuantityType**](MeasurementQuantityType.md) | [**MeasurementQuantityType**](MeasurementQuantityType.md) |  | [optional] 
**eventThresholdUphUMTS** | [**EventThresholdUphUMTSType**](EventThresholdUphUMTSType.md) | [**EventThresholdUphUMTSType**](EventThresholdUphUMTSType.md) |  | [optional] 
**pLMNList** | [**PLMNListType**](PLMNListType.md) | [**PLMNListType**](PLMNListType.md) |  | [optional] 
**positioningMethod** | [**PositioningMethodType**](PositioningMethodType.md) | [**PositioningMethodType**](PositioningMethodType.md) |  | [optional] 
**reportAmount** | [**ReportAmountType**](ReportAmountType.md) | [**ReportAmountType**](ReportAmountType.md) |  | [optional] 
**reportingTrigger** | [**ReportingTriggerType**](ReportingTriggerType.md) | [**ReportingTriggerType**](ReportingTriggerType.md) |  | [optional] 
**reportInterval** | [**ReportIntervalType**](ReportIntervalType.md) | [**ReportIntervalType**](ReportIntervalType.md) |  | [optional] 
**reportType** | [**ReportTypeType**](ReportTypeType.md) | [**ReportTypeType**](ReportTypeType.md) |  | [optional] 
**sensorInformation** | [**SensorInformationType**](SensorInformationType.md) | [**SensorInformationType**](SensorInformationType.md) |  | [optional] 
**traceCollectionEntityId** | decimal.Decimal, int,  | decimal.Decimal,  | See details in 3GPP TS 32.422 clause 5.10.11. Only TCE Id value may be sent over the air to the UE being configured for Logged MDT. | [optional] 
**excessPacketDelayThresholds** | [**ExcessPacketDelayThresholdsType**](ExcessPacketDelayThresholdsType.md) | [**ExcessPacketDelayThresholdsType**](ExcessPacketDelayThresholdsType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# areaScope

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AreaScope**](AreaScope.md) | [**AreaScope**](AreaScope.md) | [**AreaScope**](AreaScope.md) |  | 

# mBSFNAreaList

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MbsfnArea**](MbsfnArea.md) | [**MbsfnArea**](MbsfnArea.md) | [**MbsfnArea**](MbsfnArea.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

