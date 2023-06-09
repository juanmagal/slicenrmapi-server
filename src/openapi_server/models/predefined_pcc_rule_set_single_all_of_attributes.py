# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.pcc_rule import PccRule


class PredefinedPccRuleSetSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PredefinedPccRuleSetSingleAllOfAttributes - a model defined in OpenAPI

        predefined_pcc_rules: The predefined_pcc_rules of this PredefinedPccRuleSetSingleAllOfAttributes [Optional].
    """

    predefined_pcc_rules: Optional[List[PccRule]] = Field(alias="predefinedPccRules", default=None)

PredefinedPccRuleSetSingleAllOfAttributes.update_forward_refs()
