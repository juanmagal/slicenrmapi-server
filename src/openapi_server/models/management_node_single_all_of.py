# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.management_node_single_all_of_attributes import ManagementNodeSingleAllOfAttributes
from openapi_server.models.mns_agent_single import MnsAgentSingle


class ManagementNodeSingleAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ManagementNodeSingleAllOf - a model defined in OpenAPI

        attributes: The attributes of this ManagementNodeSingleAllOf [Optional].
        mns_agent: The mns_agent of this ManagementNodeSingleAllOf [Optional].
    """

    attributes: Optional[ManagementNodeSingleAllOfAttributes] = Field(alias="attributes", default=None)
    mns_agent: Optional[List[MnsAgentSingle]] = Field(alias="MnsAgent", default=None)

ManagementNodeSingleAllOf.update_forward_refs()
