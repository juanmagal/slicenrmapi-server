# openapi_client.model.plmn_target_type.PLMNTargetType

The PLMN for which sessions shall be selected in the Trace Session in case of management based activation when several PLMNs are supported in the RAN (this means that shared cells and not shared cells are allowed for the specified PLMN. Note that the PLMN Target might differ from the PLMN specified in the Trace Reference, as that specifies the PLMN that is containing the management system requesting the Trace Session from the NE. See 3GPP TS 32.422 clause 5.9b for additional details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The PLMN for which sessions shall be selected in the Trace Session in case of management based activation when several PLMNs are supported in the RAN (this means that shared cells and not shared cells are allowed for the specified PLMN. Note that the PLMN Target might differ from the PLMN specified in the Trace Reference, as that specifies the PLMN that is containing the management system requesting the Trace Session from the NE. See 3GPP TS 32.422 clause 5.9b for additional details. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mnc** | [**Mnc1**](Mnc1.md) | [**Mnc1**](Mnc1.md) |  | 
**mcc** | [**Mcc**](Mcc.md) | [**Mcc**](Mcc.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

