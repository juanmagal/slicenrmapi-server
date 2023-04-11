# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn31_single import EPN31Single


class NssfFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NssfFunctionSingleAllOf1 - a model defined in OpenAPI

        ep_n22: The ep_n22 of this NssfFunctionSingleAllOf1 [Optional].
        ep_n31: The ep_n31 of this NssfFunctionSingleAllOf1 [Optional].
    """

    ep_n22: Optional[List[EPN22Single]] = Field(alias="EP_N22", default=None)
    ep_n31: Optional[List[EPN31Single]] = Field(alias="EP_N31", default=None)

NssfFunctionSingleAllOf1.update_forward_refs()