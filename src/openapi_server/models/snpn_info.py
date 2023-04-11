# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.snpn_id import SnpnId
from openapi_server.models.snssai import Snssai


class SnpnInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SnpnInfo - a model defined in OpenAPI

        snpn_id: The snpn_id of this SnpnInfo [Optional].
        snssai: The snssai of this SnpnInfo [Optional].
    """

    snpn_id: Optional[SnpnId] = Field(alias="snpnId", default=None)
    snssai: Optional[Snssai] = Field(alias="snssai", default=None)

SnpnInfo.update_forward_refs()