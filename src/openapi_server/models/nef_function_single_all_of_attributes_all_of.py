# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.snssai import Snssai
from openapi_server.models.tai import Tai
from openapi_server.models.tai_range import TaiRange


class NefFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NefFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        s_bi_fqdn: The s_bi_fqdn of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        snssai_list: The snssai_list of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        managed_nf_profile: The managed_nf_profile of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        capability_list: The capability_list of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        is_capif_sup: The is_capif_sup of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        tai_list: The tai_list of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        tai_range_list: The tai_range_list of this NefFunctionSingleAllOfAttributesAllOf [Optional].
        dnai: The dnai of this NefFunctionSingleAllOfAttributesAllOf [Optional].
    """

    s_bi_fqdn: Optional[str] = Field(alias="sBIFqdn", default=None)
    snssai_list: Optional[List[Snssai]] = Field(alias="snssaiList", default=None)
    managed_nf_profile: Optional[ManagedNFProfile] = Field(alias="managedNFProfile", default=None)
    capability_list: Optional[List[str]] = Field(alias="capabilityList", default=None)
    is_capif_sup: Optional[bool] = Field(alias="isCAPIFSup", default=None)
    tai_list: Optional[List[Tai]] = Field(alias="taiList", default=None)
    tai_range_list: Optional[List[TaiRange]] = Field(alias="taiRangeList", default=None)
    dnai: Optional[str] = Field(alias="dnai", default=None)

NefFunctionSingleAllOfAttributesAllOf.update_forward_refs()