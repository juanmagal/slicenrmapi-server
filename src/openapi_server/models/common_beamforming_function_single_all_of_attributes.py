# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CommonBeamformingFunctionSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CommonBeamformingFunctionSingleAllOfAttributes - a model defined in OpenAPI

        coverage_shape: The coverage_shape of this CommonBeamformingFunctionSingleAllOfAttributes [Optional].
        digital_azimuth: The digital_azimuth of this CommonBeamformingFunctionSingleAllOfAttributes [Optional].
        digital_tilt: The digital_tilt of this CommonBeamformingFunctionSingleAllOfAttributes [Optional].
    """

    coverage_shape: Optional[int] = Field(alias="coverageShape", default=None)
    digital_azimuth: Optional[int] = Field(alias="digitalAzimuth", default=None)
    digital_tilt: Optional[int] = Field(alias="digitalTilt", default=None)

    @validator("coverage_shape")
    def coverage_shape_max(cls, value):
        assert value <= 65535
        return value

    @validator("digital_azimuth")
    def digital_azimuth_max(cls, value):
        assert value <= 1800
        return value

    @validator("digital_azimuth")
    def digital_azimuth_min(cls, value):
        assert value >= -1800
        return value

    @validator("digital_tilt")
    def digital_tilt_max(cls, value):
        assert value <= 900
        return value

    @validator("digital_tilt")
    def digital_tilt_min(cls, value):
        assert value >= -900
        return value

CommonBeamformingFunctionSingleAllOfAttributes.update_forward_refs()
