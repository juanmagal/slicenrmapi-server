# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.file_download_job_process_monitor import FileDownloadJobProcessMonitor


class FileDownloadJobSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FileDownloadJobSingleAllOfAttributes - a model defined in OpenAPI

        file_location: The file_location of this FileDownloadJobSingleAllOfAttributes [Optional].
        notification_recipient_address: The notification_recipient_address of this FileDownloadJobSingleAllOfAttributes [Optional].
        cancel_job: The cancel_job of this FileDownloadJobSingleAllOfAttributes [Optional].
        job_monitor: The job_monitor of this FileDownloadJobSingleAllOfAttributes [Optional].
    """

    file_location: Optional[str] = Field(alias="fileLocation", default=None)
    notification_recipient_address: Optional[str] = Field(alias="notificationRecipientAddress", default=None)
    cancel_job: Optional[str] = Field(alias="cancelJob", default=None)
    job_monitor: Optional[FileDownloadJobProcessMonitor] = Field(alias="jobMonitor", default=None)

FileDownloadJobSingleAllOfAttributes.update_forward_refs()