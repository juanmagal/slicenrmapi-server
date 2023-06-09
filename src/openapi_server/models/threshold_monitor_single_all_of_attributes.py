# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.operational_state import OperationalState
from openapi_server.models.threshold_info import ThresholdInfo


class ThresholdMonitorSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ThresholdMonitorSingleAllOfAttributes - a model defined in OpenAPI

        administrative_state: The administrative_state of this ThresholdMonitorSingleAllOfAttributes [Optional].
        operational_state: The operational_state of this ThresholdMonitorSingleAllOfAttributes [Optional].
        performance_metrics: The performance_metrics of this ThresholdMonitorSingleAllOfAttributes [Optional].
        threshold_info_list: The threshold_info_list of this ThresholdMonitorSingleAllOfAttributes [Optional].
        monitor_granularity_period: The monitor_granularity_period of this ThresholdMonitorSingleAllOfAttributes [Optional].
        object_instances: The object_instances of this ThresholdMonitorSingleAllOfAttributes [Optional].
        root_object_instances: The root_object_instances of this ThresholdMonitorSingleAllOfAttributes [Optional].
    """

    administrative_state: Optional[AdministrativeState] = Field(alias="administrativeState", default=None)
    operational_state: Optional[OperationalState] = Field(alias="operationalState", default=None)
    performance_metrics: Optional[List[str]] = Field(alias="performanceMetrics", default=None)
    threshold_info_list: Optional[List[ThresholdInfo]] = Field(alias="thresholdInfoList", default=None)
    monitor_granularity_period: Optional[int] = Field(alias="monitorGranularityPeriod", default=None)
    object_instances: Optional[List[str]] = Field(alias="objectInstances", default=None)
    root_object_instances: Optional[List[str]] = Field(alias="rootObjectInstances", default=None)

    @validator("monitor_granularity_period")
    def monitor_granularity_period_min(cls, value):
        assert value >= 1
        return value

ThresholdMonitorSingleAllOfAttributes.update_forward_refs()
