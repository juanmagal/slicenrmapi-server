# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.flow_status import FlowStatus
from openapi_server.models.multicast_access_control import MulticastAccessControl
from openapi_server.models.redirect_information import RedirectInformation
from openapi_server.models.route_to_location import RouteToLocation
from openapi_server.models.snssai import Snssai
from openapi_server.models.steering_functionality import SteeringFunctionality
from openapi_server.models.steering_mode import SteeringMode
from openapi_server.models.up_path_chg_event import UpPathChgEvent


class TrafficControlData(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TrafficControlData - a model defined in OpenAPI

        tc_id: The tc_id of this TrafficControlData [Optional].
        flow_status: The flow_status of this TrafficControlData [Optional].
        redirect_info: The redirect_info of this TrafficControlData [Optional].
        add_redirect_info: The add_redirect_info of this TrafficControlData [Optional].
        mute_notif: The mute_notif of this TrafficControlData [Optional].
        traffic_steering_pol_id_dl: The traffic_steering_pol_id_dl of this TrafficControlData [Optional].
        traffic_steering_pol_id_ul: The traffic_steering_pol_id_ul of this TrafficControlData [Optional].
        route_to_locs: The route_to_locs of this TrafficControlData [Optional].
        traff_corre_ind: The traff_corre_ind of this TrafficControlData [Optional].
        up_path_chg_event: The up_path_chg_event of this TrafficControlData [Optional].
        steer_fun: The steer_fun of this TrafficControlData [Optional].
        steer_mode_dl: The steer_mode_dl of this TrafficControlData [Optional].
        steer_mode_ul: The steer_mode_ul of this TrafficControlData [Optional].
        mul_acc_ctrl: The mul_acc_ctrl of this TrafficControlData [Optional].
        snssai_list: The snssai_list of this TrafficControlData [Optional].
    """

    tc_id: Optional[str] = Field(alias="tcId", default=None)
    flow_status: Optional[FlowStatus] = Field(alias="flowStatus", default=None)
    redirect_info: Optional[RedirectInformation] = Field(alias="redirectInfo", default=None)
    add_redirect_info: Optional[List[RedirectInformation]] = Field(alias="addRedirectInfo", default=None)
    mute_notif: Optional[bool] = Field(alias="muteNotif", default=None)
    traffic_steering_pol_id_dl: Optional[str] = Field(alias="trafficSteeringPolIdDl", default=None)
    traffic_steering_pol_id_ul: Optional[str] = Field(alias="trafficSteeringPolIdUl", default=None)
    route_to_locs: Optional[List[RouteToLocation]] = Field(alias="routeToLocs", default=None)
    traff_corre_ind: Optional[bool] = Field(alias="traffCorreInd", default=None)
    up_path_chg_event: Optional[UpPathChgEvent] = Field(alias="upPathChgEvent", default=None)
    steer_fun: Optional[SteeringFunctionality] = Field(alias="steerFun", default=None)
    steer_mode_dl: Optional[SteeringMode] = Field(alias="steerModeDl", default=None)
    steer_mode_ul: Optional[SteeringMode] = Field(alias="steerModeUl", default=None)
    mul_acc_ctrl: Optional[MulticastAccessControl] = Field(alias="mulAccCtrl", default=None)
    snssai_list: Optional[List[Snssai]] = Field(alias="snssaiList", default=None)

TrafficControlData.update_forward_refs()