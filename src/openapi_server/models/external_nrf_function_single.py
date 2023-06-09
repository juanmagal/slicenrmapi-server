# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.external_nrf_function_single_all_of_attributes import ExternalNrfFunctionSingleAllOfAttributes
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class ExternalNrfFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ExternalNrfFunctionSingle - a model defined in OpenAPI

        id: The id of this ExternalNrfFunctionSingle.
        object_class: The object_class of this ExternalNrfFunctionSingle [Optional].
        object_instance: The object_instance of this ExternalNrfFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this ExternalNrfFunctionSingle [Optional].
        attributes: The attributes of this ExternalNrfFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[ExternalNrfFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)

ExternalNrfFunctionSingle.update_forward_refs()
