# coding: utf-8

"""
    Endpoints

    Oyster uses OAuth2 to enable customers to grant access to their data to third party applications. Customers also need to use this API to authenticate themselves when making API requests.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from oyster_python_sdk.type.operation_meta import OperationMeta
from oyster_python_sdk.type.operation_request import OperationRequest

class RequiredOperation(TypedDict):
    pass

class OptionalOperation(TypedDict, total=False):
    request: OperationRequest

    data: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    meta: OperationMeta

class Operation(RequiredOperation, OptionalOperation):
    pass
