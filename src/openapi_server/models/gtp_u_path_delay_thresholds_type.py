# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class GtpUPathDelayThresholdsType(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GtpUPathDelayThresholdsType - a model defined in OpenAPI

        n3_average_packet_delay_threshold: The n3_average_packet_delay_threshold of this GtpUPathDelayThresholdsType [Optional].
        n3_min_packet_delay_threshold: The n3_min_packet_delay_threshold of this GtpUPathDelayThresholdsType [Optional].
        n3_max_packet_delay_threshold: The n3_max_packet_delay_threshold of this GtpUPathDelayThresholdsType [Optional].
        n9_average_packet_delay_threshold: The n9_average_packet_delay_threshold of this GtpUPathDelayThresholdsType [Optional].
        n9_min_packet_delay_threshold: The n9_min_packet_delay_threshold of this GtpUPathDelayThresholdsType [Optional].
        n9_max_packet_delay_threshold: The n9_max_packet_delay_threshold of this GtpUPathDelayThresholdsType [Optional].
    """

    n3_average_packet_delay_threshold: Optional[int] = Field(alias="n3AveragePacketDelayThreshold", default=None)
    n3_min_packet_delay_threshold: Optional[int] = Field(alias="n3MinPacketDelayThreshold", default=None)
    n3_max_packet_delay_threshold: Optional[int] = Field(alias="n3MaxPacketDelayThreshold", default=None)
    n9_average_packet_delay_threshold: Optional[int] = Field(alias="n9AveragePacketDelayThreshold", default=None)
    n9_min_packet_delay_threshold: Optional[int] = Field(alias="n9MinPacketDelayThreshold", default=None)
    n9_max_packet_delay_threshold: Optional[int] = Field(alias="n9MaxPacketDelayThreshold", default=None)

GtpUPathDelayThresholdsType.update_forward_refs()
