# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.area_of_interest import AreaOfInterest


class NodeFilter(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NodeFilter - a model defined in OpenAPI

        area_of_interest: The area_of_interest of this NodeFilter [Optional].
        network_domain: The network_domain of this NodeFilter [Optional].
        cp_up_type: The cp_up_type of this NodeFilter [Optional].
        sst: The sst of this NodeFilter [Optional].
    """

    area_of_interest: Optional[AreaOfInterest] = Field(alias="areaOfInterest", default=None)
    network_domain: Optional[str] = Field(alias="networkDomain", default=None)
    cp_up_type: Optional[str] = Field(alias="cpUpType", default=None)
    sst: Optional[int] = Field(alias="sst", default=None)

NodeFilter.update_forward_refs()
