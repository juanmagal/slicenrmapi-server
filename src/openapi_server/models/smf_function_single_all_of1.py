# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn10_single import EPN10Single
from openapi_server.models.epn11_single import EPN11Single
from openapi_server.models.epn16_single import EPN16Single
from openapi_server.models.epn4_single import EPN4Single
from openapi_server.models.epn7_single import EPN7Single
from openapi_server.models.eps5_c_single import EPS5CSingle
from openapi_server.models.five_qi_dscp_mapping_set_single import FiveQiDscpMappingSetSingle
from openapi_server.models.gtp_u_path_qo_s_monitoring_control_single import GtpUPathQoSMonitoringControlSingle
from openapi_server.models.predefined_pcc_rule_set_single import PredefinedPccRuleSetSingle
from openapi_server.models.qfqo_s_monitoring_control_single import QFQoSMonitoringControlSingle


class SmfFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SmfFunctionSingleAllOf1 - a model defined in OpenAPI

        ep_n4: The ep_n4 of this SmfFunctionSingleAllOf1 [Optional].
        ep_n7: The ep_n7 of this SmfFunctionSingleAllOf1 [Optional].
        ep_n10: The ep_n10 of this SmfFunctionSingleAllOf1 [Optional].
        ep_n11: The ep_n11 of this SmfFunctionSingleAllOf1 [Optional].
        ep_n16: The ep_n16 of this SmfFunctionSingleAllOf1 [Optional].
        ep_s5_c: The ep_s5_c of this SmfFunctionSingleAllOf1 [Optional].
        five_qi_dscp_mapping_set: The five_qi_dscp_mapping_set of this SmfFunctionSingleAllOf1 [Optional].
        gtp_u_path_qo_s_monitoring_control: The gtp_u_path_qo_s_monitoring_control of this SmfFunctionSingleAllOf1 [Optional].
        qfqo_s_monitoring_control: The qfqo_s_monitoring_control of this SmfFunctionSingleAllOf1 [Optional].
        predefined_pcc_rule_set: The predefined_pcc_rule_set of this SmfFunctionSingleAllOf1 [Optional].
    """

    ep_n4: Optional[List[EPN4Single]] = Field(alias="EP_N4", default=None)
    ep_n7: Optional[List[EPN7Single]] = Field(alias="EP_N7", default=None)
    ep_n10: Optional[List[EPN10Single]] = Field(alias="EP_N10", default=None)
    ep_n11: Optional[List[EPN11Single]] = Field(alias="EP_N11", default=None)
    ep_n16: Optional[List[EPN16Single]] = Field(alias="EP_N16", default=None)
    ep_s5_c: Optional[List[EPS5CSingle]] = Field(alias="EP_S5C", default=None)
    five_qi_dscp_mapping_set: Optional[FiveQiDscpMappingSetSingle] = Field(alias="FiveQiDscpMappingSet", default=None)
    gtp_u_path_qo_s_monitoring_control: Optional[GtpUPathQoSMonitoringControlSingle] = Field(alias="GtpUPathQoSMonitoringControl", default=None)
    qfqo_s_monitoring_control: Optional[QFQoSMonitoringControlSingle] = Field(alias="QFQoSMonitoringControl", default=None)
    predefined_pcc_rule_set: Optional[PredefinedPccRuleSetSingle] = Field(alias="PredefinedPccRuleSet", default=None)

SmfFunctionSingleAllOf1.update_forward_refs()
