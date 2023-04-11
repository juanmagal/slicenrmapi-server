# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn6_single import EPN6Single
from openapi_server.models.epn9_single import EPN9Single
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.upf_function_single_all_of_attributes import UpfFunctionSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class UpfFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpfFunctionSingle - a model defined in OpenAPI

        id: The id of this UpfFunctionSingle.
        object_class: The object_class of this UpfFunctionSingle [Optional].
        object_instance: The object_instance of this UpfFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this UpfFunctionSingle [Optional].
        attributes: The attributes of this UpfFunctionSingle [Optional].
        perf_metric_job: The perf_metric_job of this UpfFunctionSingle [Optional].
        threshold_monitor: The threshold_monitor of this UpfFunctionSingle [Optional].
        managed_nf_service: The managed_nf_service of this UpfFunctionSingle [Optional].
        trace_job: The trace_job of this UpfFunctionSingle [Optional].
        ep_n3: The ep_n3 of this UpfFunctionSingle [Optional].
        ep_n4: The ep_n4 of this UpfFunctionSingle [Optional].
        ep_n6: The ep_n6 of this UpfFunctionSingle [Optional].
        ep_n9: The ep_n9 of this UpfFunctionSingle [Optional].
        ep_s5_u: The ep_s5_u of this UpfFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[UpfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    ep_n3: Optional[List[EPN3Single]] = Field(alias="EP_N3", default=None)
    ep_n4: Optional[List[EPN4Single]] = Field(alias="EP_N4", default=None)
    ep_n6: Optional[List[EPN6Single]] = Field(alias="EP_N6", default=None)
    ep_n9: Optional[List[EPN9Single]] = Field(alias="EP_N9", default=None)
    ep_s5_u: Optional[List[EPS5USingle]] = Field(alias="EP_S5U", default=None)

UpfFunctionSingle.update_forward_refs()
