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


class CESManagementFunctionSingle(
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
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                cesSwitch = schemas.BoolSchema
                            
                                @staticmethod
                                def intraRatEsActivationOriginalCellLoadParameters() -> typing.Type['IntraRatEsActivationOriginalCellLoadParameters']:
                                    return IntraRatEsActivationOriginalCellLoadParameters
                            
                                @staticmethod
                                def intraRatEsActivationCandidateCellsLoadParameters() -> typing.Type['IntraRatEsActivationCandidateCellsLoadParameters']:
                                    return IntraRatEsActivationCandidateCellsLoadParameters
                            
                                @staticmethod
                                def intraRatEsDeactivationCandidateCellsLoadParameters() -> typing.Type['IntraRatEsDeactivationCandidateCellsLoadParameters']:
                                    return IntraRatEsDeactivationCandidateCellsLoadParameters
                            
                                @staticmethod
                                def esNotAllowedTimePeriod() -> typing.Type['EsNotAllowedTimePeriod']:
                                    return EsNotAllowedTimePeriod
                            
                                @staticmethod
                                def interRatEsActivationOriginalCellParameters() -> typing.Type['IntraRatEsActivationOriginalCellLoadParameters']:
                                    return IntraRatEsActivationOriginalCellLoadParameters
                            
                                @staticmethod
                                def interRatEsActivationCandidateCellParameters() -> typing.Type['IntraRatEsActivationOriginalCellLoadParameters']:
                                    return IntraRatEsActivationOriginalCellLoadParameters
                            
                                @staticmethod
                                def interRatEsDeactivationCandidateCellParameters() -> typing.Type['IntraRatEsActivationOriginalCellLoadParameters']:
                                    return IntraRatEsActivationOriginalCellLoadParameters
                                
                                
                                class energySavingControl(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "toBeEnergySaving": "TO_BE_ENERGY_SAVING",
                                            "toBeNotEnergySaving": "TO_BE_NOT_ENERGY_SAVING",
                                        }
                                    
                                    @schemas.classproperty
                                    def TO_BE_ENERGY_SAVING(cls):
                                        return cls("toBeEnergySaving")
                                    
                                    @schemas.classproperty
                                    def TO_BE_NOT_ENERGY_SAVING(cls):
                                        return cls("toBeNotEnergySaving")
                                
                                
                                class energySavingState(
                                    schemas.EnumBase,
                                    schemas.StrSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        enum_value_to_name = {
                                            "isNotEnergySaving": "IS_NOT_ENERGY_SAVING",
                                            "isEnergySaving": "IS_ENERGY_SAVING",
                                        }
                                    
                                    @schemas.classproperty
                                    def IS_NOT_ENERGY_SAVING(cls):
                                        return cls("isNotEnergySaving")
                                    
                                    @schemas.classproperty
                                    def IS_ENERGY_SAVING(cls):
                                        return cls("isEnergySaving")
                                __annotations__ = {
                                    "cesSwitch": cesSwitch,
                                    "intraRatEsActivationOriginalCellLoadParameters": intraRatEsActivationOriginalCellLoadParameters,
                                    "intraRatEsActivationCandidateCellsLoadParameters": intraRatEsActivationCandidateCellsLoadParameters,
                                    "intraRatEsDeactivationCandidateCellsLoadParameters": intraRatEsDeactivationCandidateCellsLoadParameters,
                                    "esNotAllowedTimePeriod": esNotAllowedTimePeriod,
                                    "interRatEsActivationOriginalCellParameters": interRatEsActivationOriginalCellParameters,
                                    "interRatEsActivationCandidateCellParameters": interRatEsActivationCandidateCellParameters,
                                    "interRatEsDeactivationCandidateCellParameters": interRatEsDeactivationCandidateCellParameters,
                                    "energySavingControl": energySavingControl,
                                    "energySavingState": energySavingState,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["cesSwitch"]) -> MetaOapg.properties.cesSwitch: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["intraRatEsActivationOriginalCellLoadParameters"]) -> 'IntraRatEsActivationOriginalCellLoadParameters': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["intraRatEsActivationCandidateCellsLoadParameters"]) -> 'IntraRatEsActivationCandidateCellsLoadParameters': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["intraRatEsDeactivationCandidateCellsLoadParameters"]) -> 'IntraRatEsDeactivationCandidateCellsLoadParameters': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["esNotAllowedTimePeriod"]) -> 'EsNotAllowedTimePeriod': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["interRatEsActivationOriginalCellParameters"]) -> 'IntraRatEsActivationOriginalCellLoadParameters': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["interRatEsActivationCandidateCellParameters"]) -> 'IntraRatEsActivationOriginalCellLoadParameters': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["interRatEsDeactivationCandidateCellParameters"]) -> 'IntraRatEsActivationOriginalCellLoadParameters': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["energySavingControl"]) -> MetaOapg.properties.energySavingControl: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["energySavingState"]) -> MetaOapg.properties.energySavingState: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["cesSwitch", "intraRatEsActivationOriginalCellLoadParameters", "intraRatEsActivationCandidateCellsLoadParameters", "intraRatEsDeactivationCandidateCellsLoadParameters", "esNotAllowedTimePeriod", "interRatEsActivationOriginalCellParameters", "interRatEsActivationCandidateCellParameters", "interRatEsDeactivationCandidateCellParameters", "energySavingControl", "energySavingState", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["cesSwitch"]) -> typing.Union[MetaOapg.properties.cesSwitch, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["intraRatEsActivationOriginalCellLoadParameters"]) -> typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["intraRatEsActivationCandidateCellsLoadParameters"]) -> typing.Union['IntraRatEsActivationCandidateCellsLoadParameters', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["intraRatEsDeactivationCandidateCellsLoadParameters"]) -> typing.Union['IntraRatEsDeactivationCandidateCellsLoadParameters', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["esNotAllowedTimePeriod"]) -> typing.Union['EsNotAllowedTimePeriod', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["interRatEsActivationOriginalCellParameters"]) -> typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["interRatEsActivationCandidateCellParameters"]) -> typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["interRatEsDeactivationCandidateCellParameters"]) -> typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["energySavingControl"]) -> typing.Union[MetaOapg.properties.energySavingControl, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["energySavingState"]) -> typing.Union[MetaOapg.properties.energySavingState, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cesSwitch", "intraRatEsActivationOriginalCellLoadParameters", "intraRatEsActivationCandidateCellsLoadParameters", "intraRatEsDeactivationCandidateCellsLoadParameters", "esNotAllowedTimePeriod", "interRatEsActivationOriginalCellParameters", "interRatEsActivationCandidateCellParameters", "interRatEsDeactivationCandidateCellParameters", "energySavingControl", "energySavingState", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            cesSwitch: typing.Union[MetaOapg.properties.cesSwitch, bool, schemas.Unset] = schemas.unset,
                            intraRatEsActivationOriginalCellLoadParameters: typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset] = schemas.unset,
                            intraRatEsActivationCandidateCellsLoadParameters: typing.Union['IntraRatEsActivationCandidateCellsLoadParameters', schemas.Unset] = schemas.unset,
                            intraRatEsDeactivationCandidateCellsLoadParameters: typing.Union['IntraRatEsDeactivationCandidateCellsLoadParameters', schemas.Unset] = schemas.unset,
                            esNotAllowedTimePeriod: typing.Union['EsNotAllowedTimePeriod', schemas.Unset] = schemas.unset,
                            interRatEsActivationOriginalCellParameters: typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset] = schemas.unset,
                            interRatEsActivationCandidateCellParameters: typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset] = schemas.unset,
                            interRatEsDeactivationCandidateCellParameters: typing.Union['IntraRatEsActivationOriginalCellLoadParameters', schemas.Unset] = schemas.unset,
                            energySavingControl: typing.Union[MetaOapg.properties.energySavingControl, str, schemas.Unset] = schemas.unset,
                            energySavingState: typing.Union[MetaOapg.properties.energySavingState, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'attributes':
                            return super().__new__(
                                cls,
                                *_args,
                                cesSwitch=cesSwitch,
                                intraRatEsActivationOriginalCellLoadParameters=intraRatEsActivationOriginalCellLoadParameters,
                                intraRatEsActivationCandidateCellsLoadParameters=intraRatEsActivationCandidateCellsLoadParameters,
                                intraRatEsDeactivationCandidateCellsLoadParameters=intraRatEsDeactivationCandidateCellsLoadParameters,
                                esNotAllowedTimePeriod=esNotAllowedTimePeriod,
                                interRatEsActivationOriginalCellParameters=interRatEsActivationOriginalCellParameters,
                                interRatEsActivationCandidateCellParameters=interRatEsActivationCandidateCellParameters,
                                interRatEsDeactivationCandidateCellParameters=interRatEsDeactivationCandidateCellParameters,
                                energySavingControl=energySavingControl,
                                energySavingState=energySavingState,
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
                attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
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
    ) -> 'CESManagementFunctionSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.es_not_allowed_time_period import EsNotAllowedTimePeriod
from openapi_client.model.intra_rat_es_activation_candidate_cells_load_parameters import IntraRatEsActivationCandidateCellsLoadParameters
from openapi_client.model.intra_rat_es_activation_original_cell_load_parameters import IntraRatEsActivationOriginalCellLoadParameters
from openapi_client.model.intra_rat_es_deactivation_candidate_cells_load_parameters import IntraRatEsDeactivationCandidateCellsLoadParameters
from openapi_client.model.top import Top
