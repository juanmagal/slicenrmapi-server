# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class TscaiInputContainer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TscaiInputContainer - a model defined in OpenAPI

        periodicity: The periodicity of this TscaiInputContainer [Optional].
        burst_arrival_time: The burst_arrival_time of this TscaiInputContainer [Optional].
        sur_time_in_num_msg: The sur_time_in_num_msg of this TscaiInputContainer [Optional].
        sur_time_in_time: The sur_time_in_time of this TscaiInputContainer [Optional].
    """

    periodicity: Optional[int] = Field(alias="periodicity", default=None)
    burst_arrival_time: Optional[datetime] = Field(alias="burstArrivalTime", default=None)
    sur_time_in_num_msg: Optional[int] = Field(alias="surTimeInNumMsg", default=None)
    sur_time_in_time: Optional[int] = Field(alias="surTimeInTime", default=None)

    @validator("periodicity")
    def periodicity_min(cls, value):
        assert value >= 0
        return value

    @validator("sur_time_in_num_msg")
    def sur_time_in_num_msg_min(cls, value):
        assert value >= 0
        return value

    @validator("sur_time_in_time")
    def sur_time_in_time_min(cls, value):
        assert value >= 0
        return value

TscaiInputContainer.update_forward_refs()