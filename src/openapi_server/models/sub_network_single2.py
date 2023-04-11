# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.ep_transport_single import EPTransportSingle
from openapi_server.models.feasibility_check_and_reservation_job_single import FeasibilityCheckAndReservationJobSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.network_slice_single import NetworkSliceSingle
from openapi_server.models.network_slice_subnet_provider_capabilities_single import NetworkSliceSubnetProviderCapabilitiesSingle
from openapi_server.models.network_slice_subnet_single import NetworkSliceSubnetSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.sub_network_single1_all_of_attributes import SubNetworkSingle1AllOfAttributes
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class SubNetworkSingle2(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubNetworkSingle2 - a model defined in OpenAPI

        id: The id of this SubNetworkSingle2.
        object_class: The object_class of this SubNetworkSingle2 [Optional].
        object_instance: The object_instance of this SubNetworkSingle2 [Optional].
        vs_data_container: The vs_data_container of this SubNetworkSingle2 [Optional].
        attributes: The attributes of this SubNetworkSingle2 [Optional].
        management_node: The management_node of this SubNetworkSingle2 [Optional].
        mns_agent: The mns_agent of this SubNetworkSingle2 [Optional].
        me_context: The me_context of this SubNetworkSingle2 [Optional].
        perf_metric_job: The perf_metric_job of this SubNetworkSingle2 [Optional].
        threshold_monitor: The threshold_monitor of this SubNetworkSingle2 [Optional].
        trace_job: The trace_job of this SubNetworkSingle2 [Optional].
        management_data_collection: The management_data_collection of this SubNetworkSingle2 [Optional].
        ntf_subscription_control: The ntf_subscription_control of this SubNetworkSingle2 [Optional].
        alarm_list: The alarm_list of this SubNetworkSingle2 [Optional].
        file_download_job: The file_download_job of this SubNetworkSingle2 [Optional].
        files: The files of this SubNetworkSingle2 [Optional].
        mns_registry: The mns_registry of this SubNetworkSingle2 [Optional].
        sub_network: The sub_network of this SubNetworkSingle2 [Optional].
        network_slice: The network_slice of this SubNetworkSingle2 [Optional].
        network_slice_subnet: The network_slice_subnet of this SubNetworkSingle2 [Optional].
        ep_transport: The ep_transport of this SubNetworkSingle2 [Optional].
        network_slice_subnet_provider_capabilities: The network_slice_subnet_provider_capabilities of this SubNetworkSingle2 [Optional].
        feasibility_check_and_reservation_job: The feasibility_check_and_reservation_job of this SubNetworkSingle2 [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[SubNetworkSingle1AllOfAttributes] = Field(alias="attributes", default=None)
    management_node: Optional[List[ManagementNodeSingle]] = Field(alias="ManagementNode", default=None)
    mns_agent: Optional[List[MnsAgentSingle]] = Field(alias="MnsAgent", default=None)
    me_context: Optional[List[MeContextSingle]] = Field(alias="MeContext", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    management_data_collection: Optional[List[ManagementDataCollectionSingle]] = Field(alias="ManagementDataCollection", default=None)
    ntf_subscription_control: Optional[List[NtfSubscriptionControlSingle]] = Field(alias="NtfSubscriptionControl", default=None)
    alarm_list: Optional[AlarmListSingle] = Field(alias="AlarmList", default=None)
    file_download_job: Optional[List[FileDownloadJobSingle]] = Field(alias="FileDownloadJob", default=None)
    files: Optional[List[FilesSingle]] = Field(alias="Files", default=None)
    mns_registry: Optional[MnsRegistrySingle] = Field(alias="MnsRegistry", default=None)
    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)
    network_slice: Optional[List[NetworkSliceSingle]] = Field(alias="NetworkSlice", default=None)
    network_slice_subnet: Optional[List[NetworkSliceSubnetSingle]] = Field(alias="NetworkSliceSubnet", default=None)
    ep_transport: Optional[List[EPTransportSingle]] = Field(alias="EP_Transport", default=None)
    network_slice_subnet_provider_capabilities: Optional[List[NetworkSliceSubnetProviderCapabilitiesSingle]] = Field(alias="NetworkSliceSubnetProviderCapabilities", default=None)
    feasibility_check_and_reservation_job: Optional[List[FeasibilityCheckAndReservationJobSingle]] = Field(alias="FeasibilityCheckAndReservationJob", default=None)

SubNetworkSingle2.update_forward_refs()
