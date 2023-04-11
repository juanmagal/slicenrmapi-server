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


class UESpeedTarget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is the "ExpectationTarget" data type with specialisations for UESpeedTarget      
    """


    class MetaOapg:
        
        class properties:
            
            
            class targetName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def U_ESPEED(cls):
                    return cls("uESpeed")
            
            
            class targetCondition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IS_LESS_THAN(cls):
                    return cls("IS_LESS_THAN")
            targetValueRange = schemas.IntSchema
            __annotations__ = {
                "targetName": targetName,
                "targetCondition": targetCondition,
                "targetValueRange": targetValueRange,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetName"]) -> MetaOapg.properties.targetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetCondition"]) -> MetaOapg.properties.targetCondition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetValueRange"]) -> MetaOapg.properties.targetValueRange: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["targetName", "targetCondition", "targetValueRange", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetName"]) -> typing.Union[MetaOapg.properties.targetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetCondition"]) -> typing.Union[MetaOapg.properties.targetCondition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetValueRange"]) -> typing.Union[MetaOapg.properties.targetValueRange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["targetName", "targetCondition", "targetValueRange", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        targetName: typing.Union[MetaOapg.properties.targetName, str, schemas.Unset] = schemas.unset,
        targetCondition: typing.Union[MetaOapg.properties.targetCondition, str, schemas.Unset] = schemas.unset,
        targetValueRange: typing.Union[MetaOapg.properties.targetValueRange, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UESpeedTarget':
        return super().__new__(
            cls,
            *_args,
            targetName=targetName,
            targetCondition=targetCondition,
            targetValueRange=targetValueRange,
            _configuration=_configuration,
            **kwargs,
        )
