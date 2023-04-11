# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.tx_direction import TxDirection


class NrSectorCarrierSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NrSectorCarrierSingleAllOfAttributesAllOf - a model defined in OpenAPI

        tx_direction: The tx_direction of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
        configured_max_tx_power: The configured_max_tx_power of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
        arfcn_dl: The arfcn_dl of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
        arfcn_ul: The arfcn_ul of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
        b_s_channel_bw_dl: The b_s_channel_bw_dl of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
        b_s_channel_bw_ul: The b_s_channel_bw_ul of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
        sector_equipment_function_ref: The sector_equipment_function_ref of this NrSectorCarrierSingleAllOfAttributesAllOf [Optional].
    """

    tx_direction: Optional[TxDirection] = Field(alias="txDirection", default=None)
    configured_max_tx_power: Optional[int] = Field(alias="configuredMaxTxPower", default=None)
    arfcn_dl: Optional[int] = Field(alias="arfcnDL", default=None)
    arfcn_ul: Optional[int] = Field(alias="arfcnUL", default=None)
    b_s_channel_bw_dl: Optional[int] = Field(alias="bSChannelBwDL", default=None)
    b_s_channel_bw_ul: Optional[int] = Field(alias="bSChannelBwUL", default=None)
    sector_equipment_function_ref: Optional[str] = Field(alias="sectorEquipmentFunctionRef", default=None)

NrSectorCarrierSingleAllOfAttributesAllOf.update_forward_refs()
