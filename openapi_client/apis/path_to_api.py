import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.class_nameid import ClassNameid

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CLASS_NAMEID: ClassNameid,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CLASS_NAMEID: ClassNameid,
    }
)
