# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.correlated_notification import CorrelatedNotification
from openapi_server.models.source_indicator import SourceIndicator


class NotifyMoiAttributeValueChangesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NotifyMoiAttributeValueChangesAllOf - a model defined in OpenAPI

        correlated_notifications: The correlated_notifications of this NotifyMoiAttributeValueChangesAllOf [Optional].
        additional_text: The additional_text of this NotifyMoiAttributeValueChangesAllOf [Optional].
        source_indicator: The source_indicator of this NotifyMoiAttributeValueChangesAllOf [Optional].
        attribute_list_value_changes: The attribute_list_value_changes of this NotifyMoiAttributeValueChangesAllOf.
    """

    correlated_notifications: Optional[List[CorrelatedNotification]] = Field(alias="correlatedNotifications", default=None)
    additional_text: Optional[str] = Field(alias="additionalText", default=None)
    source_indicator: Optional[SourceIndicator] = Field(alias="sourceIndicator", default=None)
    attribute_list_value_changes: List[Dict] = Field(alias="attributeListValueChanges")

NotifyMoiAttributeValueChangesAllOf.update_forward_refs()
