# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.sepp_type import SEPPType


class SeppFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SeppFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        plmn_id: The plmn_id of this SeppFunctionSingleAllOfAttributesAllOf [Optional].
        s_epp_type: The s_epp_type of this SeppFunctionSingleAllOfAttributesAllOf [Optional].
        s_eppid: The s_eppid of this SeppFunctionSingleAllOfAttributesAllOf [Optional].
        fqdn: The fqdn of this SeppFunctionSingleAllOfAttributesAllOf [Optional].
    """

    plmn_id: Optional[PlmnId] = Field(alias="plmnId", default=None)
    s_epp_type: Optional[SEPPType] = Field(alias="sEPPType", default=None)
    s_eppid: Optional[int] = Field(alias="sEPPId", default=None)
    fqdn: Optional[str] = Field(alias="fqdn", default=None)

SeppFunctionSingleAllOfAttributesAllOf.update_forward_refs()