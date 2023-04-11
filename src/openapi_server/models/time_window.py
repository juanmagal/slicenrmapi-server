# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class TimeWindow(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TimeWindow - a model defined in OpenAPI

        start_time: The start_time of this TimeWindow [Optional].
        end_time: The end_time of this TimeWindow [Optional].
    """

    start_time: Optional[datetime] = Field(alias="startTime", default=None)
    end_time: Optional[datetime] = Field(alias="endTime", default=None)

TimeWindow.update_forward_refs()
