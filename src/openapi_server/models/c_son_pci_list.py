# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class CSonPciList(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CSonPciList - a model defined in OpenAPI

        nr_pci: The nr_pci of this CSonPciList [Optional].
    """

    nr_pci: Optional[int] = Field(alias="NRPci", default=None)

CSonPciList.update_forward_refs()
