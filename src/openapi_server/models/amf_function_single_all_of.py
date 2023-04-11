# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.amf_function_single_all_of_attributes import AmfFunctionSingleAllOfAttributes


class AmfFunctionSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AmfFunctionSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this AmfFunctionSingleAllOf [Optional].
    """

    attributes: Optional[AmfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)

AmfFunctionSingleAllOf.update_forward_refs()
