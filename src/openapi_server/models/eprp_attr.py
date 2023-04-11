# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.supported_perf_metric_group import SupportedPerfMetricGroup


class EPRPAttr(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EPRPAttr - a model defined in OpenAPI

        user_label: The user_label of this EPRPAttr [Optional].
        far_end_entity: The far_end_entity of this EPRPAttr [Optional].
        supported_perf_metric_groups: The supported_perf_metric_groups of this EPRPAttr [Optional].
    """

    user_label: Optional[str] = Field(alias="userLabel", default=None)
    far_end_entity: Optional[str] = Field(alias="farEndEntity", default=None)
    supported_perf_metric_groups: Optional[List[SupportedPerfMetricGroup]] = Field(alias="supportedPerfMetricGroups", default=None)

EPRPAttr.update_forward_refs()
