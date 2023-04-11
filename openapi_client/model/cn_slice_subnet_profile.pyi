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


class CNSliceSubnetProfile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            maxNumberofUEs = schemas.IntSchema
            dLLatency = schemas.NumberSchema
            uLLatency = schemas.NumberSchema
        
            @staticmethod
            def dLThptPerSliceSubnet() -> typing.Type['XLThpt']:
                return XLThpt
        
            @staticmethod
            def dLThptPerUE() -> typing.Type['XLThpt']:
                return XLThpt
        
            @staticmethod
            def uLThptPerSliceSubnet() -> typing.Type['XLThpt']:
                return XLThpt
        
            @staticmethod
            def uLThptPerUE() -> typing.Type['XLThpt']:
                return XLThpt
            maxNumberOfPDUSessions = schemas.IntSchema
        
            @staticmethod
            def coverageAreaTAList() -> typing.Type['NrTacList']:
                return NrTacList
        
            @staticmethod
            def resourceSharingLevel() -> typing.Type['SharingLevel']:
                return SharingLevel
            dLMaxPktSize = schemas.IntSchema
            uLMaxPktSize = schemas.IntSchema
        
            @staticmethod
            def delayTolerance() -> typing.Type['DelayTolerance']:
                return DelayTolerance
        
            @staticmethod
            def synchronicity() -> typing.Type['SynchronicityRANSubnet']:
                return SynchronicityRANSubnet
        
            @staticmethod
            def sliceSimultaneousUse() -> typing.Type['SliceSimultaneousUse']:
                return SliceSimultaneousUse
            reliability = schemas.NumberSchema
            energyEfficiency = schemas.NumberSchema
        
            @staticmethod
            def dLDeterministicComm() -> typing.Type['DeterministicComm']:
                return DeterministicComm
        
            @staticmethod
            def uLDeterministicComm() -> typing.Type['DeterministicComm']:
                return DeterministicComm
            survivalTime = schemas.NumberSchema
        
            @staticmethod
            def nssaaSupport() -> typing.Type['NSSAASupport']:
                return NSSAASupport
        
            @staticmethod
            def n6Protection() -> typing.Type['N6Protection']:
                return N6Protection
            __annotations__ = {
                "maxNumberofUEs": maxNumberofUEs,
                "dLLatency": dLLatency,
                "uLLatency": uLLatency,
                "dLThptPerSliceSubnet": dLThptPerSliceSubnet,
                "dLThptPerUE": dLThptPerUE,
                "uLThptPerSliceSubnet": uLThptPerSliceSubnet,
                "uLThptPerUE": uLThptPerUE,
                "maxNumberOfPDUSessions": maxNumberOfPDUSessions,
                "coverageAreaTAList": coverageAreaTAList,
                "resourceSharingLevel": resourceSharingLevel,
                "dLMaxPktSize": dLMaxPktSize,
                "uLMaxPktSize": uLMaxPktSize,
                "delayTolerance": delayTolerance,
                "synchronicity": synchronicity,
                "sliceSimultaneousUse": sliceSimultaneousUse,
                "reliability": reliability,
                "energyEfficiency": energyEfficiency,
                "dLDeterministicComm": dLDeterministicComm,
                "uLDeterministicComm": uLDeterministicComm,
                "survivalTime": survivalTime,
                "nssaaSupport": nssaaSupport,
                "n6Protection": n6Protection,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxNumberofUEs"]) -> MetaOapg.properties.maxNumberofUEs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dLLatency"]) -> MetaOapg.properties.dLLatency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uLLatency"]) -> MetaOapg.properties.uLLatency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dLThptPerSliceSubnet"]) -> 'XLThpt': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dLThptPerUE"]) -> 'XLThpt': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uLThptPerSliceSubnet"]) -> 'XLThpt': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uLThptPerUE"]) -> 'XLThpt': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxNumberOfPDUSessions"]) -> MetaOapg.properties.maxNumberOfPDUSessions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coverageAreaTAList"]) -> 'NrTacList': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resourceSharingLevel"]) -> 'SharingLevel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dLMaxPktSize"]) -> MetaOapg.properties.dLMaxPktSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uLMaxPktSize"]) -> MetaOapg.properties.uLMaxPktSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delayTolerance"]) -> 'DelayTolerance': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["synchronicity"]) -> 'SynchronicityRANSubnet': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sliceSimultaneousUse"]) -> 'SliceSimultaneousUse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reliability"]) -> MetaOapg.properties.reliability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["energyEfficiency"]) -> MetaOapg.properties.energyEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dLDeterministicComm"]) -> 'DeterministicComm': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uLDeterministicComm"]) -> 'DeterministicComm': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["survivalTime"]) -> MetaOapg.properties.survivalTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nssaaSupport"]) -> 'NSSAASupport': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["n6Protection"]) -> 'N6Protection': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxNumberofUEs", "dLLatency", "uLLatency", "dLThptPerSliceSubnet", "dLThptPerUE", "uLThptPerSliceSubnet", "uLThptPerUE", "maxNumberOfPDUSessions", "coverageAreaTAList", "resourceSharingLevel", "dLMaxPktSize", "uLMaxPktSize", "delayTolerance", "synchronicity", "sliceSimultaneousUse", "reliability", "energyEfficiency", "dLDeterministicComm", "uLDeterministicComm", "survivalTime", "nssaaSupport", "n6Protection", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxNumberofUEs"]) -> typing.Union[MetaOapg.properties.maxNumberofUEs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dLLatency"]) -> typing.Union[MetaOapg.properties.dLLatency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uLLatency"]) -> typing.Union[MetaOapg.properties.uLLatency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dLThptPerSliceSubnet"]) -> typing.Union['XLThpt', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dLThptPerUE"]) -> typing.Union['XLThpt', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uLThptPerSliceSubnet"]) -> typing.Union['XLThpt', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uLThptPerUE"]) -> typing.Union['XLThpt', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxNumberOfPDUSessions"]) -> typing.Union[MetaOapg.properties.maxNumberOfPDUSessions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coverageAreaTAList"]) -> typing.Union['NrTacList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resourceSharingLevel"]) -> typing.Union['SharingLevel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dLMaxPktSize"]) -> typing.Union[MetaOapg.properties.dLMaxPktSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uLMaxPktSize"]) -> typing.Union[MetaOapg.properties.uLMaxPktSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delayTolerance"]) -> typing.Union['DelayTolerance', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["synchronicity"]) -> typing.Union['SynchronicityRANSubnet', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sliceSimultaneousUse"]) -> typing.Union['SliceSimultaneousUse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reliability"]) -> typing.Union[MetaOapg.properties.reliability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["energyEfficiency"]) -> typing.Union[MetaOapg.properties.energyEfficiency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dLDeterministicComm"]) -> typing.Union['DeterministicComm', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uLDeterministicComm"]) -> typing.Union['DeterministicComm', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["survivalTime"]) -> typing.Union[MetaOapg.properties.survivalTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nssaaSupport"]) -> typing.Union['NSSAASupport', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["n6Protection"]) -> typing.Union['N6Protection', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxNumberofUEs", "dLLatency", "uLLatency", "dLThptPerSliceSubnet", "dLThptPerUE", "uLThptPerSliceSubnet", "uLThptPerUE", "maxNumberOfPDUSessions", "coverageAreaTAList", "resourceSharingLevel", "dLMaxPktSize", "uLMaxPktSize", "delayTolerance", "synchronicity", "sliceSimultaneousUse", "reliability", "energyEfficiency", "dLDeterministicComm", "uLDeterministicComm", "survivalTime", "nssaaSupport", "n6Protection", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxNumberofUEs: typing.Union[MetaOapg.properties.maxNumberofUEs, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dLLatency: typing.Union[MetaOapg.properties.dLLatency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        uLLatency: typing.Union[MetaOapg.properties.uLLatency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dLThptPerSliceSubnet: typing.Union['XLThpt', schemas.Unset] = schemas.unset,
        dLThptPerUE: typing.Union['XLThpt', schemas.Unset] = schemas.unset,
        uLThptPerSliceSubnet: typing.Union['XLThpt', schemas.Unset] = schemas.unset,
        uLThptPerUE: typing.Union['XLThpt', schemas.Unset] = schemas.unset,
        maxNumberOfPDUSessions: typing.Union[MetaOapg.properties.maxNumberOfPDUSessions, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        coverageAreaTAList: typing.Union['NrTacList', schemas.Unset] = schemas.unset,
        resourceSharingLevel: typing.Union['SharingLevel', schemas.Unset] = schemas.unset,
        dLMaxPktSize: typing.Union[MetaOapg.properties.dLMaxPktSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        uLMaxPktSize: typing.Union[MetaOapg.properties.uLMaxPktSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        delayTolerance: typing.Union['DelayTolerance', schemas.Unset] = schemas.unset,
        synchronicity: typing.Union['SynchronicityRANSubnet', schemas.Unset] = schemas.unset,
        sliceSimultaneousUse: typing.Union['SliceSimultaneousUse', schemas.Unset] = schemas.unset,
        reliability: typing.Union[MetaOapg.properties.reliability, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        energyEfficiency: typing.Union[MetaOapg.properties.energyEfficiency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dLDeterministicComm: typing.Union['DeterministicComm', schemas.Unset] = schemas.unset,
        uLDeterministicComm: typing.Union['DeterministicComm', schemas.Unset] = schemas.unset,
        survivalTime: typing.Union[MetaOapg.properties.survivalTime, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        nssaaSupport: typing.Union['NSSAASupport', schemas.Unset] = schemas.unset,
        n6Protection: typing.Union['N6Protection', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CNSliceSubnetProfile':
        return super().__new__(
            cls,
            *_args,
            maxNumberofUEs=maxNumberofUEs,
            dLLatency=dLLatency,
            uLLatency=uLLatency,
            dLThptPerSliceSubnet=dLThptPerSliceSubnet,
            dLThptPerUE=dLThptPerUE,
            uLThptPerSliceSubnet=uLThptPerSliceSubnet,
            uLThptPerUE=uLThptPerUE,
            maxNumberOfPDUSessions=maxNumberOfPDUSessions,
            coverageAreaTAList=coverageAreaTAList,
            resourceSharingLevel=resourceSharingLevel,
            dLMaxPktSize=dLMaxPktSize,
            uLMaxPktSize=uLMaxPktSize,
            delayTolerance=delayTolerance,
            synchronicity=synchronicity,
            sliceSimultaneousUse=sliceSimultaneousUse,
            reliability=reliability,
            energyEfficiency=energyEfficiency,
            dLDeterministicComm=dLDeterministicComm,
            uLDeterministicComm=uLDeterministicComm,
            survivalTime=survivalTime,
            nssaaSupport=nssaaSupport,
            n6Protection=n6Protection,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.delay_tolerance import DelayTolerance
from openapi_client.model.deterministic_comm import DeterministicComm
from openapi_client.model.n6_protection import N6Protection
from openapi_client.model.nr_tac_list import NrTacList
from openapi_client.model.nssaa_support import NSSAASupport
from openapi_client.model.sharing_level import SharingLevel
from openapi_client.model.slice_simultaneous_use import SliceSimultaneousUse
from openapi_client.model.synchronicity_ran_subnet import SynchronicityRANSubnet
from openapi_client.model.xl_thpt import XLThpt