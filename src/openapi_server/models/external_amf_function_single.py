# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.external_amf_function_single_all_of_attributes import ExternalAmfFunctionSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class ExternalAmfFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ExternalAmfFunctionSingle - a model defined in OpenAPI

        id: The id of this ExternalAmfFunctionSingle.
        object_class: The object_class of this ExternalAmfFunctionSingle [Optional].
        object_instance: The object_instance of this ExternalAmfFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this ExternalAmfFunctionSingle [Optional].
        attributes: The attributes of this ExternalAmfFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[ExternalAmfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)

ExternalAmfFunctionSingle.update_forward_refs()