# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.plmn_id import PlmnId


class ExternalGnbCuCpFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ExternalGnbCuCpFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        gnb_id: The gnb_id of this ExternalGnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        gnb_id_length: The gnb_id_length of this ExternalGnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        plmn_id: The plmn_id of this ExternalGnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
    """

    gnb_id: Optional[str] = Field(alias="gnbId", default=None)
    gnb_id_length: Optional[int] = Field(alias="gnbIdLength", default=None)
    plmn_id: Optional[PlmnId] = Field(alias="plmnId", default=None)

    @validator("gnb_id_length")
    def gnb_id_length_max(cls, value):
        assert value <= 32
        return value

    @validator("gnb_id_length")
    def gnb_id_length_min(cls, value):
        assert value >= 22
        return value

ExternalGnbCuCpFunctionSingleAllOfAttributesAllOf.update_forward_refs()
