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


class SsbSubCarrierSpacing(
    schemas.EnumBase,
    schemas.IntSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            15: "POSITIVE_15",
            30: "POSITIVE_30",
            120: "POSITIVE_120",
            240: "POSITIVE_240",
        }
    
    @schemas.classproperty
    def POSITIVE_15(cls):
        return cls(15)
    
    @schemas.classproperty
    def POSITIVE_30(cls):
        return cls(30)
    
    @schemas.classproperty
    def POSITIVE_120(cls):
        return cls(120)
    
    @schemas.classproperty
    def POSITIVE_240(cls):
        return cls(240)
