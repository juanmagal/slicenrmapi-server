# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.network_slice_single_all_of_attributes import NetworkSliceSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class NetworkSliceSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NetworkSliceSingle - a model defined in OpenAPI

        id: The id of this NetworkSliceSingle.
        object_class: The object_class of this NetworkSliceSingle [Optional].
        object_instance: The object_instance of this NetworkSliceSingle [Optional].
        vs_data_container: The vs_data_container of this NetworkSliceSingle [Optional].
        attributes: The attributes of this NetworkSliceSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[NetworkSliceSingleAllOfAttributes] = Field(alias="attributes", default=None)

NetworkSliceSingle.update_forward_refs()
