# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.amf_function_single_all_of_attributes import AmfFunctionSingleAllOfAttributes
from openapi_server.models.epn11_single import EPN11Single
from openapi_server.models.epn12_single import EPN12Single
from openapi_server.models.epn14_single import EPN14Single
from openapi_server.models.epn15_single import EPN15Single
from openapi_server.models.epn17_single import EPN17Single
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn26_single import EPN26Single
from openapi_server.models.epn2_single import EPN2Single
from openapi_server.models.epn8_single import EPN8Single
from openapi_server.models.epnlg_single import EPNLGSingle
from openapi_server.models.epnls_single import EPNLSSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class AmfFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AmfFunctionSingle - a model defined in OpenAPI

        id: The id of this AmfFunctionSingle.
        object_class: The object_class of this AmfFunctionSingle [Optional].
        object_instance: The object_instance of this AmfFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this AmfFunctionSingle [Optional].
        attributes: The attributes of this AmfFunctionSingle [Optional].
        perf_metric_job: The perf_metric_job of this AmfFunctionSingle [Optional].
        threshold_monitor: The threshold_monitor of this AmfFunctionSingle [Optional].
        managed_nf_service: The managed_nf_service of this AmfFunctionSingle [Optional].
        trace_job: The trace_job of this AmfFunctionSingle [Optional].
        ep_n2: The ep_n2 of this AmfFunctionSingle [Optional].
        ep_n8: The ep_n8 of this AmfFunctionSingle [Optional].
        ep_n11: The ep_n11 of this AmfFunctionSingle [Optional].
        ep_n12: The ep_n12 of this AmfFunctionSingle [Optional].
        ep_n14: The ep_n14 of this AmfFunctionSingle [Optional].
        ep_n15: The ep_n15 of this AmfFunctionSingle [Optional].
        ep_n17: The ep_n17 of this AmfFunctionSingle [Optional].
        ep_n20: The ep_n20 of this AmfFunctionSingle [Optional].
        ep_n22: The ep_n22 of this AmfFunctionSingle [Optional].
        ep_n26: The ep_n26 of this AmfFunctionSingle [Optional].
        ep_nls: The ep_nls of this AmfFunctionSingle [Optional].
        ep_nlg: The ep_nlg of this AmfFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[AmfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    ep_n2: Optional[List[EPN2Single]] = Field(alias="EP_N2", default=None)
    ep_n8: Optional[List[EPN8Single]] = Field(alias="EP_N8", default=None)
    ep_n11: Optional[List[EPN11Single]] = Field(alias="EP_N11", default=None)
    ep_n12: Optional[List[EPN12Single]] = Field(alias="EP_N12", default=None)
    ep_n14: Optional[List[EPN14Single]] = Field(alias="EP_N14", default=None)
    ep_n15: Optional[List[EPN15Single]] = Field(alias="EP_N15", default=None)
    ep_n17: Optional[List[EPN17Single]] = Field(alias="EP_N17", default=None)
    ep_n20: Optional[List[EPN20Single]] = Field(alias="EP_N20", default=None)
    ep_n22: Optional[List[EPN22Single]] = Field(alias="EP_N22", default=None)
    ep_n26: Optional[List[EPN26Single]] = Field(alias="EP_N26", default=None)
    ep_nls: Optional[List[EPNLSSingle]] = Field(alias="EP_NLS", default=None)
    ep_nlg: Optional[List[EPNLGSingle]] = Field(alias="EP_NLG", default=None)

AmfFunctionSingle.update_forward_refs()
