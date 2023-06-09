# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.ep_transport_single import EPTransportSingle
from openapi_server.models.feasibility_check_and_reservation_job_single import FeasibilityCheckAndReservationJobSingle
from openapi_server.models.network_slice_single import NetworkSliceSingle
from openapi_server.models.network_slice_subnet_provider_capabilities_single import NetworkSliceSubnetProviderCapabilitiesSingle
from openapi_server.models.network_slice_subnet_single import NetworkSliceSubnetSingle
from openapi_server.models.sub_network_single import SubNetworkSingle


class SubNetworkSingle2AllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SubNetworkSingle2AllOf - a model defined in OpenAPI

        sub_network: The sub_network of this SubNetworkSingle2AllOf [Optional].
        network_slice: The network_slice of this SubNetworkSingle2AllOf [Optional].
        network_slice_subnet: The network_slice_subnet of this SubNetworkSingle2AllOf [Optional].
        ep_transport: The ep_transport of this SubNetworkSingle2AllOf [Optional].
        network_slice_subnet_provider_capabilities: The network_slice_subnet_provider_capabilities of this SubNetworkSingle2AllOf [Optional].
        feasibility_check_and_reservation_job: The feasibility_check_and_reservation_job of this SubNetworkSingle2AllOf [Optional].
    """

    sub_network: Optional[List[SubNetworkSingle]] = Field(alias="SubNetwork", default=None)
    network_slice: Optional[List[NetworkSliceSingle]] = Field(alias="NetworkSlice", default=None)
    network_slice_subnet: Optional[List[NetworkSliceSubnetSingle]] = Field(alias="NetworkSliceSubnet", default=None)
    ep_transport: Optional[List[EPTransportSingle]] = Field(alias="EP_Transport", default=None)
    network_slice_subnet_provider_capabilities: Optional[List[NetworkSliceSubnetProviderCapabilitiesSingle]] = Field(alias="NetworkSliceSubnetProviderCapabilities", default=None)
    feasibility_check_and_reservation_job: Optional[List[FeasibilityCheckAndReservationJobSingle]] = Field(alias="FeasibilityCheckAndReservationJob", default=None)

SubNetworkSingle2AllOf.update_forward_refs()
