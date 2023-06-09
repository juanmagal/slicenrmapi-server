# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.nsacf_info_snssai import NsacfInfoSnssai
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.tai import Tai
from openapi_server.models.vnf_parameter import VnfParameter


class NsacfFunctionSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NsacfFunctionSingleAllOfAttributes - a model defined in OpenAPI

        user_label: The user_label of this NsacfFunctionSingleAllOfAttributes [Optional].
        vnf_parameters_list: The vnf_parameters_list of this NsacfFunctionSingleAllOfAttributes [Optional].
        pee_parameters_list: The pee_parameters_list of this NsacfFunctionSingleAllOfAttributes [Optional].
        priority_label: The priority_label of this NsacfFunctionSingleAllOfAttributes [Optional].
        supported_perf_metric_groups: The supported_perf_metric_groups of this NsacfFunctionSingleAllOfAttributes [Optional].
        supported_trace_metrics: The supported_trace_metrics of this NsacfFunctionSingleAllOfAttributes [Optional].
        managed_nf_profile: The managed_nf_profile of this NsacfFunctionSingleAllOfAttributes [Optional].
        nsacf_info_snssai: The nsacf_info_snssai of this NsacfFunctionSingleAllOfAttributes [Optional].
        tai_list: The tai_list of this NsacfFunctionSingleAllOfAttributes [Optional].
    """

    user_label: Optional[str] = Field(alias="userLabel", default=None)
    vnf_parameters_list: Optional[List[VnfParameter]] = Field(alias="vnfParametersList", default=None)
    pee_parameters_list: Optional[List[PeeParameter]] = Field(alias="peeParametersList", default=None)
    priority_label: Optional[int] = Field(alias="priorityLabel", default=None)
    supported_perf_metric_groups: Optional[List[SupportedPerfMetricGroup]] = Field(alias="supportedPerfMetricGroups", default=None)
    supported_trace_metrics: Optional[List[str]] = Field(alias="supportedTraceMetrics", default=None)
    managed_nf_profile: Optional[ManagedNFProfile] = Field(alias="managedNFProfile", default=None)
    nsacf_info_snssai: Optional[List[NsacfInfoSnssai]] = Field(alias="nsacfInfoSnssai", default=None)
    tai_list: Optional[List[Tai]] = Field(alias="taiList", default=None)

NsacfFunctionSingleAllOfAttributes.update_forward_refs()
