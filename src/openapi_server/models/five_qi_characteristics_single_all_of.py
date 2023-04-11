# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.packet_error_rate import PacketErrorRate


class FiveQICharacteristicsSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FiveQICharacteristicsSingleAllOf - a model defined in OpenAPI

        five_qi_value: The five_qi_value of this FiveQICharacteristicsSingleAllOf [Optional].
        resource_type: The resource_type of this FiveQICharacteristicsSingleAllOf [Optional].
        priority_level: The priority_level of this FiveQICharacteristicsSingleAllOf [Optional].
        packet_delay_budget: The packet_delay_budget of this FiveQICharacteristicsSingleAllOf [Optional].
        packet_error_rate: The packet_error_rate of this FiveQICharacteristicsSingleAllOf [Optional].
        averaging_window: The averaging_window of this FiveQICharacteristicsSingleAllOf [Optional].
        maximum_data_burst_volume: The maximum_data_burst_volume of this FiveQICharacteristicsSingleAllOf [Optional].
    """

    five_qi_value: Optional[int] = Field(alias="fiveQIValue", default=None)
    resource_type: Optional[str] = Field(alias="resourceType", default=None)
    priority_level: Optional[int] = Field(alias="priorityLevel", default=None)
    packet_delay_budget: Optional[int] = Field(alias="packetDelayBudget", default=None)
    packet_error_rate: Optional[PacketErrorRate] = Field(alias="packetErrorRate", default=None)
    averaging_window: Optional[int] = Field(alias="averagingWindow", default=None)
    maximum_data_burst_volume: Optional[int] = Field(alias="maximumDataBurstVolume", default=None)

FiveQICharacteristicsSingleAllOf.update_forward_refs()
