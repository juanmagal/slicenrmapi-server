# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.comm_model import CommModel
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.vnf_parameter import VnfParameter


class LmfFunctionSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LmfFunctionSingleAllOfAttributes - a model defined in OpenAPI

        user_label: The user_label of this LmfFunctionSingleAllOfAttributes [Optional].
        vnf_parameters_list: The vnf_parameters_list of this LmfFunctionSingleAllOfAttributes [Optional].
        pee_parameters_list: The pee_parameters_list of this LmfFunctionSingleAllOfAttributes [Optional].
        priority_label: The priority_label of this LmfFunctionSingleAllOfAttributes [Optional].
        supported_perf_metric_groups: The supported_perf_metric_groups of this LmfFunctionSingleAllOfAttributes [Optional].
        supported_trace_metrics: The supported_trace_metrics of this LmfFunctionSingleAllOfAttributes [Optional].
        plmn_id_list: The plmn_id_list of this LmfFunctionSingleAllOfAttributes [Optional].
        managed_nf_profile: The managed_nf_profile of this LmfFunctionSingleAllOfAttributes [Optional].
        comm_model_list: The comm_model_list of this LmfFunctionSingleAllOfAttributes [Optional].
    """

    user_label: Optional[str] = Field(alias="userLabel", default=None)
    vnf_parameters_list: Optional[List[VnfParameter]] = Field(alias="vnfParametersList", default=None)
    pee_parameters_list: Optional[List[PeeParameter]] = Field(alias="peeParametersList", default=None)
    priority_label: Optional[int] = Field(alias="priorityLabel", default=None)
    supported_perf_metric_groups: Optional[List[SupportedPerfMetricGroup]] = Field(alias="supportedPerfMetricGroups", default=None)
    supported_trace_metrics: Optional[List[str]] = Field(alias="supportedTraceMetrics", default=None)
    plmn_id_list: Optional[List[PlmnId]] = Field(alias="plmnIdList", default=None)
    managed_nf_profile: Optional[ManagedNFProfile] = Field(alias="managedNFProfile", default=None)
    comm_model_list: Optional[List[CommModel]] = Field(alias="commModelList", default=None)

LmfFunctionSingleAllOfAttributes.update_forward_refs()
