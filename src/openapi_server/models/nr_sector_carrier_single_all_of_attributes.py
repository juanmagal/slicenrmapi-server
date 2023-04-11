# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.pee_parameter import PeeParameter
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup
from openapi_server.models.tx_direction import TxDirection
from openapi_server.models.vnf_parameter import VnfParameter


class NrSectorCarrierSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NrSectorCarrierSingleAllOfAttributes - a model defined in OpenAPI

        user_label: The user_label of this NrSectorCarrierSingleAllOfAttributes [Optional].
        vnf_parameters_list: The vnf_parameters_list of this NrSectorCarrierSingleAllOfAttributes [Optional].
        pee_parameters_list: The pee_parameters_list of this NrSectorCarrierSingleAllOfAttributes [Optional].
        priority_label: The priority_label of this NrSectorCarrierSingleAllOfAttributes [Optional].
        supported_perf_metric_groups: The supported_perf_metric_groups of this NrSectorCarrierSingleAllOfAttributes [Optional].
        supported_trace_metrics: The supported_trace_metrics of this NrSectorCarrierSingleAllOfAttributes [Optional].
        tx_direction: The tx_direction of this NrSectorCarrierSingleAllOfAttributes [Optional].
        configured_max_tx_power: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributes [Optional].
        arfcn_dl: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributes [Optional].
        arfcn_ul: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributes [Optional].
        b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributes [Optional].
        b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributes [Optional].
        sector_equipment_function_ref: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributes [Optional].
    """

    user_label: Optional[str] = Field(alias="userLabel", default=None)
    vnf_parameters_list: Optional[List[VnfParameter]] = Field(alias="vnfParametersList", default=None)
    pee_parameters_list: Optional[List[PeeParameter]] = Field(alias="peeParametersList", default=None)
    priority_label: Optional[int] = Field(alias="priorityLabel", default=None)
    supported_perf_metric_groups: Optional[List[SupportedPerfMetricGroup]] = Field(alias="supportedPerfMetricGroups", default=None)
    supported_trace_metrics: Optional[List[str]] = Field(alias="supportedTraceMetrics", default=None)
    tx_direction: Optional[TxDirection] = Field(alias="txDirection", default=None)
    configured_max_tx_power: Optional[int] = Field(alias="configuredMaxTxPower", default=None)
    arfcn_dl: Optional[int] = Field(alias="arfcnDL", default=None)
    arfcn_ul: Optional[int] = Field(alias="arfcnUL", default=None)
    b_s_channel_bw_dl: Optional[int] = Field(alias="bSChannelBwDL", default=None)
    b_s_channel_bw_ul: Optional[int] = Field(alias="bSChannelBwUL", default=None)
    sector_equipment_function_ref: Optional[str] = Field(alias="sectorEquipmentFunctionRef", default=None)

NrSectorCarrierSingleAllOfAttributes.update_forward_refs()
