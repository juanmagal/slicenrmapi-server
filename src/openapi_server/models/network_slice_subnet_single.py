# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.network_slice_subnet_single_all_of_attributes import NetworkSliceSubnetSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class NetworkSliceSubnetSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NetworkSliceSubnetSingle - a model defined in OpenAPI

        id: The id of this NetworkSliceSubnetSingle.
        object_class: The object_class of this NetworkSliceSubnetSingle [Optional].
        object_instance: The object_instance of this NetworkSliceSubnetSingle [Optional].
        vs_data_container: The vs_data_container of this NetworkSliceSubnetSingle [Optional].
        attributes: The attributes of this NetworkSliceSubnetSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[NetworkSliceSubnetSingleAllOfAttributes] = Field(alias="attributes", default=None)

NetworkSliceSubnetSingle.update_forward_refs()
