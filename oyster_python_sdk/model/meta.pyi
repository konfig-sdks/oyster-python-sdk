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


class Meta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            items = schemas.IntSchema
            count = schemas.IntSchema
            page = schemas.IntSchema
            pages = schemas.IntSchema
            firstUrl = schemas.StrSchema
            lastUrl = schemas.StrSchema
            pageUrl = schemas.StrSchema
            nextUrl = schemas.StrSchema
            prevUrl = schemas.StrSchema
            __annotations__ = {
                "items": items,
                "count": count,
                "page": page,
                "pages": pages,
                "firstUrl": firstUrl,
                "lastUrl": lastUrl,
                "pageUrl": pageUrl,
                "nextUrl": nextUrl,
                "prevUrl": prevUrl,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pages"]) -> MetaOapg.properties.pages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstUrl"]) -> MetaOapg.properties.firstUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUrl"]) -> MetaOapg.properties.lastUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageUrl"]) -> MetaOapg.properties.pageUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextUrl"]) -> MetaOapg.properties.nextUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prevUrl"]) -> MetaOapg.properties.prevUrl: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["items", "count", "page", "pages", "firstUrl", "lastUrl", "pageUrl", "nextUrl", "prevUrl", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pages"]) -> typing.Union[MetaOapg.properties.pages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstUrl"]) -> typing.Union[MetaOapg.properties.firstUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUrl"]) -> typing.Union[MetaOapg.properties.lastUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageUrl"]) -> typing.Union[MetaOapg.properties.pageUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextUrl"]) -> typing.Union[MetaOapg.properties.nextUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prevUrl"]) -> typing.Union[MetaOapg.properties.prevUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["items", "count", "page", "pages", "firstUrl", "lastUrl", "pageUrl", "nextUrl", "prevUrl", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        items: typing.Union[MetaOapg.properties.items, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pages: typing.Union[MetaOapg.properties.pages, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        firstUrl: typing.Union[MetaOapg.properties.firstUrl, str, schemas.Unset] = schemas.unset,
        lastUrl: typing.Union[MetaOapg.properties.lastUrl, str, schemas.Unset] = schemas.unset,
        pageUrl: typing.Union[MetaOapg.properties.pageUrl, str, schemas.Unset] = schemas.unset,
        nextUrl: typing.Union[MetaOapg.properties.nextUrl, str, schemas.Unset] = schemas.unset,
        prevUrl: typing.Union[MetaOapg.properties.prevUrl, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Meta':
        return super().__new__(
            cls,
            *args,
            items=items,
            count=count,
            page=page,
            pages=pages,
            firstUrl=firstUrl,
            lastUrl=lastUrl,
            pageUrl=pageUrl,
            nextUrl=nextUrl,
            prevUrl=prevUrl,
            _configuration=_configuration,
            **kwargs,
        )
