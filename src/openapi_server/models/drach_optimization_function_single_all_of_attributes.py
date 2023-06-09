# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.ue_acc_delay_probility_dist import UeAccDelayProbilityDist
from openapi_server.models.ue_acc_probility_dist import UeAccProbilityDist


class DRACHOptimizationFunctionSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DRACHOptimizationFunctionSingleAllOfAttributes - a model defined in OpenAPI

        drach_optimization_control: The drach_optimization_control of this DRACHOptimizationFunctionSingleAllOfAttributes [Optional].
        ue_acc_probility_dist: The ue_acc_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes [Optional].
        ue_acc_delay_probility_dist: The ue_acc_delay_probility_dist of this DRACHOptimizationFunctionSingleAllOfAttributes [Optional].
    """

    drach_optimization_control: Optional[bool] = Field(alias="drachOptimizationControl", default=None)
    ue_acc_probility_dist: Optional[UeAccProbilityDist] = Field(alias="ueAccProbilityDist", default=None)
    ue_acc_delay_probility_dist: Optional[UeAccDelayProbilityDist] = Field(alias="ueAccDelayProbilityDist", default=None)

DRACHOptimizationFunctionSingleAllOfAttributes.update_forward_refs()
