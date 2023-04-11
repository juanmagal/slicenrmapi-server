# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class DLBOFunctionSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DLBOFunctionSingleAllOfAttributes - a model defined in OpenAPI

        dlbo_control: The dlbo_control of this DLBOFunctionSingleAllOfAttributes [Optional].
        maximum_deviation_ho_trigger: The maximum_deviation_ho_trigger of this DLBOFunctionSingleAllOfAttributes [Optional].
        minimum_time_between_ho_trigger_change: The minimum_time_between_ho_trigger_change of this DLBOFunctionSingleAllOfAttributes [Optional].
    """

    dlbo_control: Optional[bool] = Field(alias="dlboControl", default=None)
    maximum_deviation_ho_trigger: Optional[int] = Field(alias="maximumDeviationHoTrigger", default=None)
    minimum_time_between_ho_trigger_change: Optional[int] = Field(alias="minimumTimeBetweenHoTriggerChange", default=None)

    @validator("maximum_deviation_ho_trigger")
    def maximum_deviation_ho_trigger_max(cls, value):
        assert value <= 20
        return value

    @validator("maximum_deviation_ho_trigger")
    def maximum_deviation_ho_trigger_min(cls, value):
        assert value >= -20
        return value

    @validator("minimum_time_between_ho_trigger_change")
    def minimum_time_between_ho_trigger_change_max(cls, value):
        assert value <= 604800
        return value

    @validator("minimum_time_between_ho_trigger_change")
    def minimum_time_between_ho_trigger_change_min(cls, value):
        assert value >= 0
        return value

DLBOFunctionSingleAllOfAttributes.update_forward_refs()