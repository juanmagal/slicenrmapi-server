# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epe1_single import EPE1Single
from openapi_server.models.epf1_c_single import EPF1CSingle
from openapi_server.models.epxn_c_single import EPXnCSingle
from openapi_server.models.external_nr_cell_cu_single import ExternalNrCellCuSingle


class ExternalGnbCuCpFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ExternalGnbCuCpFunctionSingleAllOf1 - a model defined in OpenAPI

        external_nr_cell_cu: The external_nr_cell_cu of this ExternalGnbCuCpFunctionSingleAllOf1 [Optional].
        ep_xn_c: The ep_xn_c of this ExternalGnbCuCpFunctionSingleAllOf1 [Optional].
        ep_e1: The ep_e1 of this ExternalGnbCuCpFunctionSingleAllOf1 [Optional].
        ep_f1_c: The ep_f1_c of this ExternalGnbCuCpFunctionSingleAllOf1 [Optional].
    """

    external_nr_cell_cu: Optional[List[ExternalNrCellCuSingle]] = Field(alias="ExternalNrCellCu", default=None)
    ep_xn_c: Optional[List[EPXnCSingle]] = Field(alias="EP_XnC", default=None)
    ep_e1: Optional[List[EPE1Single]] = Field(alias="EP_E1", default=None)
    ep_f1_c: Optional[List[EPF1CSingle]] = Field(alias="EP_F1C", default=None)

ExternalGnbCuCpFunctionSingleAllOf1.update_forward_refs()
