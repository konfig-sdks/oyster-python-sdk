# coding: utf-8

"""
    Endpoints

    Oyster uses OAuth2 to enable customers to grant access to their data to third party applications. Customers also need to use this API to authenticate themselves when making API requests.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
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

from oyster_python_sdk import schemas  # noqa: F401


class TimeOffEntitlements(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TimeOffEntitlementsItem']:
            return TimeOffEntitlementsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TimeOffEntitlementsItem'], typing.List['TimeOffEntitlementsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TimeOffEntitlements':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TimeOffEntitlementsItem':
        return super().__getitem__(i)

from oyster_python_sdk.model.time_off_entitlements_item import TimeOffEntitlementsItem
