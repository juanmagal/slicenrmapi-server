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


class SequenceDomainPara(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            nrofRIMRSSequenceCandidatesofRS1 = schemas.IntSchema
            
            
            class rimRSScrambleIdListofRS1(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rimRSScrambleIdListofRS1':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            nrofRIMRSSequenceCandidatesofRS2 = schemas.IntSchema
            
            
            class rimRSScrambleIdListofRS2(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rimRSScrambleIdListofRS2':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class enableEnoughNotEnoughIndication(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ENABLE(cls):
                    return cls("ENABLE")
                
                @schemas.classproperty
                def DISABLE(cls):
                    return cls("DISABLE")
            RIMRSScrambleTimerMultiplier = schemas.IntSchema
            RIMRSScrambleTimerOffset = schemas.IntSchema
            __annotations__ = {
                "nrofRIMRSSequenceCandidatesofRS1": nrofRIMRSSequenceCandidatesofRS1,
                "rimRSScrambleIdListofRS1": rimRSScrambleIdListofRS1,
                "nrofRIMRSSequenceCandidatesofRS2": nrofRIMRSSequenceCandidatesofRS2,
                "rimRSScrambleIdListofRS2": rimRSScrambleIdListofRS2,
                "enableEnoughNotEnoughIndication": enableEnoughNotEnoughIndication,
                "RIMRSScrambleTimerMultiplier": RIMRSScrambleTimerMultiplier,
                "RIMRSScrambleTimerOffset": RIMRSScrambleTimerOffset,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nrofRIMRSSequenceCandidatesofRS1"]) -> MetaOapg.properties.nrofRIMRSSequenceCandidatesofRS1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rimRSScrambleIdListofRS1"]) -> MetaOapg.properties.rimRSScrambleIdListofRS1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nrofRIMRSSequenceCandidatesofRS2"]) -> MetaOapg.properties.nrofRIMRSSequenceCandidatesofRS2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rimRSScrambleIdListofRS2"]) -> MetaOapg.properties.rimRSScrambleIdListofRS2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableEnoughNotEnoughIndication"]) -> MetaOapg.properties.enableEnoughNotEnoughIndication: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RIMRSScrambleTimerMultiplier"]) -> MetaOapg.properties.RIMRSScrambleTimerMultiplier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RIMRSScrambleTimerOffset"]) -> MetaOapg.properties.RIMRSScrambleTimerOffset: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nrofRIMRSSequenceCandidatesofRS1", "rimRSScrambleIdListofRS1", "nrofRIMRSSequenceCandidatesofRS2", "rimRSScrambleIdListofRS2", "enableEnoughNotEnoughIndication", "RIMRSScrambleTimerMultiplier", "RIMRSScrambleTimerOffset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nrofRIMRSSequenceCandidatesofRS1"]) -> typing.Union[MetaOapg.properties.nrofRIMRSSequenceCandidatesofRS1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rimRSScrambleIdListofRS1"]) -> typing.Union[MetaOapg.properties.rimRSScrambleIdListofRS1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nrofRIMRSSequenceCandidatesofRS2"]) -> typing.Union[MetaOapg.properties.nrofRIMRSSequenceCandidatesofRS2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rimRSScrambleIdListofRS2"]) -> typing.Union[MetaOapg.properties.rimRSScrambleIdListofRS2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableEnoughNotEnoughIndication"]) -> typing.Union[MetaOapg.properties.enableEnoughNotEnoughIndication, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RIMRSScrambleTimerMultiplier"]) -> typing.Union[MetaOapg.properties.RIMRSScrambleTimerMultiplier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RIMRSScrambleTimerOffset"]) -> typing.Union[MetaOapg.properties.RIMRSScrambleTimerOffset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nrofRIMRSSequenceCandidatesofRS1", "rimRSScrambleIdListofRS1", "nrofRIMRSSequenceCandidatesofRS2", "rimRSScrambleIdListofRS2", "enableEnoughNotEnoughIndication", "RIMRSScrambleTimerMultiplier", "RIMRSScrambleTimerOffset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        nrofRIMRSSequenceCandidatesofRS1: typing.Union[MetaOapg.properties.nrofRIMRSSequenceCandidatesofRS1, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rimRSScrambleIdListofRS1: typing.Union[MetaOapg.properties.rimRSScrambleIdListofRS1, list, tuple, schemas.Unset] = schemas.unset,
        nrofRIMRSSequenceCandidatesofRS2: typing.Union[MetaOapg.properties.nrofRIMRSSequenceCandidatesofRS2, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        rimRSScrambleIdListofRS2: typing.Union[MetaOapg.properties.rimRSScrambleIdListofRS2, list, tuple, schemas.Unset] = schemas.unset,
        enableEnoughNotEnoughIndication: typing.Union[MetaOapg.properties.enableEnoughNotEnoughIndication, str, schemas.Unset] = schemas.unset,
        RIMRSScrambleTimerMultiplier: typing.Union[MetaOapg.properties.RIMRSScrambleTimerMultiplier, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        RIMRSScrambleTimerOffset: typing.Union[MetaOapg.properties.RIMRSScrambleTimerOffset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SequenceDomainPara':
        return super().__new__(
            cls,
            *_args,
            nrofRIMRSSequenceCandidatesofRS1=nrofRIMRSSequenceCandidatesofRS1,
            rimRSScrambleIdListofRS1=rimRSScrambleIdListofRS1,
            nrofRIMRSSequenceCandidatesofRS2=nrofRIMRSSequenceCandidatesofRS2,
            rimRSScrambleIdListofRS2=rimRSScrambleIdListofRS2,
            enableEnoughNotEnoughIndication=enableEnoughNotEnoughIndication,
            RIMRSScrambleTimerMultiplier=RIMRSScrambleTimerMultiplier,
            RIMRSScrambleTimerOffset=RIMRSScrambleTimerOffset,
            _configuration=_configuration,
            **kwargs,
        )
