# coding: utf-8

"""
    Provisioning MnS

    OAS 3.0.1 definition of the Provisioning MnS Â© 2022, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.  # noqa: E501

    The version of the OpenAPI document: 17.2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class AttributeValueChangeSet(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The first array item contains the attribute name value pairs with the new values, and the second array item the attribute name value pairs with the optional old values.
    """


    class MetaOapg:
        max_items = 2
        min_items = 1
        
        @staticmethod
        def items() -> typing.Type['AttributeNameValuePairSet']:
            return AttributeNameValuePairSet

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['AttributeNameValuePairSet'], typing.List['AttributeNameValuePairSet']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'AttributeValueChangeSet':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'AttributeNameValuePairSet':
        return super().__getitem__(i)

from openapi_client.model.attribute_name_value_pair_set import AttributeNameValuePairSet