# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.cell_state import CellState
from openapi_server.models.npn_identity import NpnIdentity
from openapi_server.models.operational_state import OperationalState
from openapi_server.models.plmn_info import PlmnInfo
from openapi_server.models.ssb_duration import SsbDuration
from openapi_server.models.ssb_periodicity import SsbPeriodicity
from openapi_server.models.ssb_sub_carrier_spacing import SsbSubCarrierSpacing


class NrCellDuSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NrCellDuSingleAllOfAttributesAllOf - a model defined in OpenAPI

        administrative_state: The administrative_state of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        operational_state: The operational_state of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        cell_local_id: The cell_local_id of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        cell_state: The cell_state of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        plmn_info_list: The plmn_info_list of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        npn_identity_list: The npn_identity_list of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        nr_pci: The nr_pci of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        nr_tac: The nr_tac of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        arfcn_dl: The arfcn_dl of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        arfcn_ul: The arfcn_ul of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        arfcn_sul: The arfcn_sul of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        b_s_channel_bw_sul: The b_s_channel_bw_sul of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        ssb_frequency: The ssb_frequency of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        ssb_periodicity: The ssb_periodicity of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        ssb_sub_carrier_spacing: The ssb_sub_carrier_spacing of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        ssb_offset: The ssb_offset of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        ssb_duration: The ssb_duration of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        nr_sector_carrier_ref: The nr_sector_carrier_ref of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        bwp_ref: The bwp_ref of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_start_time: The rim_rs_monitoring_start_time of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_stop_time: The rim_rs_monitoring_stop_time of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_window_duration: The rim_rs_monitoring_window_duration of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_window_starting_offset: The rim_rs_monitoring_window_starting_offset of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_window_periodicity: The rim_rs_monitoring_window_periodicity of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_occasion_interval: The rim_rs_monitoring_occasion_interval of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        rim_rs_monitoring_occasion_starting_offset: The rim_rs_monitoring_occasion_starting_offset of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        n_r_frequency_ref: The n_r_frequency_ref of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        victim_set_ref: The victim_set_ref of this NrCellDuSingleAllOfAttributesAllOf [Optional].
        aggressor_set_ref: The aggressor_set_ref of this NrCellDuSingleAllOfAttributesAllOf [Optional].
    """

    administrative_state: Optional[AdministrativeState] = Field(alias="administrativeState", default=None)
    operational_state: Optional[OperationalState] = Field(alias="operationalState", default=None)
    cell_local_id: Optional[int] = Field(alias="cellLocalId", default=None)
    cell_state: Optional[CellState] = Field(alias="cellState", default=None)
    plmn_info_list: Optional[List[PlmnInfo]] = Field(alias="plmnInfoList", default=None)
    npn_identity_list: Optional[List[NpnIdentity]] = Field(alias="npnIdentityList", default=None)
    nr_pci: Optional[int] = Field(alias="nrPci", default=None)
    nr_tac: Optional[int] = Field(alias="nrTac", default=None)
    arfcn_dl: Optional[int] = Field(alias="arfcnDL", default=None)
    arfcn_ul: Optional[int] = Field(alias="arfcnUL", default=None)
    arfcn_sul: Optional[int] = Field(alias="arfcnSUL", default=None)
    b_s_channel_bw_dl: Optional[int] = Field(alias="bSChannelBwDL", default=None)
    b_s_channel_bw_ul: Optional[int] = Field(alias="bSChannelBwUL", default=None)
    b_s_channel_bw_sul: Optional[int] = Field(alias="bSChannelBwSUL", default=None)
    ssb_frequency: Optional[int] = Field(alias="ssbFrequency", default=None)
    ssb_periodicity: Optional[SsbPeriodicity] = Field(alias="ssbPeriodicity", default=None)
    ssb_sub_carrier_spacing: Optional[SsbSubCarrierSpacing] = Field(alias="ssbSubCarrierSpacing", default=None)
    ssb_offset: Optional[int] = Field(alias="ssbOffset", default=None)
    ssb_duration: Optional[SsbDuration] = Field(alias="ssbDuration", default=None)
    nr_sector_carrier_ref: Optional[List[str]] = Field(alias="nrSectorCarrierRef", default=None)
    bwp_ref: Optional[List[str]] = Field(alias="bwpRef", default=None)
    rim_rs_monitoring_start_time: Optional[str] = Field(alias="rimRSMonitoringStartTime", default=None)
    rim_rs_monitoring_stop_time: Optional[str] = Field(alias="rimRSMonitoringStopTime", default=None)
    rim_rs_monitoring_window_duration: Optional[int] = Field(alias="rimRSMonitoringWindowDuration", default=None)
    rim_rs_monitoring_window_starting_offset: Optional[int] = Field(alias="rimRSMonitoringWindowStartingOffset", default=None)
    rim_rs_monitoring_window_periodicity: Optional[int] = Field(alias="rimRSMonitoringWindowPeriodicity", default=None)
    rim_rs_monitoring_occasion_interval: Optional[int] = Field(alias="rimRSMonitoringOccasionInterval", default=None)
    rim_rs_monitoring_occasion_starting_offset: Optional[int] = Field(alias="rimRSMonitoringOccasionStartingOffset", default=None)
    n_r_frequency_ref: Optional[str] = Field(alias="nRFrequencyRef", default=None)
    victim_set_ref: Optional[str] = Field(alias="victimSetRef", default=None)
    aggressor_set_ref: Optional[str] = Field(alias="aggressorSetRef", default=None)

    @validator("nr_pci")
    def nr_pci_max(cls, value):
        assert value <= 503
        return value

    @validator("nr_tac")
    def nr_tac_max(cls, value):
        assert value <= 16777215
        return value

    @validator("ssb_frequency")
    def ssb_frequency_max(cls, value):
        assert value <= 3279165
        return value

    @validator("ssb_frequency")
    def ssb_frequency_min(cls, value):
        assert value >= 0
        return value

    @validator("ssb_offset")
    def ssb_offset_max(cls, value):
        assert value <= 159
        return value

    @validator("ssb_offset")
    def ssb_offset_min(cls, value):
        assert value >= 0
        return value

NrCellDuSingleAllOfAttributesAllOf.update_forward_refs()