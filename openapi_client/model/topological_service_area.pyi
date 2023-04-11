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


class TopologicalServiceArea(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class cellIdList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cellIdList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def trackingAreaIdList() -> typing.Type['TaiList']:
                return TaiList
        
            @staticmethod
            def servingPLMN() -> typing.Type['PlmnId1']:
                return PlmnId1
            __annotations__ = {
                "cellIdList": cellIdList,
                "trackingAreaIdList": trackingAreaIdList,
                "servingPLMN": servingPLMN,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cellIdList"]) -> MetaOapg.properties.cellIdList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackingAreaIdList"]) -> 'TaiList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["servingPLMN"]) -> 'PlmnId1': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cellIdList", "trackingAreaIdList", "servingPLMN", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cellIdList"]) -> typing.Union[MetaOapg.properties.cellIdList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackingAreaIdList"]) -> typing.Union['TaiList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["servingPLMN"]) -> typing.Union['PlmnId1', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cellIdList", "trackingAreaIdList", "servingPLMN", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cellIdList: typing.Union[MetaOapg.properties.cellIdList, list, tuple, schemas.Unset] = schemas.unset,
        trackingAreaIdList: typing.Union['TaiList', schemas.Unset] = schemas.unset,
        servingPLMN: typing.Union['PlmnId1', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TopologicalServiceArea':
        return super().__new__(
            cls,
            *_args,
            cellIdList=cellIdList,
            trackingAreaIdList=trackingAreaIdList,
            servingPLMN=servingPLMN,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.plmn_id1 import PlmnId1
from openapi_client.model.tai_list import TaiList