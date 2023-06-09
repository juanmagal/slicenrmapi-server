# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.epn11_single import EPN11Single
from openapi_server.models.epn12_single import EPN12Single
from openapi_server.models.epn14_single import EPN14Single
from openapi_server.models.epn15_single import EPN15Single
from openapi_server.models.epn17_single import EPN17Single
from openapi_server.models.epn20_single import EPN20Single
from openapi_server.models.epn22_single import EPN22Single
from openapi_server.models.epn26_single import EPN26Single
from openapi_server.models.epn2_single import EPN2Single
from openapi_server.models.epn8_single import EPN8Single
from openapi_server.models.epnlg_single import EPNLGSingle
from openapi_server.models.epnls_single import EPNLSSingle


class AmfFunctionSingleAllOf1(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AmfFunctionSingleAllOf1 - a model defined in OpenAPI

        ep_n2: The ep_n2 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n8: The ep_n8 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n11: The ep_n11 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n12: The ep_n12 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n14: The ep_n14 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n15: The ep_n15 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n17: The ep_n17 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n20: The ep_n20 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n22: The ep_n22 of this AmfFunctionSingleAllOf1 [Optional].
        ep_n26: The ep_n26 of this AmfFunctionSingleAllOf1 [Optional].
        ep_nls: The ep_nls of this AmfFunctionSingleAllOf1 [Optional].
        ep_nlg: The ep_nlg of this AmfFunctionSingleAllOf1 [Optional].
    """

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

AmfFunctionSingleAllOf1.update_forward_refs()
