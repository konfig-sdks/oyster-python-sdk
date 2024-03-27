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

from oyster_python_sdk.type.time_off_engagement_details import TimeOffEngagementDetails

class RequiredTimeOffRequest(TypedDict):
    pass

class OptionalTimeOffRequest(TypedDict, total=False):
    timeOffRequestId: str

    engagement: TimeOffEngagementDetails

    startDate: date

    endDate: date

    firstDayDuration: str

    lastDayDuration: typing.Optional[str]

    state: str

    type: str

    requesterComments: typing.Optional[str]

    rejectionReason: typing.Optional[str]

    reason: str

    periodInHours: typing.Union[int, float]

class TimeOffRequest(RequiredTimeOffRequest, OptionalTimeOffRequest):
    pass
