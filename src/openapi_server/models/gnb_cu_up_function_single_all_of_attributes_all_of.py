# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.plmn_info import PlmnInfo


class GnbCuUpFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GnbCuUpFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        gnb_id: The gnb_id of this GnbCuUpFunctionSingleAllOfAttributesAllOf [Optional].
        gnb_id_length: The gnb_id_length of this GnbCuUpFunctionSingleAllOfAttributesAllOf [Optional].
        gnb_cu_up_id: The gnb_cu_up_id of this GnbCuUpFunctionSingleAllOfAttributesAllOf [Optional].
        plmn_info_list: The plmn_info_list of this GnbCuUpFunctionSingleAllOfAttributesAllOf [Optional].
        configurable5_qi_set_ref: The configurable5_qi_set_ref of this GnbCuUpFunctionSingleAllOfAttributesAllOf [Optional].
        dynamic5_qi_set_ref: The dynamic5_qi_set_ref of this GnbCuUpFunctionSingleAllOfAttributesAllOf [Optional].
    """

    gnb_id: Optional[str] = Field(alias="gnbId", default=None)
    gnb_id_length: Optional[int] = Field(alias="gnbIdLength", default=None)
    gnb_cu_up_id: Optional[float] = Field(alias="gnbCuUpId", default=None)
    plmn_info_list: Optional[List[PlmnInfo]] = Field(alias="plmnInfoList", default=None)
    configurable5_qi_set_ref: Optional[str] = Field(alias="configurable5QISetRef", default=None)
    dynamic5_qi_set_ref: Optional[str] = Field(alias="dynamic5QISetRef", default=None)

    @validator("gnb_id_length")
    def gnb_id_length_max(cls, value):
        assert value <= 32
        return value

    @validator("gnb_id_length")
    def gnb_id_length_min(cls, value):
        assert value >= 22
        return value

    @validator("gnb_cu_up_id")
    def gnb_cu_up_id_max(cls, value):
        assert value <= 68719476735
        return value

    @validator("gnb_cu_up_id")
    def gnb_cu_up_id_min(cls, value):
        assert value >= 0
        return value

GnbCuUpFunctionSingleAllOfAttributesAllOf.update_forward_refs()
