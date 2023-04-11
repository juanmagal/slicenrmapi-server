# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.moi_change import MoiChange
from openapi_server.models.notification_type import NotificationType


class NotifyMoiChanges(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NotifyMoiChanges - a model defined in OpenAPI

        href: The href of this NotifyMoiChanges.
        notification_id: The notification_id of this NotifyMoiChanges.
        notification_type: The notification_type of this NotifyMoiChanges.
        event_time: The event_time of this NotifyMoiChanges.
        system_dn: The system_dn of this NotifyMoiChanges.
        moi_changes: The moi_changes of this NotifyMoiChanges.
    """

    href: str = Field(alias="href")
    notification_id: int = Field(alias="notificationId")
    notification_type: NotificationType = Field(alias="notificationType")
    event_time: datetime = Field(alias="eventTime")
    system_dn: str = Field(alias="systemDN")
    moi_changes: List[MoiChange] = Field(alias="moiChanges")

NotifyMoiChanges.update_forward_refs()