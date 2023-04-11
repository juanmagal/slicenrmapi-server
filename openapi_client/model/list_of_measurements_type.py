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


class ListOfMeasurementsType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    See details in 3GPP TS 32.422 clause 5.10.3 for details.
    """


    class MetaOapg:
        
        class properties:
            
            
            class UMTS(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "M1": "M1",
                                "M2": "M2",
                                "M3": "M3",
                                "M4": "M4",
                                "M5": "M5",
                                "M6_DL": "M6_DL",
                                "M6_UL": "M6_UL",
                                "M7_DL": "M7_DL",
                                "M7_UL": "M7_UL",
                            }
                        
                        @schemas.classproperty
                        def M1(cls):
                            return cls("M1")
                        
                        @schemas.classproperty
                        def M2(cls):
                            return cls("M2")
                        
                        @schemas.classproperty
                        def M3(cls):
                            return cls("M3")
                        
                        @schemas.classproperty
                        def M4(cls):
                            return cls("M4")
                        
                        @schemas.classproperty
                        def M5(cls):
                            return cls("M5")
                        
                        @schemas.classproperty
                        def M6_DL(cls):
                            return cls("M6_DL")
                        
                        @schemas.classproperty
                        def M6_UL(cls):
                            return cls("M6_UL")
                        
                        @schemas.classproperty
                        def M7_DL(cls):
                            return cls("M7_DL")
                        
                        @schemas.classproperty
                        def M7_UL(cls):
                            return cls("M7_UL")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'UMTS':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class LTE(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "M1": "M1",
                                "M2": "M2",
                                "M3": "M3",
                                "M4": "M4",
                                "M5": "M5",
                                "M1_EVENT_TRIGGERED": "M1_EVENT_TRIGGERED",
                                "M6": "M6",
                                "M7": "M7",
                                "M8": "M8",
                                "M9": "M9",
                            }
                        
                        @schemas.classproperty
                        def M1(cls):
                            return cls("M1")
                        
                        @schemas.classproperty
                        def M2(cls):
                            return cls("M2")
                        
                        @schemas.classproperty
                        def M3(cls):
                            return cls("M3")
                        
                        @schemas.classproperty
                        def M4(cls):
                            return cls("M4")
                        
                        @schemas.classproperty
                        def M5(cls):
                            return cls("M5")
                        
                        @schemas.classproperty
                        def M1_EVENT_TRIGGERED(cls):
                            return cls("M1_EVENT_TRIGGERED")
                        
                        @schemas.classproperty
                        def M6(cls):
                            return cls("M6")
                        
                        @schemas.classproperty
                        def M7(cls):
                            return cls("M7")
                        
                        @schemas.classproperty
                        def M8(cls):
                            return cls("M8")
                        
                        @schemas.classproperty
                        def M9(cls):
                            return cls("M9")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LTE':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class NR(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "M1": "M1",
                                "M2": "M2",
                                "M3": "M3",
                                "M4": "M4",
                                "M5": "M5",
                                "M6": "M6",
                                "M7": "M7",
                                "M1_EVENT_TRIGGERED": "M1_EVENT_TRIGGERED",
                                "M8": "M8",
                                "M9": "M9",
                            }
                        
                        @schemas.classproperty
                        def M1(cls):
                            return cls("M1")
                        
                        @schemas.classproperty
                        def M2(cls):
                            return cls("M2")
                        
                        @schemas.classproperty
                        def M3(cls):
                            return cls("M3")
                        
                        @schemas.classproperty
                        def M4(cls):
                            return cls("M4")
                        
                        @schemas.classproperty
                        def M5(cls):
                            return cls("M5")
                        
                        @schemas.classproperty
                        def M6(cls):
                            return cls("M6")
                        
                        @schemas.classproperty
                        def M7(cls):
                            return cls("M7")
                        
                        @schemas.classproperty
                        def M1_EVENT_TRIGGERED(cls):
                            return cls("M1_EVENT_TRIGGERED")
                        
                        @schemas.classproperty
                        def M8(cls):
                            return cls("M8")
                        
                        @schemas.classproperty
                        def M9(cls):
                            return cls("M9")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NR':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "UMTS": UMTS,
                "LTE": LTE,
                "NR": NR,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UMTS"]) -> MetaOapg.properties.UMTS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LTE"]) -> MetaOapg.properties.LTE: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NR"]) -> MetaOapg.properties.NR: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["UMTS", "LTE", "NR", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UMTS"]) -> typing.Union[MetaOapg.properties.UMTS, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LTE"]) -> typing.Union[MetaOapg.properties.LTE, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NR"]) -> typing.Union[MetaOapg.properties.NR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["UMTS", "LTE", "NR", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        UMTS: typing.Union[MetaOapg.properties.UMTS, list, tuple, schemas.Unset] = schemas.unset,
        LTE: typing.Union[MetaOapg.properties.LTE, list, tuple, schemas.Unset] = schemas.unset,
        NR: typing.Union[MetaOapg.properties.NR, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ListOfMeasurementsType':
        return super().__new__(
            cls,
            *_args,
            UMTS=UMTS,
            LTE=LTE,
            NR=NR,
            _configuration=_configuration,
            **kwargs,
        )
