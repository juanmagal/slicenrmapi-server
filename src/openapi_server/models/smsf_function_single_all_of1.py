# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn21_single import EPN21Single


class SmsfFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SmsfFunctionSingleAllOf1 - a model defined in OpenAPI

        ep_n20: The ep_n20 of this SmsfFunctionSingleAllOf1 [Optional].
        ep_n21: The ep_n21 of this SmsfFunctionSingleAllOf1 [Optional].
        ep_map_smsc: The ep_map_smsc of this SmsfFunctionSingleAllOf1 [Optional].
    """

    ep_n20: Optional[List[EPN20Single]] = Field(alias="EP_N20", default=None)
    ep_n21: Optional[List[EPN21Single]] = Field(alias="EP_N21", default=None)
    ep_map_smsc: Optional[List[EPMAPSMSCSingle]] = Field(alias="EP_MAP_SMSC", default=None)

SmsfFunctionSingleAllOf1.update_forward_refs()
