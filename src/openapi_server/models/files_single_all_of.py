# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.files_single_all_of_attributes import FilesSingleAllOfAttributes


class FilesSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FilesSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this FilesSingleAllOf [Optional].
    """

    attributes: Optional[FilesSingleAllOfAttributes] = Field(alias="attributes", default=None)

FilesSingleAllOf.update_forward_refs()
