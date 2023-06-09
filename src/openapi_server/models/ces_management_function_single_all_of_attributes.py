# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.es_not_allowed_time_period import EsNotAllowedTimePeriod
from openapi_server.models.intra_rat_es_activation_candidate_cells_load_parameters import IntraRatEsActivationCandidateCellsLoadParameters
from openapi_server.models.intra_rat_es_activation_original_cell_load_parameters import IntraRatEsActivationOriginalCellLoadParameters
from openapi_server.models.intra_rat_es_deactivation_candidate_cells_load_parameters import IntraRatEsDeactivationCandidateCellsLoadParameters


class CESManagementFunctionSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CESManagementFunctionSingleAllOfAttributes - a model defined in OpenAPI

        ces_switch: The ces_switch of this CESManagementFunctionSingleAllOfAttributes [Optional].
        intra_rat_es_activation_original_cell_load_parameters: The intra_rat_es_activation_original_cell_load_parameters of this CESManagementFunctionSingleAllOfAttributes [Optional].
        intra_rat_es_activation_candidate_cells_load_parameters: The intra_rat_es_activation_candidate_cells_load_parameters of this CESManagementFunctionSingleAllOfAttributes [Optional].
        intra_rat_es_deactivation_candidate_cells_load_parameters: The intra_rat_es_deactivation_candidate_cells_load_parameters of this CESManagementFunctionSingleAllOfAttributes [Optional].
        es_not_allowed_time_period: The es_not_allowed_time_period of this CESManagementFunctionSingleAllOfAttributes [Optional].
        inter_rat_es_activation_original_cell_parameters: The inter_rat_es_activation_original_cell_parameters of this CESManagementFunctionSingleAllOfAttributes [Optional].
        inter_rat_es_activation_candidate_cell_parameters: The inter_rat_es_activation_candidate_cell_parameters of this CESManagementFunctionSingleAllOfAttributes [Optional].
        inter_rat_es_deactivation_candidate_cell_parameters: The inter_rat_es_deactivation_candidate_cell_parameters of this CESManagementFunctionSingleAllOfAttributes [Optional].
        energy_saving_control: The energy_saving_control of this CESManagementFunctionSingleAllOfAttributes [Optional].
        energy_saving_state: The energy_saving_state of this CESManagementFunctionSingleAllOfAttributes [Optional].
    """

    ces_switch: Optional[bool] = Field(alias="cesSwitch", default=None)
    intra_rat_es_activation_original_cell_load_parameters: Optional[IntraRatEsActivationOriginalCellLoadParameters] = Field(alias="intraRatEsActivationOriginalCellLoadParameters", default=None)
    intra_rat_es_activation_candidate_cells_load_parameters: Optional[IntraRatEsActivationCandidateCellsLoadParameters] = Field(alias="intraRatEsActivationCandidateCellsLoadParameters", default=None)
    intra_rat_es_deactivation_candidate_cells_load_parameters: Optional[IntraRatEsDeactivationCandidateCellsLoadParameters] = Field(alias="intraRatEsDeactivationCandidateCellsLoadParameters", default=None)
    es_not_allowed_time_period: Optional[EsNotAllowedTimePeriod] = Field(alias="esNotAllowedTimePeriod", default=None)
    inter_rat_es_activation_original_cell_parameters: Optional[IntraRatEsActivationOriginalCellLoadParameters] = Field(alias="interRatEsActivationOriginalCellParameters", default=None)
    inter_rat_es_activation_candidate_cell_parameters: Optional[IntraRatEsActivationOriginalCellLoadParameters] = Field(alias="interRatEsActivationCandidateCellParameters", default=None)
    inter_rat_es_deactivation_candidate_cell_parameters: Optional[IntraRatEsActivationOriginalCellLoadParameters] = Field(alias="interRatEsDeactivationCandidateCellParameters", default=None)
    energy_saving_control: Optional[str] = Field(alias="energySavingControl", default=None)
    energy_saving_state: Optional[str] = Field(alias="energySavingState", default=None)

CESManagementFunctionSingleAllOfAttributes.update_forward_refs()
