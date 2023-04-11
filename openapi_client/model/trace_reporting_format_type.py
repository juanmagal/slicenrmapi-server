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


class TraceReportingFormatType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specifies whether file-based or streaming reporting shall be used for this Trace Session. See 3GPP TS 32.422 clause 5.11 for additional details.
    """


    class MetaOapg:
        enum_value_to_name = {
            "FILE-BASED": "FILEBASED",
            "STREAMING": "STREAMING",
        }
    
    @schemas.classproperty
    def FILEBASED(cls):
        return cls("FILE-BASED")
    
    @schemas.classproperty
    def STREAMING(cls):
        return cls("STREAMING")
