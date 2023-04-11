# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.q_offset_range_list import QOffsetRangeList
from openapi_server.models.t_reselection_nrsf import TReselectionNRSf


class NRFreqRelationSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NRFreqRelationSingleAllOfAttributes - a model defined in OpenAPI

        offset_mo: The offset_mo of this NRFreqRelationSingleAllOfAttributes [Optional].
        block_list_entry: The block_list_entry of this NRFreqRelationSingleAllOfAttributes [Optional].
        block_list_entry_idle_mode: The block_list_entry_idle_mode of this NRFreqRelationSingleAllOfAttributes [Optional].
        cell_reselection_priority: The cell_reselection_priority of this NRFreqRelationSingleAllOfAttributes [Optional].
        cell_reselection_sub_priority: The cell_reselection_sub_priority of this NRFreqRelationSingleAllOfAttributes [Optional].
        p_max: The p_max of this NRFreqRelationSingleAllOfAttributes [Optional].
        q_offset_freq: The q_offset_freq of this NRFreqRelationSingleAllOfAttributes [Optional].
        q_qual_min: The q_qual_min of this NRFreqRelationSingleAllOfAttributes [Optional].
        q_rx_lev_min: The q_rx_lev_min of this NRFreqRelationSingleAllOfAttributes [Optional].
        thresh_x_high_p: The thresh_x_high_p of this NRFreqRelationSingleAllOfAttributes [Optional].
        thresh_x_high_q: The thresh_x_high_q of this NRFreqRelationSingleAllOfAttributes [Optional].
        thresh_x_low_p: The thresh_x_low_p of this NRFreqRelationSingleAllOfAttributes [Optional].
        thresh_x_low_q: The thresh_x_low_q of this NRFreqRelationSingleAllOfAttributes [Optional].
        t_reselection_nr: The t_reselection_nr of this NRFreqRelationSingleAllOfAttributes [Optional].
        t_reselection_nrsf_high: The t_reselection_nrsf_high of this NRFreqRelationSingleAllOfAttributes [Optional].
        t_reselection_nrsf_medium: The t_reselection_nrsf_medium of this NRFreqRelationSingleAllOfAttributes [Optional].
        n_r_frequency_ref: The n_r_frequency_ref of this NRFreqRelationSingleAllOfAttributes [Optional].
    """

    offset_mo: Optional[QOffsetRangeList] = Field(alias="offsetMO", default=None)
    block_list_entry: Optional[List[int]] = Field(alias="blockListEntry", default=None)
    block_list_entry_idle_mode: Optional[int] = Field(alias="blockListEntryIdleMode", default=None)
    cell_reselection_priority: Optional[int] = Field(alias="cellReselectionPriority", default=None)
    cell_reselection_sub_priority: Optional[float] = Field(alias="cellReselectionSubPriority", default=None)
    p_max: Optional[int] = Field(alias="pMax", default=None)
    q_offset_freq: Optional[float] = Field(alias="qOffsetFreq", default=None)
    q_qual_min: Optional[float] = Field(alias="qQualMin", default=None)
    q_rx_lev_min: Optional[int] = Field(alias="qRxLevMin", default=None)
    thresh_x_high_p: Optional[int] = Field(alias="threshXHighP", default=None)
    thresh_x_high_q: Optional[int] = Field(alias="threshXHighQ", default=None)
    thresh_x_low_p: Optional[int] = Field(alias="threshXLowP", default=None)
    thresh_x_low_q: Optional[int] = Field(alias="threshXLowQ", default=None)
    t_reselection_nr: Optional[int] = Field(alias="tReselectionNr", default=None)
    t_reselection_nrsf_high: Optional[TReselectionNRSf] = Field(alias="tReselectionNRSfHigh", default=None)
    t_reselection_nrsf_medium: Optional[TReselectionNRSf] = Field(alias="tReselectionNRSfMedium", default=None)
    n_r_frequency_ref: Optional[str] = Field(alias="nRFrequencyRef", default=None)

    @validator("cell_reselection_sub_priority")
    def cell_reselection_sub_priority_max(cls, value):
        assert value <= 0.8
        return value

    @validator("cell_reselection_sub_priority")
    def cell_reselection_sub_priority_min(cls, value):
        assert value >= 0.2
        return value

    @validator("p_max")
    def p_max_max(cls, value):
        assert value <= 33
        return value

    @validator("p_max")
    def p_max_min(cls, value):
        assert value >= -30
        return value

    @validator("q_rx_lev_min")
    def q_rx_lev_min_max(cls, value):
        assert value <= -44
        return value

    @validator("q_rx_lev_min")
    def q_rx_lev_min_min(cls, value):
        assert value >= -140
        return value

    @validator("thresh_x_high_p")
    def thresh_x_high_p_max(cls, value):
        assert value <= 62
        return value

    @validator("thresh_x_high_p")
    def thresh_x_high_p_min(cls, value):
        assert value >= 0
        return value

    @validator("thresh_x_high_q")
    def thresh_x_high_q_max(cls, value):
        assert value <= 31
        return value

    @validator("thresh_x_high_q")
    def thresh_x_high_q_min(cls, value):
        assert value >= 0
        return value

    @validator("thresh_x_low_p")
    def thresh_x_low_p_max(cls, value):
        assert value <= 62
        return value

    @validator("thresh_x_low_p")
    def thresh_x_low_p_min(cls, value):
        assert value >= 0
        return value

    @validator("thresh_x_low_q")
    def thresh_x_low_q_max(cls, value):
        assert value <= 31
        return value

    @validator("thresh_x_low_q")
    def thresh_x_low_q_min(cls, value):
        assert value >= 0
        return value

    @validator("t_reselection_nr")
    def t_reselection_nr_max(cls, value):
        assert value <= 7
        return value

    @validator("t_reselection_nr")
    def t_reselection_nr_min(cls, value):
        assert value >= 0
        return value

NRFreqRelationSingleAllOfAttributes.update_forward_refs()