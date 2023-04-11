# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class LoggingIntervalType(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LoggingIntervalType - a model defined in OpenAPI

        umts: The umts of this LoggingIntervalType [Optional].
        lte: The lte of this LoggingIntervalType [Optional].
        nr: The nr of this LoggingIntervalType [Optional].
    """

    umts: Optional[List[str]] = Field(alias="UMTS", default=None)
    lte: Optional[List[str]] = Field(alias="LTE", default=None)
    nr: Optional[List[str]] = Field(alias="NR", default=None)

LoggingIntervalType.update_forward_refs()
