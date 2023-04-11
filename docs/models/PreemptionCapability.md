# openapi_client.model.preemption_capability.PreemptionCapability

The enumeration PreemptionCapability indicates the pre-emption capability of a request on other QoS flows. See clause 5.7.2.2 of 3GPP TS 23.501. It shall comply with the provisions defined in table 5.5.3.1-1. 

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The enumeration PreemptionCapability indicates the pre-emption capability of a request on other QoS flows. See clause 5.7.2.2 of 3GPP TS 23.501. It shall comply with the provisions defined in table 5.5.3.1-1.  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["NOT_PREEMPT", "MAY_PREEMPT", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["NOT_PREEMPT", "MAY_PREEMPT", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

