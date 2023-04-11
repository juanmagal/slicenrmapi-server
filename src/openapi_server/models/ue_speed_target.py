# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UESpeedTarget(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UESpeedTarget - a model defined in OpenAPI

        target_name: The target_name of this UESpeedTarget [Optional].
        target_condition: The target_condition of this UESpeedTarget [Optional].
        target_value_range: The target_value_range of this UESpeedTarget [Optional].
    """

    target_name: Optional[str] = Field(alias="targetName", default=None)
    target_condition: Optional[str] = Field(alias="targetCondition", default=None)
    target_value_range: Optional[int] = Field(alias="targetValueRange", default=None)

UESpeedTarget.update_forward_refs()
