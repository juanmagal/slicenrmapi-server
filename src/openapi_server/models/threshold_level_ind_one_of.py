# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.threshold_hysteresis import ThresholdHysteresis


class ThresholdLevelIndOneOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ThresholdLevelIndOneOf - a model defined in OpenAPI

        up: The up of this ThresholdLevelIndOneOf [Optional].
    """

    up: Optional[ThresholdHysteresis] = Field(alias="up", default=None)

ThresholdLevelIndOneOf.update_forward_refs()
