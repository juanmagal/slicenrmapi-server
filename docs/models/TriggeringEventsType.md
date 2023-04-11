# openapi_client.model.triggering_events_type.TriggeringEventsType

Specifies when to start a Trace Recording Session and which message shall be recorded first, when to stop a Trace Recording Session and which message shall be recorded last respectively. See 3GPP TS 32.422 clause 5.1 for additional detials.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies when to start a Trace Recording Session and which message shall be recorded first, when to stop a Trace Recording Session and which message shall be recorded last respectively. See 3GPP TS 32.422 clause 5.1 for additional detials. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[MSC_SERVER](#MSC_SERVER)** | list, tuple,  | tuple,  |  | [optional] 
**[SGSN](#SGSN)** | list, tuple,  | tuple,  |  | [optional] 
**[MGW](#MGW)** | list, tuple,  | tuple,  |  | [optional] 
**[GGSN](#GGSN)** | list, tuple,  | tuple,  |  | [optional] 
**[IMS](#IMS)** | list, tuple,  | tuple,  |  | [optional] 
**[BM_SC](#BM_SC)** | list, tuple,  | tuple,  |  | [optional] 
**[MME](#MME)** | list, tuple,  | tuple,  |  | [optional] 
**[SGW](#SGW)** | list, tuple,  | tuple,  |  | [optional] 
**[PGW](#PGW)** | list, tuple,  | tuple,  |  | [optional] 
**[AMF](#AMF)** | list, tuple,  | tuple,  |  | [optional] 
**[SMF](#SMF)** | list, tuple,  | tuple,  |  | [optional] 
**[PCF](#PCF)** | list, tuple,  | tuple,  |  | [optional] 
**[UPF](#UPF)** | list, tuple,  | tuple,  |  | [optional] 
**[AUSF](#AUSF)** | list, tuple,  | tuple,  |  | [optional] 
**[NEF](#NEF)** | list, tuple,  | tuple,  |  | [optional] 
**[NRF](#NRF)** | list, tuple,  | tuple,  |  | [optional] 
**[NSSF](#NSSF)** | list, tuple,  | tuple,  |  | [optional] 
**[SMSF](#SMSF)** | list, tuple,  | tuple,  |  | [optional] 
**[UDM](#UDM)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# MSC_SERVER

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["MO_MT_CALLS", "MO_MT_SMS", "LU_IMSIattach_IMSIdetach", "HANDOVER", "SS", ] 

# SGSN

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PDPcontext", "MO_MT_SMS", "RAU_GPRSattach_GPRSdetach", "MBMScontext", ] 

# MGW

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["CONTEXT", ] 

# GGSN

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PDPcontext", "MBMScontext", ] 

# IMS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["SIPsession_StandaloneTransaction", ] 

# BM_SC

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["MBMSactivation", ] 

# MME

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["UEinitiatedPDNconnectivityRequest", "ServiceRequest", "InitialAttach_TAU_Detach", "UEinitiatedPDNdisconnection", "BearerActivationModificationDeletion", "Handover", ] 

# SGW

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PDNconnectionCreation", "PDNconnectionTermination", "BearerActivationModificationDeletion", ] 

# PGW

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PDNconnectionCreation", "PDNconnectionTermination", "BearerActivationModificationDeletion", ] 

# AMF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Registration", "ServiceRequest", "Handover", "UEderegistration", "NetworkDeregistration", "UEMobilityFromEPC", "UEMobilityToEPC", ] 

# SMF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["PDUsessionEstablishment", "PDUsessionModification", "PDUsessionRelease", "PDUsessionUPactivationDeactivation", "MobilityBtw3gppAndN3gppTo5GC", "MobilityFromEpc", ] 

# PCF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["AMpolicy", "SMpolicy", "Authorization", "BDTpolicy", ] 

# UPF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N4Session", ] 

# AUSF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["UEauthentication", ] 

# NEF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["EventExposure", "PFDmanagement", "ParameterProvision", "Trigger", ] 

# NRF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NFmanagement", "NFdiscovery", ] 

# NSSF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NSSelection", "NSSAI", ] 

# SMSF

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["SMservice", ] 

# UDM

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["UEcontext", "SubscriberData", "UEauthentication", "EventExposure", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

