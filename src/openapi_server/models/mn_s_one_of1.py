# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.managed_element_single import ManagedElementSingle


class MnSOneOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MnSOneOf1 - a model defined in OpenAPI

        managed_element: The managed_element of this MnSOneOf1 [Optional].
    """

    managed_element: Optional[List[ManagedElementSingle]] = Field(alias="ManagedElement", default=None)

MnSOneOf1.update_forward_refs()
