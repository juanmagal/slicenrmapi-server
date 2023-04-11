# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.bwp_single import BwpSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.gnb_du_function_single_all_of_attributes import GnbDuFunctionSingleAllOfAttributes
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.nr_cell_du_single import NrCellDuSingle
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle
from openapi_server.models.operator_du_single import OperatorDuSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class GnbDuFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GnbDuFunctionSingle - a model defined in OpenAPI

        id: The id of this GnbDuFunctionSingle.
        object_class: The object_class of this GnbDuFunctionSingle [Optional].
        object_instance: The object_instance of this GnbDuFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this GnbDuFunctionSingle [Optional].
        attributes: The attributes of this GnbDuFunctionSingle [Optional].
        perf_metric_job: The perf_metric_job of this GnbDuFunctionSingle [Optional].
        threshold_monitor: The threshold_monitor of this GnbDuFunctionSingle [Optional].
        managed_nf_service: The managed_nf_service of this GnbDuFunctionSingle [Optional].
        trace_job: The trace_job of this GnbDuFunctionSingle [Optional].
        rrm_policy_ratio: The rrm_policy_ratio of this GnbDuFunctionSingle [Optional].
        nr_cell_du: The nr_cell_du of this GnbDuFunctionSingle [Optional].
        bwp_multiple: The bwp_multiple of this GnbDuFunctionSingle [Optional].
        nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this GnbDuFunctionSingle [Optional].
        ep_f1_c: The ep_f1_c of this GnbDuFunctionSingle [Optional].
        ep_f1_u: The ep_f1_u of this GnbDuFunctionSingle [Optional].
        drach_optimization_function: The drach_optimization_function of this GnbDuFunctionSingle [Optional].
        operator_du: The operator_du of this GnbDuFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[GnbDuFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    rrm_policy_ratio: Optional[List[RRMPolicyRatioSingle]] = Field(alias="RRMPolicyRatio", default=None)
    nr_cell_du: Optional[List[NrCellDuSingle]] = Field(alias="NrCellDu", default=None)
    bwp_multiple: Optional[List[BwpSingle]] = Field(alias="Bwp-Multiple", default=None)
    nr_sector_carrier_multiple: Optional[List[NrSectorCarrierSingle]] = Field(alias="NrSectorCarrier-Multiple", default=None)
    ep_f1_c: Optional[EPF1CSingle] = Field(alias="EP_F1C", default=None)
    ep_f1_u: Optional[List[EPF1USingle]] = Field(alias="EP_F1U", default=None)
    drach_optimization_function: Optional[DRACHOptimizationFunctionSingle] = Field(alias="DRACHOptimizationFunction", default=None)
    operator_du: Optional[List[OperatorDuSingle]] = Field(alias="OperatorDU", default=None)

GnbDuFunctionSingle.update_forward_refs()