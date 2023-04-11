# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.amf_function_single import AmfFunctionSingle
from openapi_server.models.amf_region_single import AmfRegionSingle
from openapi_server.models.amf_set_single import AmfSetSingle
from openapi_server.models.assurance_closed_control_loop_single import AssuranceClosedControlLoopSingle
from openapi_server.models.assurance_goal_single import AssuranceGoalSingle
from openapi_server.models.ausf_function_single import AusfFunctionSingle
from openapi_server.models.beam_single import BeamSingle
from openapi_server.models.bwp_single import BwpSingle
from openapi_server.models.cco_function_single import CCOFunctionSingle
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
from openapi_server.models.easdf_function_single import EASDFFunctionSingle
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epf1_u_single import EPF1USingle
from openapi_server.models.epmapsmsc_single import EPMAPSMSCSingle
from openapi_server.models.epn10_single import EPN10Single
from openapi_server.models.epn11_single import EPN11Single
from openapi_server.models.epn12_single import EPN12Single
from openapi_server.models.epn13_single import EPN13Single
from openapi_server.models.epn14_single import EPN14Single
from openapi_server.models.epn15_single import EPN15Single
from openapi_server.models.epn16_single import EPN16Single
from openapi_server.models.epn17_single import EPN17Single
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn21_single import EPN21Single
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn26_single import EPN26Single
from openapi_server.models.epn27_single import EPN27Single
from openapi_server.models.epn2_single import EPN2Single
from openapi_server.models.epn31_single import EPN31Single
from openapi_server.models.epn32_single import EPN32Single
from openapi_server.models.epn33_single import EPN33Single
from openapi_server.models.epn3_single import EPN3Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn5_single import EPN5Single
from openapi_server.models.epn60_single import EPN60Single
from openapi_server.models.epn6_single import EPN6Single
from openapi_server.models.epn7_single import EPN7Single
from openapi_server.models.epn88_single import EPN88Single
from openapi_server.models.epn8_single import EPN8Single
from openapi_server.models.epn9_single import EPN9Single
from openapi_server.models.epnlg_single import EPNLGSingle
from openapi_server.models.epnls_single import EPNLSSingle
from openapi_server.models.epng_c_single import EPNgCSingle
from openapi_server.models.epng_u_single import EPNgUSingle
from openapi_server.models.ep_npc4_single import EPNpc4Single
from openapi_server.models.ep_npc6_single import EPNpc6Single
from openapi_server.models.ep_npc7_single import EPNpc7Single
from openapi_server.models.ep_npc8_single import EPNpc8Single
from openapi_server.models.eprx_single import EPRxSingle
from openapi_server.models.eps1_u_single import EPS1USingle
from openapi_server.models.eps5_c_single import EPS5CSingle
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server.models.ep_transport_single import EPTransportSingle
from openapi_server.models.epx2_c_single import EPX2CSingle
from openapi_server.models.epx2_u_single import EPX2USingle
from openapi_server.models.epxn_c_single import EPXnCSingle
from openapi_server.models.epxn_u_single import EPXnUSingle
from openapi_server.models.e_utran_cell_relation_single import EUtranCellRelationSingle
from openapi_server.models.e_utran_freq_relation_single import EUtranFreqRelationSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle
from openapi_server.models.external_amf_function_single import ExternalAmfFunctionSingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_eu_tran_cell_single import ExternalEUTranCellSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle
from openapi_server.models.external_nrf_function_single import ExternalNrfFunctionSingle
from openapi_server.models.external_nssf_function_single import ExternalNssfFunctionSingle
from openapi_server.models.feasibility_check_and_reservation_job_single import FeasibilityCheckAndReservationJobSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle
from openapi_server.models.fulfilment_info import FulfilmentInfo
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle
from openapi_server.models.heartbeat_control_single import HeartbeatControlSingle
from openapi_server.models.intent_context import IntentContext
from openapi_server.models.intent_single import IntentSingle
from openapi_server.models.intent_single_all_of_intent_expectations_inner import IntentSingleAllOfIntentExpectationsInner
from openapi_server.models.lmf_function_single import LmfFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_info_single import MnsInfoSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.nef_function_single import NefFunctionSingle
from openapi_server.models.network_slice_single import NetworkSliceSingle
from openapi_server.models.network_slice_subnet_provider_capabilities_single import NetworkSliceSubnetProviderCapabilitiesSingle
from openapi_server.models.network_slice_subnet_single import NetworkSliceSubnetSingle
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle
from openapi_server.models.nr_cell_cu_single import NrCellCuSingle
from openapi_server.models.nr_cell_du_single import NrCellDuSingle
from openapi_server.models.nr_operator_cell_du_single import NrOperatorCellDuSingle
from openapi_server.models.nr_sector_carrier_single import NrSectorCarrierSingle
from openapi_server.models.nrf_function_single import NrfFunctionSingle
from openapi_server.models.nssf_function_single import NssfFunctionSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle
from openapi_server.models.operator_du_single import OperatorDuSingle
from openapi_server.models.pcf_function_single import PcfFunctionSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.plmn_info import PlmnInfo
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle
from openapi_server.models.resources5gc_nrm import Resources5gcNrm
from openapi_server.models.resources_cosla_nrm import ResourcesCoslaNrm
from openapi_server.models.resources_generic_nrm import ResourcesGenericNrm
from openapi_server.models.resources_intent_nrm import ResourcesIntentNrm
from openapi_server.models.resources_nr_nrm import ResourcesNrNrm
from openapi_server.models.resources_slice_nrm import ResourcesSliceNrm
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.rim_rs_set_single import RimRSSetSingle
from openapi_server.models.scp_function_single import ScpFunctionSingle
from openapi_server.models.sepp_function_single import SeppFunctionSingle
from openapi_server.models.smf_function_single import SmfFunctionSingle
from openapi_server.models.smsf_function_single import SmsfFunctionSingle
from openapi_server.models.sub_network_attr import SubNetworkAttr
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.udm_function_single import UdmFunctionSingle
from openapi_server.models.udr_function_single import UdrFunctionSingle
from openapi_server.models.udsf_function_single import UdsfFunctionSingle
from openapi_server.models.upf_function_single import UpfFunctionSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class ResourceOneOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ResourceOneOf1 - a model defined in OpenAPI

        id: The id of this ResourceOneOf1.
        attributes: The attributes of this ResourceOneOf1 [Optional].
        vs_data_container: The vs_data_container of this ResourceOneOf1 [Optional].
        object_class: The object_class of this ResourceOneOf1 [Optional].
        object_instance: The object_instance of this ResourceOneOf1 [Optional].
        mns_agent: The mns_agent of this ResourceOneOf1 [Optional].
        files: The files of this ResourceOneOf1 [Optional].
        heartbeat_control: The heartbeat_control of this ResourceOneOf1 [Optional].
        mns_info: The mns_info of this ResourceOneOf1 [Optional].
        mns_label: The mns_label of this ResourceOneOf1 [Optional].
        mns_type: The mns_type of this ResourceOneOf1 [Optional].
        mns_version: The mns_version of this ResourceOneOf1 [Optional].
        mns_address: The mns_address of this ResourceOneOf1 [Optional].
        mns_scope: The mns_scope of this ResourceOneOf1 [Optional].
        sub_network: The sub_network of this ResourceOneOf1 [Optional].
        managed_element: The managed_element of this ResourceOneOf1 [Optional].
        management_node: The management_node of this ResourceOneOf1 [Optional].
        me_context: The me_context of this ResourceOneOf1 [Optional].
        perf_metric_job: The perf_metric_job of this ResourceOneOf1 [Optional].
        threshold_monitor: The threshold_monitor of this ResourceOneOf1 [Optional].
        trace_job: The trace_job of this ResourceOneOf1 [Optional].
        management_data_collection: The management_data_collection of this ResourceOneOf1 [Optional].
        ntf_subscription_control: The ntf_subscription_control of this ResourceOneOf1 [Optional].
        alarm_list: The alarm_list of this ResourceOneOf1 [Optional].
        file_download_job: The file_download_job of this ResourceOneOf1 [Optional].
        mns_registry: The mns_registry of this ResourceOneOf1 [Optional].
        nr_frequency: The nr_frequency of this ResourceOneOf1 [Optional].
        external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this ResourceOneOf1 [Optional].
        external_enb_function: The external_enb_function of this ResourceOneOf1 [Optional].
        e_utran_frequency: The e_utran_frequency of this ResourceOneOf1 [Optional].
        des_management_function: The des_management_function of this ResourceOneOf1 [Optional].
        drach_optimization_function: The drach_optimization_function of this ResourceOneOf1 [Optional].
        dmro_function: The dmro_function of this ResourceOneOf1 [Optional].
        dlbo_function: The dlbo_function of this ResourceOneOf1 [Optional].
        dpci_configuration_function: The dpci_configuration_function of this ResourceOneOf1 [Optional].
        cpci_configuration_function: The cpci_configuration_function of this ResourceOneOf1 [Optional].
        ces_management_function: The ces_management_function of this ResourceOneOf1 [Optional].
        configurable5_qi_set: The configurable5_qi_set of this ResourceOneOf1 [Optional].
        rim_rs_global: The rim_rs_global of this ResourceOneOf1 [Optional].
        dynamic5_qi_set: The dynamic5_qi_set of this ResourceOneOf1 [Optional].
        cco_function: The cco_function of this ResourceOneOf1 [Optional].
        gnb_du_function: The gnb_du_function of this ResourceOneOf1 [Optional].
        gnb_cu_up_function: The gnb_cu_up_function of this ResourceOneOf1 [Optional].
        gnb_cu_cp_function: The gnb_cu_cp_function of this ResourceOneOf1 [Optional].
        managed_nf_service: The managed_nf_service of this ResourceOneOf1 [Optional].
        rrm_policy_ratio: The rrm_policy_ratio of this ResourceOneOf1 [Optional].
        nr_cell_du: The nr_cell_du of this ResourceOneOf1 [Optional].
        bwp_multiple: The bwp_multiple of this ResourceOneOf1 [Optional].
        nr_sector_carrier_multiple: The nr_sector_carrier_multiple of this ResourceOneOf1 [Optional].
        ep_f1_c: The ep_f1_c of this ResourceOneOf1 [Optional].
        ep_f1_u: The ep_f1_u of this ResourceOneOf1 [Optional].
        operator_du: The operator_du of this ResourceOneOf1 [Optional].
        ep_e1: The ep_e1 of this ResourceOneOf1 [Optional].
        ep_xn_u: The ep_xn_u of this ResourceOneOf1 [Optional].
        ep_ng_u: The ep_ng_u of this ResourceOneOf1 [Optional].
        ep_x2_u: The ep_x2_u of this ResourceOneOf1 [Optional].
        ep_s1_u: The ep_s1_u of this ResourceOneOf1 [Optional].
        nr_cell_cu: The nr_cell_cu of this ResourceOneOf1 [Optional].
        ep_xn_c: The ep_xn_c of this ResourceOneOf1 [Optional].
        ep_ng_c: The ep_ng_c of this ResourceOneOf1 [Optional].
        ep_x2_c: The ep_x2_c of this ResourceOneOf1 [Optional].
        danr_management_function: The danr_management_function of this ResourceOneOf1 [Optional].
        gnb_id: The gnb_id of this ResourceOneOf1 [Optional].
        gnb_id_length: The gnb_id_length of this ResourceOneOf1 [Optional].
        nr_cell_relation: The nr_cell_relation of this ResourceOneOf1 [Optional].
        e_utran_cell_relation: The e_utran_cell_relation of this ResourceOneOf1 [Optional].
        nr_freq_relation: The nr_freq_relation of this ResourceOneOf1 [Optional].
        e_utran_freq_relation: The e_utran_freq_relation of this ResourceOneOf1 [Optional].
        nr_operator_cell_du: The nr_operator_cell_du of this ResourceOneOf1 [Optional].
        cell_local_id: The cell_local_id of this ResourceOneOf1 [Optional].
        administrative_state: The administrative_state of this ResourceOneOf1 [Optional].
        plmn_info_list: The plmn_info_list of this ResourceOneOf1 [Optional].
        nr_tac: The nr_tac of this ResourceOneOf1 [Optional].
        common_beamforming_function: The common_beamforming_function of this ResourceOneOf1 [Optional].
        beam: The beam of this ResourceOneOf1 [Optional].
        rim_rs_set: The rim_rs_set of this ResourceOneOf1 [Optional].
        external_nr_cell_cu: The external_nr_cell_cu of this ResourceOneOf1 [Optional].
        external_eu_tran_cell: The external_eu_tran_cell of this ResourceOneOf1 [Optional].
        external_amf_function: The external_amf_function of this ResourceOneOf1 [Optional].
        external_nrf_function: The external_nrf_function of this ResourceOneOf1 [Optional].
        external_nssf_function: The external_nssf_function of this ResourceOneOf1 [Optional].
        amf_set: The amf_set of this ResourceOneOf1 [Optional].
        amf_region: The amf_region of this ResourceOneOf1 [Optional].
        ecm_connection_info: The ecm_connection_info of this ResourceOneOf1 [Optional].
        amf_function: The amf_function of this ResourceOneOf1 [Optional].
        smf_function: The smf_function of this ResourceOneOf1 [Optional].
        upf_function: The upf_function of this ResourceOneOf1 [Optional].
        n3iwf_function: The n3iwf_function of this ResourceOneOf1 [Optional].
        pcf_function: The pcf_function of this ResourceOneOf1 [Optional].
        ausf_function: The ausf_function of this ResourceOneOf1 [Optional].
        udm_function: The udm_function of this ResourceOneOf1 [Optional].
        udr_function: The udr_function of this ResourceOneOf1 [Optional].
        udsf_function: The udsf_function of this ResourceOneOf1 [Optional].
        nrf_function: The nrf_function of this ResourceOneOf1 [Optional].
        nssf_function: The nssf_function of this ResourceOneOf1 [Optional].
        smsf_function: The smsf_function of this ResourceOneOf1 [Optional].
        lmf_function: The lmf_function of this ResourceOneOf1 [Optional].
        ngeir_function: The ngeir_function of this ResourceOneOf1 [Optional].
        sepp_function: The sepp_function of this ResourceOneOf1 [Optional].
        nwdaf_function: The nwdaf_function of this ResourceOneOf1 [Optional].
        scp_function: The scp_function of this ResourceOneOf1 [Optional].
        nef_function: The nef_function of this ResourceOneOf1 [Optional].
        easdf_function: The easdf_function of this ResourceOneOf1 [Optional].
        ep_n2: The ep_n2 of this ResourceOneOf1 [Optional].
        ep_n8: The ep_n8 of this ResourceOneOf1 [Optional].
        ep_n11: The ep_n11 of this ResourceOneOf1 [Optional].
        ep_n12: The ep_n12 of this ResourceOneOf1 [Optional].
        ep_n14: The ep_n14 of this ResourceOneOf1 [Optional].
        ep_n15: The ep_n15 of this ResourceOneOf1 [Optional].
        ep_n17: The ep_n17 of this ResourceOneOf1 [Optional].
        ep_n20: The ep_n20 of this ResourceOneOf1 [Optional].
        ep_n22: The ep_n22 of this ResourceOneOf1 [Optional].
        ep_n26: The ep_n26 of this ResourceOneOf1 [Optional].
        ep_nls: The ep_nls of this ResourceOneOf1 [Optional].
        ep_nlg: The ep_nlg of this ResourceOneOf1 [Optional].
        ep_n4: The ep_n4 of this ResourceOneOf1 [Optional].
        ep_n7: The ep_n7 of this ResourceOneOf1 [Optional].
        ep_n10: The ep_n10 of this ResourceOneOf1 [Optional].
        ep_n16: The ep_n16 of this ResourceOneOf1 [Optional].
        ep_s5_c: The ep_s5_c of this ResourceOneOf1 [Optional].
        five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this ResourceOneOf1 [Optional].
        gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this ResourceOneOf1 [Optional].
        qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this ResourceOneOf1 [Optional].
        predefined_pcc_rule_set: The predefined_pcc_rule_set of this ResourceOneOf1 [Optional].
        ep_n3: The ep_n3 of this ResourceOneOf1 [Optional].
        ep_n6: The ep_n6 of this ResourceOneOf1 [Optional].
        ep_n9: The ep_n9 of this ResourceOneOf1 [Optional].
        ep_s5_u: The ep_s5_u of this ResourceOneOf1 [Optional].
        ep_n5: The ep_n5 of this ResourceOneOf1 [Optional].
        ep_rx: The ep_rx of this ResourceOneOf1 [Optional].
        ep_n13: The ep_n13 of this ResourceOneOf1 [Optional].
        ep_n27: The ep_n27 of this ResourceOneOf1 [Optional].
        ep_n31: The ep_n31 of this ResourceOneOf1 [Optional].
        ep_n21: The ep_n21 of this ResourceOneOf1 [Optional].
        ep_map_smsc: The ep_map_smsc of this ResourceOneOf1 [Optional].
        ep_n32: The ep_n32 of this ResourceOneOf1 [Optional].
        ep_n33: The ep_n33 of this ResourceOneOf1 [Optional].
        ep_n60: The ep_n60 of this ResourceOneOf1 [Optional].
        ep_npc4: The ep_npc4 of this ResourceOneOf1 [Optional].
        ep_npc6: The ep_npc6 of this ResourceOneOf1 [Optional].
        ep_npc7: The ep_npc7 of this ResourceOneOf1 [Optional].
        ep_npc8: The ep_npc8 of this ResourceOneOf1 [Optional].
        ep_n88: The ep_n88 of this ResourceOneOf1 [Optional].
        network_slice: The network_slice of this ResourceOneOf1 [Optional].
        network_slice_subnet: The network_slice_subnet of this ResourceOneOf1 [Optional].
        ep_transport: The ep_transport of this ResourceOneOf1 [Optional].
        network_slice_subnet_provider_capabilities: The network_slice_subnet_provider_capabilities of this ResourceOneOf1 [Optional].
        feasibility_check_and_reservation_job: The feasibility_check_and_reservation_job of this ResourceOneOf1 [Optional].
        assurance_goal: The assurance_goal of this ResourceOneOf1 [Optional].
        assurance_closed_control_loop: The assurance_closed_control_loop of this ResourceOneOf1 [Optional].
        intent: The intent of this ResourceOneOf1 [Optional].
        user_label: The user_label of this ResourceOneOf1 [Optional].
        intent_expectations: The intent_expectations of this ResourceOneOf1 [Optional].
        intent_contexts: The intent_contexts of this ResourceOneOf1 [Optional].
        intent_fulfilment_info: The intent_fulfilment_info of this ResourceOneOf1 [Optional].
    """

    id: str = Field(alias="id")
    attributes: Optional[SubNetworkAttr] = Field(alias="attributes", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    mns_agent: Optional[List[MnsAgentSingle]] = Field(alias="MnsAgent", default=None)
    files: Optional[List[FilesSingle]] = Field(alias="Files", default=None)
    heartbeat_control: Optional[HeartbeatControlSingle] = Field(alias="HeartbeatControl", default=None)
    mns_info: Optional[List[MnsInfoSingle]] = Field(alias="MnsInfo", default=None)
    mns_label: Optional[str] = Field(alias="mnsLabel", default=None)
    mns_type: Optional[str] = Field(alias="mnsType", default=None)
    mns_version: Optional[str] = Field(alias="mnsVersion", default=None)
    mns_address: Optional[str] = Field(alias="mnsAddress", default=None)
    mns_scope: Optional[List[str]] = Field(alias="mnsScope", default=None)
    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)
    managed_element: Optional[List[ManagedElementSingle]] = Field(alias="ManagedElement", default=None)
    management_node: Optional[List[ManagementNodeSingle]] = Field(alias="ManagementNode", default=None)
    me_context: Optional[List[MeContextSingle]] = Field(alias="MeContext", default=None)
    perf_metric_job: Optional[List[PerfMetricJobSingle]] = Field(alias="PerfMetricJob", default=None)
    threshold_monitor: Optional[List[ThresholdMonitorSingle]] = Field(alias="ThresholdMonitor", default=None)
    trace_job: Optional[List[TraceJobSingle]] = Field(alias="TraceJob", default=None)
    management_data_collection: Optional[List[ManagementDataCollectionSingle]] = Field(alias="ManagementDataCollection", default=None)
    ntf_subscription_control: Optional[List[NtfSubscriptionControlSingle]] = Field(alias="NtfSubscriptionControl", default=None)
    alarm_list: Optional[AlarmListSingle] = Field(alias="AlarmList", default=None)
    file_download_job: Optional[List[FileDownloadJobSingle]] = Field(alias="FileDownloadJob", default=None)
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
    external_amf_function: Optional[List[ExternalAmfFunctionSingle]] = Field(alias="ExternalAmfFunction", default=None)
    external_nrf_function: Optional[List[ExternalNrfFunctionSingle]] = Field(alias="ExternalNrfFunction", default=None)
    external_nssf_function: Optional[List[ExternalNssfFunctionSingle]] = Field(alias="ExternalNssfFunction", default=None)
    amf_set: Optional[List[AmfSetSingle]] = Field(alias="AmfSet", default=None)
    amf_region: Optional[List[AmfRegionSingle]] = Field(alias="AmfRegion", default=None)
    ecm_connection_info: Optional[List[EcmConnectionInfoSingle]] = Field(alias="EcmConnectionInfo", default=None)
    amf_function: Optional[List[AmfFunctionSingle]] = Field(alias="AmfFunction", default=None)
    smf_function: Optional[List[SmfFunctionSingle]] = Field(alias="SmfFunction", default=None)
    upf_function: Optional[List[UpfFunctionSingle]] = Field(alias="UpfFunction", default=None)
    n3iwf_function: Optional[List[N3iwfFunctionSingle]] = Field(alias="N3iwfFunction", default=None)
    pcf_function: Optional[List[PcfFunctionSingle]] = Field(alias="PcfFunction", default=None)
    ausf_function: Optional[List[AusfFunctionSingle]] = Field(alias="AusfFunction", default=None)
    udm_function: Optional[List[UdmFunctionSingle]] = Field(alias="UdmFunction", default=None)
    udr_function: Optional[List[UdrFunctionSingle]] = Field(alias="UdrFunction", default=None)
    udsf_function: Optional[List[UdsfFunctionSingle]] = Field(alias="UdsfFunction", default=None)
    nrf_function: Optional[List[NrfFunctionSingle]] = Field(alias="NrfFunction", default=None)
    nssf_function: Optional[List[NssfFunctionSingle]] = Field(alias="NssfFunction", default=None)
    smsf_function: Optional[List[SmsfFunctionSingle]] = Field(alias="SmsfFunction", default=None)
    lmf_function: Optional[List[LmfFunctionSingle]] = Field(alias="LmfFunction", default=None)
    ngeir_function: Optional[List[NgeirFunctionSingle]] = Field(alias="NgeirFunction", default=None)
    sepp_function: Optional[List[SeppFunctionSingle]] = Field(alias="SeppFunction", default=None)
    nwdaf_function: Optional[List[NwdafFunctionSingle]] = Field(alias="NwdafFunction", default=None)
    scp_function: Optional[List[ScpFunctionSingle]] = Field(alias="ScpFunction", default=None)
    nef_function: Optional[List[NefFunctionSingle]] = Field(alias="NefFunction", default=None)
    easdf_function: Optional[List[EASDFFunctionSingle]] = Field(alias="EASDFFunction", default=None)
    ep_n2: Optional[List[EPN2Single]] = Field(alias="EP_N2", default=None)
    ep_n8: Optional[List[EPN8Single]] = Field(alias="EP_N8", default=None)
    ep_n11: Optional[List[EPN11Single]] = Field(alias="EP_N11", default=None)
    ep_n12: Optional[List[EPN12Single]] = Field(alias="EP_N12", default=None)
    ep_n14: Optional[List[EPN14Single]] = Field(alias="EP_N14", default=None)
    ep_n15: Optional[List[EPN15Single]] = Field(alias="EP_N15", default=None)
    ep_n17: Optional[List[EPN17Single]] = Field(alias="EP_N17", default=None)
    ep_n20: Optional[List[EPN20Single]] = Field(alias="EP_N20", default=None)
    ep_n22: Optional[List[EPN22Single]] = Field(alias="EP_N22", default=None)
    ep_n26: Optional[List[EPN26Single]] = Field(alias="EP_N26", default=None)
    ep_nls: Optional[List[EPNLSSingle]] = Field(alias="EP_NLS", default=None)
    ep_nlg: Optional[List[EPNLGSingle]] = Field(alias="EP_NLG", default=None)
    ep_n4: Optional[List[EPN4Single]] = Field(alias="EP_N4", default=None)
    ep_n7: Optional[List[EPN7Single]] = Field(alias="EP_N7", default=None)
    ep_n10: Optional[List[EPN10Single]] = Field(alias="EP_N10", default=None)
    ep_n16: Optional[List[EPN16Single]] = Field(alias="EP_N16", default=None)
    ep_s5_c: Optional[List[EPS5CSingle]] = Field(alias="EP_S5C", default=None)
    five_qi_dscp_mapping_set: Optional[FiveQiDscpMappingSetSingle] = Field(alias="FiveQiDscpMappingSet", default=None)
    gtp_u_path_qo_s_monitoring_control: Optional[GtpUPathQoSMonitoringControlSingle] = Field(alias="GtpUPathQoSMonitoringControl", default=None)
    qfqo_s_monitoring_control: Optional[QFQoSMonitoringControlSingle] = Field(alias="QFQoSMonitoringControl", default=None)
    predefined_pcc_rule_set: Optional[PredefinedPccRuleSetSingle] = Field(alias="PredefinedPccRuleSet", default=None)
    ep_n3: Optional[List[EPN3Single]] = Field(alias="EP_N3", default=None)
    ep_n6: Optional[List[EPN6Single]] = Field(alias="EP_N6", default=None)
    ep_n9: Optional[List[EPN9Single]] = Field(alias="EP_N9", default=None)
    ep_s5_u: Optional[List[EPS5USingle]] = Field(alias="EP_S5U", default=None)
    ep_n5: Optional[List[EPN5Single]] = Field(alias="EP_N5", default=None)
    ep_rx: Optional[List[EPRxSingle]] = Field(alias="EP_Rx", default=None)
    ep_n13: Optional[List[EPN13Single]] = Field(alias="EP_N13", default=None)
    ep_n27: Optional[List[EPN27Single]] = Field(alias="EP_N27", default=None)
    ep_n31: Optional[List[EPN31Single]] = Field(alias="EP_N31", default=None)
    ep_n21: Optional[List[EPN21Single]] = Field(alias="EP_N21", default=None)
    ep_map_smsc: Optional[List[EPMAPSMSCSingle]] = Field(alias="EP_MAP_SMSC", default=None)
    ep_n32: Optional[List[EPN32Single]] = Field(alias="EP_N32", default=None)
    ep_n33: Optional[List[EPN33Single]] = Field(alias="EP_N33", default=None)
    ep_n60: Optional[List[EPN60Single]] = Field(alias="EP_N60", default=None)
    ep_npc4: Optional[List[EPNpc4Single]] = Field(alias="EP_Npc4", default=None)
    ep_npc6: Optional[List[EPNpc6Single]] = Field(alias="EP_Npc6", default=None)
    ep_npc7: Optional[List[EPNpc7Single]] = Field(alias="EP_Npc7", default=None)
    ep_npc8: Optional[List[EPNpc8Single]] = Field(alias="EP_Npc8", default=None)
    ep_n88: Optional[List[EPN88Single]] = Field(alias="EP_N88", default=None)
    network_slice: Optional[List[NetworkSliceSingle]] = Field(alias="NetworkSlice", default=None)
    network_slice_subnet: Optional[List[NetworkSliceSubnetSingle]] = Field(alias="NetworkSliceSubnet", default=None)
    ep_transport: Optional[List[EPTransportSingle]] = Field(alias="EP_Transport", default=None)
    network_slice_subnet_provider_capabilities: Optional[List[NetworkSliceSubnetProviderCapabilitiesSingle]] = Field(alias="NetworkSliceSubnetProviderCapabilities", default=None)
    feasibility_check_and_reservation_job: Optional[List[FeasibilityCheckAndReservationJobSingle]] = Field(alias="FeasibilityCheckAndReservationJob", default=None)
    assurance_goal: Optional[List[AssuranceGoalSingle]] = Field(alias="AssuranceGoal", default=None)
    assurance_closed_control_loop: Optional[List[AssuranceClosedControlLoopSingle]] = Field(alias="AssuranceClosedControlLoop", default=None)
    intent: Optional[List[IntentSingle]] = Field(alias="Intent", default=None)
    user_label: Optional[str] = Field(alias="userLabel", default=None)
    intent_expectations: Optional[List[IntentSingleAllOfIntentExpectationsInner]] = Field(alias="intentExpectations", default=None)
    intent_contexts: Optional[List[IntentContext]] = Field(alias="intentContexts", default=None)
    intent_fulfilment_info: Optional[FulfilmentInfo] = Field(alias="intentFulfilmentInfo", default=None)

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

ResourceOneOf1.update_forward_refs()
