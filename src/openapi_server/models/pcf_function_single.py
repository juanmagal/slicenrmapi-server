# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn15_single import EPN15Single
from openapi_server.models.epn16_single import EPN16Single
from openapi_server.models.epn5_single import EPN5Single
from openapi_server.models.epn7_single import EPN7Single
from openapi_server.models.eprx_single import EPRxSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.pcf_function_single_all_of_attributes import PcfFunctionSingleAllOfAttributes
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class PcfFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PcfFunctionSingle - a model defined in OpenAPI

        id: The id of this PcfFunctionSingle.
        object_class: The object_class of this PcfFunctionSingle [Optional].
        object_instance: The object_instance of this PcfFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this PcfFunctionSingle [Optional].
        attributes: The attributes of this PcfFunctionSingle [Optional].
        perf_metric_job: The perf_metric_job of this PcfFunctionSingle [Optional].
        threshold_monitor: The threshold_monitor of this PcfFunctionSingle [Optional].
        managed_nf_service: The managed_nf_service of this PcfFunctionSingle [Optional].
        trace_job: The trace_job of this PcfFunctionSingle [Optional].
        ep_n5: The ep_n5 of this PcfFunctionSingle [Optional].
        ep_n7: The ep_n7 of this PcfFunctionSingle [Optional].
        ep_n15: The ep_n15 of this PcfFunctionSingle [Optional].
        ep_n16: The ep_n16 of this PcfFunctionSingle [Optional].
        ep_rx: The ep_rx of this PcfFunctionSingle [Optional].
        predefined_pcc_rule_set: The predefined_pcc_rule_set of this PcfFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[PcfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    ep_n5: Optional[List[EPN5Single]] = Field(alias="EP_N5", default=None)
    ep_n7: Optional[List[EPN7Single]] = Field(alias="EP_N7", default=None)
    ep_n15: Optional[List[EPN15Single]] = Field(alias="EP_N15", default=None)
    ep_n16: Optional[List[EPN16Single]] = Field(alias="EP_N16", default=None)
    ep_rx: Optional[List[EPRxSingle]] = Field(alias="EP_Rx", default=None)
    predefined_pcc_rule_set: Optional[PredefinedPccRuleSetSingle] = Field(alias="PredefinedPccRuleSet", default=None)

PcfFunctionSingle.update_forward_refs()
