from openapi_client.paths.class_nameid.get import ApiForget
from openapi_client.paths.class_nameid.put import ApiForput
from openapi_client.paths.class_nameid.delete import ApiFordelete
from openapi_client.paths.class_nameid.patch import ApiForpatch


class ClassNameid(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
