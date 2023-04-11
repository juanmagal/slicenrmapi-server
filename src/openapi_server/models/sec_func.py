# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SecFunc(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SecFunc - a model defined in OpenAPI

        sec_fun_id: The sec_fun_id of this SecFunc [Optional].
        sec_fun_type: The sec_fun_type of this SecFunc [Optional].
        sec_rules: The sec_rules of this SecFunc [Optional].
    """

    sec_fun_id: Optional[str] = Field(alias="secFunId", default=None)
    sec_fun_type: Optional[str] = Field(alias="secFunType", default=None)
    sec_rules: Optional[List[str]] = Field(alias="secRules", default=None)

SecFunc.update_forward_refs()
