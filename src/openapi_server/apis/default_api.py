# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patch_item import PatchItem
from openapi_server.models.resource import Resource
from openapi_server.models.scope import Scope


router = APIRouter()


@router.delete(
    "/{className}&#x3D;{id}",
    responses={
        200: {"description": "Success case (\&quot;200 OK\&quot;). This status code is returned, when the resource has been successfully deleted. The response body is empty."},
        200: {"model": ErrorResponse, "description": "Error case."},
    },
    tags=["default"],
    summary="Deletes one resource",
    response_model_by_alias=True,
)
async def class_nameid_delete(
    className: str = Path(None, description=""),
    id: str = Path(None, description=""),
) -> None:
    """With HTTP DELETE one resource is deleted. The resources to be deleted is identified with the target URI."""
    ...


@router.get(
    "/{className}&#x3D;{id}",
    responses={
        200: {"model": Resource, "description": "Success case (\&quot;200 OK\&quot;). The resources identified in the request for retrieval are returned in the response message body. In case the attributes or fields query parameters are used, only the selected attributes or sub-attributes are returned. The response message body is constructed according to the hierarchical response construction method (TS 32.158 [15])."},
        200: {"model": ErrorResponse, "description": "Error case."},
    },
    tags=["default"],
    summary="Reads one or multiple resources",
    response_model_by_alias=True,
)
async def class_nameid_get(
    className: str = Path(None, description=""),
    id: str = Path(None, description=""),
    attributes: List[str] = Query(None, description="This parameter specifies the attributes of the scoped resources that are returned."),
    scope: Scope = Query(None, description="This parameter extends the set of targeted resources beyond the base resource identified with the path component of the URI. No scoping mechanism is specified in the present document."),
    filter: str = Query(None, description="This parameter reduces the targeted set of resources by applying a filter to the scoped set of resource representations. Only resource representations for which the filter construct evaluates to \&quot;true\&quot; are targeted. No filter language is specified in the present document."),
    fields: List[str] = Query(None, description="This parameter specifies the attribute field of the scoped resources that are returned."),
) -> Resource:
    """With HTTP GET resources are read. The resources to be retrieved are identified with the target URI. The attributes and fields parameter of the query components allow to select the resource properties to be returned."""
    ...


@router.patch(
    "/{className}&#x3D;{id}",
    responses={
        200: {"model": Resource, "description": "Success case (\&quot;200 OK\&quot;). This status code is returned when the updated the resource representations shall be returned for some reason. The resource representations are returned in the response message body. The response message body is constructed according to the hierarchical response construction method (TS 32.158 [15])"},
        204: {"description": "Success case (\&quot;204 No Content\&quot;). This status code is returned when there is no need to return the updated resource representations. The response message body is empty."},
        200: {"model": ErrorResponse, "description": "Error case."},
    },
    tags=["default"],
    summary="Patches one or multiple resources",
    response_model_by_alias=True,
)
async def class_nameid_patch(
    className: str = Path(None, description=""),
    id: str = Path(None, description=""),
    resource: Resource = Body(None, description="The request body describes changes to be made to the target resources. The following patch media types are available   - \&quot;application/merge-patch+json\&quot; (RFC 7396)   - \&quot;application/3gpp-merge-patch+json\&quot; (TS 32.158)   - \&quot;application/json-patch+json\&quot; (RFC 6902)   - \&quot;application/3gpp-json-patch+json\&quot; (TS 32.158)"),
) -> Resource:
    """With HTTP PATCH resources are created, updated or deleted. The resources to be modified are identified with the target URI (base resource) and the patch document included in the request message body."""
    ...


@router.put(
    "/{className}&#x3D;{id}",
    responses={
        200: {"model": Resource, "description": "Success case (\&quot;200 OK\&quot;). This status code shall be returned when the resource is replaced, and when the replaced resource representation is not identical to the resource representation in the request. This status code may be retourned when the resource is updated and when the updated resource representation is identical to the resource representation in the request. The representation of the updated resource is returned in the response message body."},
        201: {"model": Resource, "description": "Success case (\&quot;201 Created\&quot;). This status code shall be returned when the resource is created. The representation of the created resource is returned in the response message body."},
        204: {"description": "Success case (\&quot;204 No Content\&quot;). This status code may be returned only when the replaced resource representation is identical to the representation in the request. The response has no message body."},
        200: {"model": ErrorResponse, "description": "Error case."},
    },
    tags=["default"],
    summary="Replaces a complete single resource or creates it if it does not exist",
    response_model_by_alias=True,
)
async def class_nameid_put(
    className: str = Path(None, description=""),
    id: str = Path(None, description=""),
    resource: Resource = Body(None, description=""),
) -> Resource:
    """With HTTP PUT a complete resource is replaced or created if it does not exist. The target resource is identified by the target URI."""
    ...
