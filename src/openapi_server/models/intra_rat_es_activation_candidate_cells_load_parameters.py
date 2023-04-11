# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class IntraRatEsActivationCandidateCellsLoadParameters(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    IntraRatEsActivationCandidateCellsLoadParameters - a model defined in OpenAPI

        load_threshold: The load_threshold of this IntraRatEsActivationCandidateCellsLoadParameters [Optional].
        time_duration: The time_duration of this IntraRatEsActivationCandidateCellsLoadParameters [Optional].
    """

    load_threshold: Optional[int] = Field(alias="loadThreshold", default=None)
    time_duration: Optional[int] = Field(alias="timeDuration", default=None)

IntraRatEsActivationCandidateCellsLoadParameters.update_forward_refs()
