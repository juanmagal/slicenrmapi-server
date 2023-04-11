# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.event_threshold_type_event_threshold1_f import EventThresholdTypeEventThreshold1F
from openapi_server.models.event_threshold_type_event_threshold_rsrp import EventThresholdTypeEventThresholdRSRP
from openapi_server.models.event_threshold_type_event_threshold_rsrq import EventThresholdTypeEventThresholdRSRQ


class EventThresholdType(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EventThresholdType - a model defined in OpenAPI

        event_threshold_rsrp: The event_threshold_rsrp of this EventThresholdType [Optional].
        event_threshold_rsrq: The event_threshold_rsrq of this EventThresholdType [Optional].
        event_threshold1_f: The event_threshold1_f of this EventThresholdType [Optional].
        event_threshold1_i: The event_threshold1_i of this EventThresholdType [Optional].
    """

    event_threshold_rsrp: Optional[EventThresholdTypeEventThresholdRSRP] = Field(alias="EventThresholdRSRP", default=None)
    event_threshold_rsrq: Optional[EventThresholdTypeEventThresholdRSRQ] = Field(alias="EventThresholdRSRQ", default=None)
    event_threshold1_f: Optional[EventThresholdTypeEventThreshold1F] = Field(alias="EventThreshold1F", default=None)
    event_threshold1_i: Optional[int] = Field(alias="EventThreshold1I", default=None)

    @validator("event_threshold1_i")
    def event_threshold1_i_max(cls, value):
        assert value <= 25
        return value

    @validator("event_threshold1_i")
    def event_threshold1_i_min(cls, value):
        assert value >= -120
        return value

EventThresholdType.update_forward_refs()
