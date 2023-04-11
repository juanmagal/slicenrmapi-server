# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.assurance_goal_status import AssuranceGoalStatus


class AssuranceReportSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AssuranceReportSingleAllOfAttributes - a model defined in OpenAPI

        assurance_goal_status_list: The assurance_goal_status_list of this AssuranceReportSingleAllOfAttributes [Optional].
    """

    assurance_goal_status_list: Optional[List[AssuranceGoalStatus]] = Field(alias="assuranceGoalStatusList", default=None)

AssuranceReportSingleAllOfAttributes.update_forward_refs()
