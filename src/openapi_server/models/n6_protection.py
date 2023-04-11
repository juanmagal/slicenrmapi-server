# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.sec_func import SecFunc
from openapi_server.models.serv_attr_com import ServAttrCom


class N6Protection(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    N6Protection - a model defined in OpenAPI

        serv_attr_com: The serv_attr_com of this N6Protection [Optional].
        sec_func_list: The sec_func_list of this N6Protection [Optional].
    """

    serv_attr_com: Optional[ServAttrCom] = Field(alias="servAttrCom", default=None)
    sec_func_list: Optional[List[SecFunc]] = Field(alias="secFuncList", default=None)

N6Protection.update_forward_refs()
