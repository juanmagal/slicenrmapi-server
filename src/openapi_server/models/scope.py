# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.scope_type import ScopeType


class Scope(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Scope - a model defined in OpenAPI

        scope_type: The scope_type of this Scope [Optional].
        scope_level: The scope_level of this Scope [Optional].
    """

    scope_type: Optional[ScopeType] = Field(alias="scopeType", default=None)
    scope_level: Optional[int] = Field(alias="scopeLevel", default=None)

Scope.update_forward_refs()
