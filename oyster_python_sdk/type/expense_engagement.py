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


class RequiredExpenseEngagement(TypedDict):
    pass

class OptionalExpenseEngagement(TypedDict, total=False):
    engagementId: str

    name: typing.Optional[str]

    engagementType: str

class ExpenseEngagement(RequiredExpenseEngagement, OptionalExpenseEngagement):
    pass
