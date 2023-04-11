# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.plmn_id import PlmnId


class Tai(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Tai - a model defined in OpenAPI

        plmn_id: The plmn_id of this Tai [Optional].
        nr_tac: The nr_tac of this Tai [Optional].
    """

    plmn_id: Optional[PlmnId] = Field(alias="plmnId", default=None)
    nr_tac: Optional[int] = Field(alias="nrTac", default=None)

    @validator("nr_tac")
    def nr_tac_max(cls, value):
        assert value <= 16777215
        return value

Tai.update_forward_refs()
