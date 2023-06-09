# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class UPFConnectionInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UPFConnectionInfo - a model defined in OpenAPI

        u_pfip_address: The u_pfip_address of this UPFConnectionInfo [Optional].
        u_pf_ref: The u_pf_ref of this UPFConnectionInfo [Optional].
    """

    u_pfip_address: Optional[str] = Field(alias="uPFIpAddress", default=None)
    u_pf_ref: Optional[str] = Field(alias="uPFRef", default=None)

UPFConnectionInfo.update_forward_refs()
