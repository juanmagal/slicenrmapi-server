# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.serv_attr_com import ServAttrCom
from openapi_server.models.support import Support


class DeterministicComm(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DeterministicComm - a model defined in OpenAPI

        serv_attr_com: The serv_attr_com of this DeterministicComm [Optional].
        availability: The availability of this DeterministicComm [Optional].
        periodicity_list: The periodicity_list of this DeterministicComm [Optional].
    """

    serv_attr_com: Optional[ServAttrCom] = Field(alias="servAttrCom", default=None)
    availability: Optional[Support] = Field(alias="availability", default=None)
    periodicity_list: Optional[List[int]] = Field(alias="periodicityList", default=None)

DeterministicComm.update_forward_refs()
