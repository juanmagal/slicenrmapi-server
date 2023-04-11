# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.rim_rs_global_single_all_of_attributes import RimRSGlobalSingleAllOfAttributes
from openapi_server.models.rim_rs_set_single import RimRSSetSingle


class RimRSGlobalSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RimRSGlobalSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this RimRSGlobalSingleAllOf [Optional].
        rim_rs_set: The rim_rs_set of this RimRSGlobalSingleAllOf [Optional].
    """

    attributes: Optional[RimRSGlobalSingleAllOfAttributes] = Field(alias="attributes", default=None)
    rim_rs_set: Optional[List[RimRSSetSingle]] = Field(alias="RimRSSet", default=None)

RimRSGlobalSingleAllOf.update_forward_refs()