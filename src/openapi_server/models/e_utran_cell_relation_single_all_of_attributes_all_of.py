# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class EUtranCellRelationSingleAllOfAttributesAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EUtranCellRelationSingleAllOfAttributesAllOf - a model defined in OpenAPI

        adjacent_e_utran_cell_ref: The adjacent_e_utran_cell_ref of this EUtranCellRelationSingleAllOfAttributesAllOf [Optional].
    """

    adjacent_e_utran_cell_ref: Optional[str] = Field(alias="adjacentEUtranCellRef", default=None)

EUtranCellRelationSingleAllOfAttributesAllOf.update_forward_refs()
