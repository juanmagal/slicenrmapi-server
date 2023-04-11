# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UeAccDelayProbilityDist(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UeAccDelayProbilityDist - a model defined in OpenAPI

        target_probability: The target_probability of this UeAccDelayProbilityDist [Optional].
        accessdelay: The accessdelay of this UeAccDelayProbilityDist [Optional].
    """

    target_probability: Optional[int] = Field(alias="targetProbability", default=None)
    accessdelay: Optional[int] = Field(alias="accessdelay", default=None)

UeAccDelayProbilityDist.update_forward_refs()