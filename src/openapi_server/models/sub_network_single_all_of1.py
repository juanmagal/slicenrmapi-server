# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.cco_function_single import CCOFunctionSingle
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.e_utran_frequency_single import EUtranFrequencySingle
from openapi_server.models.external_enb_function_single import ExternalENBFunctionSingle
from openapi_server.models.external_gnb_cu_cp_function_single import ExternalGnbCuCpFunctionSingle
from openapi_server.models.managed_element_single import ManagedElementSingle
from openapi_server.models.nr_frequency_single import NRFrequencySingle
from openapi_server.models.rim_rs_global_single import RimRSGlobalSingle
from openapi_server.models.sub_network_single import SubNetworkSingle


class SubNetworkSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubNetworkSingleAllOf1 - a model defined in OpenAPI

        sub_network: The sub_network of this SubNetworkSingleAllOf1 [Optional].
        managed_element: The managed_element of this SubNetworkSingleAllOf1 [Optional].
        nr_frequency: The nr_frequency of this SubNetworkSingleAllOf1 [Optional].
        external_gnb_cu_cp_function: The external_gnb_cu_cp_function of this SubNetworkSingleAllOf1 [Optional].
        external_enb_function: The external_enb_function of this SubNetworkSingleAllOf1 [Optional].
        e_utran_frequency: The e_utran_frequency of this SubNetworkSingleAllOf1 [Optional].
        des_management_function: The des_management_function of this SubNetworkSingleAllOf1 [Optional].
        drach_optimization_function: The drach_optimization_function of this SubNetworkSingleAllOf1 [Optional].
        dmro_function: The dmro_function of this SubNetworkSingleAllOf1 [Optional].
        dlbo_function: The dlbo_function of this SubNetworkSingleAllOf1 [Optional].
        dpci_configuration_function: The dpci_configuration_function of this SubNetworkSingleAllOf1 [Optional].
        cpci_configuration_function: The cpci_configuration_function of this SubNetworkSingleAllOf1 [Optional].
        ces_management_function: The ces_management_function of this SubNetworkSingleAllOf1 [Optional].
        configurable5_qi_set: The configurable5_qi_set of this SubNetworkSingleAllOf1 [Optional].
        rim_rs_global: The rim_rs_global of this SubNetworkSingleAllOf1 [Optional].
        dynamic5_qi_set: The dynamic5_qi_set of this SubNetworkSingleAllOf1 [Optional].
        cco_function: The cco_function of this SubNetworkSingleAllOf1 [Optional].
    """

    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)
    managed_element: Optional[List[ManagedElementSingle]] = Field(alias="ManagedElement", default=None)
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

SubNetworkSingleAllOf1.update_forward_refs()
