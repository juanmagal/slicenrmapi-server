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


class TraceDepthType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies how detailed information should be recorded in the Network Element. The Trace Depth is a paremeter for Trace Session level, i.e., the Trace Depth is the same for all of the NEs to be traced in the same Trace Session. See 3GPP TS 32.422 clause 5.3 for additional details.
    """


    class MetaOapg:
        enum_value_to_name = {
            "MINIMUM": "MINIMUM",
            "MEDIUM": "MEDIUM",
            "MAXIMUM": "MAXIMUM",
            "VENDORMINIMUM": "VENDORMINIMUM",
            "VENDORMEDIUM": "VENDORMEDIUM",
            "VENDORMAXIMUM": "VENDORMAXIMUM",
        }
    
    @schemas.classproperty
    def MINIMUM(cls):
        return cls("MINIMUM")
    
    @schemas.classproperty
    def MEDIUM(cls):
        return cls("MEDIUM")
    
    @schemas.classproperty
    def MAXIMUM(cls):
        return cls("MAXIMUM")
    
    @schemas.classproperty
    def VENDORMINIMUM(cls):
        return cls("VENDORMINIMUM")
    
    @schemas.classproperty
    def VENDORMEDIUM(cls):
        return cls("VENDORMEDIUM")
    
    @schemas.classproperty
    def VENDORMAXIMUM(cls):
        return cls("VENDORMAXIMUM")
