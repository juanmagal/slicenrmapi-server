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


class DeterministicComm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def servAttrCom() -> typing.Type['ServAttrCom']:
                return ServAttrCom
        
            @staticmethod
            def availability() -> typing.Type['Support']:
                return Support
            
            
            class periodicityList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'periodicityList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "servAttrCom": servAttrCom,
                "availability": availability,
                "periodicityList": periodicityList,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["servAttrCom"]) -> 'ServAttrCom': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availability"]) -> 'Support': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodicityList"]) -> MetaOapg.properties.periodicityList: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["servAttrCom", "availability", "periodicityList", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["servAttrCom"]) -> typing.Union['ServAttrCom', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availability"]) -> typing.Union['Support', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodicityList"]) -> typing.Union[MetaOapg.properties.periodicityList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["servAttrCom", "availability", "periodicityList", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        servAttrCom: typing.Union['ServAttrCom', schemas.Unset] = schemas.unset,
        availability: typing.Union['Support', schemas.Unset] = schemas.unset,
        periodicityList: typing.Union[MetaOapg.properties.periodicityList, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeterministicComm':
        return super().__new__(
            cls,
            *_args,
            servAttrCom=servAttrCom,
            availability=availability,
            periodicityList=periodicityList,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.serv_attr_com import ServAttrCom
from openapi_client.model.support import Support
