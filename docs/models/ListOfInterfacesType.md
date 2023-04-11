# openapi_client.model.list_of_interfaces_type.ListOfInterfacesType

The interfaces to be recorded in the Network Element. See 3GPP TS 32.422 clause 5.5 for additional details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The interfaces to be recorded in the Network Element. See 3GPP TS 32.422 clause 5.5 for additional details. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[MSCServerInterfaces](#MSCServerInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[MGWInterfaces](#MGWInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[RNCInterfaces](#RNCInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[SGSNInterfaces](#SGSNInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[GGSNInterfaces](#GGSNInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[S-CSCFInterfaces](#S-CSCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[P-CSCFInterfaces](#P-CSCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[I-CSCFInterfaces](#I-CSCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[MRFCInterfaces](#MRFCInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[MGCFInterfaces](#MGCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[IBCFInterfaces](#IBCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[E-CSCFInterfaces](#E-CSCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[BGCFInterfaces](#BGCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[ASInterfaces](#ASInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[HSSInterfaces](#HSSInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[EIRInterfaces](#EIRInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[BM-SCInterfaces](#BM-SCInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[MMEInterfaces](#MMEInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[SGWInterfaces](#SGWInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[PDN_GWInterfaces](#PDN_GWInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[eNBInterfaces](#eNBInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[en-gNBInterfaces](#en-gNBInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[AMFInterfaces](#AMFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[AUSFInterfaces](#AUSFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[NEFInterfaces](#NEFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[NRFInterfaces](#NRFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[NSSFInterfaces](#NSSFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[PCFInterfaces](#PCFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[SMFInterfaces](#SMFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[SMSFInterfaces](#SMSFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[UDMInterfaces](#UDMInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[UPFInterfaces](#UPFInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[ng-eNBInterfaces](#ng-eNBInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[gNB-CU-CPInterfaces](#gNB-CU-CPInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[gNB-CU-UPInterfaces](#gNB-CU-UPInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**[gNB-DUInterfaces](#gNB-DUInterfaces)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# MSCServerInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["A", "Iu-CS", "Mc", "MAP-G", "MAP-B", "MAP-E", "MAP-F", "MAP-D", "MAP-C", "CAP", ] 

# MGWInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Mc", "Nb-UP", "Iu-UP", ] 

# RNCInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Iu-CS", "Iu-PS", "Iur", "Iub", "Uu", ] 

# SGSNInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Gb", "Iu-PS", "Gn", "MAP-Gr", "MAP-Gd", "MAP-Gf", "Ge", "Gs", "S6d", "S4", "S3", "S13", ] 

# GGSNInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Gn", "Gi", "Gmb", ] 

# S-CSCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Mw", "Mg", "Mr", "Mi", ] 

# P-CSCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Gm", "Mw", ] 

# I-CSCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Cx", "Dx", "Mg", "Mw", ] 

# MRFCInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Mp", "Mr", ] 

# MGCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Mg", "Mj", "Mn", ] 

# IBCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Ix", "Mx", ] 

# E-CSCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Mw", "Ml", "Mm", "Mi/Mg", ] 

# BGCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Mi", "Mj", "Mk", ] 

# ASInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Dh", "Sh", "ISC", "Ut", ] 

# HSSInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["MAP-C", "MAP-D", "Gc", "Gr", "Cx", "S6d", "S6a", "Sh", "N70", "N71", "NU1", ] 

# EIRInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["MAP-F", "S13", "MAP-Gf", ] 

# BM-SCInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["Gmb", ] 

# MMEInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["S1-MME", "S3", "S6a", "S10", "S11", "S13", ] 

# SGWInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["S4", "S5", "S8", "S11", "Gxc", ] 

# PDN_GWInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["S2a", "S2b", "S2c", "S5", "S6b", "Gx", "S8", "SGi", ] 

# eNBInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["S1-MME", "X2", ] 

# en-gNBInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["S1-MME", "X2", "Uu", "F1-C", "E1", ] 

# AMFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N1", "N2", "N8", "N11", "N12", "N14", "N15", "N20", "N22", "N26", ] 

# AUSFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N12", "N13", ] 

# NEFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N29", "N30", "N33", ] 

# NRFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N27", ] 

# NSSFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N22", "N31", ] 

# PCFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N5", "N7", "N15", ] 

# SMFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N4", "N7", "N10", "N11", "S5-C", "N16", "N16a", ] 

# SMSFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N20", "N21", ] 

# UDMInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N8", "N10", "N13", "N21", "NU1", ] 

# UPFInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["N4", ] 

# ng-eNBInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NG-C", "Xn-C", "Uu", ] 

# gNB-CU-CPInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["NG-C", "Xn-C", "Uu", "F1-C", "E1", "X2-C", ] 

# gNB-CU-UPInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["E1", ] 

# gNB-DUInterfaces

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["F1-C", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

