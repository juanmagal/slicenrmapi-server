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


class MeasurementQuantityType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    See details in 3GPP TS 32.422 clause 5.10.15.
    """
    
    @schemas.classproperty
    def CPICH_EC_NO(cls):
        return cls("CPICH_EcNo")
    
    @schemas.classproperty
    def CPICH_RSCP(cls):
        return cls("CPICH_RSCP")
    
    @schemas.classproperty
    def PATH_LOSS(cls):
        return cls("PathLoss")
