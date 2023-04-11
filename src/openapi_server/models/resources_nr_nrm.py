# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.beam_single import BeamSingle
from openapi_server.models.bwp_single import BwpSingle
from openapi_server.models.cco_function_single import CCOFunctionSingle
from openapi_server.models.cco_overshoot_coverage_parameters_single import CCOOvershootCoverageParametersSingle
from openapi_server.models.cco_parameters_attr_all_of_attributes import CCOParametersAttrAllOfAttributes
from openapi_server.models.cco_pilot_pollution_parameters_single import CCOPilotPollutionParametersSingle
from openapi_server.models.cco_weak_coverage_parameters_single import CCOWeakCoverageParametersSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.common_beamforming_function_single import CommonBeamformingFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.danr_management_function_single import DANRManagementFunctionSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.epng_c_single import EPNgCSingle
from openapi_server.models.epng_u_single import EPNgUSingle
from openapi_server.models.eps1_u_single import EPS1USingle
from openapi_server.models.epx2_c_single import EPX2CSingle
from openapi_server.models.epx2_u_single import EPX2USingle
from openapi_server.models.epxn_c_single import EPXnCSingle
from openapi_server.models.epxn_u_single import EPXnUSingle
from openapi_server.models.e_utran_cell_relation_single import EUtranCellRelationSingle
from openapi_server.models.e_utran_freq_relation_single import EUtranFreqRelationSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.external_gnb_cu_up_function_single import ExternalGnbCuUpFunctionSingle
from openapi_server.models.external_gnb_du_function_single import ExternalGnbDuFunctionSingle
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mn_s import MnS
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle
from openapi_server.models.nr_cell_du_single import NrCellDuSingle
from openapi_server.models.nr_operator_cell_du_single import NrOperatorCellDuSingle
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.operator_du_single import OperatorDuSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.plmn_info import PlmnInfo
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.rim_rs_set_single import RimRSSetSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class ResourcesNrNrm(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResourcesNrNrm - a model defined in OpenAPI

        sub_network: The sub_network of this ResourcesNrNrm [Optional].
        managed_element: The managed_element of this ResourcesNrNrm [Optional].
        id: The id of this ResourcesNrNrm.
        object_class: The object_class of this ResourcesNrNrm [Optional].
        object_instance: The object_instance of this ResourcesNrNrm [Optional].
        vs_data_container: The vs_data_container of this ResourcesNrNrm [Optional].
        attributes: The attributes of this ResourcesNrNrm [Optional].
        management_node: The management_node of this ResourcesNrNrm [Optional].
        mns_agent: The mns_agent of this ResourcesNrNrm [Optional].
        me_context: The me_context of this ResourcesNrNrm [Optional].
        perf_metric_job: The perf_metric_job of this ResourcesNrNrm [Optional].
        threshold_monitor: The threshold_monitor of this ResourcesNrNrm [Optional].
        trace_job: The trace_job of this ResourcesNrNrm [Optional].
        management_data_collection: The management_data_collection of this ResourcesNrNrm [Optional].
        ntf_subscription_control: The ntf_subscription_control of this ResourcesNrNrm [Optional].
        alarm_list: The alarm_list of this ResourcesNrNrm [Optional].
        file_download_job: The file_download_job of this ResourcesNrNrm [Optional].
        files: The files of this ResourcesNrNrm [Optional].
        mns_registry: The mns_registry of this ResourcesNrNrm [Optional].
        nr_frequency: The nr_frequency of this ResourcesNrNrm [Optional].
        external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this ResourcesNrNrm [Optional].
        external_enb_function: The external_enb_function of this ResourcesNrNrm [Optional].
        e_utran_frequency: The e_utran_frequency of this ResourcesNrNrm [Optional].
        des_management_function: The des_management_function of this ResourcesNrNrm [Optional].
        drach_optimization_function: The drach_optimization_function of this ResourcesNrNrm [Optional].
        dmro_function: The dmro_function of this ResourcesNrNrm [Optional].
        dlbo_function: The dlbo_function of this ResourcesNrNrm [Optional].
        dpci_configuration_function: The dpci_configuration_function of this ResourcesNrNrm [Optional].
        cpci_configuration_function: The cpci_configuration_function of this ResourcesNrNrm [Optional].
        ces_management_function: The ces_management_function of this ResourcesNrNrm [Optional].
        configurable5_qi_set: The configurable5_qi_set of this ResourcesNrNrm [Optional].
        rim_rs_global: The rim_rs_global of this ResourcesNrNrm [Optional].
        dynamic5_qi_set: The dynamic5_qi_set of this ResourcesNrNrm [Optional].
        cco_function: The cco_function of this ResourcesNrNrm [Optional].
        gnb_du_function: The gnb_du_function of this ResourcesNrNrm [Optional].
        gnb_cu_up_function: The gnb_cu_up_function of this ResourcesNrNrm [Optional].
        gnb_cu_cp_function: The gnb_cu_cp_function of this ResourcesNrNrm [Optional].
        managed_nf_service: The managed_nf_service of this ResourcesNrNrm [Optional].
        rrm_policy_ratio: The rrm_policy_ratio of this ResourcesNrNrm [Optional].
        nr_cell_du: The nr_cell_du of this ResourcesNrNrm [Optional].
        bwp_multiple: The bwp_multiple of this ResourcesNrNrm [Optional].
        nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this ResourcesNrNrm [Optional].
        ep_f1_c: The ep_f1_c of this ResourcesNrNrm [Optional].
        ep_f1_u: The ep_f1_u of this ResourcesNrNrm [Optional].
        operator_du: The operator_du of this ResourcesNrNrm [Optional].
        ep_e1: The ep_e1 of this ResourcesNrNrm [Optional].
        ep_xn_u: The ep_xn_u of this ResourcesNrNrm [Optional].
        ep_ng_u: The ep_ng_u of this ResourcesNrNrm [Optional].
        ep_x2_u: The ep_x2_u of this ResourcesNrNrm [Optional].
        ep_s1_u: The ep_s1_u of this ResourcesNrNrm [Optional].
        nr_cell_cu: The nr_cell_cu of this ResourcesNrNrm [Optional].
        ep_xn_c: The ep_xn_c of this ResourcesNrNrm [Optional].
        ep_ng_c: The ep_ng_c of this ResourcesNrNrm [Optional].
        ep_x2_c: The ep_x2_c of this ResourcesNrNrm [Optional].
        danr_management_function: The danr_management_function of this ResourcesNrNrm [Optional].
        gnb_id: The gnb_id of this ResourcesNrNrm [Optional].
        gnb_id_length: The gnb_id_length of this ResourcesNrNrm [Optional].
        nr_cell_relation: The nr_cell_relation of this ResourcesNrNrm [Optional].
        e_utran_cell_relation: The e_utran_cell_relation of this ResourcesNrNrm [Optional].
        nr_freq_relation: The nr_freq_relation of this ResourcesNrNrm [Optional].
        e_utran_freq_relation: The e_utran_freq_relation of this ResourcesNrNrm [Optional].
        nr_operator_cell_du: The nr_operator_cell_du of this ResourcesNrNrm [Optional].
        cell_local_id: The cell_local_id of this ResourcesNrNrm [Optional].
        administrative_state: The administrative_state of this ResourcesNrNrm [Optional].
        plmn_info_list: The plmn_info_list of this ResourcesNrNrm [Optional].
        nr_tac: The nr_tac of this ResourcesNrNrm [Optional].
        common_beamforming_function: The common_beamforming_function of this ResourcesNrNrm [Optional].
        beam: The beam of this ResourcesNrNrm [Optional].
        rim_rs_set: The rim_rs_set of this ResourcesNrNrm [Optional].
        external_nr_cell_cu: The external_nr_cell_cu of this ResourcesNrNrm [Optional].
        external_eu_tran_cell: The external_eu_tran_cell of this ResourcesNrNrm [Optional].
    """

    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)
    managed_element: Optional[List[ManagedElementSingle]] = Field(alias="ManagedElement", default=None)
    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[CCOParametersAttrAllOfAttributes] = Field(alias="attributes", default=None)
    management_node: Optional[List[ManagementNodeSingle]] = Field(alias="ManagementNode", default=None)
    mns_agent: Optional[List[MnsAgentSingle]] = Field(alias="MnsAgent", default=None)
    me_context: Optional[List[MeContextSingle]] = Field(alias="MeContext", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    management_data_collection: Optional[List[ManagementDataCollectionSingle]] = Field(alias="ManagementDataCollection", default=None)
    ntf_subscription_control: Optional[List[NtfSubscriptionControlSingle]] = Field(alias="NtfSubscriptionControl", default=None)
    alarm_list: Optional[AlarmListSingle] = Field(alias="AlarmList", default=None)
    file_download_job: Optional[List[FileDownloadJobSingle]] = Field(alias="FileDownloadJob", default=None)
    files: Optional[List[FilesSingle]] = Field(alias="Files", default=None)
    mns_registry: Optional[MnsRegistrySingle] = Field(alias="MnsRegistry", default=None)
    nr_frequency: Optional[List[NRFrequencySingle]] = Field(alias="NRFrequency", default=None)
    external_gnb_cu_cp_function: Optional[List[ExternalGnbCuCpFunctionSingle]] = Field(alias="ExternalGnbCuCpFunction", default=None)
    external_enb_function: Optional[List[ExternalENBFunctionSingle]] = Field(alias="ExternalENBFunction", default=None)
    e_utran_frequency: Optional[List[EUtranFrequencySingle]] = Field(alias="EUtranFrequency", default=None)
    des_management_function: Optional[DESManagementFunctionSingle] = Field(alias="DESManagementFunction", default=None)
    drach_optimization_function: Optional[DRACHOptimizationFunctionSingle] = Field(alias="DRACHOptimizationFunction", default=None)
    dmro_function: Optional[DMROFunctionSingle] = Field(alias="DMROFunction", default=None)
    dlbo_function: Optional[DLBOFunctionSingle] = Field(alias="DLBOFunction", default=None)
    dpci_configuration_function: Optional[DPCIConfigurationFunctionSingle] = Field(alias="DPCIConfigurationFunction", default=None)
    cpci_configuration_function: Optional[CPCIConfigurationFunctionSingle] = Field(alias="CPCIConfigurationFunction", default=None)
    ces_management_function: Optional[CESManagementFunctionSingle] = Field(alias="CESManagementFunction", default=None)
    configurable5_qi_set: Optional[List[Configurable5QISetSingle]] = Field(alias="Configurable5QISet", default=None)
    rim_rs_global: Optional[RimRSGlobalSingle] = Field(alias="RimRSGlobal", default=None)
    dynamic5_qi_set: Optional[List[Dynamic5QISetSingle]] = Field(alias="Dynamic5QISet", default=None)
    cco_function: Optional[CCOFunctionSingle] = Field(alias="CCOFunction", default=None)
    gnb_du_function: Optional[List[GnbDuFunctionSingle]] = Field(alias="GnbDuFunction", default=None)
    gnb_cu_up_function: Optional[List[GnbCuUpFunctionSingle]] = Field(alias="GnbCuUpFunction", default=None)
    gnb_cu_cp_function: Optional[List[GnbCuCpFunctionSingle]] = Field(alias="GnbCuCpFunction", default=None)
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
    rrm_policy_ratio: Optional[List[RRMPolicyRatioSingle]] = Field(alias="RRMPolicyRatio", default=None)
    nr_cell_du: Optional[List[NrCellDuSingle]] = Field(alias="NrCellDu", default=None)
    bwp_multiple: Optional[List[BwpSingle]] = Field(alias="Bwp-Multiple", default=None)
    nr_sector_carrier_multiple: Optional[List[NrSectorCarrierSingle]] = Field(alias="NrSectorCarrier-Multiple", default=None)
    ep_f1_c: Optional[List[EPF1CSingle]] = Field(alias="EP_F1C", default=None)
    ep_f1_u: Optional[List[EPF1USingle]] = Field(alias="EP_F1U", default=None)
    operator_du: Optional[List[OperatorDuSingle]] = Field(alias="OperatorDU", default=None)
    ep_e1: Optional[List[EPE1Single]] = Field(alias="EP_E1", default=None)
    ep_xn_u: Optional[List[EPXnUSingle]] = Field(alias="EP_XnU", default=None)
    ep_ng_u: Optional[List[EPNgUSingle]] = Field(alias="EP_NgU", default=None)
    ep_x2_u: Optional[List[EPX2USingle]] = Field(alias="EP_X2U", default=None)
    ep_s1_u: Optional[List[EPS1USingle]] = Field(alias="EP_S1U", default=None)
    nr_cell_cu: Optional[List[NrCellCuSingle]] = Field(alias="NrCellCu", default=None)
    ep_xn_c: Optional[List[EPXnCSingle]] = Field(alias="EP_XnC", default=None)
    ep_ng_c: Optional[List[EPNgCSingle]] = Field(alias="EP_NgC", default=None)
    ep_x2_c: Optional[List[EPX2CSingle]] = Field(alias="EP_X2C", default=None)
    danr_management_function: Optional[DANRManagementFunctionSingle] = Field(alias="DANRManagementFunction", default=None)
    gnb_id: Optional[str] = Field(alias="gnbId", default=None)
    gnb_id_length: Optional[int] = Field(alias="gnbIdLength", default=None)
    nr_cell_relation: Optional[List[NRCellRelationSingle]] = Field(alias="NRCellRelation", default=None)
    e_utran_cell_relation: Optional[List[EUtranCellRelationSingle]] = Field(alias="EUtranCellRelation", default=None)
    nr_freq_relation: Optional[List[NRFreqRelationSingle]] = Field(alias="NRFreqRelation", default=None)
    e_utran_freq_relation: Optional[List[EUtranFreqRelationSingle]] = Field(alias="EUtranFreqRelation", default=None)
    nr_operator_cell_du: Optional[List[NrOperatorCellDuSingle]] = Field(alias="NrOperatorCellDu", default=None)
    cell_local_id: Optional[int] = Field(alias="cellLocalId", default=None)
    administrative_state: Optional[AdministrativeState] = Field(alias="administrativeState", default=None)
    plmn_info_list: Optional[List[PlmnInfo]] = Field(alias="plmnInfoList", default=None)
    nr_tac: Optional[int] = Field(alias="nrTac", default=None)
    common_beamforming_function: Optional[CommonBeamformingFunctionSingle] = Field(alias="CommonBeamformingFunction", default=None)
    beam: Optional[List[BeamSingle]] = Field(alias="Beam", default=None)
    rim_rs_set: Optional[List[RimRSSetSingle]] = Field(alias="RimRSSet", default=None)
    external_nr_cell_cu: Optional[List[ExternalNrCellCuSingle]] = Field(alias="ExternalNrCellCu", default=None)
    external_eu_tran_cell: Optional[List[ExternalEUTranCellSingle]] = Field(alias="ExternalEUTranCell", default=None)

    @validator("gnb_id_length")
    def gnb_id_length_max(cls, value):
        assert value <= 32
        return value

    @validator("gnb_id_length")
    def gnb_id_length_min(cls, value):
        assert value >= 22
        return value

    @validator("nr_tac")
    def nr_tac_max(cls, value):
        assert value <= 16777215
        return value

ResourcesNrNrm.update_forward_refs()
