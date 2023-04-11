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


class ExpectationObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    This data type is the "ExpectationObject" data type without specialisations
    """


    class MetaOapg:
        
        class properties:
            
            
            class objectType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "RAN_SubNetwork": "RAN_SUB_NETWORK",
                        "Service_Support": "SERVICE_SUPPORT",
                        "TBD": "TBD",
                    }
                
                @schemas.classproperty
                def RAN_SUB_NETWORK(cls):
                    return cls("RAN_SubNetwork")
                
                @schemas.classproperty
                def SERVICE_SUPPORT(cls):
                    return cls("Service_Support")
                
                @schemas.classproperty
                def TBD(cls):
                    return cls("TBD")
            objectInstance = schemas.StrSchema
            
            
            class objectContexts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ObjectContext']:
                        return ObjectContext
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ObjectContext'], typing.List['ObjectContext']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'objectContexts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ObjectContext':
                    return super().__getitem__(i)
            __annotations__ = {
                "objectType": objectType,
                "objectInstance": objectInstance,
                "objectContexts": objectContexts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectType"]) -> MetaOapg.properties.objectType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectInstance"]) -> MetaOapg.properties.objectInstance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectContexts"]) -> MetaOapg.properties.objectContexts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["objectType", "objectInstance", "objectContexts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectType"]) -> typing.Union[MetaOapg.properties.objectType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectInstance"]) -> typing.Union[MetaOapg.properties.objectInstance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectContexts"]) -> typing.Union[MetaOapg.properties.objectContexts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["objectType", "objectInstance", "objectContexts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        objectType: typing.Union[MetaOapg.properties.objectType, str, schemas.Unset] = schemas.unset,
        objectInstance: typing.Union[MetaOapg.properties.objectInstance, str, schemas.Unset] = schemas.unset,
        objectContexts: typing.Union[MetaOapg.properties.objectContexts, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExpectationObject':
        return super().__new__(
            cls,
            *_args,
            objectType=objectType,
            objectInstance=objectInstance,
            objectContexts=objectContexts,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.object_context import ObjectContext
