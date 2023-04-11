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
from openapi_server.models.nr_cell_relation_single import NRCellRelationSingle
from openapi_server.models.nr_freq_relation_single import NRFreqRelationSingle
from openapi_server.models.rrm_policy_ratio_single import RRMPolicyRatioSingle


class NrCellCuSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NrCellCuSingleAllOf1 - a model defined in OpenAPI

        rrm_policy_ratio: The rrm_policy_ratio of this NrCellCuSingleAllOf1 [Optional].
        nr_cell_relation: The nr_cell_relation of this NrCellCuSingleAllOf1 [Optional].
        e_utran_cell_relation: The e_utran_cell_relation of this NrCellCuSingleAllOf1 [Optional].
        nr_freq_relation: The nr_freq_relation of this NrCellCuSingleAllOf1 [Optional].
        e_utran_freq_relation: The e_utran_freq_relation of this NrCellCuSingleAllOf1 [Optional].
        des_management_function: The des_management_function of this NrCellCuSingleAllOf1 [Optional].
        dmro_function: The dmro_function of this NrCellCuSingleAllOf1 [Optional].
        dlbo_function: The dlbo_function of this NrCellCuSingleAllOf1 [Optional].
        ces_management_function: The ces_management_function of this NrCellCuSingleAllOf1 [Optional].
        dpci_configuration_function: The dpci_configuration_function of this NrCellCuSingleAllOf1 [Optional].
    """

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

NrCellCuSingleAllOf1.update_forward_refs()