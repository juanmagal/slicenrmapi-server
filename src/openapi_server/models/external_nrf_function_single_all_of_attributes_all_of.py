# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.plmn_id import PlmnId


class ExternalNrfFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ExternalNrfFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        plmn_id_list: The plmn_id_list of this ExternalNrfFunctionSingleAllOfAttributesAllOf [Optional].
    """

    plmn_id_list: Optional[List[PlmnId]] = Field(alias="plmnIdList", default=None)

ExternalNrfFunctionSingleAllOfAttributesAllOf.update_forward_refs()
