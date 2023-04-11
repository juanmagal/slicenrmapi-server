# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.nf_profile import NFProfile
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.snssai import Snssai


class NrfFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NrfFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        plmn_id_list: The plmn_id_list of this NrfFunctionSingleAllOfAttributesAllOf [Optional].
        s_bi_fqdn: The s_bi_fqdn of this NrfFunctionSingleAllOfAttributesAllOf [Optional].
        c_nsiid_list: The c_nsiid_list of this NrfFunctionSingleAllOfAttributesAllOf [Optional].
        n_f_profile_list: The n_f_profile_list of this NrfFunctionSingleAllOfAttributesAllOf [Optional].
        snssai_list: The snssai_list of this NrfFunctionSingleAllOfAttributesAllOf [Optional].
    """

    plmn_id_list: Optional[List[PlmnId]] = Field(alias="plmnIdList", default=None)
    s_bi_fqdn: Optional[str] = Field(alias="sBIFqdn", default=None)
    c_nsiid_list: Optional[List[str]] = Field(alias="cNSIIdList", default=None)
    n_f_profile_list: Optional[List[NFProfile]] = Field(alias="nFProfileList", default=None)
    snssai_list: Optional[List[Snssai]] = Field(alias="snssaiList", default=None)

NrfFunctionSingleAllOfAttributesAllOf.update_forward_refs()