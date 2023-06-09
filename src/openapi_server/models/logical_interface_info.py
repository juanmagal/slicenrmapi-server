# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class LogicalInterfaceInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LogicalInterfaceInfo - a model defined in OpenAPI

        logical_interface_type: The logical_interface_type of this LogicalInterfaceInfo [Optional].
        logical_interface_id: The logical_interface_id of this LogicalInterfaceInfo [Optional].
    """

    logical_interface_type: Optional[str] = Field(alias="logicalInterfaceType", default=None)
    logical_interface_id: Optional[str] = Field(alias="logicalInterfaceId", default=None)

LogicalInterfaceInfo.update_forward_refs()
