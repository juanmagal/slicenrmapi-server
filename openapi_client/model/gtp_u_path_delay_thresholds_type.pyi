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


class GtpUPathDelayThresholdsType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            n3AveragePacketDelayThreshold = schemas.IntSchema
            n3MinPacketDelayThreshold = schemas.IntSchema
            n3MaxPacketDelayThreshold = schemas.IntSchema
            n9AveragePacketDelayThreshold = schemas.IntSchema
            n9MinPacketDelayThreshold = schemas.IntSchema
            n9MaxPacketDelayThreshold = schemas.IntSchema
            __annotations__ = {
                "n3AveragePacketDelayThreshold": n3AveragePacketDelayThreshold,
                "n3MinPacketDelayThreshold": n3MinPacketDelayThreshold,
                "n3MaxPacketDelayThreshold": n3MaxPacketDelayThreshold,
                "n9AveragePacketDelayThreshold": n9AveragePacketDelayThreshold,
                "n9MinPacketDelayThreshold": n9MinPacketDelayThreshold,
                "n9MaxPacketDelayThreshold": n9MaxPacketDelayThreshold,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n3AveragePacketDelayThreshold"]) -> MetaOapg.properties.n3AveragePacketDelayThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n3MinPacketDelayThreshold"]) -> MetaOapg.properties.n3MinPacketDelayThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n3MaxPacketDelayThreshold"]) -> MetaOapg.properties.n3MaxPacketDelayThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n9AveragePacketDelayThreshold"]) -> MetaOapg.properties.n9AveragePacketDelayThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n9MinPacketDelayThreshold"]) -> MetaOapg.properties.n9MinPacketDelayThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n9MaxPacketDelayThreshold"]) -> MetaOapg.properties.n9MaxPacketDelayThreshold: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["n3AveragePacketDelayThreshold", "n3MinPacketDelayThreshold", "n3MaxPacketDelayThreshold", "n9AveragePacketDelayThreshold", "n9MinPacketDelayThreshold", "n9MaxPacketDelayThreshold", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n3AveragePacketDelayThreshold"]) -> typing.Union[MetaOapg.properties.n3AveragePacketDelayThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n3MinPacketDelayThreshold"]) -> typing.Union[MetaOapg.properties.n3MinPacketDelayThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n3MaxPacketDelayThreshold"]) -> typing.Union[MetaOapg.properties.n3MaxPacketDelayThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n9AveragePacketDelayThreshold"]) -> typing.Union[MetaOapg.properties.n9AveragePacketDelayThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n9MinPacketDelayThreshold"]) -> typing.Union[MetaOapg.properties.n9MinPacketDelayThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n9MaxPacketDelayThreshold"]) -> typing.Union[MetaOapg.properties.n9MaxPacketDelayThreshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["n3AveragePacketDelayThreshold", "n3MinPacketDelayThreshold", "n3MaxPacketDelayThreshold", "n9AveragePacketDelayThreshold", "n9MinPacketDelayThreshold", "n9MaxPacketDelayThreshold", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        n3AveragePacketDelayThreshold: typing.Union[MetaOapg.properties.n3AveragePacketDelayThreshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        n3MinPacketDelayThreshold: typing.Union[MetaOapg.properties.n3MinPacketDelayThreshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        n3MaxPacketDelayThreshold: typing.Union[MetaOapg.properties.n3MaxPacketDelayThreshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        n9AveragePacketDelayThreshold: typing.Union[MetaOapg.properties.n9AveragePacketDelayThreshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        n9MinPacketDelayThreshold: typing.Union[MetaOapg.properties.n9MinPacketDelayThreshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        n9MaxPacketDelayThreshold: typing.Union[MetaOapg.properties.n9MaxPacketDelayThreshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GtpUPathDelayThresholdsType':
        return super().__new__(
            cls,
            *_args,
            n3AveragePacketDelayThreshold=n3AveragePacketDelayThreshold,
            n3MinPacketDelayThreshold=n3MinPacketDelayThreshold,
            n3MaxPacketDelayThreshold=n3MaxPacketDelayThreshold,
            n9AveragePacketDelayThreshold=n9AveragePacketDelayThreshold,
            n9MinPacketDelayThreshold=n9MinPacketDelayThreshold,
            n9MaxPacketDelayThreshold=n9MaxPacketDelayThreshold,
            _configuration=_configuration,
            **kwargs,
        )
