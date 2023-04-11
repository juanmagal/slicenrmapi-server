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


class AmfIdentifier(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    AmfIdentifier comprise of amfRegionId, amfSetId and amfPointer
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def amfRegionId() -> typing.Type['AmfRegionId']:
                return AmfRegionId
        
            @staticmethod
            def amfSetId() -> typing.Type['AmfSetId']:
                return AmfSetId
        
            @staticmethod
            def amfPointer() -> typing.Type['AmfPointer']:
                return AmfPointer
            __annotations__ = {
                "amfRegionId": amfRegionId,
                "amfSetId": amfSetId,
                "amfPointer": amfPointer,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amfRegionId"]) -> 'AmfRegionId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amfSetId"]) -> 'AmfSetId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amfPointer"]) -> 'AmfPointer': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amfRegionId", "amfSetId", "amfPointer", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amfRegionId"]) -> typing.Union['AmfRegionId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amfSetId"]) -> typing.Union['AmfSetId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amfPointer"]) -> typing.Union['AmfPointer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amfRegionId", "amfSetId", "amfPointer", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        amfRegionId: typing.Union['AmfRegionId', schemas.Unset] = schemas.unset,
        amfSetId: typing.Union['AmfSetId', schemas.Unset] = schemas.unset,
        amfPointer: typing.Union['AmfPointer', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AmfIdentifier':
        return super().__new__(
            cls,
            *_args,
            amfRegionId=amfRegionId,
            amfSetId=amfSetId,
            amfPointer=amfPointer,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.amf_pointer import AmfPointer
from openapi_client.model.amf_region_id import AmfRegionId
from openapi_client.model.amf_set_id import AmfSetId
