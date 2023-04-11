<a name="__pageTop"></a>
# openapi_client.apis.tags.default_api.DefaultApi

All URIs are relative to *http://example.com/3GPPManagement/ProvMnS/XXX*

Method | HTTP request | Description
------------- | ------------- | -------------
[**class_nameid_delete**](#class_nameid_delete) | **delete** /{className}&#x3D;{id} | Deletes one resource
[**class_nameid_get**](#class_nameid_get) | **get** /{className}&#x3D;{id} | Reads one or multiple resources
[**class_nameid_patch**](#class_nameid_patch) | **patch** /{className}&#x3D;{id} | Patches one or multiple resources
[**class_nameid_put**](#class_nameid_put) | **put** /{className}&#x3D;{id} | Replaces a complete single resource or creates it if it does not exist

# **class_nameid_delete**
<a name="class_nameid_delete"></a>
> class_nameid_delete(class_nameid)

Deletes one resource

With HTTP DELETE one resource is deleted. The resources to be deleted is identified with the target URI.

### Example

```python
import openapi_client
from openapi_client.apis.tags import default_api
from openapi_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/3GPPManagement/ProvMnS/XXX
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://example.com/3GPPManagement/ProvMnS/XXX"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'className': "className_example",
        'id': "id_example",
    }
    try:
        # Deletes one resource
        api_response = api_instance.class_nameid_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->class_nameid_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
className | ClassNameSchema | | 
id | IdSchema | | 

# ClassNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#class_nameid_delete.ApiResponseFor200) | Success case (\&quot;200 OK\&quot;). This status code is returned, when the resource has been successfully deleted. The response body is empty.
default | [ApiResponseForDefault](#class_nameid_delete.ApiResponseForDefault) | Error case.

#### class_nameid_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### class_nameid_delete.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **class_nameid_get**
<a name="class_nameid_get"></a>
> Resource class_nameid_get(class_nameidattributes)

Reads one or multiple resources

With HTTP GET resources are read. The resources to be retrieved are identified with the target URI. The attributes and fields parameter of the query components allow to select the resource properties to be returned.

### Example

```python
import openapi_client
from openapi_client.apis.tags import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.scope import Scope
from openapi_client.model.resource import Resource
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/3GPPManagement/ProvMnS/XXX
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://example.com/3GPPManagement/ProvMnS/XXX"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'className': "className_example",
        'id': "id_example",
    }
    query_params = {
        'attributes': [
        "attributes_example"
    ],
    }
    try:
        # Reads one or multiple resources
        api_response = api_instance.class_nameid_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->class_nameid_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'className': "className_example",
        'id': "id_example",
    }
    query_params = {
        'scope': Scope(
        scope_type=ScopeType("BASE_ONLY"),
        scope_level=1,
    ),
        'filter': "filter_example",
        'attributes': [
        "attributes_example"
    ],
        'fields': [
        "fields_example"
    ],
    }
    try:
        # Reads one or multiple resources
        api_response = api_instance.class_nameid_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->class_nameid_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/vnd.3gpp.object-tree-hierarchical+json', 'application/vnd.3gpp.object-tree-flat+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
scope | ScopeSchema | | optional
filter | FilterSchema | | optional
attributes | AttributesSchema | | 
fields | FieldsSchema | | optional


# ScopeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**Scope**](../../models/Scope.md) |  | 


# FilterSchema

The filter format shall be compliant to XPath 1.0.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The filter format shall be compliant to XPath 1.0. | 

# AttributesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FieldsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
className | ClassNameSchema | | 
id | IdSchema | | 

# ClassNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#class_nameid_get.ApiResponseFor200) | Success case (\&quot;200 OK\&quot;). The resources identified in the request for retrieval are returned in the response message body. In case the attributes or fields query parameters are used, only the selected attributes or sub-attributes are returned. The response message body is constructed according to the hierarchical response construction method (TS 32.158 [15]).
default | [ApiResponseForDefault](#class_nameid_get.ApiResponseForDefault) | Error case.

#### class_nameid_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationVnd3gppObjectTreeHierarchicaljson, SchemaFor200ResponseBodyApplicationVnd3gppObjectTreeFlatjson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


# SchemaFor200ResponseBodyApplicationVnd3gppObjectTreeHierarchicaljson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


# SchemaFor200ResponseBodyApplicationVnd3gppObjectTreeFlatjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Resource**]({{complexTypePrefix}}Resource.md) | [**Resource**]({{complexTypePrefix}}Resource.md) | [**Resource**]({{complexTypePrefix}}Resource.md) |  | 

#### class_nameid_get.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **class_nameid_patch**
<a name="class_nameid_patch"></a>
> Resource class_nameid_patch(class_nameidresource)

Patches one or multiple resources

With HTTP PATCH resources are created, updated or deleted. The resources to be modified are identified with the target URI (base resource) and the patch document included in the request message body.

### Example

```python
import openapi_client
from openapi_client.apis.tags import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.resource import Resource
from openapi_client.model.patch_item import PatchItem
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/3GPPManagement/ProvMnS/XXX
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://example.com/3GPPManagement/ProvMnS/XXX"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'className': "className_example",
        'id': "id_example",
    }
    body = Resource(None)
    try:
        # Patches one or multiple resources
        api_response = api_instance.class_nameid_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->class_nameid_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationMergePatchjson, SchemaForRequestBodyApplication3gppMergePatchjson, SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplication3gppJsonPatchjson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/merge-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationMergePatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


# SchemaForRequestBodyApplication3gppMergePatchjson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


# SchemaForRequestBodyApplicationJsonPatchjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PatchItem**]({{complexTypePrefix}}PatchItem.md) | [**PatchItem**]({{complexTypePrefix}}PatchItem.md) | [**PatchItem**]({{complexTypePrefix}}PatchItem.md) |  | 

# SchemaForRequestBodyApplication3gppJsonPatchjson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PatchItem**]({{complexTypePrefix}}PatchItem.md) | [**PatchItem**]({{complexTypePrefix}}PatchItem.md) | [**PatchItem**]({{complexTypePrefix}}PatchItem.md) |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
className | ClassNameSchema | | 
id | IdSchema | | 

# ClassNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#class_nameid_patch.ApiResponseFor200) | Success case (\&quot;200 OK\&quot;). This status code is returned when the updated the resource representations shall be returned for some reason. The resource representations are returned in the response message body. The response message body is constructed according to the hierarchical response construction method (TS 32.158 [15])
204 | [ApiResponseFor204](#class_nameid_patch.ApiResponseFor204) | Success case (\&quot;204 No Content\&quot;). This status code is returned when there is no need to return the updated resource representations. The response message body is empty.
default | [ApiResponseForDefault](#class_nameid_patch.ApiResponseForDefault) | Error case.

#### class_nameid_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


#### class_nameid_patch.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### class_nameid_patch.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **class_nameid_put**
<a name="class_nameid_put"></a>
> Resource class_nameid_put(class_nameidresource)

Replaces a complete single resource or creates it if it does not exist

With HTTP PUT a complete resource is replaced or created if it does not exist. The target resource is identified by the target URI.

### Example

```python
import openapi_client
from openapi_client.apis.tags import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.resource import Resource
from pprint import pprint
# Defining the host is optional and defaults to http://example.com/3GPPManagement/ProvMnS/XXX
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://example.com/3GPPManagement/ProvMnS/XXX"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'className': "className_example",
        'id': "id_example",
    }
    body = Resource(None)
    try:
        # Replaces a complete single resource or creates it if it does not exist
        api_response = api_instance.class_nameid_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->class_nameid_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
className | ClassNameSchema | | 
id | IdSchema | | 

# ClassNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#class_nameid_put.ApiResponseFor200) | Success case (\&quot;200 OK\&quot;). This status code shall be returned when the resource is replaced, and when the replaced resource representation is not identical to the resource representation in the request. This status code may be retourned when the resource is updated and when the updated resource representation is identical to the resource representation in the request. The representation of the updated resource is returned in the response message body.
201 | [ApiResponseFor201](#class_nameid_put.ApiResponseFor201) | Success case (\&quot;201 Created\&quot;). This status code shall be returned when the resource is created. The representation of the created resource is returned in the response message body.
204 | [ApiResponseFor204](#class_nameid_put.ApiResponseFor204) | Success case (\&quot;204 No Content\&quot;). This status code may be returned only when the replaced resource representation is identical to the representation in the request. The response has no message body.
default | [ApiResponseForDefault](#class_nameid_put.ApiResponseForDefault) | Error case.

#### class_nameid_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


#### class_nameid_put.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


#### class_nameid_put.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### class_nameid_put.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

