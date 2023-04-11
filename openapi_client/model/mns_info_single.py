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


class MnsInfoSingle(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            mnsLabel = schemas.StrSchema
            
            
            class mnsType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ProvMnS": "PROV_MN_S",
                        "FaultSupervisionMnS": "FAULT_SUPERVISION_MN_S",
                        "StreamingDataReportingMnS": "STREAMING_DATA_REPORTING_MN_S",
                        "FileDataReportingMnS": "FILE_DATA_REPORTING_MN_S",
                    }
                
                @schemas.classproperty
                def PROV_MN_S(cls):
                    return cls("ProvMnS")
                
                @schemas.classproperty
                def FAULT_SUPERVISION_MN_S(cls):
                    return cls("FaultSupervisionMnS")
                
                @schemas.classproperty
                def STREAMING_DATA_REPORTING_MN_S(cls):
                    return cls("StreamingDataReportingMnS")
                
                @schemas.classproperty
                def FILE_DATA_REPORTING_MN_S(cls):
                    return cls("FileDataReportingMnS")
            mnsVersion = schemas.StrSchema
            mnsAddress = schemas.StrSchema
            
            
            class mnsScope(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mnsScope':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "mnsLabel": mnsLabel,
                "mnsType": mnsType,
                "mnsVersion": mnsVersion,
                "mnsAddress": mnsAddress,
                "mnsScope": mnsScope,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mnsLabel"]) -> MetaOapg.properties.mnsLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mnsType"]) -> MetaOapg.properties.mnsType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mnsVersion"]) -> MetaOapg.properties.mnsVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mnsAddress"]) -> MetaOapg.properties.mnsAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mnsScope"]) -> MetaOapg.properties.mnsScope: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mnsLabel", "mnsType", "mnsVersion", "mnsAddress", "mnsScope", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mnsLabel"]) -> typing.Union[MetaOapg.properties.mnsLabel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mnsType"]) -> typing.Union[MetaOapg.properties.mnsType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mnsVersion"]) -> typing.Union[MetaOapg.properties.mnsVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mnsAddress"]) -> typing.Union[MetaOapg.properties.mnsAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mnsScope"]) -> typing.Union[MetaOapg.properties.mnsScope, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mnsLabel", "mnsType", "mnsVersion", "mnsAddress", "mnsScope", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mnsLabel: typing.Union[MetaOapg.properties.mnsLabel, str, schemas.Unset] = schemas.unset,
        mnsType: typing.Union[MetaOapg.properties.mnsType, str, schemas.Unset] = schemas.unset,
        mnsVersion: typing.Union[MetaOapg.properties.mnsVersion, str, schemas.Unset] = schemas.unset,
        mnsAddress: typing.Union[MetaOapg.properties.mnsAddress, str, schemas.Unset] = schemas.unset,
        mnsScope: typing.Union[MetaOapg.properties.mnsScope, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MnsInfoSingle':
        return super().__new__(
            cls,
            *_args,
            mnsLabel=mnsLabel,
            mnsType=mnsType,
            mnsVersion=mnsVersion,
            mnsAddress=mnsAddress,
            mnsScope=mnsScope,
            _configuration=_configuration,
            **kwargs,
        )
