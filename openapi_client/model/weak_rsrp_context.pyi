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


class WeakRSRPContext(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is the "TargetContext" data type with specialisations for WeakRSRPContext
    """


    class MetaOapg:
        
        class properties:
            
            
            class contextAttribute(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WEAK_RSRPTHRESHOLD(cls):
                    return cls("WeakRSRPThreshold")
            
            
            class contextCondition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IS_LESS_THAN(cls):
                    return cls("IS_LESS_THAN")
            contextValueRange = schemas.NumberSchema
            __annotations__ = {
                "contextAttribute": contextAttribute,
                "contextCondition": contextCondition,
                "contextValueRange": contextValueRange,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextAttribute"]) -> MetaOapg.properties.contextAttribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextCondition"]) -> MetaOapg.properties.contextCondition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contextValueRange"]) -> MetaOapg.properties.contextValueRange: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contextAttribute", "contextCondition", "contextValueRange", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextAttribute"]) -> typing.Union[MetaOapg.properties.contextAttribute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextCondition"]) -> typing.Union[MetaOapg.properties.contextCondition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contextValueRange"]) -> typing.Union[MetaOapg.properties.contextValueRange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contextAttribute", "contextCondition", "contextValueRange", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        contextAttribute: typing.Union[MetaOapg.properties.contextAttribute, str, schemas.Unset] = schemas.unset,
        contextCondition: typing.Union[MetaOapg.properties.contextCondition, str, schemas.Unset] = schemas.unset,
        contextValueRange: typing.Union[MetaOapg.properties.contextValueRange, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WeakRSRPContext':
        return super().__new__(
            cls,
            *_args,
            contextAttribute=contextAttribute,
            contextCondition=contextCondition,
            contextValueRange=contextValueRange,
            _configuration=_configuration,
            **kwargs,
        )
