# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CellIndividualOffset(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CellIndividualOffset - a model defined in OpenAPI

        rsrp_offset_ssb: The rsrp_offset_ssb of this CellIndividualOffset [Optional].
        rsrq_offset_ssb: The rsrq_offset_ssb of this CellIndividualOffset [Optional].
        sinr_offset_ssb: The sinr_offset_ssb of this CellIndividualOffset [Optional].
        rsrp_offset_csi_rs: The rsrp_offset_csi_rs of this CellIndividualOffset [Optional].
        rsrq_offset_csi_rs: The rsrq_offset_csi_rs of this CellIndividualOffset [Optional].
        sinr_offset_csi_rs: The sinr_offset_csi_rs of this CellIndividualOffset [Optional].
    """

    rsrp_offset_ssb: Optional[int] = Field(alias="rsrpOffsetSSB", default=None)
    rsrq_offset_ssb: Optional[int] = Field(alias="rsrqOffsetSSB", default=None)
    sinr_offset_ssb: Optional[int] = Field(alias="sinrOffsetSSB", default=None)
    rsrp_offset_csi_rs: Optional[int] = Field(alias="rsrpOffsetCSI-RS", default=None)
    rsrq_offset_csi_rs: Optional[int] = Field(alias="rsrqOffsetCSI-RS", default=None)
    sinr_offset_csi_rs: Optional[int] = Field(alias="sinrOffsetCSI-RS", default=None)

CellIndividualOffset.update_forward_refs()
