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


class PLMNListType(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    See details in 3GPP TS 32.422 clause 5.10.24.
    """


    class MetaOapg:
        
        
        class items(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "mnc",
                    "mcc",
                }
                
                class properties:
                
                    @staticmethod
                    def mcc() -> typing.Type['Mcc']:
                        return Mcc
                
                    @staticmethod
                    def mnc() -> typing.Type['Mnc1']:
                        return Mnc1
                    __annotations__ = {
                        "mcc": mcc,
                        "mnc": mnc,
                    }
            
            mnc: 'Mnc1'
            mcc: 'Mcc'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["mcc"]) -> 'Mcc': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["mnc"]) -> 'Mnc1': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["mcc", "mnc", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["mcc"]) -> 'Mcc': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["mnc"]) -> 'Mnc1': ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mcc", "mnc", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                mnc: 'Mnc1',
                mcc: 'Mcc',
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *_args,
                    mnc=mnc,
                    mcc=mcc,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PLMNListType':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from openapi_client.model.mcc import Mcc
from openapi_client.model.mnc1 import Mnc1
