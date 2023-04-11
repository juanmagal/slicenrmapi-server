# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.ces_management_function_single import CESManagementFunctionSingle
from openapi_server.models.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_server.models.configurable5_qi_set_single import Configurable5QISetSingle
from openapi_server.models.des_management_function_single import DESManagementFunctionSingle
from openapi_server.models.dlbo_function_single import DLBOFunctionSingle
from openapi_server.models.dmro_function_single import DMROFunctionSingle
from openapi_server.models.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_server.models.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_server.models.dynamic5_qi_set_single import Dynamic5QISetSingle
from openapi_server.models.gnb_cu_cp_function_single import GnbCuCpFunctionSingle
from openapi_server.models.gnb_cu_up_function_single import GnbCuUpFunctionSingle
from openapi_server.models.gnb_du_function_single import GnbDuFunctionSingle


class ManagedElementSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ManagedElementSingleAllOf1 - a model defined in OpenAPI

        gnb_du_function: The gnb_du_function of this ManagedElementSingleAllOf1 [Optional].
        gnb_cu_up_function: The gnb_cu_up_function of this ManagedElementSingleAllOf1 [Optional].
        gnb_cu_cp_function: The gnb_cu_cp_function of this ManagedElementSingleAllOf1 [Optional].
        des_management_function: The des_management_function of this ManagedElementSingleAllOf1 [Optional].
        drach_optimization_function: The drach_optimization_function of this ManagedElementSingleAllOf1 [Optional].
        dmro_function: The dmro_function of this ManagedElementSingleAllOf1 [Optional].
        dlbo_function: The dlbo_function of this ManagedElementSingleAllOf1 [Optional].
        dpci_configuration_function: The dpci_configuration_function of this ManagedElementSingleAllOf1 [Optional].
        cpci_configuration_function: The cpci_configuration_function of this ManagedElementSingleAllOf1 [Optional].
        ces_management_function: The ces_management_function of this ManagedElementSingleAllOf1 [Optional].
        configurable5_qi_set: The configurable5_qi_set of this ManagedElementSingleAllOf1 [Optional].
        dynamic5_qi_set: The dynamic5_qi_set of this ManagedElementSingleAllOf1 [Optional].
    """

    gnb_du_function: Optional[List[GnbDuFunctionSingle]] = Field(alias="GnbDuFunction", default=None)
    gnb_cu_up_function: Optional[List[GnbCuUpFunctionSingle]] = Field(alias="GnbCuUpFunction", default=None)
    gnb_cu_cp_function: Optional[List[GnbCuCpFunctionSingle]] = Field(alias="GnbCuCpFunction", default=None)
    des_management_function: Optional[DESManagementFunctionSingle] = Field(alias="DESManagementFunction", default=None)
    drach_optimization_function: Optional[DRACHOptimizationFunctionSingle] = Field(alias="DRACHOptimizationFunction", default=None)
    dmro_function: Optional[DMROFunctionSingle] = Field(alias="DMROFunction", default=None)
    dlbo_function: Optional[DLBOFunctionSingle] = Field(alias="DLBOFunction", default=None)
    dpci_configuration_function: Optional[DPCIConfigurationFunctionSingle] = Field(alias="DPCIConfigurationFunction", default=None)
    cpci_configuration_function: Optional[CPCIConfigurationFunctionSingle] = Field(alias="CPCIConfigurationFunction", default=None)
    ces_management_function: Optional[CESManagementFunctionSingle] = Field(alias="CESManagementFunction", default=None)
    configurable5_qi_set: Optional[List[Configurable5QISetSingle]] = Field(alias="Configurable5QISet", default=None)
    dynamic5_qi_set: Optional[List[Dynamic5QISetSingle]] = Field(alias="Dynamic5QISet", default=None)

ManagedElementSingleAllOf1.update_forward_refs()
