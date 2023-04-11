# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.snssai import Snssai


class UdrFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UdrFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        plmn_id_list: The plmn_id_list of this UdrFunctionSingleAllOfAttributesAllOf [Optional].
        s_bi_fqdn: The s_bi_fqdn of this UdrFunctionSingleAllOfAttributesAllOf [Optional].
        snssai_list: The snssai_list of this UdrFunctionSingleAllOfAttributesAllOf [Optional].
        managed_nf_profile: The managed_nf_profile of this UdrFunctionSingleAllOfAttributesAllOf [Optional].
    """

    plmn_id_list: Optional[List[PlmnId]] = Field(alias="plmnIdList", default=None)
    s_bi_fqdn: Optional[str] = Field(alias="sBIFqdn", default=None)
    snssai_list: Optional[List[Snssai]] = Field(alias="snssaiList", default=None)
    managed_nf_profile: Optional[ManagedNFProfile] = Field(alias="managedNFProfile", default=None)

UdrFunctionSingleAllOfAttributesAllOf.update_forward_refs()
