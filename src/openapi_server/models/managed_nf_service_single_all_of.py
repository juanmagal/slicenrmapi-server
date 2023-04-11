# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.managed_nf_service_single_all_of_attributes import ManagedNFServiceSingleAllOfAttributes


class ManagedNFServiceSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ManagedNFServiceSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this ManagedNFServiceSingleAllOf [Optional].
    """

    attributes: Optional[ManagedNFServiceSingleAllOfAttributes] = Field(alias="attributes", default=None)

ManagedNFServiceSingleAllOf.update_forward_refs()
