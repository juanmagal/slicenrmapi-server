# openapi_client.model.trace_reference_type.TraceReferenceType

The Trace Reference parameter shall be globally unique, therefore the Trace Reference shall compose as follows - MCC+MNC+Trace ID, where the MCC and MNC are coming with the Trace activation request from the management system to identify one PLMN containing the management system, and Trace ID is a 3 byte Octet String. See 3GPP TS 32.422 clause 5.6 for additional details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The Trace Reference parameter shall be globally unique, therefore the Trace Reference shall compose as follows - MCC+MNC+Trace ID, where the MCC and MNC are coming with the Trace activation request from the management system to identify one PLMN containing the management system, and Trace ID is a 3 byte Octet String. See 3GPP TS 32.422 clause 5.6 for additional details. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**traceId** | str,  | str,  |  | 
**mnc** | [**Mnc1**](Mnc1.md) | [**Mnc1**](Mnc1.md) |  | 
**mcc** | [**Mcc**](Mcc.md) | [**Mcc**](Mcc.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

