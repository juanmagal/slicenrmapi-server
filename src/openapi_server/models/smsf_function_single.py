# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn21_single import EPN21Single
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.smsf_function_single_all_of_attributes import SmsfFunctionSingleAllOfAttributes
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class SmsfFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SmsfFunctionSingle - a model defined in OpenAPI

        id: The id of this SmsfFunctionSingle.
        object_class: The object_class of this SmsfFunctionSingle [Optional].
        object_instance: The object_instance of this SmsfFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this SmsfFunctionSingle [Optional].
        attributes: The attributes of this SmsfFunctionSingle [Optional].
        perf_metric_job: The perf_metric_job of this SmsfFunctionSingle [Optional].
        threshold_monitor: The threshold_monitor of this SmsfFunctionSingle [Optional].
        managed_nf_service: The managed_nf_service of this SmsfFunctionSingle [Optional].
        trace_job: The trace_job of this SmsfFunctionSingle [Optional].
        ep_n20: The ep_n20 of this SmsfFunctionSingle [Optional].
        ep_n21: The ep_n21 of this SmsfFunctionSingle [Optional].
        ep_map_smsc: The ep_map_smsc of this SmsfFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[SmsfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    ep_n20: Optional[List[EPN20Single]] = Field(alias="EP_N20", default=None)
    ep_n21: Optional[List[EPN21Single]] = Field(alias="EP_N21", default=None)
    ep_map_smsc: Optional[List[EPMAPSMSCSingle]] = Field(alias="EP_MAP_SMSC", default=None)

SmsfFunctionSingle.update_forward_refs()
