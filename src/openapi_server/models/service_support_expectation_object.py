# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.service_support_expectation_object_object_contexts_inner import ServiceSupportExpectationObjectObjectContextsInner


class ServiceSupportExpectationObject(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceSupportExpectationObject - a model defined in OpenAPI

        object_type: The object_type of this ServiceSupportExpectationObject [Optional].
        object_instance: The object_instance of this ServiceSupportExpectationObject [Optional].
        object_contexts: The object_contexts of this ServiceSupportExpectationObject [Optional].
    """

    object_type: Optional[str] = Field(alias="objectType", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    object_contexts: Optional[List[ServiceSupportExpectationObjectObjectContextsInner]] = Field(alias="objectContexts", default=None)

ServiceSupportExpectationObject.update_forward_refs()
