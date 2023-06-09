# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.trace_job_attr import TraceJobAttr


class TraceJobSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TraceJobSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this TraceJobSingleAllOf [Optional].
        files: The files of this TraceJobSingleAllOf [Optional].
    """

    attributes: Optional[TraceJobAttr] = Field(alias="attributes", default=None)
    files: Optional[List[FilesSingle]] = Field(alias="Files", default=None)

TraceJobSingleAllOf.update_forward_refs()
