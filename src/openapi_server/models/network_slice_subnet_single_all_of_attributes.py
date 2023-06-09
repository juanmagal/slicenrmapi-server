# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.administrative_state import AdministrativeState
from openapi_server.models.ns_info import NsInfo
from openapi_server.models.operational_state import OperationalState
from openapi_server.models.slice_profile import SliceProfile


class NetworkSliceSubnetSingleAllOfAttributes(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    NetworkSliceSubnetSingleAllOfAttributes - a model defined in OpenAPI

        managed_function_ref_list: The managed_function_ref_list of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        network_slice_subnet_ref_list: The network_slice_subnet_ref_list of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        operational_state: The operational_state of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        administrative_state: The administrative_state of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        ns_info: The ns_info of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        slice_profile_list: The slice_profile_list of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        ep_transport_ref_list: The ep_transport_ref_list of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        priority_label: The priority_label of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
        network_slice_subnet_type: The network_slice_subnet_type of this NetworkSliceSubnetSingleAllOfAttributes [Optional].
    """

    managed_function_ref_list: Optional[List[str]] = Field(alias="managedFunctionRefList", default=None)
    network_slice_subnet_ref_list: Optional[List[str]] = Field(alias="networkSliceSubnetRefList", default=None)
    operational_state: Optional[OperationalState] = Field(alias="operationalState", default=None)
    administrative_state: Optional[AdministrativeState] = Field(alias="administrativeState", default=None)
    ns_info: Optional[NsInfo] = Field(alias="nsInfo", default=None)
    slice_profile_list: Optional[List[SliceProfile]] = Field(alias="sliceProfileList", default=None)
    ep_transport_ref_list: Optional[List[str]] = Field(alias="epTransportRefList", default=None)
    priority_label: Optional[int] = Field(alias="priorityLabel", default=None)
    network_slice_subnet_type: Optional[str] = Field(alias="networkSliceSubnetType", default=None)

NetworkSliceSubnetSingleAllOfAttributes.update_forward_refs()
