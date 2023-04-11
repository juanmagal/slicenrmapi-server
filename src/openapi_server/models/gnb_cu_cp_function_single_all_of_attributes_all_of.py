# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.mapping_set_id_backhaul_address import MappingSetIDBackhaulAddress
from openapi_server.models.plmn_id import PlmnId
from openapi_server.models.tce_mapping_info import TceMappingInfo


class GnbCuCpFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GnbCuCpFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        gnb_id: The gnb_id of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        gnb_id_length: The gnb_id_length of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        gnb_cu_name: The gnb_cu_name of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        plmn_id: The plmn_id of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        x2_block_list: The x2_block_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        xn_block_list: The xn_block_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        x2_allow_list: The x2_allow_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        xn_allow_list: The xn_allow_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        x2_ho_black_list: The x2_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        xn_ho_black_list: The xn_ho_black_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        mapping_set_id_backhaul_address: The mapping_set_id_backhaul_address of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        tce_mapping_info_list: The tce_mapping_info_list of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        configurable5_qi_set_ref: The configurable5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        dynamic5_qi_set_ref: The dynamic5_qi_set_ref of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        d_cho_control: The d_cho_control of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
        d_dapsho_control: The d_dapsho_control of this GnbCuCpFunctionSingleAllOfAttributesAllOf [Optional].
    """

    gnb_id: Optional[str] = Field(alias="gnbId", default=None)
    gnb_id_length: Optional[int] = Field(alias="gnbIdLength", default=None)
    gnb_cu_name: Optional[str] = Field(alias="gnbCuName", default=None)
    plmn_id: Optional[PlmnId] = Field(alias="plmnId", default=None)
    x2_block_list: Optional[List[str]] = Field(alias="x2BlockList", default=None)
    xn_block_list: Optional[List[str]] = Field(alias="xnBlockList", default=None)
    x2_allow_list: Optional[List[str]] = Field(alias="x2AllowList", default=None)
    xn_allow_list: Optional[List[str]] = Field(alias="xnAllowList", default=None)
    x2_ho_black_list: Optional[List[str]] = Field(alias="x2HOBlackList", default=None)
    xn_ho_black_list: Optional[List[str]] = Field(alias="xnHOBlackList", default=None)
    mapping_set_id_backhaul_address: Optional[MappingSetIDBackhaulAddress] = Field(alias="mappingSetIDBackhaulAddress", default=None)
    tce_mapping_info_list: Optional[List[TceMappingInfo]] = Field(alias="tceMappingInfoList", default=None)
    configurable5_qi_set_ref: Optional[str] = Field(alias="configurable5QISetRef", default=None)
    dynamic5_qi_set_ref: Optional[str] = Field(alias="dynamic5QISetRef", default=None)
    d_cho_control: Optional[bool] = Field(alias="dCHOControl", default=None)
    d_dapsho_control: Optional[bool] = Field(alias="dDAPSHOControl", default=None)

    @validator("gnb_id_length")
    def gnb_id_length_max(cls, value):
        assert value <= 32
        return value

    @validator("gnb_id_length")
    def gnb_id_length_min(cls, value):
        assert value >= 22
        return value

    @validator("gnb_cu_name")
    def gnb_cu_name_max_length(cls, value):
        assert len(value) <= 150
        return value

GnbCuCpFunctionSingleAllOfAttributesAllOf.update_forward_refs()
