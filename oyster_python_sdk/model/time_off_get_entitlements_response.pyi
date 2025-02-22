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


class TimeOffGetEntitlementsResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "data",
            "meta",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['TimeOffEntitlements']:
                return TimeOffEntitlements
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
            __annotations__ = {
                "data": data,
                "meta": meta,
            }
    
    data: 'TimeOffEntitlements'
    meta: 'Meta'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'TimeOffEntitlements': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'TimeOffEntitlements': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: 'TimeOffEntitlements',
        meta: 'Meta',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffGetEntitlementsResponse':
        return super().__new__(
            cls,
            *args,
            data=data,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from oyster_python_sdk.model.meta import Meta
from oyster_python_sdk.model.time_off_entitlements import TimeOffEntitlements
