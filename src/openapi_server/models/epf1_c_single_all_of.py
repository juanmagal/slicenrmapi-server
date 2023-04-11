# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epf1_c_single_all_of_attributes import EPF1CSingleAllOfAttributes


class EPF1CSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EPF1CSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this EPF1CSingleAllOf [Optional].
    """

    attributes: Optional[EPF1CSingleAllOfAttributes] = Field(alias="attributes", default=None)

EPF1CSingleAllOf.update_forward_refs()