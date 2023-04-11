# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.reporting_ctrl_one_of import ReportingCtrlOneOf
from openapi_server.models.reporting_ctrl_one_of1 import ReportingCtrlOneOf1
from openapi_server.models.reporting_ctrl_one_of2 import ReportingCtrlOneOf2


class ReportingCtrl(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ReportingCtrl - a model defined in OpenAPI

        file_reporting_period: The file_reporting_period of this ReportingCtrl [Optional].
        file_location: The file_location of this ReportingCtrl [Optional].
        stream_target: The stream_target of this ReportingCtrl [Optional].
    """

    file_reporting_period: Optional[int] = Field(alias="fileReportingPeriod", default=None)
    file_location: Optional[str] = Field(alias="fileLocation", default=None)
    stream_target: Optional[str] = Field(alias="streamTarget", default=None)

ReportingCtrl.update_forward_refs()
