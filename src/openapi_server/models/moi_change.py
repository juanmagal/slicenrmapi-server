# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.correlated_notification import CorrelatedNotification
from openapi_server.models.insert import Insert
from openapi_server.models.operation import Operation
from openapi_server.models.source_indicator import SourceIndicator


class MoiChange(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    MoiChange - a model defined in OpenAPI

        notification_id: The notification_id of this MoiChange.
        correlated_notifications: The correlated_notifications of this MoiChange [Optional].
        additional_text: The additional_text of this MoiChange [Optional].
        source_indicator: The source_indicator of this MoiChange [Optional].
        op: The op of this MoiChange.
        path: The path of this MoiChange.
        insert: The insert of this MoiChange [Optional].
        value: The value of this MoiChange [Optional].
        old_value: The old_value of this MoiChange [Optional].
    """

    notification_id: int = Field(alias="notificationId")
    correlated_notifications: Optional[List[CorrelatedNotification]] = Field(alias="correlatedNotifications", default=None)
    additional_text: Optional[str] = Field(alias="additionalText", default=None)
    source_indicator: Optional[SourceIndicator] = Field(alias="sourceIndicator", default=None)
    op: Operation = Field(alias="op")
    path: str = Field(alias="path")
    insert: Optional[Insert] = Field(alias="insert", default=None)
    value: Optional[object] = Field(alias="value", default=None)
    old_value: Optional[object] = Field(alias="oldValue", default=None)

MoiChange.update_forward_refs()
