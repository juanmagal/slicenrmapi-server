# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epf1_c_single_all_of_attributes import EPF1CSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class EPN10Single(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EPN10Single - a model defined in OpenAPI

        id: The id of this EPN10Single.
        object_class: The object_class of this EPN10Single [Optional].
        object_instance: The object_instance of this EPN10Single [Optional].
        vs_data_container: The vs_data_container of this EPN10Single [Optional].
        attributes: The attributes of this EPN10Single [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[EPF1CSingleAllOfAttributes] = Field(alias="attributes", default=None)

EPN10Single.update_forward_refs()
