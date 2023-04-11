# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn33_single import EPN33Single


class NefFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NefFunctionSingleAllOf1 - a model defined in OpenAPI

        ep_n33: The ep_n33 of this NefFunctionSingleAllOf1 [Optional].
    """

    ep_n33: Optional[List[EPN33Single]] = Field(alias="EP_N33", default=None)

NefFunctionSingleAllOf1.update_forward_refs()