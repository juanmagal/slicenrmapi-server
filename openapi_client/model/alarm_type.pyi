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


class AlarmType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def COMMUNICATIONS_ALARM(cls):
        return cls("COMMUNICATIONS_ALARM")
    
    @schemas.classproperty
    def QUALITY_OF_SERVICE_ALARM(cls):
        return cls("QUALITY_OF_SERVICE_ALARM")
    
    @schemas.classproperty
    def PROCESSING_ERROR_ALARM(cls):
        return cls("PROCESSING_ERROR_ALARM")
    
    @schemas.classproperty
    def EQUIPMENT_ALARM(cls):
        return cls("EQUIPMENT_ALARM")
    
    @schemas.classproperty
    def ENVIRONMENTAL_ALARM(cls):
        return cls("ENVIRONMENTAL_ALARM")
    
    @schemas.classproperty
    def INTEGRITY_VIOLATION(cls):
        return cls("INTEGRITY_VIOLATION")
    
    @schemas.classproperty
    def OPERATIONAL_VIOLATION(cls):
        return cls("OPERATIONAL_VIOLATION")
    
    @schemas.classproperty
    def PHYSICAL_VIOLATION(cls):
        return cls("PHYSICAL_VIOLATION")
    
    @schemas.classproperty
    def SECURITY_SERVICE_OR_MECHANISM_VIOLATION(cls):
        return cls("SECURITY_SERVICE_OR_MECHANISM_VIOLATION")
    
    @schemas.classproperty
    def TIME_DOMAIN_VIOLATION(cls):
        return cls("TIME_DOMAIN_VIOLATION")