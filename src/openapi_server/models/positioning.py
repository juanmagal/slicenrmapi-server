# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.predictionfrequency import Predictionfrequency
from openapi_server.models.serv_attr_com import ServAttrCom


class Positioning(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Positioning - a model defined in OpenAPI

        serv_attr_com: The serv_attr_com of this Positioning [Optional].
        availability: The availability of this Positioning [Optional].
        predictionfrequency: The predictionfrequency of this Positioning [Optional].
        accuracy: The accuracy of this Positioning [Optional].
    """

    serv_attr_com: Optional[ServAttrCom] = Field(alias="servAttrCom", default=None)
    availability: Optional[List[str]] = Field(alias="availability", default=None)
    predictionfrequency: Optional[Predictionfrequency] = Field(alias="predictionfrequency", default=None)
    accuracy: Optional[float] = Field(alias="accuracy", default=None)

Positioning.update_forward_refs()