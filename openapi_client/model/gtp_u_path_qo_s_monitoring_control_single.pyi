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


class GtpUPathQoSMonitoringControlSingle(
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
                                        
                                        
                                        class gtpUPathQoSMonitoringState(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                            
                                            @schemas.classproperty
                                            def ENABLED(cls):
                                                return cls("ENABLED")
                                            
                                            @schemas.classproperty
                                            def DISABLED(cls):
                                                return cls("DISABLED")
                                        
                                        
                                        class gtpUPathMonitoredSNSSAIs(
                                            schemas.ListSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                @staticmethod
                                                def items() -> typing.Type['Snssai']:
                                                    return Snssai
                                        
                                            def __new__(
                                                cls,
                                                _arg: typing.Union[typing.Tuple['Snssai'], typing.List['Snssai']],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'gtpUPathMonitoredSNSSAIs':
                                                return super().__new__(
                                                    cls,
                                                    _arg,
                                                    _configuration=_configuration,
                                                )
                                        
                                            def __getitem__(self, i: int) -> 'Snssai':
                                                return super().__getitem__(i)
                                        
                                        
                                        class monitoredDSCPs(
                                            schemas.ListSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                
                                                
                                                class items(
                                                    schemas.IntSchema
                                                ):
                                                    pass
                                        
                                            def __new__(
                                                cls,
                                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                                                _configuration: typing.Optional[schemas.Configuration] = None,
                                            ) -> 'monitoredDSCPs':
                                                return super().__new__(
                                                    cls,
                                                    _arg,
                                                    _configuration=_configuration,
                                                )
                                        
                                            def __getitem__(self, i: int) -> MetaOapg.items:
                                                return super().__getitem__(i)
                                        isEventTriggeredGtpUPathMonitoringSupported = schemas.BoolSchema
                                        isPeriodicGtpUMonitoringSupported = schemas.BoolSchema
                                        isImmediateGtpUMonitoringSupported = schemas.BoolSchema
                                    
                                        @staticmethod
                                        def gtpUPathDelayThresholds() -> typing.Type['GtpUPathDelayThresholdsType']:
                                            return GtpUPathDelayThresholdsType
                                        gtpUPathMinimumWaitTime = schemas.IntSchema
                                        gtpUPathMeasurementPeriod = schemas.IntSchema
                                        __annotations__ = {
                                            "gtpUPathQoSMonitoringState": gtpUPathQoSMonitoringState,
                                            "gtpUPathMonitoredSNSSAIs": gtpUPathMonitoredSNSSAIs,
                                            "monitoredDSCPs": monitoredDSCPs,
                                            "isEventTriggeredGtpUPathMonitoringSupported": isEventTriggeredGtpUPathMonitoringSupported,
                                            "isPeriodicGtpUMonitoringSupported": isPeriodicGtpUMonitoringSupported,
                                            "isImmediateGtpUMonitoringSupported": isImmediateGtpUMonitoringSupported,
                                            "gtpUPathDelayThresholds": gtpUPathDelayThresholds,
                                            "gtpUPathMinimumWaitTime": gtpUPathMinimumWaitTime,
                                            "gtpUPathMeasurementPeriod": gtpUPathMeasurementPeriod,
                                        }
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gtpUPathQoSMonitoringState"]) -> MetaOapg.properties.gtpUPathQoSMonitoringState: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gtpUPathMonitoredSNSSAIs"]) -> MetaOapg.properties.gtpUPathMonitoredSNSSAIs: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["monitoredDSCPs"]) -> MetaOapg.properties.monitoredDSCPs: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["isEventTriggeredGtpUPathMonitoringSupported"]) -> MetaOapg.properties.isEventTriggeredGtpUPathMonitoringSupported: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["isPeriodicGtpUMonitoringSupported"]) -> MetaOapg.properties.isPeriodicGtpUMonitoringSupported: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["isImmediateGtpUMonitoringSupported"]) -> MetaOapg.properties.isImmediateGtpUMonitoringSupported: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gtpUPathDelayThresholds"]) -> 'GtpUPathDelayThresholdsType': ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gtpUPathMinimumWaitTime"]) -> MetaOapg.properties.gtpUPathMinimumWaitTime: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["gtpUPathMeasurementPeriod"]) -> MetaOapg.properties.gtpUPathMeasurementPeriod: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["gtpUPathQoSMonitoringState", "gtpUPathMonitoredSNSSAIs", "monitoredDSCPs", "isEventTriggeredGtpUPathMonitoringSupported", "isPeriodicGtpUMonitoringSupported", "isImmediateGtpUMonitoringSupported", "gtpUPathDelayThresholds", "gtpUPathMinimumWaitTime", "gtpUPathMeasurementPeriod", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gtpUPathQoSMonitoringState"]) -> typing.Union[MetaOapg.properties.gtpUPathQoSMonitoringState, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gtpUPathMonitoredSNSSAIs"]) -> typing.Union[MetaOapg.properties.gtpUPathMonitoredSNSSAIs, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["monitoredDSCPs"]) -> typing.Union[MetaOapg.properties.monitoredDSCPs, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["isEventTriggeredGtpUPathMonitoringSupported"]) -> typing.Union[MetaOapg.properties.isEventTriggeredGtpUPathMonitoringSupported, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["isPeriodicGtpUMonitoringSupported"]) -> typing.Union[MetaOapg.properties.isPeriodicGtpUMonitoringSupported, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["isImmediateGtpUMonitoringSupported"]) -> typing.Union[MetaOapg.properties.isImmediateGtpUMonitoringSupported, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gtpUPathDelayThresholds"]) -> typing.Union['GtpUPathDelayThresholdsType', schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gtpUPathMinimumWaitTime"]) -> typing.Union[MetaOapg.properties.gtpUPathMinimumWaitTime, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["gtpUPathMeasurementPeriod"]) -> typing.Union[MetaOapg.properties.gtpUPathMeasurementPeriod, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gtpUPathQoSMonitoringState", "gtpUPathMonitoredSNSSAIs", "monitoredDSCPs", "isEventTriggeredGtpUPathMonitoringSupported", "isPeriodicGtpUMonitoringSupported", "isImmediateGtpUMonitoringSupported", "gtpUPathDelayThresholds", "gtpUPathMinimumWaitTime", "gtpUPathMeasurementPeriod", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                    gtpUPathQoSMonitoringState: typing.Union[MetaOapg.properties.gtpUPathQoSMonitoringState, str, schemas.Unset] = schemas.unset,
                                    gtpUPathMonitoredSNSSAIs: typing.Union[MetaOapg.properties.gtpUPathMonitoredSNSSAIs, list, tuple, schemas.Unset] = schemas.unset,
                                    monitoredDSCPs: typing.Union[MetaOapg.properties.monitoredDSCPs, list, tuple, schemas.Unset] = schemas.unset,
                                    isEventTriggeredGtpUPathMonitoringSupported: typing.Union[MetaOapg.properties.isEventTriggeredGtpUPathMonitoringSupported, bool, schemas.Unset] = schemas.unset,
                                    isPeriodicGtpUMonitoringSupported: typing.Union[MetaOapg.properties.isPeriodicGtpUMonitoringSupported, bool, schemas.Unset] = schemas.unset,
                                    isImmediateGtpUMonitoringSupported: typing.Union[MetaOapg.properties.isImmediateGtpUMonitoringSupported, bool, schemas.Unset] = schemas.unset,
                                    gtpUPathDelayThresholds: typing.Union['GtpUPathDelayThresholdsType', schemas.Unset] = schemas.unset,
                                    gtpUPathMinimumWaitTime: typing.Union[MetaOapg.properties.gtpUPathMinimumWaitTime, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                    gtpUPathMeasurementPeriod: typing.Union[MetaOapg.properties.gtpUPathMeasurementPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'all_of_0':
                                    return super().__new__(
                                        cls,
                                        *_args,
                                        gtpUPathQoSMonitoringState=gtpUPathQoSMonitoringState,
                                        gtpUPathMonitoredSNSSAIs=gtpUPathMonitoredSNSSAIs,
                                        monitoredDSCPs=monitoredDSCPs,
                                        isEventTriggeredGtpUPathMonitoringSupported=isEventTriggeredGtpUPathMonitoringSupported,
                                        isPeriodicGtpUMonitoringSupported=isPeriodicGtpUMonitoringSupported,
                                        isImmediateGtpUMonitoringSupported=isImmediateGtpUMonitoringSupported,
                                        gtpUPathDelayThresholds=gtpUPathDelayThresholds,
                                        gtpUPathMinimumWaitTime=gtpUPathMinimumWaitTime,
                                        gtpUPathMeasurementPeriod=gtpUPathMeasurementPeriod,
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
    ) -> 'GtpUPathQoSMonitoringControlSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.gtp_u_path_delay_thresholds_type import GtpUPathDelayThresholdsType
from openapi_client.model.snssai import Snssai
from openapi_client.model.top import Top
