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


class EngagementPersonalDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "addresses",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def addresses() -> typing.Type['EngagementPersonalDetailsAddresses']:
                return EngagementPersonalDetailsAddresses
        
            @staticmethod
            def citizenships() -> typing.Type['EngagementPersonalDetailsCitizenships']:
                return EngagementPersonalDetailsCitizenships
            
            
            class dateOfBirth(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dateOfBirth':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def phoneNumbers() -> typing.Type['EngagementPersonalDetailsPhoneNumbers']:
                return EngagementPersonalDetailsPhoneNumbers
            __annotations__ = {
                "name": name,
                "addresses": addresses,
                "citizenships": citizenships,
                "dateOfBirth": dateOfBirth,
                "phoneNumbers": phoneNumbers,
            }
    
    addresses: 'EngagementPersonalDetailsAddresses'
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addresses"]) -> 'EngagementPersonalDetailsAddresses': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["citizenships"]) -> 'EngagementPersonalDetailsCitizenships': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateOfBirth"]) -> MetaOapg.properties.dateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneNumbers"]) -> 'EngagementPersonalDetailsPhoneNumbers': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "addresses", "citizenships", "dateOfBirth", "phoneNumbers", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addresses"]) -> 'EngagementPersonalDetailsAddresses': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["citizenships"]) -> typing.Union['EngagementPersonalDetailsCitizenships', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateOfBirth"]) -> typing.Union[MetaOapg.properties.dateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneNumbers"]) -> typing.Union['EngagementPersonalDetailsPhoneNumbers', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "addresses", "citizenships", "dateOfBirth", "phoneNumbers", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        addresses: 'EngagementPersonalDetailsAddresses',
        name: typing.Union[MetaOapg.properties.name, None, str, ],
        citizenships: typing.Union['EngagementPersonalDetailsCitizenships', schemas.Unset] = schemas.unset,
        dateOfBirth: typing.Union[MetaOapg.properties.dateOfBirth, None, str, schemas.Unset] = schemas.unset,
        phoneNumbers: typing.Union['EngagementPersonalDetailsPhoneNumbers', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EngagementPersonalDetails':
        return super().__new__(
            cls,
            *args,
            addresses=addresses,
            name=name,
            citizenships=citizenships,
            dateOfBirth=dateOfBirth,
            phoneNumbers=phoneNumbers,
            _configuration=_configuration,
            **kwargs,
        )

from oyster_python_sdk.model.engagement_personal_details_addresses import EngagementPersonalDetailsAddresses
from oyster_python_sdk.model.engagement_personal_details_citizenships import EngagementPersonalDetailsCitizenships
from oyster_python_sdk.model.engagement_personal_details_phone_numbers import EngagementPersonalDetailsPhoneNumbers
