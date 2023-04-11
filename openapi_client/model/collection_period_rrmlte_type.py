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


class CollectionPeriodRRMLTEType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    See details in 3GPP TS 32.422 clause 5.10.20.
    """


    class MetaOapg:
        enum_value_to_name = {
            "100ms": "DIGIT_ONE_00MS",
            "1000ms": "DIGIT_ONE_000MS",
            "1024ms": "DIGIT_ONE_024MS",
            "1280ms": "DIGIT_ONE_280MS",
            "2048ms": "DIGIT_TWO_048MS",
            "2560ms": "DIGIT_TWO_560MS",
            "5120ms": "DIGIT_FIVE_120MS",
            "10000ms": "DIGIT_ONE_0000MS",
            "10240ms": "DIGIT_ONE_0240MS",
            "60000ms": "DIGIT_SIX_0000MS",
        }
    
    @schemas.classproperty
    def DIGIT_ONE_00MS(cls):
        return cls("100ms")
    
    @schemas.classproperty
    def DIGIT_ONE_000MS(cls):
        return cls("1000ms")
    
    @schemas.classproperty
    def DIGIT_ONE_024MS(cls):
        return cls("1024ms")
    
    @schemas.classproperty
    def DIGIT_ONE_280MS(cls):
        return cls("1280ms")
    
    @schemas.classproperty
    def DIGIT_TWO_048MS(cls):
        return cls("2048ms")
    
    @schemas.classproperty
    def DIGIT_TWO_560MS(cls):
        return cls("2560ms")
    
    @schemas.classproperty
    def DIGIT_FIVE_120MS(cls):
        return cls("5120ms")
    
    @schemas.classproperty
    def DIGIT_ONE_0000MS(cls):
        return cls("10000ms")
    
    @schemas.classproperty
    def DIGIT_ONE_0240MS(cls):
        return cls("10240ms")
    
    @schemas.classproperty
    def DIGIT_SIX_0000MS(cls):
        return cls("60000ms")
