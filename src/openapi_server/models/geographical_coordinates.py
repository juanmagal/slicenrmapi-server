# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GeographicalCoordinates(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GeographicalCoordinates - a model defined in OpenAPI

        lattitude: The lattitude of this GeographicalCoordinates [Optional].
        longitude: The longitude of this GeographicalCoordinates [Optional].
    """

    lattitude: Optional[int] = Field(alias="lattitude", default=None)
    longitude: Optional[int] = Field(alias="longitude", default=None)

GeographicalCoordinates.update_forward_refs()