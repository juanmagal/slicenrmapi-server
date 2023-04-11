# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.alarm_list_single import AlarmListSingle
from openapi_server.models.amf_function_single import AmfFunctionSingle
from openapi_server.models.amf_region_single import AmfRegionSingle
from openapi_server.models.amf_set_single import AmfSetSingle
from openapi_server.models.ausf_function_single import AusfFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.ddnmf_function_single import DDNMFFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.easdf_function_single import EASDFFunctionSingle
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
from openapi_server.models.ep_npc4_single import EPNpc4Single
from openapi_server.models.ep_npc6_single import EPNpc6Single
from openapi_server.models.ep_npc7_single import EPNpc7Single
from openapi_server.models.ep_npc8_single import EPNpc8Single
from openapi_server.models.eprx_single import EPRxSingle
from openapi_server.models.eps5_c_single import EPS5CSingle
from openapi_server.models.eps5_u_single import EPS5USingle
from openapi_server.models.ecm_connection_info_single import EcmConnectionInfoSingle
from openapi_server.models.ecm_connection_info_single_all_of_attributes import EcmConnectionInfoSingleAllOfAttributes
from openapi_server.models.external_amf_function_single import ExternalAmfFunctionSingle
from openapi_server.models.external_nrf_function_single import ExternalNrfFunctionSingle
from openapi_server.models.external_nssf_function_single import ExternalNssfFunctionSingle
from openapi_server.models.external_sepp_function_single import ExternalSeppFunctionSingle
from openapi_server.models.file_download_job_single import FileDownloadJobSingle
from openapi_server.models.files_single import FilesSingle
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle
from openapi_server.models.lmf_function_single import LmfFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.managed_element_single1 import ManagedElementSingle1
from openapi_server.models.managed_nf_service_single import ManagedNFServiceSingle
from openapi_server.models.management_data_collection_single import ManagementDataCollectionSingle
from openapi_server.models.management_node_single import ManagementNodeSingle
from openapi_server.models.me_context_single import MeContextSingle
from openapi_server.models.mns_agent_single import MnsAgentSingle
from openapi_server.models.mns_registry_single import MnsRegistrySingle
from openapi_server.models.n3iwf_function_single import N3iwfFunctionSingle
from openapi_server.models.nef_function_single import NefFunctionSingle
from openapi_server.models.ngeir_function_single import NgeirFunctionSingle
from openapi_server.models.nrf_function_single import NrfFunctionSingle
from openapi_server.models.nsacf_function_single import NsacfFunctionSingle
from openapi_server.models.nssf_function_single import NssfFunctionSingle
from openapi_server.models.ntf_subscription_control_single import NtfSubscriptionControlSingle
from openapi_server.models.nwdaf_function_single import NwdafFunctionSingle
from openapi_server.models.pcf_function_single import PcfFunctionSingle
from openapi_server.models.perf_metric_job_single import PerfMetricJobSingle
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_server.models.prov_mn_s import ProvMnS
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle
from openapi_server.models.scp_function_single import ScpFunctionSingle
from openapi_server.models.sepp_function_single import SeppFunctionSingle
from openapi_server.models.smf_function_single import SmfFunctionSingle
from openapi_server.models.smsf_function_single import SmsfFunctionSingle
from openapi_server.models.sub_network_single import SubNetworkSingle
from openapi_server.models.sub_network_single1 import SubNetworkSingle1
from openapi_server.models.threshold_monitor_single import ThresholdMonitorSingle
from openapi_server.models.trace_job_single import TraceJobSingle
from openapi_server.models.udm_function_single import UdmFunctionSingle
from openapi_server.models.udr_function_single import UdrFunctionSingle
from openapi_server.models.udsf_function_single import UdsfFunctionSingle
from openapi_server.models.upf_function_single import UpfFunctionSingle
from openapi_server.models.vs_data_container_single import VsDataContainerSingle


class Resources5gcNrm(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Resources5gcNrm - a model defined in OpenAPI

        sub_network: The sub_network of this Resources5gcNrm [Optional].
        managed_element: The managed_element of this Resources5gcNrm [Optional].
        id: The id of this Resources5gcNrm.
        object_class: The object_class of this Resources5gcNrm [Optional].
        object_instance: The object_instance of this Resources5gcNrm [Optional].
        vs_data_container: The vs_data_container of this Resources5gcNrm [Optional].
        attributes: The attributes of this Resources5gcNrm [Optional].
        management_node: The management_node of this Resources5gcNrm [Optional].
        mns_agent: The mns_agent of this Resources5gcNrm [Optional].
        me_context: The me_context of this Resources5gcNrm [Optional].
        perf_metric_job: The perf_metric_job of this Resources5gcNrm [Optional].
        threshold_monitor: The threshold_monitor of this Resources5gcNrm [Optional].
        trace_job: The trace_job of this Resources5gcNrm [Optional].
        management_data_collection: The management_data_collection of this Resources5gcNrm [Optional].
        ntf_subscription_control: The ntf_subscription_control of this Resources5gcNrm [Optional].
        alarm_list: The alarm_list of this Resources5gcNrm [Optional].
        file_download_job: The file_download_job of this Resources5gcNrm [Optional].
        files: The files of this Resources5gcNrm [Optional].
        mns_registry: The mns_registry of this Resources5gcNrm [Optional].
        external_amf_function: The external_amf_function of this Resources5gcNrm [Optional].
        external_nrf_function: The external_nrf_function of this Resources5gcNrm [Optional].
        external_nssf_function: The external_nssf_function of this Resources5gcNrm [Optional].
        amf_set: The amf_set of this Resources5gcNrm [Optional].
        amf_region: The amf_region of this Resources5gcNrm [Optional].
        configurable5_qi_set: The configurable5_qi_set of this Resources5gcNrm [Optional].
        dynamic5_qi_set: The dynamic5_qi_set of this Resources5gcNrm [Optional].
        ecm_connection_info: The ecm_connection_info of this Resources5gcNrm [Optional].
        amf_function: The amf_function of this Resources5gcNrm [Optional].
        smf_function: The smf_function of this Resources5gcNrm [Optional].
        upf_function: The upf_function of this Resources5gcNrm [Optional].
        n3iwf_function: The n3iwf_function of this Resources5gcNrm [Optional].
        pcf_function: The pcf_function of this Resources5gcNrm [Optional].
        ausf_function: The ausf_function of this Resources5gcNrm [Optional].
        udm_function: The udm_function of this Resources5gcNrm [Optional].
        udr_function: The udr_function of this Resources5gcNrm [Optional].
        udsf_function: The udsf_function of this Resources5gcNrm [Optional].
        nrf_function: The nrf_function of this Resources5gcNrm [Optional].
        nssf_function: The nssf_function of this Resources5gcNrm [Optional].
        smsf_function: The smsf_function of this Resources5gcNrm [Optional].
        lmf_function: The lmf_function of this Resources5gcNrm [Optional].
        ngeir_function: The ngeir_function of this Resources5gcNrm [Optional].
        sepp_function: The sepp_function of this Resources5gcNrm [Optional].
        nwdaf_function: The nwdaf_function of this Resources5gcNrm [Optional].
        scp_function: The scp_function of this Resources5gcNrm [Optional].
        nef_function: The nef_function of this Resources5gcNrm [Optional].
        easdf_function: The easdf_function of this Resources5gcNrm [Optional].
        managed_nf_service: The managed_nf_service of this Resources5gcNrm [Optional].
        ep_n2: The ep_n2 of this Resources5gcNrm [Optional].
        ep_n8: The ep_n8 of this Resources5gcNrm [Optional].
        ep_n11: The ep_n11 of this Resources5gcNrm [Optional].
        ep_n12: The ep_n12 of this Resources5gcNrm [Optional].
        ep_n14: The ep_n14 of this Resources5gcNrm [Optional].
        ep_n15: The ep_n15 of this Resources5gcNrm [Optional].
        ep_n17: The ep_n17 of this Resources5gcNrm [Optional].
        ep_n20: The ep_n20 of this Resources5gcNrm [Optional].
        ep_n22: The ep_n22 of this Resources5gcNrm [Optional].
        ep_n26: The ep_n26 of this Resources5gcNrm [Optional].
        ep_nls: The ep_nls of this Resources5gcNrm [Optional].
        ep_nlg: The ep_nlg of this Resources5gcNrm [Optional].
        ep_n4: The ep_n4 of this Resources5gcNrm [Optional].
        ep_n7: The ep_n7 of this Resources5gcNrm [Optional].
        ep_n10: The ep_n10 of this Resources5gcNrm [Optional].
        ep_n16: The ep_n16 of this Resources5gcNrm [Optional].
        ep_s5_c: The ep_s5_c of this Resources5gcNrm [Optional].
        five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this Resources5gcNrm [Optional].
        gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this Resources5gcNrm [Optional].
        qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this Resources5gcNrm [Optional].
        predefined_pcc_rule_set: The predefined_pcc_rule_set of this Resources5gcNrm [Optional].
        ep_n3: The ep_n3 of this Resources5gcNrm [Optional].
        ep_n6: The ep_n6 of this Resources5gcNrm [Optional].
        ep_n9: The ep_n9 of this Resources5gcNrm [Optional].
        ep_s5_u: The ep_s5_u of this Resources5gcNrm [Optional].
        ep_n5: The ep_n5 of this Resources5gcNrm [Optional].
        ep_rx: The ep_rx of this Resources5gcNrm [Optional].
        ep_n13: The ep_n13 of this Resources5gcNrm [Optional].
        ep_n27: The ep_n27 of this Resources5gcNrm [Optional].
        ep_n31: The ep_n31 of this Resources5gcNrm [Optional].
        ep_n21: The ep_n21 of this Resources5gcNrm [Optional].
        ep_map_smsc: The ep_map_smsc of this Resources5gcNrm [Optional].
        ep_n32: The ep_n32 of this Resources5gcNrm [Optional].
        ep_n33: The ep_n33 of this Resources5gcNrm [Optional].
        ep_n60: The ep_n60 of this Resources5gcNrm [Optional].
        ep_npc4: The ep_npc4 of this Resources5gcNrm [Optional].
        ep_npc6: The ep_npc6 of this Resources5gcNrm [Optional].
        ep_npc7: The ep_npc7 of this Resources5gcNrm [Optional].
        ep_npc8: The ep_npc8 of this Resources5gcNrm [Optional].
        ep_n88: The ep_n88 of this Resources5gcNrm [Optional].
    """

    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)
    managed_element: Optional[List[ManagedElementSingle]] = Field(alias="ManagedElement", default=None)
    id: str = Field(alias="id")
    object_class: Optional[str] = Field(alias="objectClass", default=None)
    object_instance: Optional[str] = Field(alias="objectInstance", default=None)
    vs_data_container: Optional[List[VsDataContainerSingle]] = Field(alias="VsDataContainer", default=None)
    attributes: Optional[EcmConnectionInfoSingleAllOfAttributes] = Field(alias="attributes", default=None)
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
    external_amf_function: Optional[List[ExternalAmfFunctionSingle]] = Field(alias="ExternalAmfFunction", default=None)
    external_nrf_function: Optional[List[ExternalNrfFunctionSingle]] = Field(alias="ExternalNrfFunction", default=None)
    external_nssf_function: Optional[List[ExternalNssfFunctionSingle]] = Field(alias="ExternalNssfFunction", default=None)
    amf_set: Optional[List[AmfSetSingle]] = Field(alias="AmfSet", default=None)
    amf_region: Optional[List[AmfRegionSingle]] = Field(alias="AmfRegion", default=None)
    configurable5_qi_set: Optional[List[Configurable5QISetSingle]] = Field(alias="Configurable5QISet", default=None)
    dynamic5_qi_set: Optional[List[Dynamic5QISetSingle]] = Field(alias="Dynamic5QISet", default=None)
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
    managed_nf_service: Optional[List[ManagedNFServiceSingle]] = Field(alias="ManagedNFService", default=None)
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

Resources5gcNrm.update_forward_refs()
