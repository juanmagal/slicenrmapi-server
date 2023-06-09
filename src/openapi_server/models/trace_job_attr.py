# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.anonymization_of_mdt_data_type import AnonymizationOfMDTDataType
from openapi_server.models.area_config import AreaConfig
from openapi_server.models.area_scope import AreaScope
from openapi_server.models.collection_period_m6_lte_type import CollectionPeriodM6LTEType
from openapi_server.models.collection_period_m6_nr_type import CollectionPeriodM6NRType
from openapi_server.models.collection_period_rrmlte_type import CollectionPeriodRRMLTEType
from openapi_server.models.collection_period_rrmnr_type import CollectionPeriodRRMNRType
from openapi_server.models.collection_period_rrmumts_type import CollectionPeriodRRMUMTSType
from openapi_server.models.event_list_for_event_triggered_measurement_type import EventListForEventTriggeredMeasurementType
from openapi_server.models.event_threshold_l1_type import EventThresholdL1Type
from openapi_server.models.event_threshold_type import EventThresholdType
from openapi_server.models.ip_addr import IpAddr
from openapi_server.models.job_type_type import JobTypeType
from openapi_server.models.list_of_interfaces_type import ListOfInterfacesType
from openapi_server.models.list_of_measurements_type import ListOfMeasurementsType
from openapi_server.models.logging_duration_type import LoggingDurationType
from openapi_server.models.logging_interval_type import LoggingIntervalType
from openapi_server.models.mbsfn_area import MbsfnArea
from openapi_server.models.measurement_period_lte_type import MeasurementPeriodLTEType
from openapi_server.models.measurement_period_umts_type import MeasurementPeriodUMTSType
from openapi_server.models.measurement_quantity_type import MeasurementQuantityType
from openapi_server.models.plmn_list_type_inner import PLMNListTypeInner
from openapi_server.models.plmn_target_type import PLMNTargetType
from openapi_server.models.positioning_method_type import PositioningMethodType
from openapi_server.models.report_amount_type import ReportAmountType
from openapi_server.models.report_interval_type import ReportIntervalType
from openapi_server.models.report_type_type import ReportTypeType
from openapi_server.models.time_to_trigger_l1_type import TimeToTriggerL1Type
from openapi_server.models.trace_depth_type import TraceDepthType
from openapi_server.models.trace_reference_type import TraceReferenceType
from openapi_server.models.trace_reporting_format_type import TraceReportingFormatType
from openapi_server.models.trace_target_type import TraceTargetType
from openapi_server.models.triggering_events_type import TriggeringEventsType


class TraceJobAttr(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TraceJobAttr - a model defined in OpenAPI

        job_type: The job_type of this TraceJobAttr [Optional].
        list_of_interfaces: The list_of_interfaces of this TraceJobAttr [Optional].
        list_of_ne_types: The list_of_ne_types of this TraceJobAttr [Optional].
        p_lmn_target: The p_lmn_target of this TraceJobAttr [Optional].
        trace_reporting_consumer_uri: The trace_reporting_consumer_uri of this TraceJobAttr [Optional].
        trace_collection_entity_ip_address: The trace_collection_entity_ip_address of this TraceJobAttr [Optional].
        trace_depth: The trace_depth of this TraceJobAttr [Optional].
        trace_reference: The trace_reference of this TraceJobAttr [Optional].
        trace_recording_session_reference: The trace_recording_session_reference of this TraceJobAttr [Optional].
        job_id: The job_id of this TraceJobAttr [Optional].
        trace_reporting_format: The trace_reporting_format of this TraceJobAttr [Optional].
        trace_target: The trace_target of this TraceJobAttr [Optional].
        triggering_events: The triggering_events of this TraceJobAttr [Optional].
        anonymization_of_mdt_data: The anonymization_of_mdt_data of this TraceJobAttr [Optional].
        area_configuration_for_neigh_cell: The area_configuration_for_neigh_cell of this TraceJobAttr [Optional].
        area_scope: The area_scope of this TraceJobAttr [Optional].
        beam_level_measurement: The beam_level_measurement of this TraceJobAttr [Optional].
        collection_period_rrmlte: The collection_period_rrmlte of this TraceJobAttr [Optional].
        collection_period_m6_lte: The collection_period_m6_lte of this TraceJobAttr [Optional].
        collection_period_m7_lte: The collection_period_m7_lte of this TraceJobAttr [Optional].
        collection_period_rrmumts: The collection_period_rrmumts of this TraceJobAttr [Optional].
        collection_period_rrmnr: The collection_period_rrmnr of this TraceJobAttr [Optional].
        collection_period_m6_nr: The collection_period_m6_nr of this TraceJobAttr [Optional].
        collection_period_m7_nr: The collection_period_m7_nr of this TraceJobAttr [Optional].
        event_list_for_event_triggered_measurement: The event_list_for_event_triggered_measurement of this TraceJobAttr [Optional].
        event_threshold: The event_threshold of this TraceJobAttr [Optional].
        list_of_measurements: The list_of_measurements of this TraceJobAttr [Optional].
        logging_duration: The logging_duration of this TraceJobAttr [Optional].
        logging_interval: The logging_interval of this TraceJobAttr [Optional].
        event_threshold_l1: The event_threshold_l1 of this TraceJobAttr [Optional].
        hysteresis_l1: The hysteresis_l1 of this TraceJobAttr [Optional].
        time_to_trigger_l1: The time_to_trigger_l1 of this TraceJobAttr [Optional].
        m_bsfn_area_list: The m_bsfn_area_list of this TraceJobAttr [Optional].
        measurement_period_lte: The measurement_period_lte of this TraceJobAttr [Optional].
        measurement_period_umts: The measurement_period_umts of this TraceJobAttr [Optional].
        measurement_quantity: The measurement_quantity of this TraceJobAttr [Optional].
        event_threshold_uph_umts: The event_threshold_uph_umts of this TraceJobAttr [Optional].
        p_lmn_list: The p_lmn_list of this TraceJobAttr [Optional].
        positioning_method: The positioning_method of this TraceJobAttr [Optional].
        report_amount: The report_amount of this TraceJobAttr [Optional].
        reporting_trigger: The reporting_trigger of this TraceJobAttr [Optional].
        report_interval: The report_interval of this TraceJobAttr [Optional].
        report_type: The report_type of this TraceJobAttr [Optional].
        sensor_information: The sensor_information of this TraceJobAttr [Optional].
        trace_collection_entity_id: The trace_collection_entity_id of this TraceJobAttr [Optional].
        excess_packet_delay_thresholds: The excess_packet_delay_thresholds of this TraceJobAttr [Optional].
    """

    job_type: Optional[JobTypeType] = Field(alias="jobType", default=None)
    list_of_interfaces: Optional[ListOfInterfacesType] = Field(alias="listOfInterfaces", default=None)
    list_of_ne_types: Optional[List[str]] = Field(alias="listOfNETypes", default=None)
    p_lmn_target: Optional[PLMNTargetType] = Field(alias="pLMNTarget", default=None)
    trace_reporting_consumer_uri: Optional[str] = Field(alias="traceReportingConsumerUri", default=None)
    trace_collection_entity_ip_address: Optional[IpAddr] = Field(alias="traceCollectionEntityIPAddress", default=None)
    trace_depth: Optional[TraceDepthType] = Field(alias="traceDepth", default=None)
    trace_reference: Optional[TraceReferenceType] = Field(alias="traceReference", default=None)
    trace_recording_session_reference: Optional[str] = Field(alias="traceRecordingSessionReference", default=None)
    job_id: Optional[str] = Field(alias="jobId", default=None)
    trace_reporting_format: Optional[TraceReportingFormatType] = Field(alias="traceReportingFormat", default=None)
    trace_target: Optional[TraceTargetType] = Field(alias="traceTarget", default=None)
    triggering_events: Optional[TriggeringEventsType] = Field(alias="triggeringEvents", default=None)
    anonymization_of_mdt_data: Optional[AnonymizationOfMDTDataType] = Field(alias="anonymizationOfMDTData", default=None)
    area_configuration_for_neigh_cell: Optional[AreaConfig] = Field(alias="areaConfigurationForNeighCell", default=None)
    area_scope: Optional[List[AreaScope]] = Field(alias="areaScope", default=None)
    beam_level_measurement: Optional[bool] = Field(alias="beamLevelMeasurement", default=None)
    collection_period_rrmlte: Optional[CollectionPeriodRRMLTEType] = Field(alias="collectionPeriodRRMLTE", default=None)
    collection_period_m6_lte: Optional[CollectionPeriodM6LTEType] = Field(alias="collectionPeriodM6LTE", default=None)
    collection_period_m7_lte: Optional[int] = Field(alias="collectionPeriodM7LTE", default=None)
    collection_period_rrmumts: Optional[CollectionPeriodRRMUMTSType] = Field(alias="collectionPeriodRRMUMTS", default=None)
    collection_period_rrmnr: Optional[CollectionPeriodRRMNRType] = Field(alias="collectionPeriodRRMNR", default=None)
    collection_period_m6_nr: Optional[CollectionPeriodM6NRType] = Field(alias="collectionPeriodM6NR", default=None)
    collection_period_m7_nr: Optional[int] = Field(alias="collectionPeriodM7NR", default=None)
    event_list_for_event_triggered_measurement: Optional[EventListForEventTriggeredMeasurementType] = Field(alias="eventListForEventTriggeredMeasurement", default=None)
    event_threshold: Optional[EventThresholdType] = Field(alias="eventThreshold", default=None)
    list_of_measurements: Optional[ListOfMeasurementsType] = Field(alias="listOfMeasurements", default=None)
    logging_duration: Optional[LoggingDurationType] = Field(alias="loggingDuration", default=None)
    logging_interval: Optional[LoggingIntervalType] = Field(alias="loggingInterval", default=None)
    event_threshold_l1: Optional[EventThresholdL1Type] = Field(alias="eventThresholdL1", default=None)
    hysteresis_l1: Optional[int] = Field(alias="hysteresisL1", default=None)
    time_to_trigger_l1: Optional[TimeToTriggerL1Type] = Field(alias="timeToTriggerL1", default=None)
    m_bsfn_area_list: Optional[List[MbsfnArea]] = Field(alias="mBSFNAreaList", default=None)
    measurement_period_lte: Optional[MeasurementPeriodLTEType] = Field(alias="measurementPeriodLTE", default=None)
    measurement_period_umts: Optional[MeasurementPeriodUMTSType] = Field(alias="measurementPeriodUMTS", default=None)
    measurement_quantity: Optional[MeasurementQuantityType] = Field(alias="measurementQuantity", default=None)
    event_threshold_uph_umts: Optional[int] = Field(alias="eventThresholdUphUMTS", default=None)
    p_lmn_list: Optional[List[PLMNListTypeInner]] = Field(alias="pLMNList", default=None)
    positioning_method: Optional[PositioningMethodType] = Field(alias="positioningMethod", default=None)
    report_amount: Optional[ReportAmountType] = Field(alias="reportAmount", default=None)
    reporting_trigger: Optional[List[str]] = Field(alias="reportingTrigger", default=None)
    report_interval: Optional[ReportIntervalType] = Field(alias="reportInterval", default=None)
    report_type: Optional[ReportTypeType] = Field(alias="reportType", default=None)
    sensor_information: Optional[List[str]] = Field(alias="sensorInformation", default=None)
    trace_collection_entity_id: Optional[int] = Field(alias="traceCollectionEntityId", default=None)
    excess_packet_delay_thresholds: Optional[object] = Field(alias="excessPacketDelayThresholds", default=None)

    @validator("collection_period_m7_lte")
    def collection_period_m7_lte_max(cls, value):
        assert value <= 60
        return value

    @validator("collection_period_m7_lte")
    def collection_period_m7_lte_min(cls, value):
        assert value >= 1
        return value

    @validator("collection_period_m7_nr")
    def collection_period_m7_nr_max(cls, value):
        assert value <= 60
        return value

    @validator("collection_period_m7_nr")
    def collection_period_m7_nr_min(cls, value):
        assert value >= 1
        return value

    @validator("hysteresis_l1")
    def hysteresis_l1_max(cls, value):
        assert value <= 30
        return value

    @validator("hysteresis_l1")
    def hysteresis_l1_min(cls, value):
        assert value >= 0
        return value

    @validator("event_threshold_uph_umts")
    def event_threshold_uph_umts_max(cls, value):
        assert value <= 31
        return value

    @validator("event_threshold_uph_umts")
    def event_threshold_uph_umts_min(cls, value):
        assert value >= 0
        return value

TraceJobAttr.update_forward_refs()
