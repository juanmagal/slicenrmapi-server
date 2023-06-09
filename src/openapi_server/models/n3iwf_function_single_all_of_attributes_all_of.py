# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.comm_model import CommModel
from openapi_server.models.plmn_id import PlmnId


class N3iwfFunctionSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    N3iwfFunctionSingleAllOfAttributesAllOf - a model defined in OpenAPI

        plmn_id_list: The plmn_id_list of this N3iwfFunctionSingleAllOfAttributesAllOf [Optional].
        comm_model_list: The comm_model_list of this N3iwfFunctionSingleAllOfAttributesAllOf [Optional].
    """

    plmn_id_list: Optional[List[PlmnId]] = Field(alias="plmnIdList", default=None)
    comm_model_list: Optional[List[CommModel]] = Field(alias="commModelList", default=None)

N3iwfFunctionSingleAllOfAttributesAllOf.update_forward_refs()
