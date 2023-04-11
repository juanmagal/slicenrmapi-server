# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error_response import ErrorResponse  # noqa: F401
from openapi_server.models.patch_item import PatchItem  # noqa: F401
from openapi_server.models.resource import Resource  # noqa: F401
from openapi_server.models.scope import Scope  # noqa: F401


def test_class_nameid_delete(client: TestClient):
    """Test case for class_nameid_delete

    Deletes one resource
    """

    headers = {
    }
    response = client.request(
        "DELETE",
        "/{className}={id}".format(className='class_name_example', id='id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_class_nameid_get(client: TestClient):
    """Test case for class_nameid_get

    Reads one or multiple resources
    """
    params = [("scope", {'key': openapi_server.Scope()}),     ("filter", 'filter_example'),     ("attributes", ['attributes_example']),     ("fields", ['fields_example'])]
    headers = {
    }
    response = client.request(
        "GET",
        "/{className}={id}".format(className='class_name_example', id='id_example'),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_class_nameid_patch(client: TestClient):
    """Test case for class_nameid_patch

    Patches one or multiple resources
    """
    resource = openapi_server.Resource()

    headers = {
    }
    response = client.request(
        "PATCH",
        "/{className}={id}".format(className='class_name_example', id='id_example'),
        headers=headers,
        json=resource,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_class_nameid_put(client: TestClient):
    """Test case for class_nameid_put

    Replaces a complete single resource or creates it if it does not exist
    """
    resource = null

    headers = {
    }
    response = client.request(
        "PUT",
        "/{className}={id}".format(className='class_name_example', id='id_example'),
        headers=headers,
        json=resource,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

