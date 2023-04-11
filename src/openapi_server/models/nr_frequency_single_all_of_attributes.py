# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.ssb_sub_carrier_spacing import SsbSubCarrierSpacing


class NRFrequencySingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NRFrequencySingleAllOfAttributes - a model defined in OpenAPI

        absolute_frequency_ssb: The absolute_frequency_ssb of this NRFrequencySingleAllOfAttributes [Optional].
        ssb_sub_carrier_spacing: The ssb_sub_carrier_spacing of this NRFrequencySingleAllOfAttributes [Optional].
        multi_frequency_band_list_nr: The multi_frequency_band_list_nr of this NRFrequencySingleAllOfAttributes [Optional].
    """

    absolute_frequency_ssb: Optional[int] = Field(alias="absoluteFrequencySSB", default=None)
    ssb_sub_carrier_spacing: Optional[SsbSubCarrierSpacing] = Field(alias="ssbSubCarrierSpacing", default=None)
    multi_frequency_band_list_nr: Optional[int] = Field(alias="multiFrequencyBandListNR", default=None)

    @validator("absolute_frequency_ssb")
    def absolute_frequency_ssb_max(cls, value):
        assert value <= 3279165
        return value

    @validator("absolute_frequency_ssb")
    def absolute_frequency_ssb_min(cls, value):
        assert value >= 0
        return value

    @validator("multi_frequency_band_list_nr")
    def multi_frequency_band_list_nr_max(cls, value):
        assert value <= 256
        return value

    @validator("multi_frequency_band_list_nr")
    def multi_frequency_band_list_nr_min(cls, value):
        assert value >= 1
        return value

NRFrequencySingleAllOfAttributes.update_forward_refs()