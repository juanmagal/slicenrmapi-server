# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.file_download_job_process_monitor_result_state_info import FileDownloadJobProcessMonitorResultStateInfo


class FileDownloadJobProcessMonitor(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FileDownloadJobProcessMonitor - a model defined in OpenAPI

        job_id: The job_id of this FileDownloadJobProcessMonitor [Optional].
        status: The status of this FileDownloadJobProcessMonitor [Optional].
        progress_percentage: The progress_percentage of this FileDownloadJobProcessMonitor [Optional].
        progress_state_info: The progress_state_info of this FileDownloadJobProcessMonitor [Optional].
        result_state_info: The result_state_info of this FileDownloadJobProcessMonitor [Optional].
        start_time: The start_time of this FileDownloadJobProcessMonitor [Optional].
        end_time: The end_time of this FileDownloadJobProcessMonitor [Optional].
        timer: The timer of this FileDownloadJobProcessMonitor [Optional].
    """

    job_id: Optional[str] = Field(alias="jobId", default=None)
    status: Optional[str] = Field(alias="status", default=None)
    progress_percentage: Optional[int] = Field(alias="progressPercentage", default=None)
    progress_state_info: Optional[str] = Field(alias="progressStateInfo", default=None)
    result_state_info: Optional[FileDownloadJobProcessMonitorResultStateInfo] = Field(alias="resultStateInfo", default=None)
    start_time: Optional[datetime] = Field(alias="startTime", default=None)
    end_time: Optional[datetime] = Field(alias="endTime", default=None)
    timer: Optional[int] = Field(alias="timer", default=None)

    @validator("progress_percentage")
    def progress_percentage_max(cls, value):
        assert value <= 100
        return value

    @validator("progress_percentage")
    def progress_percentage_min(cls, value):
        assert value >= 0
        return value

FileDownloadJobProcessMonitor.update_forward_refs()
