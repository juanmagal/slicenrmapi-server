# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.freq_info import FreqInfo


class AreaConfig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AreaConfig - a model defined in OpenAPI

        freq_info: The freq_info of this AreaConfig [Optional].
        pci_list: The pci_list of this AreaConfig [Optional].
    """

    freq_info: Optional[FreqInfo] = Field(alias="freqInfo", default=None)
    pci_list: Optional[List[int]] = Field(alias="pciList", default=None)

AreaConfig.update_forward_refs()