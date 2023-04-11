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


class NFProfile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    NF profile stored in NRF, defined in TS 29.510
    """


    class MetaOapg:
        
        class properties:
            nFInstanceId = schemas.StrSchema
        
            @staticmethod
            def nFType() -> typing.Type['NFType']:
                return NFType
        
            @staticmethod
            def nFStatus() -> typing.Type['NFStatus']:
                return NFStatus
        
            @staticmethod
            def plmn() -> typing.Type['PlmnId']:
                return PlmnId
        
            @staticmethod
            def sNssais() -> typing.Type['Snssai']:
                return Snssai
            fqdn = schemas.StrSchema
            interPlmnFqdn = schemas.StrSchema
            
            
            class nfServices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NFService']:
                        return NFService
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NFService'], typing.List['NFService']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'nfServices':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NFService':
                    return super().__getitem__(i)
            __annotations__ = {
                "nFInstanceId": nFInstanceId,
                "nFType": nFType,
                "nFStatus": nFStatus,
                "plmn": plmn,
                "sNssais": sNssais,
                "fqdn": fqdn,
                "interPlmnFqdn": interPlmnFqdn,
                "nfServices": nfServices,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nFInstanceId"]) -> MetaOapg.properties.nFInstanceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nFType"]) -> 'NFType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nFStatus"]) -> 'NFStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plmn"]) -> 'PlmnId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sNssais"]) -> 'Snssai': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fqdn"]) -> MetaOapg.properties.fqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interPlmnFqdn"]) -> MetaOapg.properties.interPlmnFqdn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nfServices"]) -> MetaOapg.properties.nfServices: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nFInstanceId", "nFType", "nFStatus", "plmn", "sNssais", "fqdn", "interPlmnFqdn", "nfServices", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nFInstanceId"]) -> typing.Union[MetaOapg.properties.nFInstanceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nFType"]) -> typing.Union['NFType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nFStatus"]) -> typing.Union['NFStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plmn"]) -> typing.Union['PlmnId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sNssais"]) -> typing.Union['Snssai', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fqdn"]) -> typing.Union[MetaOapg.properties.fqdn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interPlmnFqdn"]) -> typing.Union[MetaOapg.properties.interPlmnFqdn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nfServices"]) -> typing.Union[MetaOapg.properties.nfServices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nFInstanceId", "nFType", "nFStatus", "plmn", "sNssais", "fqdn", "interPlmnFqdn", "nfServices", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        nFInstanceId: typing.Union[MetaOapg.properties.nFInstanceId, str, schemas.Unset] = schemas.unset,
        nFType: typing.Union['NFType', schemas.Unset] = schemas.unset,
        nFStatus: typing.Union['NFStatus', schemas.Unset] = schemas.unset,
        plmn: typing.Union['PlmnId', schemas.Unset] = schemas.unset,
        sNssais: typing.Union['Snssai', schemas.Unset] = schemas.unset,
        fqdn: typing.Union[MetaOapg.properties.fqdn, str, schemas.Unset] = schemas.unset,
        interPlmnFqdn: typing.Union[MetaOapg.properties.interPlmnFqdn, str, schemas.Unset] = schemas.unset,
        nfServices: typing.Union[MetaOapg.properties.nfServices, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NFProfile':
        return super().__new__(
            cls,
            *_args,
            nFInstanceId=nFInstanceId,
            nFType=nFType,
            nFStatus=nFStatus,
            plmn=plmn,
            sNssais=sNssais,
            fqdn=fqdn,
            interPlmnFqdn=interPlmnFqdn,
            nfServices=nfServices,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.nf_service import NFService
from openapi_client.model.nf_status import NFStatus
from openapi_client.model.nf_type import NFType
from openapi_client.model.plmn_id import PlmnId
from openapi_client.model.snssai import Snssai
