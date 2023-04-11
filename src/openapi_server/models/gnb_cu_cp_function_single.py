# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.danr_management_function_single import DANRManagementFunctionSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epng_c_single import EPNgCSingle
from openapi_server.models.epx2_c_single import EPX2CSingle
from openapi_server.models.epxn_c_single import EPXnCSingle
from openapi_server.models.gnb_cu_cp_function_single_all_of_attributes import GnbCuCpFunctionSingleAllOfAttributes
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class GnbCuCpFunctionSingle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GnbCuCpFunctionSingle - a model defined in OpenAPI

        id: The id of this GnbCuCpFunctionSingle.
        object_class: The object_class of this GnbCuCpFunctionSingle [Optional].
        object_instance: The object_instance of this GnbCuCpFunctionSingle [Optional].
        vs_data_container: The vs_data_container of this GnbCuCpFunctionSingle [Optional].
        attributes: The attributes of this GnbCuCpFunctionSingle [Optional].
        perf_metric_job: The perf_metric_job of this GnbCuCpFunctionSingle [Optional].
        threshold_monitor: The threshold_monitor of this GnbCuCpFunctionSingle [Optional].
        managed_nf_service: The managed_nf_service of this GnbCuCpFunctionSingle [Optional].
        trace_job: The trace_job of this GnbCuCpFunctionSingle [Optional].
        rrm_policy_ratio: The rrm_policy_ratio of this GnbCuCpFunctionSingle [Optional].
        nr_cell_cu: The nr_cell_cu of this GnbCuCpFunctionSingle [Optional].
        ep_xn_c: The ep_xn_c of this GnbCuCpFunctionSingle [Optional].
        ep_e1: The ep_e1 of this GnbCuCpFunctionSingle [Optional].
        ep_f1_c: The ep_f1_c of this GnbCuCpFunctionSingle [Optional].
        ep_ng_c: The ep_ng_c of this GnbCuCpFunctionSingle [Optional].
        ep_x2_c: The ep_x2_c of this GnbCuCpFunctionSingle [Optional].
        danr_management_function: The danr_management_function of this GnbCuCpFunctionSingle [Optional].
        des_management_function: The des_management_function of this GnbCuCpFunctionSingle [Optional].
        dmro_function: The dmro_function of this GnbCuCpFunctionSingle [Optional].
        dlbo_function: The dlbo_function of this GnbCuCpFunctionSingle [Optional].
    """

    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[GnbCuCpFunctionSingleAllOfAttributes] = Field(alias="attributes", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    rrm_policy_ratio: Optional[List[RRMPolicyRatioSingle]] = Field(alias="RRMPolicyRatio", default=None)
    nr_cell_cu: Optional[List[NrCellCuSingle]] = Field(alias="NrCellCu", default=None)
    ep_xn_c: Optional[List[EPXnCSingle]] = Field(alias="EP_XnC", default=None)
    ep_e1: Optional[List[EPE1Single]] = Field(alias="EP_E1", default=None)
    ep_f1_c: Optional[List[EPF1CSingle]] = Field(alias="EP_F1C", default=None)
    ep_ng_c: Optional[List[EPNgCSingle]] = Field(alias="EP_NgC", default=None)
    ep_x2_c: Optional[List[EPX2CSingle]] = Field(alias="EP_X2C", default=None)
    danr_management_function: Optional[DANRManagementFunctionSingle] = Field(alias="DANRManagementFunction", default=None)
    des_management_function: Optional[DESManagementFunctionSingle] = Field(alias="DESManagementFunction", default=None)
    dmro_function: Optional[DMROFunctionSingle] = Field(alias="DMROFunction", default=None)
    dlbo_function: Optional[DLBOFunctionSingle] = Field(alias="DLBOFunction", default=None)

GnbCuCpFunctionSingle.update_forward_refs()
