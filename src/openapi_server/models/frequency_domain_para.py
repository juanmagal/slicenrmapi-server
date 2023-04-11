# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class FrequencyDomainPara(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    FrequencyDomainPara - a model defined in OpenAPI

        rim_rs_subcarrier_spacing: The rim_rs_subcarrier_spacing of this FrequencyDomainPara [Optional].
        r_imrs_bandwidth: The r_imrs_bandwidth of this FrequencyDomainPara [Optional].
        nrof_global_rimrs_frequency_candidates: The nrof_global_rimrs_frequency_candidates of this FrequencyDomainPara [Optional].
        rim_rs_common_carrier_reference_point: The rim_rs_common_carrier_reference_point of this FrequencyDomainPara [Optional].
        rim_rs_starting_frequency_offset_id_list: The rim_rs_starting_frequency_offset_id_list of this FrequencyDomainPara [Optional].
    """

    rim_rs_subcarrier_spacing: Optional[int] = Field(alias="rimRSSubcarrierSpacing", default=None)
    r_imrs_bandwidth: Optional[int] = Field(alias="rIMRSBandwidth", default=None)
    nrof_global_rimrs_frequency_candidates: Optional[int] = Field(alias="nrofGlobalRIMRSFrequencyCandidates", default=None)
    rim_rs_common_carrier_reference_point: Optional[int] = Field(alias="rimRSCommonCarrierReferencePoint", default=None)
    rim_rs_starting_frequency_offset_id_list: Optional[List[int]] = Field(alias="rimRSStartingFrequencyOffsetIdList", default=None)

FrequencyDomainPara.update_forward_refs()
