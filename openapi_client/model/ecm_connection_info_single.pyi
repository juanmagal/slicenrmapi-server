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


class EcmConnectionInfoSingle(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class attributes(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_0(
                                schemas.DictSchema
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                    
                                        @staticmethod
                                        def eASServiceArea() -> typing.Type['ServingLocation']:
                                            return ServingLocation
                                    
                                        @staticmethod
                                        def eESServiceArea() -> typing.Type['ServingLocation']:
                                            return ServingLocation
                                    
                                        @staticmethod
                                        def eDNServiceArea() -> typing.Type['ServingLocation']:
                                            return ServingLocation
                                        eASIpAddress = schemas.StrSchema
                                        eESIpAddress = schemas.StrSchema
                                        eCSIpAddress = schemas.StrSchema
                                        ednIdentifier = schemas.StrSchema
                                        
                                        
                                        class ecmConnectionType(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def USERPLANE(cls):
                                                return cls("USERPLANE")
                                            
                                            @schemas.classproperty
                                            def CONTROLPLANE(cls):
                                                return cls("CONTROLPLANE")
                                            
                                            @schemas.classproperty
                                            def BOTH(cls):
                                                return cls("BOTH")
                                    
                                        @staticmethod
                                        def _5_gcnf_conn_ecm_info_list() -> typing.Type['Model5GCNfConnEcmInfoList']:
                                            return Model5GCNfConnEcmInfoList
                                    
                                        @staticmethod
                                        def uPFConnectionInfo() -> typing.Type['UPFConnectionInfo']:
                                            return UPFConnectionInfo
                                        __annotations__ = {
                                            "eASServiceArea": eASServiceArea,
                                            "eESServiceArea": eESServiceArea,
                                            "eDNServiceArea": eDNServiceArea,
                                            "eASIpAddress": eASIpAddress,
                                            "eESIpAddress": eESIpAddress,
                                            "eCSIpAddress": eCSIpAddress,
                                            "ednIdentifier": ednIdentifier,
                                            "ecmConnectionType": ecmConnectionType,
                                            "5GCNfConnEcmInfoList": _5_gcnf_conn_ecm_info_list,
                                            "uPFConnectionInfo": uPFConnectionInfo,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["eASServiceArea"]) -> 'ServingLocation': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["eESServiceArea"]) -> 'ServingLocation': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["eDNServiceArea"]) -> 'ServingLocation': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["eASIpAddress"]) -> MetaOapg.properties.eASIpAddress: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["eESIpAddress"]) -> MetaOapg.properties.eESIpAddress: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["eCSIpAddress"]) -> MetaOapg.properties.eCSIpAddress: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["ednIdentifier"]) -> MetaOapg.properties.ednIdentifier: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["ecmConnectionType"]) -> MetaOapg.properties.ecmConnectionType: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["5GCNfConnEcmInfoList"]) -> 'Model5GCNfConnEcmInfoList': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["uPFConnectionInfo"]) -> 'UPFConnectionInfo': ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["eASServiceArea", "eESServiceArea", "eDNServiceArea", "eASIpAddress", "eESIpAddress", "eCSIpAddress", "ednIdentifier", "ecmConnectionType", "5GCNfConnEcmInfoList", "uPFConnectionInfo", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["eASServiceArea"]) -> typing.Union['ServingLocation', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["eESServiceArea"]) -> typing.Union['ServingLocation', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["eDNServiceArea"]) -> typing.Union['ServingLocation', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["eASIpAddress"]) -> typing.Union[MetaOapg.properties.eASIpAddress, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["eESIpAddress"]) -> typing.Union[MetaOapg.properties.eESIpAddress, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["eCSIpAddress"]) -> typing.Union[MetaOapg.properties.eCSIpAddress, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["ednIdentifier"]) -> typing.Union[MetaOapg.properties.ednIdentifier, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["ecmConnectionType"]) -> typing.Union[MetaOapg.properties.ecmConnectionType, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["5GCNfConnEcmInfoList"]) -> typing.Union['Model5GCNfConnEcmInfoList', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["uPFConnectionInfo"]) -> typing.Union['UPFConnectionInfo', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["eASServiceArea", "eESServiceArea", "eDNServiceArea", "eASIpAddress", "eESIpAddress", "eCSIpAddress", "ednIdentifier", "ecmConnectionType", "5GCNfConnEcmInfoList", "uPFConnectionInfo", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    eASServiceArea: typing.Union['ServingLocation', schemas.Unset] = schemas.unset,
                                    eESServiceArea: typing.Union['ServingLocation', schemas.Unset] = schemas.unset,
                                    eDNServiceArea: typing.Union['ServingLocation', schemas.Unset] = schemas.unset,
                                    eASIpAddress: typing.Union[MetaOapg.properties.eASIpAddress, str, schemas.Unset] = schemas.unset,
                                    eESIpAddress: typing.Union[MetaOapg.properties.eESIpAddress, str, schemas.Unset] = schemas.unset,
                                    eCSIpAddress: typing.Union[MetaOapg.properties.eCSIpAddress, str, schemas.Unset] = schemas.unset,
                                    ednIdentifier: typing.Union[MetaOapg.properties.ednIdentifier, str, schemas.Unset] = schemas.unset,
                                    ecmConnectionType: typing.Union[MetaOapg.properties.ecmConnectionType, str, schemas.Unset] = schemas.unset,
                                    uPFConnectionInfo: typing.Union['UPFConnectionInfo', schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_0':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        eASServiceArea=eASServiceArea,
                                        eESServiceArea=eESServiceArea,
                                        eDNServiceArea=eDNServiceArea,
                                        eASIpAddress=eASIpAddress,
                                        eESIpAddress=eESIpAddress,
                                        eCSIpAddress=eCSIpAddress,
                                        ednIdentifier=ednIdentifier,
                                        ecmConnectionType=ecmConnectionType,
                                        uPFConnectionInfo=uPFConnectionInfo,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            @classmethod
                            @functools.lru_cache()
                            def all_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.all_of_0,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "attributes": attributes,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    attributes=attributes,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                Top,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EcmConnectionInfoSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.model5_gcnf_conn_ecm_info_list import Model5GCNfConnEcmInfoList
from openapi_client.model.serving_location import ServingLocation
from openapi_client.model.top import Top
from openapi_client.model.upf_connection_info import UPFConnectionInfo