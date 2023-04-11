# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.route_information import RouteInformation


class RouteToLocation(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RouteToLocation - a model defined in OpenAPI

        dnai: The dnai of this RouteToLocation.
        route_info: The route_info of this RouteToLocation [Optional].
        route_prof_id: The route_prof_id of this RouteToLocation [Optional].
    """

    dnai: str = Field(alias="dnai")
    route_info: Optional[RouteInformation] = Field(alias="routeInfo", default=None)
    route_prof_id: Optional[str] = Field(alias="routeProfId", default=None)

RouteToLocation.update_forward_refs()
