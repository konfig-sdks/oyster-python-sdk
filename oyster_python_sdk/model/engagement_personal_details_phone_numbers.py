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


class EngagementPersonalDetailsPhoneNumbers(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            default = schemas.DictSchema
            emergency = schemas.DictSchema
            __annotations__ = {
                "default": default,
                "emergency": emergency,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default"]) -> MetaOapg.properties.default: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emergency"]) -> MetaOapg.properties.emergency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["default", "emergency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default"]) -> typing.Union[MetaOapg.properties.default, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emergency"]) -> typing.Union[MetaOapg.properties.emergency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["default", "emergency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        default: typing.Union[MetaOapg.properties.default, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        emergency: typing.Union[MetaOapg.properties.emergency, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EngagementPersonalDetailsPhoneNumbers':
        return super().__new__(
            cls,
            *args,
            default=default,
            emergency=emergency,
            _configuration=_configuration,
            **kwargs,
        )
