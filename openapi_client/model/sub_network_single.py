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


class SubNetworkSingle(
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
                
                    @staticmethod
                    def attributes() -> typing.Type['SubNetworkAttr']:
                        return SubNetworkAttr
                    __annotations__ = {
                        "attributes": attributes,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> 'SubNetworkAttr': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union['SubNetworkAttr', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                attributes: typing.Union['SubNetworkAttr', schemas.Unset] = schemas.unset,
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
        
        
        class all_of_3(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def SubNetwork() -> typing.Type['SubNetworkMultiple']:
                        return SubNetworkMultiple
                
                    @staticmethod
                    def ManagedElement() -> typing.Type['ManagedElementMultiple']:
                        return ManagedElementMultiple
                
                    @staticmethod
                    def NRFrequency() -> typing.Type['NRFrequencyMultiple']:
                        return NRFrequencyMultiple
                
                    @staticmethod
                    def ExternalGnbCuCpFunction() -> typing.Type['ExternalGnbCuCpFunctionMultiple']:
                        return ExternalGnbCuCpFunctionMultiple
                
                    @staticmethod
                    def ExternalENBFunction() -> typing.Type['ExternalENBFunctionMultiple']:
                        return ExternalENBFunctionMultiple
                
                    @staticmethod
                    def EUtranFrequency() -> typing.Type['EUtranFrequencyMultiple']:
                        return EUtranFrequencyMultiple
                
                    @staticmethod
                    def DESManagementFunction() -> typing.Type['DESManagementFunctionSingle']:
                        return DESManagementFunctionSingle
                
                    @staticmethod
                    def DRACHOptimizationFunction() -> typing.Type['DRACHOptimizationFunctionSingle']:
                        return DRACHOptimizationFunctionSingle
                
                    @staticmethod
                    def DMROFunction() -> typing.Type['DMROFunctionSingle']:
                        return DMROFunctionSingle
                
                    @staticmethod
                    def DLBOFunction() -> typing.Type['DLBOFunctionSingle']:
                        return DLBOFunctionSingle
                
                    @staticmethod
                    def DPCIConfigurationFunction() -> typing.Type['DPCIConfigurationFunctionSingle']:
                        return DPCIConfigurationFunctionSingle
                
                    @staticmethod
                    def CPCIConfigurationFunction() -> typing.Type['CPCIConfigurationFunctionSingle']:
                        return CPCIConfigurationFunctionSingle
                
                    @staticmethod
                    def CESManagementFunction() -> typing.Type['CESManagementFunctionSingle']:
                        return CESManagementFunctionSingle
                
                    @staticmethod
                    def Configurable5QISet() -> typing.Type['Configurable5QISetMultiple']:
                        return Configurable5QISetMultiple
                
                    @staticmethod
                    def RimRSGlobal() -> typing.Type['RimRSGlobalSingle']:
                        return RimRSGlobalSingle
                
                    @staticmethod
                    def Dynamic5QISet() -> typing.Type['Dynamic5QISetMultiple']:
                        return Dynamic5QISetMultiple
                
                    @staticmethod
                    def CCOFunction() -> typing.Type['CCOFunctionSingle']:
                        return CCOFunctionSingle
                    __annotations__ = {
                        "SubNetwork": SubNetwork,
                        "ManagedElement": ManagedElement,
                        "NRFrequency": NRFrequency,
                        "ExternalGnbCuCpFunction": ExternalGnbCuCpFunction,
                        "ExternalENBFunction": ExternalENBFunction,
                        "EUtranFrequency": EUtranFrequency,
                        "DESManagementFunction": DESManagementFunction,
                        "DRACHOptimizationFunction": DRACHOptimizationFunction,
                        "DMROFunction": DMROFunction,
                        "DLBOFunction": DLBOFunction,
                        "DPCIConfigurationFunction": DPCIConfigurationFunction,
                        "CPCIConfigurationFunction": CPCIConfigurationFunction,
                        "CESManagementFunction": CESManagementFunction,
                        "Configurable5QISet": Configurable5QISet,
                        "RimRSGlobal": RimRSGlobal,
                        "Dynamic5QISet": Dynamic5QISet,
                        "CCOFunction": CCOFunction,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["SubNetwork"]) -> 'SubNetworkMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ManagedElement"]) -> 'ManagedElementMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["NRFrequency"]) -> 'NRFrequencyMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ExternalGnbCuCpFunction"]) -> 'ExternalGnbCuCpFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["ExternalENBFunction"]) -> 'ExternalENBFunctionMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["EUtranFrequency"]) -> 'EUtranFrequencyMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["DESManagementFunction"]) -> 'DESManagementFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["DRACHOptimizationFunction"]) -> 'DRACHOptimizationFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["DMROFunction"]) -> 'DMROFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["DLBOFunction"]) -> 'DLBOFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["DPCIConfigurationFunction"]) -> 'DPCIConfigurationFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["CPCIConfigurationFunction"]) -> 'CPCIConfigurationFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["CESManagementFunction"]) -> 'CESManagementFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Configurable5QISet"]) -> 'Configurable5QISetMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["RimRSGlobal"]) -> 'RimRSGlobalSingle': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["Dynamic5QISet"]) -> 'Dynamic5QISetMultiple': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["CCOFunction"]) -> 'CCOFunctionSingle': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["SubNetwork", "ManagedElement", "NRFrequency", "ExternalGnbCuCpFunction", "ExternalENBFunction", "EUtranFrequency", "DESManagementFunction", "DRACHOptimizationFunction", "DMROFunction", "DLBOFunction", "DPCIConfigurationFunction", "CPCIConfigurationFunction", "CESManagementFunction", "Configurable5QISet", "RimRSGlobal", "Dynamic5QISet", "CCOFunction", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["SubNetwork"]) -> typing.Union['SubNetworkMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ManagedElement"]) -> typing.Union['ManagedElementMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["NRFrequency"]) -> typing.Union['NRFrequencyMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ExternalGnbCuCpFunction"]) -> typing.Union['ExternalGnbCuCpFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["ExternalENBFunction"]) -> typing.Union['ExternalENBFunctionMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["EUtranFrequency"]) -> typing.Union['EUtranFrequencyMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["DESManagementFunction"]) -> typing.Union['DESManagementFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["DRACHOptimizationFunction"]) -> typing.Union['DRACHOptimizationFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["DMROFunction"]) -> typing.Union['DMROFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["DLBOFunction"]) -> typing.Union['DLBOFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["DPCIConfigurationFunction"]) -> typing.Union['DPCIConfigurationFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["CPCIConfigurationFunction"]) -> typing.Union['CPCIConfigurationFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["CESManagementFunction"]) -> typing.Union['CESManagementFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Configurable5QISet"]) -> typing.Union['Configurable5QISetMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["RimRSGlobal"]) -> typing.Union['RimRSGlobalSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["Dynamic5QISet"]) -> typing.Union['Dynamic5QISetMultiple', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["CCOFunction"]) -> typing.Union['CCOFunctionSingle', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SubNetwork", "ManagedElement", "NRFrequency", "ExternalGnbCuCpFunction", "ExternalENBFunction", "EUtranFrequency", "DESManagementFunction", "DRACHOptimizationFunction", "DMROFunction", "DLBOFunction", "DPCIConfigurationFunction", "CPCIConfigurationFunction", "CESManagementFunction", "Configurable5QISet", "RimRSGlobal", "Dynamic5QISet", "CCOFunction", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                SubNetwork: typing.Union['SubNetworkMultiple', schemas.Unset] = schemas.unset,
                ManagedElement: typing.Union['ManagedElementMultiple', schemas.Unset] = schemas.unset,
                NRFrequency: typing.Union['NRFrequencyMultiple', schemas.Unset] = schemas.unset,
                ExternalGnbCuCpFunction: typing.Union['ExternalGnbCuCpFunctionMultiple', schemas.Unset] = schemas.unset,
                ExternalENBFunction: typing.Union['ExternalENBFunctionMultiple', schemas.Unset] = schemas.unset,
                EUtranFrequency: typing.Union['EUtranFrequencyMultiple', schemas.Unset] = schemas.unset,
                DESManagementFunction: typing.Union['DESManagementFunctionSingle', schemas.Unset] = schemas.unset,
                DRACHOptimizationFunction: typing.Union['DRACHOptimizationFunctionSingle', schemas.Unset] = schemas.unset,
                DMROFunction: typing.Union['DMROFunctionSingle', schemas.Unset] = schemas.unset,
                DLBOFunction: typing.Union['DLBOFunctionSingle', schemas.Unset] = schemas.unset,
                DPCIConfigurationFunction: typing.Union['DPCIConfigurationFunctionSingle', schemas.Unset] = schemas.unset,
                CPCIConfigurationFunction: typing.Union['CPCIConfigurationFunctionSingle', schemas.Unset] = schemas.unset,
                CESManagementFunction: typing.Union['CESManagementFunctionSingle', schemas.Unset] = schemas.unset,
                Configurable5QISet: typing.Union['Configurable5QISetMultiple', schemas.Unset] = schemas.unset,
                RimRSGlobal: typing.Union['RimRSGlobalSingle', schemas.Unset] = schemas.unset,
                Dynamic5QISet: typing.Union['Dynamic5QISetMultiple', schemas.Unset] = schemas.unset,
                CCOFunction: typing.Union['CCOFunctionSingle', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_3':
                return super().__new__(
                    cls,
                    *_args,
                    SubNetwork=SubNetwork,
                    ManagedElement=ManagedElement,
                    NRFrequency=NRFrequency,
                    ExternalGnbCuCpFunction=ExternalGnbCuCpFunction,
                    ExternalENBFunction=ExternalENBFunction,
                    EUtranFrequency=EUtranFrequency,
                    DESManagementFunction=DESManagementFunction,
                    DRACHOptimizationFunction=DRACHOptimizationFunction,
                    DMROFunction=DMROFunction,
                    DLBOFunction=DLBOFunction,
                    DPCIConfigurationFunction=DPCIConfigurationFunction,
                    CPCIConfigurationFunction=CPCIConfigurationFunction,
                    CESManagementFunction=CESManagementFunction,
                    Configurable5QISet=Configurable5QISet,
                    RimRSGlobal=RimRSGlobal,
                    Dynamic5QISet=Dynamic5QISet,
                    CCOFunction=CCOFunction,
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
                SubNetworkNcO,
                cls.all_of_3,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubNetworkSingle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.cco_function_single import CCOFunctionSingle
from openapi_client.model.ces_management_function_single import CESManagementFunctionSingle
from openapi_client.model.configurable5_qi_set_multiple import Configurable5QISetMultiple
from openapi_client.model.cpci_configuration_function_single import CPCIConfigurationFunctionSingle
from openapi_client.model.des_management_function_single import DESManagementFunctionSingle
from openapi_client.model.dlbo_function_single import DLBOFunctionSingle
from openapi_client.model.dmro_function_single import DMROFunctionSingle
from openapi_client.model.dpci_configuration_function_single import DPCIConfigurationFunctionSingle
from openapi_client.model.drach_optimization_function_single import DRACHOptimizationFunctionSingle
from openapi_client.model.dynamic5_qi_set_multiple import Dynamic5QISetMultiple
from openapi_client.model.e_utran_frequency_multiple import EUtranFrequencyMultiple
from openapi_client.model.external_enb_function_multiple import ExternalENBFunctionMultiple
from openapi_client.model.external_gnb_cu_cp_function_multiple import ExternalGnbCuCpFunctionMultiple
from openapi_client.model.managed_element_multiple import ManagedElementMultiple
from openapi_client.model.nr_frequency_multiple import NRFrequencyMultiple
from openapi_client.model.rim_rs_global_single import RimRSGlobalSingle
from openapi_client.model.sub_network_attr import SubNetworkAttr
from openapi_client.model.sub_network_multiple import SubNetworkMultiple
from openapi_client.model.sub_network_nc_o import SubNetworkNcO
from openapi_client.model.top import Top