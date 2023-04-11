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


class Udrinfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class supportedDataSetIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SupportedDataSetId']:
                        return SupportedDataSetId
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SupportedDataSetId'], typing.List['SupportedDataSetId']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'supportedDataSetIds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SupportedDataSetId':
                    return super().__getitem__(i)
            nFSrvGroupId = schemas.StrSchema
            __annotations__ = {
                "supportedDataSetIds": supportedDataSetIds,
                "nFSrvGroupId": nFSrvGroupId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportedDataSetIds"]) -> MetaOapg.properties.supportedDataSetIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nFSrvGroupId"]) -> MetaOapg.properties.nFSrvGroupId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["supportedDataSetIds", "nFSrvGroupId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportedDataSetIds"]) -> typing.Union[MetaOapg.properties.supportedDataSetIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nFSrvGroupId"]) -> typing.Union[MetaOapg.properties.nFSrvGroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["supportedDataSetIds", "nFSrvGroupId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        supportedDataSetIds: typing.Union[MetaOapg.properties.supportedDataSetIds, list, tuple, schemas.Unset] = schemas.unset,
        nFSrvGroupId: typing.Union[MetaOapg.properties.nFSrvGroupId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Udrinfo':
        return super().__new__(
            cls,
            *_args,
            supportedDataSetIds=supportedDataSetIds,
            nFSrvGroupId=nFSrvGroupId,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.supported_data_set_id import SupportedDataSetId
