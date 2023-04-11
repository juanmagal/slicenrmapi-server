# coding: utf-8

"""
    Provisioning MnS

    OAS 3.0.1 definition of the Provisioning MnS Â© 2022, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.  # noqa: E501

    The version of the OpenAPI document: 17.2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ExtMaxDataBurstVolRm(
    schemas.IntBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneDecimalMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is defined in the same way as the 'ExtMaxDataBurstVol' data type, but with the OpenAPI 'nullable: true' property.

    """


    class MetaOapg:
        inclusive_maximum = 2000000
        inclusive_minimum = 4096


    def __new__(
        cls,
        *_args: typing.Union[None, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExtMaxDataBurstVolRm':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
