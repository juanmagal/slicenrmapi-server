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


class TrafficControlData(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            tcId = schemas.StrSchema
        
            @staticmethod
            def flowStatus() -> typing.Type['FlowStatus']:
                return FlowStatus
        
            @staticmethod
            def redirectInfo() -> typing.Type['RedirectInformation']:
                return RedirectInformation
            
            
            class addRedirectInfo(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['RedirectInformation']:
                        return RedirectInformation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RedirectInformation'], typing.List['RedirectInformation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addRedirectInfo':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RedirectInformation':
                    return super().__getitem__(i)
            muteNotif = schemas.BoolSchema
            
            
            class trafficSteeringPolIdDl(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'trafficSteeringPolIdDl':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class trafficSteeringPolIdUl(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'trafficSteeringPolIdUl':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class routeToLocs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['RouteToLocation']:
                        return RouteToLocation
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RouteToLocation'], typing.List['RouteToLocation']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'routeToLocs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RouteToLocation':
                    return super().__getitem__(i)
            traffCorreInd = schemas.BoolSchema
        
            @staticmethod
            def upPathChgEvent() -> typing.Type['UpPathChgEvent']:
                return UpPathChgEvent
        
            @staticmethod
            def steerFun() -> typing.Type['SteeringFunctionality']:
                return SteeringFunctionality
        
            @staticmethod
            def steerModeDl() -> typing.Type['SteeringMode']:
                return SteeringMode
        
            @staticmethod
            def steerModeUl() -> typing.Type['SteeringMode']:
                return SteeringMode
        
            @staticmethod
            def mulAccCtrl() -> typing.Type['MulticastAccessControl']:
                return MulticastAccessControl
        
            @staticmethod
            def snssaiList() -> typing.Type['SnssaiList']:
                return SnssaiList
            __annotations__ = {
                "tcId": tcId,
                "flowStatus": flowStatus,
                "redirectInfo": redirectInfo,
                "addRedirectInfo": addRedirectInfo,
                "muteNotif": muteNotif,
                "trafficSteeringPolIdDl": trafficSteeringPolIdDl,
                "trafficSteeringPolIdUl": trafficSteeringPolIdUl,
                "routeToLocs": routeToLocs,
                "traffCorreInd": traffCorreInd,
                "upPathChgEvent": upPathChgEvent,
                "steerFun": steerFun,
                "steerModeDl": steerModeDl,
                "steerModeUl": steerModeUl,
                "mulAccCtrl": mulAccCtrl,
                "snssaiList": snssaiList,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tcId"]) -> MetaOapg.properties.tcId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flowStatus"]) -> 'FlowStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirectInfo"]) -> 'RedirectInformation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addRedirectInfo"]) -> MetaOapg.properties.addRedirectInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["muteNotif"]) -> MetaOapg.properties.muteNotif: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trafficSteeringPolIdDl"]) -> MetaOapg.properties.trafficSteeringPolIdDl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trafficSteeringPolIdUl"]) -> MetaOapg.properties.trafficSteeringPolIdUl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routeToLocs"]) -> MetaOapg.properties.routeToLocs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["traffCorreInd"]) -> MetaOapg.properties.traffCorreInd: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upPathChgEvent"]) -> 'UpPathChgEvent': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steerFun"]) -> 'SteeringFunctionality': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steerModeDl"]) -> 'SteeringMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["steerModeUl"]) -> 'SteeringMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mulAccCtrl"]) -> 'MulticastAccessControl': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snssaiList"]) -> 'SnssaiList': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tcId", "flowStatus", "redirectInfo", "addRedirectInfo", "muteNotif", "trafficSteeringPolIdDl", "trafficSteeringPolIdUl", "routeToLocs", "traffCorreInd", "upPathChgEvent", "steerFun", "steerModeDl", "steerModeUl", "mulAccCtrl", "snssaiList", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tcId"]) -> typing.Union[MetaOapg.properties.tcId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flowStatus"]) -> typing.Union['FlowStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirectInfo"]) -> typing.Union['RedirectInformation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addRedirectInfo"]) -> typing.Union[MetaOapg.properties.addRedirectInfo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["muteNotif"]) -> typing.Union[MetaOapg.properties.muteNotif, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trafficSteeringPolIdDl"]) -> typing.Union[MetaOapg.properties.trafficSteeringPolIdDl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trafficSteeringPolIdUl"]) -> typing.Union[MetaOapg.properties.trafficSteeringPolIdUl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routeToLocs"]) -> typing.Union[MetaOapg.properties.routeToLocs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["traffCorreInd"]) -> typing.Union[MetaOapg.properties.traffCorreInd, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upPathChgEvent"]) -> typing.Union['UpPathChgEvent', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steerFun"]) -> typing.Union['SteeringFunctionality', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steerModeDl"]) -> typing.Union['SteeringMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["steerModeUl"]) -> typing.Union['SteeringMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mulAccCtrl"]) -> typing.Union['MulticastAccessControl', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snssaiList"]) -> typing.Union['SnssaiList', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tcId", "flowStatus", "redirectInfo", "addRedirectInfo", "muteNotif", "trafficSteeringPolIdDl", "trafficSteeringPolIdUl", "routeToLocs", "traffCorreInd", "upPathChgEvent", "steerFun", "steerModeDl", "steerModeUl", "mulAccCtrl", "snssaiList", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tcId: typing.Union[MetaOapg.properties.tcId, str, schemas.Unset] = schemas.unset,
        flowStatus: typing.Union['FlowStatus', schemas.Unset] = schemas.unset,
        redirectInfo: typing.Union['RedirectInformation', schemas.Unset] = schemas.unset,
        addRedirectInfo: typing.Union[MetaOapg.properties.addRedirectInfo, list, tuple, schemas.Unset] = schemas.unset,
        muteNotif: typing.Union[MetaOapg.properties.muteNotif, bool, schemas.Unset] = schemas.unset,
        trafficSteeringPolIdDl: typing.Union[MetaOapg.properties.trafficSteeringPolIdDl, None, str, schemas.Unset] = schemas.unset,
        trafficSteeringPolIdUl: typing.Union[MetaOapg.properties.trafficSteeringPolIdUl, None, str, schemas.Unset] = schemas.unset,
        routeToLocs: typing.Union[MetaOapg.properties.routeToLocs, list, tuple, schemas.Unset] = schemas.unset,
        traffCorreInd: typing.Union[MetaOapg.properties.traffCorreInd, bool, schemas.Unset] = schemas.unset,
        upPathChgEvent: typing.Union['UpPathChgEvent', schemas.Unset] = schemas.unset,
        steerFun: typing.Union['SteeringFunctionality', schemas.Unset] = schemas.unset,
        steerModeDl: typing.Union['SteeringMode', schemas.Unset] = schemas.unset,
        steerModeUl: typing.Union['SteeringMode', schemas.Unset] = schemas.unset,
        mulAccCtrl: typing.Union['MulticastAccessControl', schemas.Unset] = schemas.unset,
        snssaiList: typing.Union['SnssaiList', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrafficControlData':
        return super().__new__(
            cls,
            *_args,
            tcId=tcId,
            flowStatus=flowStatus,
            redirectInfo=redirectInfo,
            addRedirectInfo=addRedirectInfo,
            muteNotif=muteNotif,
            trafficSteeringPolIdDl=trafficSteeringPolIdDl,
            trafficSteeringPolIdUl=trafficSteeringPolIdUl,
            routeToLocs=routeToLocs,
            traffCorreInd=traffCorreInd,
            upPathChgEvent=upPathChgEvent,
            steerFun=steerFun,
            steerModeDl=steerModeDl,
            steerModeUl=steerModeUl,
            mulAccCtrl=mulAccCtrl,
            snssaiList=snssaiList,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.flow_status import FlowStatus
from openapi_client.model.multicast_access_control import MulticastAccessControl
from openapi_client.model.redirect_information import RedirectInformation
from openapi_client.model.route_to_location import RouteToLocation
from openapi_client.model.snssai_list import SnssaiList
from openapi_client.model.steering_functionality import SteeringFunctionality
from openapi_client.model.steering_mode import SteeringMode
from openapi_client.model.up_path_chg_event import UpPathChgEvent