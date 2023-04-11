# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server.models.managed_element_attr import ManagedElementAttr
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class ManagedElementSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ManagedElementSingle - a model defined in OpenAPI

        id: The id of this ManagedElementSingle.
        object_class: The object_class of this ManagedElementSingle [Optional].
        object_instance: The object_instance of this ManagedElementSingle [Optional].
        vs_data_container: The vs_data_container of this ManagedElementSingle [Optional].
        attributes: The attributes of this ManagedElementSingle [Optional].
        mns_agent: The mns_agent of this ManagedElementSingle [Optional].
        perf_metric_job: The perf_metric_job of this ManagedElementSingle [Optional].
        threshold_monitor: The threshold_monitor of this ManagedElementSingle [Optional].
        trace_job: The trace_job of this ManagedElementSingle [Optional].
        ntf_subscription_control: The ntf_subscription_control of this ManagedElementSingle [Optional].
        alarm_list: The alarm_list of this ManagedElementSingle [Optional].
        file_download_job: The file_download_job of this ManagedElementSingle [Optional].
        files: The files of this ManagedElementSingle [Optional].
        gnb_du_function: The gnb_du_function of this ManagedElementSingle [Optional].
        gnb_cu_up_function: The gnb_cu_up_function of this ManagedElementSingle [Optional].
        gnb_cu_cp_function: The gnb_cu_cp_function of this ManagedElementSingle [Optional].
        des_management_function: The des_management_function of this ManagedElementSingle [Optional].
        drach_optimization_function: The drach_optimization_function of this ManagedElementSingle [Optional].
        dmro_function: The dmro_function of this ManagedElementSingle [Optional].
        dlbo_function: The dlbo_function of this ManagedElementSingle [Optional].
        dpci_configuration_function: The dpci_configuration_function of this ManagedElementSingle [Optional].
        cpci_configuration_function: The cpci_configuration_function of this ManagedElementSingle [Optional].
        ces_management_function: The ces_management_function of this ManagedElementSingle [Optional].
        configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingle [Optional].
        dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[ManagedElementAttr] = Field(alias="attributes", default=None)
    mns_agent: Optional[List[MnsAgentSingle]] = Field(alias="MnsAgent", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    ntf_subscription_control: Optional[List[NtfSubscriptionControlSingle]] = Field(alias="NtfSubscriptionControl", default=None)
    alarm_list: Optional[AlarmListSingle] = Field(alias="AlarmList", default=None)
    file_download_job: Optional[List[FileDownloadJobSingle]] = Field(alias="FileDownloadJob", default=None)
    files: Optional[List[FilesSingle]] = Field(alias="Files", default=None)
    gnb_du_function: Optional[List[GnbDuFunctionSingle]] = Field(alias="GnbDuFunction", default=None)
    gnb_cu_up_function: Optional[List[GnbCuUpFunctionSingle]] = Field(alias="GnbCuUpFunction", default=None)
    gnb_cu_cp_function: Optional[List[GnbCuCpFunctionSingle]] = Field(alias="GnbCuCpFunction", default=None)
    des_management_function: Optional[DESManagementFunctionSingle] = Field(alias="DESManagementFunction", default=None)
    drach_optimization_function: Optional[DRACHOptimizationFunctionSingle] = Field(alias="DRACHOptimizationFunction", default=None)
    dmro_function: Optional[DMROFunctionSingle] = Field(alias="DMROFunction", default=None)
    dlbo_function: Optional[DLBOFunctionSingle] = Field(alias="DLBOFunction", default=None)
    dpci_configuration_function: Optional[DPCIConfigurationFunctionSingle] = Field(alias="DPCIConfigurationFunction", default=None)
    cpci_configuration_function: Optional[CPCIConfigurationFunctionSingle] = Field(alias="CPCIConfigurationFunction", default=None)
    ces_management_function: Optional[CESManagementFunctionSingle] = Field(alias="CESManagementFunction", default=None)
    configurable5_qi_set: Optional[List[Configurable5QISetSingle]] = Field(alias="Configurable5QISet", default=None)
    dynamic5_qi_set: Optional[List[Dynamic5QISetSingle]] = Field(alias="Dynamic5QISet", default=None)

ManagedElementSingle.update_forward_refs()
