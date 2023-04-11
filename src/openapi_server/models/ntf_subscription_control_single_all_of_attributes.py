# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.notification_type import NotificationType
from openapi_server.models.scope1 import Scope1


class NtfSubscriptionControlSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NtfSubscriptionControlSingleAllOfAttributes - a model defined in OpenAPI

        notification_recipient_address: The notification_recipient_address of this NtfSubscriptionControlSingleAllOfAttributes [Optional].
        notification_types: The notification_types of this NtfSubscriptionControlSingleAllOfAttributes [Optional].
        scope: The scope of this NtfSubscriptionControlSingleAllOfAttributes [Optional].
        notification_filter: The notification_filter of this NtfSubscriptionControlSingleAllOfAttributes [Optional].
    """

    notification_recipient_address: Optional[str] = Field(alias="notificationRecipientAddress", default=None)
    notification_types: Optional[List[NotificationType]] = Field(alias="notificationTypes", default=None)
    scope: Optional[Scope1] = Field(alias="scope", default=None)
    notification_filter: Optional[str] = Field(alias="notificationFilter", default=None)

NtfSubscriptionControlSingleAllOfAttributes.update_forward_refs()
