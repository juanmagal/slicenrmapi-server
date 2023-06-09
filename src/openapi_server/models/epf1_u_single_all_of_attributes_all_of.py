# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.local_address import LocalAddress
from openapi_server.models.remote_address import RemoteAddress


class EPF1USingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EPF1USingleAllOfAttributesAllOf - a model defined in OpenAPI

        local_address: The local_address of this EPF1USingleAllOfAttributesAllOf [Optional].
        remote_address: The remote_address of this EPF1USingleAllOfAttributesAllOf [Optional].
        ep_transport_refs: The ep_transport_refs of this EPF1USingleAllOfAttributesAllOf [Optional].
    """

    local_address: Optional[LocalAddress] = Field(alias="localAddress", default=None)
    remote_address: Optional[RemoteAddress] = Field(alias="remoteAddress", default=None)
    ep_transport_refs: Optional[List[str]] = Field(alias="epTransportRefs", default=None)

EPF1USingleAllOfAttributesAllOf.update_forward_refs()
