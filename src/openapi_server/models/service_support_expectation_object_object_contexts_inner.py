# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.condition import Condition
from openapi_server.models.coverage_area_ta_context import CoverageAreaTAContext
from openapi_server.models.edge_idenfitication_id_context import EdgeIdenfiticationIdContext
from openapi_server.models.edge_idenfitication_loc_context import EdgeIdenfiticationLocContext
from openapi_server.models.object_context import ObjectContext


class ServiceSupportExpectationObjectObjectContextsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ServiceSupportExpectationObjectObjectContextsInner - a model defined in OpenAPI

        context_attribute: The context_attribute of this ServiceSupportExpectationObjectObjectContextsInner [Optional].
        context_condition: The context_condition of this ServiceSupportExpectationObjectObjectContextsInner [Optional].
        context_value_range: The context_value_range of this ServiceSupportExpectationObjectObjectContextsInner [Optional].
    """

    context_attribute: Optional[str] = Field(alias="contextAttribute", default=None)
    context_condition: Optional[Condition] = Field(alias="contextCondition", default=None)
    context_value_range: Optional[List[float]] = Field(alias="contextValueRange", default=None)

ServiceSupportExpectationObjectObjectContextsInner.update_forward_refs()
