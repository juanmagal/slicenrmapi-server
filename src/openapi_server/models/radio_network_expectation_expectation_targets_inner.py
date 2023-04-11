# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.ave_dlranue_thpt_target import AveDLRANUEThptTarget
from openapi_server.models.ave_ulranue_thpt_target import AveULRANUEThptTarget
from openapi_server.models.condition import Condition
from openapi_server.models.expectation_target import ExpectationTarget
from openapi_server.models.fulfilment_info import FulfilmentInfo
from openapi_server.models.low_dlranue_thpt_ratio_target import LowDLRANUEThptRatioTarget
from openapi_server.models.low_sinr_ratio_target import LowSINRRatioTarget
from openapi_server.models.low_ulranue_thpt_ratio_target import LowULRANUEThptRatioTarget
from openapi_server.models.target_context import TargetContext
from openapi_server.models.weak_rsrp_ratio_target import WeakRSRPRatioTarget


class RadioNetworkExpectationExpectationTargetsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RadioNetworkExpectationExpectationTargetsInner - a model defined in OpenAPI

        target_name: The target_name of this RadioNetworkExpectationExpectationTargetsInner [Optional].
        target_condition: The target_condition of this RadioNetworkExpectationExpectationTargetsInner [Optional].
        target_value_range: The target_value_range of this RadioNetworkExpectationExpectationTargetsInner [Optional].
        target_contexts: The target_contexts of this RadioNetworkExpectationExpectationTargetsInner [Optional].
        target_fulfilment_info: The target_fulfilment_info of this RadioNetworkExpectationExpectationTargetsInner [Optional].
    """

    target_name: Optional[str] = Field(alias="targetName", default=None)
    target_condition: Optional[Condition] = Field(alias="targetCondition", default=None)
    target_value_range: Optional[float] = Field(alias="targetValueRange", default=None)
    target_contexts: Optional[List[TargetContext]] = Field(alias="targetContexts", default=None)
    target_fulfilment_info: Optional[FulfilmentInfo] = Field(alias="targetFulfilmentInfo", default=None)

RadioNetworkExpectationExpectationTargetsInner.update_forward_refs()
