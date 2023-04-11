# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.alarm_notification_types import AlarmNotificationTypes
from openapi_server.models.cm_notification_types import CmNotificationTypes
from openapi_server.models.file_notification_types import FileNotificationTypes
from openapi_server.models.heartbeat_notification_types import HeartbeatNotificationTypes
from openapi_server.models.perf_notification_types import PerfNotificationTypes


class NotificationType(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NotificationType - a model defined in OpenAPI

    """


NotificationType.update_forward_refs()
