# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.fulfilment_info import FulfilmentInfo
from openapi_server.models.intent_context import IntentContext
from openapi_server.models.intent_single_all_of_intent_expectations_inner import IntentSingleAllOfIntentExpectationsInner


class IntentSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IntentSingleAllOf - a model defined in OpenAPI

        user_label: The user_label of this IntentSingleAllOf [Optional].
        intent_expectations: The intent_expectations of this IntentSingleAllOf [Optional].
        intent_contexts: The intent_contexts of this IntentSingleAllOf [Optional].
        intent_fulfilment_info: The intent_fulfilment_info of this IntentSingleAllOf [Optional].
    """

    user_label: Optional[str] = Field(alias="userLabel", default=None)
    intent_expectations: Optional[List[IntentSingleAllOfIntentExpectationsInner]] = Field(alias="intentExpectations", default=None)
    intent_contexts: Optional[List[IntentContext]] = Field(alias="intentContexts", default=None)
    intent_fulfilment_info: Optional[FulfilmentInfo] = Field(alias="intentFulfilmentInfo", default=None)

IntentSingleAllOf.update_forward_refs()
