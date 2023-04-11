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


class AssuranceTarget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            assuranceTargetName = schemas.StrSchema
            assuranceTargetValue = schemas.StrSchema
            __annotations__ = {
                "assuranceTargetName": assuranceTargetName,
                "assuranceTargetValue": assuranceTargetValue,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assuranceTargetName"]) -> MetaOapg.properties.assuranceTargetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["assuranceTargetValue"]) -> MetaOapg.properties.assuranceTargetValue: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["assuranceTargetName", "assuranceTargetValue", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assuranceTargetName"]) -> typing.Union[MetaOapg.properties.assuranceTargetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["assuranceTargetValue"]) -> typing.Union[MetaOapg.properties.assuranceTargetValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["assuranceTargetName", "assuranceTargetValue", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        assuranceTargetName: typing.Union[MetaOapg.properties.assuranceTargetName, str, schemas.Unset] = schemas.unset,
        assuranceTargetValue: typing.Union[MetaOapg.properties.assuranceTargetValue, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssuranceTarget':
        return super().__new__(
            cls,
            *_args,
            assuranceTargetName=assuranceTargetName,
            assuranceTargetValue=assuranceTargetValue,
            _configuration=_configuration,
            **kwargs,
        )
