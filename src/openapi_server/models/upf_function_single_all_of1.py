# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn6_single import EPN6Single
from openapi_server.models.epn9_single import EPN9Single
from openapi_server.models.eps5_u_single import EPS5USingle


class UpfFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UpfFunctionSingleAllOf1 - a model defined in OpenAPI

        ep_n3: The ep_n3 of this UpfFunctionSingleAllOf1 [Optional].
        ep_n4: The ep_n4 of this UpfFunctionSingleAllOf1 [Optional].
        ep_n6: The ep_n6 of this UpfFunctionSingleAllOf1 [Optional].
        ep_n9: The ep_n9 of this UpfFunctionSingleAllOf1 [Optional].
        ep_s5_u: The ep_s5_u of this UpfFunctionSingleAllOf1 [Optional].
    """

    ep_n3: Optional[List[EPN3Single]] = Field(alias="EP_N3", default=None)
    ep_n4: Optional[List[EPN4Single]] = Field(alias="EP_N4", default=None)
    ep_n6: Optional[List[EPN6Single]] = Field(alias="EP_N6", default=None)
    ep_n9: Optional[List[EPN9Single]] = Field(alias="EP_N9", default=None)
    ep_s5_u: Optional[List[EPS5USingle]] = Field(alias="EP_S5U", default=None)

UpfFunctionSingleAllOf1.update_forward_refs()
