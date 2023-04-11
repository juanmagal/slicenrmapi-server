# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.e_utran_cell_relation_single import EUtranCellRelationSingle
from openapi_server.models.e_utran_freq_relation_single import EUtranFreqRelationSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle
from openapi_server.models.nr_cell_cu_single_all_of_attributes import NrCellCuSingleAllOfAttributes
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class NrCellCuSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NrCellCuSingle - a model defined in OpenAPI

        id: The id of this NrCellCuSingle.
        object_class: The object_class of this NrCellCuSingle [Optional].
        object_instance: The object_instance of this NrCellCuSingle [Optional].
        vs_data_container: The vs_data_container of this NrCellCuSingle [Optional].
        attributes: The attributes of this NrCellCuSingle [Optional].
        perf_metric_job: The perf_metric_job of this NrCellCuSingle [Optional].
        threshold_monitor: The threshold_monitor of this NrCellCuSingle [Optional].
        managed_nf_service: The managed_nf_service of this NrCellCuSingle [Optional].
        trace_job: The trace_job of this NrCellCuSingle [Optional].
        rrm_policy_ratio: The rrm_policy_ratio of this NrCellCuSingle [Optional].
        nr_cell_relation: The nr_cell_relation of this NrCellCuSingle [Optional].
        e_utran_cell_relation: The e_utran_cell_relation of this NrCellCuSingle [Optional].
        nr_freq_relation: The nr_freq_relation of this NrCellCuSingle [Optional].
        e_utran_freq_relation: The e_utran_freq_relation of this NrCellCuSingle [Optional].
        des_management_function: The des_management_function of this NrCellCuSingle [Optional].
        dmro_function: The dmro_function of this NrCellCuSingle [Optional].
        dlbo_function: The dlbo_function of this NrCellCuSingle [Optional].
        ces_management_function: The ces_management_function of this NrCellCuSingle [Optional].
        dpci_configuration_function: The dpci_configuration_function of this NrCellCuSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[NrCellCuSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    rrm_policy_ratio: Optional[List[RRMPolicyRatioSingle]] = Field(alias="RRMPolicyRatio", default=None)
    nr_cell_relation: Optional[List[NRCellRelationSingle]] = Field(alias="NRCellRelation", default=None)
    e_utran_cell_relation: Optional[List[EUtranCellRelationSingle]] = Field(alias="EUtranCellRelation", default=None)
    nr_freq_relation: Optional[List[NRFreqRelationSingle]] = Field(alias="NRFreqRelation", default=None)
    e_utran_freq_relation: Optional[List[EUtranFreqRelationSingle]] = Field(alias="EUtranFreqRelation", default=None)
    des_management_function: Optional[DESManagementFunctionSingle] = Field(alias="DESManagementFunction", default=None)
    dmro_function: Optional[DMROFunctionSingle] = Field(alias="DMROFunction", default=None)
    dlbo_function: Optional[DLBOFunctionSingle] = Field(alias="DLBOFunction", default=None)
    ces_management_function: Optional[CESManagementFunctionSingle] = Field(alias="CESManagementFunction", default=None)
    dpci_configuration_function: Optional[DPCIConfigurationFunctionSingle] = Field(alias="DPCIConfigurationFunction", default=None)

NrCellCuSingle.update_forward_refs()
