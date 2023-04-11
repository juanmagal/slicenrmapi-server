# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class EUtranFrequencySingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EUtranFrequencySingleAllOfAttributes - a model defined in OpenAPI

        earfcn_dl: The earfcn_dl of this EUtranFrequencySingleAllOfAttributes [Optional].
        multi_band_info_list_eutra: The multi_band_info_list_eutra of this EUtranFrequencySingleAllOfAttributes [Optional].
    """

    earfcn_dl: Optional[int] = Field(alias="earfcnDL", default=None)
    multi_band_info_list_eutra: Optional[int] = Field(alias="multiBandInfoListEutra", default=None)

    @validator("earfcn_dl")
    def earfcn_dl_max(cls, value):
        assert value <= 262143
        return value

    @validator("earfcn_dl")
    def earfcn_dl_min(cls, value):
        assert value >= 0
        return value

    @validator("multi_band_info_list_eutra")
    def multi_band_info_list_eutra_max(cls, value):
        assert value <= 256
        return value

    @validator("multi_band_info_list_eutra")
    def multi_band_info_list_eutra_min(cls, value):
        assert value >= 1
        return value

EUtranFrequencySingleAllOfAttributes.update_forward_refs()
