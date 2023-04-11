# openapi_client.model.feasibility_check_and_reservation_job_single.FeasibilityCheckAndReservationJobSingle

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Top](Top.md) | [**Top**](Top.md) | [**Top**](Top.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[attributes](#attributes)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[profile](#profile)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**resourceReservation** | bool,  | BoolClass,  | An attribute represents MnS consumer&#x27;s requirements for resource reservation. | [optional] 
**requestedReservationExpiration** | str,  | str,  | An attribute which specifes MnS consuner&#x27;s requirements for the validity period of the resource reservation. | [optional] 
**processMonitor** | [**ProcessMonitor**](ProcessMonitor.md) | [**ProcessMonitor**](ProcessMonitor.md) |  | [optional] 
**feasibilityResult** | [**FeasibilityResult**](FeasibilityResult.md) | [**FeasibilityResult**](FeasibilityResult.md) |  | [optional] 
**inFeasibleReason** | str,  | str,  | An attribute that specifies the additional reason information if the feasibility check result is infeasible.The detailed ENUM value is FFS.  | [optional] 
**resourceReservationStatus** | [**ResourceReservationStatus**](ResourceReservationStatus.md) | [**ResourceReservationStatus**](ResourceReservationStatus.md) |  | [optional] 
**reservationFailureReason** | str,  | str,  | An attribute that specifies the additional reason information if the reservation is failed.  | [optional] 
**reservationExpiration** | str,  | str,  | An attribute which specifes the actual validity period of the resource reservation.. | [optional] 
**recommendedRequirements** | str,  | str,  | An attribute that specifies the recommended network slicing related requirements (i.e. ServiceProfile and SliceProfile information) which can be supported by the MnS producer..  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SliceProfile](SliceProfile.md) | [**SliceProfile**](SliceProfile.md) | [**SliceProfile**](SliceProfile.md) |  | 
[ServiceProfile](ServiceProfile.md) | [**ServiceProfile**](ServiceProfile.md) | [**ServiceProfile**](ServiceProfile.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

