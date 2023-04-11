# openapi_client.model.trace_target_type.TraceTargetType

Trace target conveying both the type and value of the target ID. For additional details see 3GPP TS 32.422

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Trace target conveying both the type and value of the target ID. For additional details see 3GPP TS 32.422 | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**TargetIdType** | str,  | str,  |  | must be one of ["IMSI", "IMEI", "IMEISV", "PUBLIC_ID", "UTRAN_CELL", "E-UTRAN_CELL", "NG-RAN_CELL", "eNB", "RNC", "gNB", "SUPI", ] 
**TargetIdValue** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

