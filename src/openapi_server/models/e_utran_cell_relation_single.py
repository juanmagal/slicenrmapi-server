# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.e_utran_cell_relation_single_all_of_attributes import EUtranCellRelationSingleAllOfAttributes
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class EUtranCellRelationSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EUtranCellRelationSingle - a model defined in OpenAPI

        id: The id of this EUtranCellRelationSingle.
        object_class: The object_class of this EUtranCellRelationSingle [Optional].
        object_instance: The object_instance of this EUtranCellRelationSingle [Optional].
        vs_data_container: The vs_data_container of this EUtranCellRelationSingle [Optional].
        attributes: The attributes of this EUtranCellRelationSingle [Optional].
        perf_metric_job: The perf_metric_job of this EUtranCellRelationSingle [Optional].
        threshold_monitor: The threshold_monitor of this EUtranCellRelationSingle [Optional].
        managed_nf_service: The managed_nf_service of this EUtranCellRelationSingle [Optional].
        trace_job: The trace_job of this EUtranCellRelationSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[EUtranCellRelationSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)

EUtranCellRelationSingle.update_forward_refs()
