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


class LowULRANUEThptRatioTarget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is the "ExpectationTarget" data type with specialisations for LowULRANUEThptRatioTarget        
    """


    class MetaOapg:
        
        class properties:
            
            
            class targetName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "LowULRANUEThptRatio": "LOW_ULRANUETHPT_RATIO",
                    }
                
                @schemas.classproperty
                def LOW_ULRANUETHPT_RATIO(cls):
                    return cls("LowULRANUEThptRatio")
            
            
            class targetCondition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "IS_LESS_THAN": "IS_LESS_THAN",
                    }
                
                @schemas.classproperty
                def IS_LESS_THAN(cls):
                    return cls("IS_LESS_THAN")
            
            
            class targetValueRange(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 100
                    inclusive_minimum = 0
        
            @staticmethod
            def targetContexts() -> typing.Type['LowULRANUEThptContext']:
                return LowULRANUEThptContext
        
            @staticmethod
            def targetFulfilmentInfo() -> typing.Type['FulfilmentInfo']:
                return FulfilmentInfo
            __annotations__ = {
                "targetName": targetName,
                "targetCondition": targetCondition,
                "targetValueRange": targetValueRange,
                "targetContexts": targetContexts,
                "targetFulfilmentInfo": targetFulfilmentInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetName"]) -> MetaOapg.properties.targetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetCondition"]) -> MetaOapg.properties.targetCondition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetValueRange"]) -> MetaOapg.properties.targetValueRange: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetContexts"]) -> 'LowULRANUEThptContext': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetFulfilmentInfo"]) -> 'FulfilmentInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["targetName", "targetCondition", "targetValueRange", "targetContexts", "targetFulfilmentInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetName"]) -> typing.Union[MetaOapg.properties.targetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetCondition"]) -> typing.Union[MetaOapg.properties.targetCondition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetValueRange"]) -> typing.Union[MetaOapg.properties.targetValueRange, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetContexts"]) -> typing.Union['LowULRANUEThptContext', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetFulfilmentInfo"]) -> typing.Union['FulfilmentInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["targetName", "targetCondition", "targetValueRange", "targetContexts", "targetFulfilmentInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        targetName: typing.Union[MetaOapg.properties.targetName, str, schemas.Unset] = schemas.unset,
        targetCondition: typing.Union[MetaOapg.properties.targetCondition, str, schemas.Unset] = schemas.unset,
        targetValueRange: typing.Union[MetaOapg.properties.targetValueRange, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        targetContexts: typing.Union['LowULRANUEThptContext', schemas.Unset] = schemas.unset,
        targetFulfilmentInfo: typing.Union['FulfilmentInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LowULRANUEThptRatioTarget':
        return super().__new__(
            cls,
            *_args,
            targetName=targetName,
            targetCondition=targetCondition,
            targetValueRange=targetValueRange,
            targetContexts=targetContexts,
            targetFulfilmentInfo=targetFulfilmentInfo,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.fulfilment_info import FulfilmentInfo
from openapi_client.model.low_ulranue_thpt_context import LowULRANUEThptContext
