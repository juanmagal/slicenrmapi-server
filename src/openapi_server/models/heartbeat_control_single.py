# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.heartbeat_control_single_all_of_attributes import HeartbeatControlSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class HeartbeatControlSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    HeartbeatControlSingle - a model defined in OpenAPI

        id: The id of this HeartbeatControlSingle.
        object_class: The object_class of this HeartbeatControlSingle [Optional].
        object_instance: The object_instance of this HeartbeatControlSingle [Optional].
        vs_data_container: The vs_data_container of this HeartbeatControlSingle [Optional].
        attributes: The attributes of this HeartbeatControlSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[HeartbeatControlSingleAllOfAttributes] = Field(alias="attributes", default=None)

HeartbeatControlSingle.update_forward_refs()
