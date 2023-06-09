# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.n3iwf_function_single_all_of_attributes import N3iwfFunctionSingleAllOfAttributes


class N3iwfFunctionSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    N3iwfFunctionSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this N3iwfFunctionSingleAllOf [Optional].
    """

    attributes: Optional[N3iwfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)

N3iwfFunctionSingleAllOf.update_forward_refs()
