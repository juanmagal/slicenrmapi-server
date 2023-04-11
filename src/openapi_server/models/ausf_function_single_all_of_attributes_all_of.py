# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.comm_model import CommModel
from openapi_server.models.managed_nf_profile import ManagedNFProfile
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.snssai import Snssai


class AusfFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AusfFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        plmn_id_list: The plmn_id_list of this AusfFunctionSingleAllOfAttributesAllOf [Optional].
        s_bi_fqdn: The s_bi_fqdn of this AusfFunctionSingleAllOfAttributesAllOf [Optional].
        snssai_list: The snssai_list of this AusfFunctionSingleAllOfAttributesAllOf [Optional].
        managed_nf_profile: The managed_nf_profile of this AusfFunctionSingleAllOfAttributesAllOf [Optional].
        comm_model_list: The comm_model_list of this AusfFunctionSingleAllOfAttributesAllOf [Optional].
    """

    plmn_id_list: Optional[List[PlmnId]] = Field(alias="plmnIdList", default=None)
    s_bi_fqdn: Optional[str] = Field(alias="sBIFqdn", default=None)
    snssai_list: Optional[List[Snssai]] = Field(alias="snssaiList", default=None)
    managed_nf_profile: Optional[ManagedNFProfile] = Field(alias="managedNFProfile", default=None)
    comm_model_list: Optional[List[CommModel]] = Field(alias="commModelList", default=None)

AusfFunctionSingleAllOfAttributesAllOf.update_forward_refs()
