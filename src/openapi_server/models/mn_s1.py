# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.mn_s_one_of import MnSOneOf
from openapi_server.models.sub_network_single import SubNetworkSingle


class MnS1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MnS1 - a model defined in OpenAPI

        sub_network: The sub_network of this MnS1 [Optional].
    """

    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)

MnS1.update_forward_refs()