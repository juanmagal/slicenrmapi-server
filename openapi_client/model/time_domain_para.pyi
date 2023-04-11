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


class TimeDomainPara(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class dlULSwitchingPeriod1(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MS0P5(cls):
                    return cls("MS0P5")
                
                @schemas.classproperty
                def MS0P625(cls):
                    return cls("MS0P625")
                
                @schemas.classproperty
                def MS1(cls):
                    return cls("MS1")
                
                @schemas.classproperty
                def MS1P25(cls):
                    return cls("MS1P25")
                
                @schemas.classproperty
                def MS2(cls):
                    return cls("MS2")
                
                @schemas.classproperty
                def MS2P5(cls):
                    return cls("MS2P5")
                
                @schemas.classproperty
                def MS3(cls):
                    return cls("MS3")
                
                @schemas.classproperty
                def MS4(cls):
                    return cls("MS4")
                
                @schemas.classproperty
                def MS5(cls):
                    return cls("MS5")
                
                @schemas.classproperty
                def MS10(cls):
                    return cls("MS10")
                
                @schemas.classproperty
                def MS20(cls):
                    return cls("MS20")
            symbolOffsetOfReferencePoint1 = schemas.IntSchema
            
            
            class dlULSwitchingPeriod2(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MS0P5(cls):
                    return cls("MS0P5")
                
                @schemas.classproperty
                def MS0P625(cls):
                    return cls("MS0P625")
                
                @schemas.classproperty
                def MS1(cls):
                    return cls("MS1")
                
                @schemas.classproperty
                def MS1P25(cls):
                    return cls("MS1P25")
                
                @schemas.classproperty
                def MS2(cls):
                    return cls("MS2")
                
                @schemas.classproperty
                def MS2P5(cls):
                    return cls("MS2P5")
                
                @schemas.classproperty
                def MS3(cls):
                    return cls("MS3")
                
                @schemas.classproperty
                def MS4(cls):
                    return cls("MS4")
                
                @schemas.classproperty
                def MS5(cls):
                    return cls("MS5")
                
                @schemas.classproperty
                def MS10(cls):
                    return cls("MS10")
                
                @schemas.classproperty
                def MS20(cls):
                    return cls("MS20")
            symbolOffsetOfReferencePoint2 = schemas.IntSchema
            totalnrofSetIdofRS1 = schemas.IntSchema
            totalnrofSetIdofRS2 = schemas.IntSchema
            nrofConsecutiveRIMRS1 = schemas.IntSchema
            nrofConsecutiveRIMRS2 = schemas.IntSchema
            
            
            class consecutiveRIMRS1List(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'consecutiveRIMRS1List':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class consecutiveRIMRS2List(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'consecutiveRIMRS2List':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class enablenearfarIndicationRS1(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ENABLE(cls):
                    return cls("ENABLE")
                
                @schemas.classproperty
                def DISABLE(cls):
                    return cls("DISABLE")
            
            
            class enablenearfarIndicationRS2(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ENABLE(cls):
                    return cls("ENABLE")
                
                @schemas.classproperty
                def DISABLE(cls):
                    return cls("DISABLE")
            __annotations__ = {
                "dlULSwitchingPeriod1": dlULSwitchingPeriod1,
                "symbolOffsetOfReferencePoint1": symbolOffsetOfReferencePoint1,
                "dlULSwitchingPeriod2": dlULSwitchingPeriod2,
                "symbolOffsetOfReferencePoint2": symbolOffsetOfReferencePoint2,
                "totalnrofSetIdofRS1": totalnrofSetIdofRS1,
                "totalnrofSetIdofRS2": totalnrofSetIdofRS2,
                "nrofConsecutiveRIMRS1": nrofConsecutiveRIMRS1,
                "nrofConsecutiveRIMRS2": nrofConsecutiveRIMRS2,
                "consecutiveRIMRS1List": consecutiveRIMRS1List,
                "consecutiveRIMRS2List": consecutiveRIMRS2List,
                "enablenearfarIndicationRS1": enablenearfarIndicationRS1,
                "enablenearfarIndicationRS2": enablenearfarIndicationRS2,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dlULSwitchingPeriod1"]) -> MetaOapg.properties.dlULSwitchingPeriod1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbolOffsetOfReferencePoint1"]) -> MetaOapg.properties.symbolOffsetOfReferencePoint1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dlULSwitchingPeriod2"]) -> MetaOapg.properties.dlULSwitchingPeriod2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbolOffsetOfReferencePoint2"]) -> MetaOapg.properties.symbolOffsetOfReferencePoint2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalnrofSetIdofRS1"]) -> MetaOapg.properties.totalnrofSetIdofRS1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalnrofSetIdofRS2"]) -> MetaOapg.properties.totalnrofSetIdofRS2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nrofConsecutiveRIMRS1"]) -> MetaOapg.properties.nrofConsecutiveRIMRS1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nrofConsecutiveRIMRS2"]) -> MetaOapg.properties.nrofConsecutiveRIMRS2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consecutiveRIMRS1List"]) -> MetaOapg.properties.consecutiveRIMRS1List: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["consecutiveRIMRS2List"]) -> MetaOapg.properties.consecutiveRIMRS2List: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enablenearfarIndicationRS1"]) -> MetaOapg.properties.enablenearfarIndicationRS1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enablenearfarIndicationRS2"]) -> MetaOapg.properties.enablenearfarIndicationRS2: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dlULSwitchingPeriod1", "symbolOffsetOfReferencePoint1", "dlULSwitchingPeriod2", "symbolOffsetOfReferencePoint2", "totalnrofSetIdofRS1", "totalnrofSetIdofRS2", "nrofConsecutiveRIMRS1", "nrofConsecutiveRIMRS2", "consecutiveRIMRS1List", "consecutiveRIMRS2List", "enablenearfarIndicationRS1", "enablenearfarIndicationRS2", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dlULSwitchingPeriod1"]) -> typing.Union[MetaOapg.properties.dlULSwitchingPeriod1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbolOffsetOfReferencePoint1"]) -> typing.Union[MetaOapg.properties.symbolOffsetOfReferencePoint1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dlULSwitchingPeriod2"]) -> typing.Union[MetaOapg.properties.dlULSwitchingPeriod2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbolOffsetOfReferencePoint2"]) -> typing.Union[MetaOapg.properties.symbolOffsetOfReferencePoint2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalnrofSetIdofRS1"]) -> typing.Union[MetaOapg.properties.totalnrofSetIdofRS1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalnrofSetIdofRS2"]) -> typing.Union[MetaOapg.properties.totalnrofSetIdofRS2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nrofConsecutiveRIMRS1"]) -> typing.Union[MetaOapg.properties.nrofConsecutiveRIMRS1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nrofConsecutiveRIMRS2"]) -> typing.Union[MetaOapg.properties.nrofConsecutiveRIMRS2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consecutiveRIMRS1List"]) -> typing.Union[MetaOapg.properties.consecutiveRIMRS1List, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["consecutiveRIMRS2List"]) -> typing.Union[MetaOapg.properties.consecutiveRIMRS2List, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enablenearfarIndicationRS1"]) -> typing.Union[MetaOapg.properties.enablenearfarIndicationRS1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enablenearfarIndicationRS2"]) -> typing.Union[MetaOapg.properties.enablenearfarIndicationRS2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dlULSwitchingPeriod1", "symbolOffsetOfReferencePoint1", "dlULSwitchingPeriod2", "symbolOffsetOfReferencePoint2", "totalnrofSetIdofRS1", "totalnrofSetIdofRS2", "nrofConsecutiveRIMRS1", "nrofConsecutiveRIMRS2", "consecutiveRIMRS1List", "consecutiveRIMRS2List", "enablenearfarIndicationRS1", "enablenearfarIndicationRS2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dlULSwitchingPeriod1: typing.Union[MetaOapg.properties.dlULSwitchingPeriod1, str, schemas.Unset] = schemas.unset,
        symbolOffsetOfReferencePoint1: typing.Union[MetaOapg.properties.symbolOffsetOfReferencePoint1, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dlULSwitchingPeriod2: typing.Union[MetaOapg.properties.dlULSwitchingPeriod2, str, schemas.Unset] = schemas.unset,
        symbolOffsetOfReferencePoint2: typing.Union[MetaOapg.properties.symbolOffsetOfReferencePoint2, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalnrofSetIdofRS1: typing.Union[MetaOapg.properties.totalnrofSetIdofRS1, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalnrofSetIdofRS2: typing.Union[MetaOapg.properties.totalnrofSetIdofRS2, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nrofConsecutiveRIMRS1: typing.Union[MetaOapg.properties.nrofConsecutiveRIMRS1, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        nrofConsecutiveRIMRS2: typing.Union[MetaOapg.properties.nrofConsecutiveRIMRS2, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        consecutiveRIMRS1List: typing.Union[MetaOapg.properties.consecutiveRIMRS1List, list, tuple, schemas.Unset] = schemas.unset,
        consecutiveRIMRS2List: typing.Union[MetaOapg.properties.consecutiveRIMRS2List, list, tuple, schemas.Unset] = schemas.unset,
        enablenearfarIndicationRS1: typing.Union[MetaOapg.properties.enablenearfarIndicationRS1, str, schemas.Unset] = schemas.unset,
        enablenearfarIndicationRS2: typing.Union[MetaOapg.properties.enablenearfarIndicationRS2, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeDomainPara':
        return super().__new__(
            cls,
            *_args,
            dlULSwitchingPeriod1=dlULSwitchingPeriod1,
            symbolOffsetOfReferencePoint1=symbolOffsetOfReferencePoint1,
            dlULSwitchingPeriod2=dlULSwitchingPeriod2,
            symbolOffsetOfReferencePoint2=symbolOffsetOfReferencePoint2,
            totalnrofSetIdofRS1=totalnrofSetIdofRS1,
            totalnrofSetIdofRS2=totalnrofSetIdofRS2,
            nrofConsecutiveRIMRS1=nrofConsecutiveRIMRS1,
            nrofConsecutiveRIMRS2=nrofConsecutiveRIMRS2,
            consecutiveRIMRS1List=consecutiveRIMRS1List,
            consecutiveRIMRS2List=consecutiveRIMRS2List,
            enablenearfarIndicationRS1=enablenearfarIndicationRS1,
            enablenearfarIndicationRS2=enablenearfarIndicationRS2,
            _configuration=_configuration,
            **kwargs,
        )