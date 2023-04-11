# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.access_type import AccessType
from openapi_server.models.access_type_rm import AccessTypeRm
from openapi_server.models.steer_mode_value import SteerModeValue


class SteeringMode(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SteeringMode - a model defined in OpenAPI

        steer_mode_value: The steer_mode_value of this SteeringMode [Optional].
        active: The active of this SteeringMode [Optional].
        standby: The standby of this SteeringMode [Optional].
        three_g_load: The three_g_load of this SteeringMode [Optional].
        prio_acc: The prio_acc of this SteeringMode [Optional].
    """

    steer_mode_value: Optional[SteerModeValue] = Field(alias="steerModeValue", default=None)
    active: Optional[AccessType] = Field(alias="active", default=None)
    standby: Optional[AccessTypeRm] = Field(alias="standby", default=None)
    three_g_load: Optional[int] = Field(alias="threeGLoad", default=None)
    prio_acc: Optional[AccessType] = Field(alias="prioAcc", default=None)

    @validator("three_g_load")
    def three_g_load_min(cls, value):
        assert value >= 0
        return value

SteeringMode.update_forward_refs()