# openapi_client.model.probable_cause.ProbableCause

The value of the probable cause may be a specific standardized string, or any vendor provided string. Probable cause strings are not standardized in the present document. They may be added in a future version. Up to then the mapping of the generic probable cause strings \"PROBABLE_CAUSE_001\" to \"PROBABLE_CAUSE_005\" is vendor specific. The value of the probable cause may also be an integer. The mapping of integer values to probable causes is vendor specific.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The value of the probable cause may be a specific standardized string, or any vendor provided string. Probable cause strings are not standardized in the present document. They may be added in a future version. Up to then the mapping of the generic probable cause strings \&quot;PROBABLE_CAUSE_001\&quot; to \&quot;PROBABLE_CAUSE_005\&quot; is vendor specific. The value of the probable cause may also be an integer. The mapping of integer values to probable causes is vendor specific. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[one_of_0](#one_of_0) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
[one_of_1](#one_of_1) | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# one_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["PROBABLE_CAUSE_001", "PROBABLE_CAUSE_002", "PROBABLE_CAUSE_003", "PROBABLE_CAUSE_004", "PROBABLE_CAUSE_005", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["PROBABLE_CAUSE_001", "PROBABLE_CAUSE_002", "PROBABLE_CAUSE_003", "PROBABLE_CAUSE_004", "PROBABLE_CAUSE_005", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# one_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

