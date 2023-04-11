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


class MeasurementPeriodUMTSType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    See details in 3GPP TS 32.422 clause 5.10.22.
    """
    
    @schemas.classproperty
    def DIGIT_ONE_000MS(cls):
        return cls("1000ms")
    
    @schemas.classproperty
    def DIGIT_TWO_000MS(cls):
        return cls("2000ms")
    
    @schemas.classproperty
    def DIGIT_THREE_000MS(cls):
        return cls("3000ms")
    
    @schemas.classproperty
    def DIGIT_FOUR_000MS(cls):
        return cls("4000ms")
    
    @schemas.classproperty
    def DIGIT_SIX_000MS(cls):
        return cls("6000ms")
    
    @schemas.classproperty
    def DIGIT_EIGHT_000MS(cls):
        return cls("8000ms")
    
    @schemas.classproperty
    def DIGIT_ONE_2000MS(cls):
        return cls("12000ms")
    
    @schemas.classproperty
    def DIGIT_ONE_6000MS(cls):
        return cls("16000ms")
    
    @schemas.classproperty
    def DIGIT_TWO_0000MS(cls):
        return cls("20000ms")
    
    @schemas.classproperty
    def DIGIT_TWO_4000MS(cls):
        return cls("24000ms")
    
    @schemas.classproperty
    def DIGIT_TWO_8000MS(cls):
        return cls("28000ms")
    
    @schemas.classproperty
    def DIGIT_THREE_2000MS(cls):
        return cls("32000ms")
    
    @schemas.classproperty
    def DIGIT_SIX_4000MS(cls):
        return cls("64000ms")
