# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.nssf_function_single_all_of_attributes import NssfFunctionSingleAllOfAttributes


class NssfFunctionSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NssfFunctionSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this NssfFunctionSingleAllOf [Optional].
    """

    attributes: Optional[NssfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)

NssfFunctionSingleAllOf.update_forward_refs()
