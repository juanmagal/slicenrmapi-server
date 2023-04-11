# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.activity_factor_target import ActivityFactorTarget
from openapi_server.models.condition import Condition
from openapi_server.models.dl_latency_target import DLLatencyTarget
from openapi_server.models.dl_thpt_per_ue_target import DLThptPerUETarget
from openapi_server.models.expectation_target import ExpectationTarget
from openapi_server.models.max_numberof_ues_target import MaxNumberofUEsTarget
from openapi_server.models.target_context import TargetContext
from openapi_server.models.ue_speed_target import UESpeedTarget
from openapi_server.models.ul_latency_target import ULLatencyTarget
from openapi_server.models.ul_thpt_per_ue_target import ULThptPerUETarget


class ServiceSupportExpectationExpectationTargetsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceSupportExpectationExpectationTargetsInner - a model defined in OpenAPI

        target_name: The target_name of this ServiceSupportExpectationExpectationTargetsInner [Optional].
        target_condition: The target_condition of this ServiceSupportExpectationExpectationTargetsInner [Optional].
        target_value_range: The target_value_range of this ServiceSupportExpectationExpectationTargetsInner [Optional].
        target_contexts: The target_contexts of this ServiceSupportExpectationExpectationTargetsInner [Optional].
    """

    target_name: Optional[str] = Field(alias="targetName", default=None)
    target_condition: Optional[Condition] = Field(alias="targetCondition", default=None)
    target_value_range: Optional[float] = Field(alias="targetValueRange", default=None)
    target_contexts: Optional[List[TargetContext]] = Field(alias="targetContexts", default=None)

ServiceSupportExpectationExpectationTargetsInner.update_forward_refs()