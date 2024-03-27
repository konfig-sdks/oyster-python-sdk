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


class TimeOffEntitlementsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def engagement() -> typing.Type['TimeOffEngagementDetails']:
                return TimeOffEngagementDetails
            annualEntitlement = schemas.Float32Schema
            accrued = schemas.Float32Schema
            carried = schemas.Float32Schema
            adjustedAdhoc = schemas.Float32Schema
            taken = schemas.Float32Schema
            availableBalance = schemas.Float32Schema
            upcoming = schemas.Float32Schema
            projectedBalance = schemas.Float32Schema
            
            
            class units(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DAYS": "DAYS",
                    }
                
                @schemas.classproperty
                def DAYS(cls):
                    return cls("DAYS")
            __annotations__ = {
                "engagement": engagement,
                "annualEntitlement": annualEntitlement,
                "accrued": accrued,
                "carried": carried,
                "adjustedAdhoc": adjustedAdhoc,
                "taken": taken,
                "availableBalance": availableBalance,
                "upcoming": upcoming,
                "projectedBalance": projectedBalance,
                "units": units,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engagement"]) -> 'TimeOffEngagementDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annualEntitlement"]) -> MetaOapg.properties.annualEntitlement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accrued"]) -> MetaOapg.properties.accrued: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["carried"]) -> MetaOapg.properties.carried: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adjustedAdhoc"]) -> MetaOapg.properties.adjustedAdhoc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taken"]) -> MetaOapg.properties.taken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableBalance"]) -> MetaOapg.properties.availableBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upcoming"]) -> MetaOapg.properties.upcoming: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectedBalance"]) -> MetaOapg.properties.projectedBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["engagement", "annualEntitlement", "accrued", "carried", "adjustedAdhoc", "taken", "availableBalance", "upcoming", "projectedBalance", "units", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engagement"]) -> typing.Union['TimeOffEngagementDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annualEntitlement"]) -> typing.Union[MetaOapg.properties.annualEntitlement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accrued"]) -> typing.Union[MetaOapg.properties.accrued, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["carried"]) -> typing.Union[MetaOapg.properties.carried, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adjustedAdhoc"]) -> typing.Union[MetaOapg.properties.adjustedAdhoc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taken"]) -> typing.Union[MetaOapg.properties.taken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableBalance"]) -> typing.Union[MetaOapg.properties.availableBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upcoming"]) -> typing.Union[MetaOapg.properties.upcoming, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectedBalance"]) -> typing.Union[MetaOapg.properties.projectedBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> typing.Union[MetaOapg.properties.units, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["engagement", "annualEntitlement", "accrued", "carried", "adjustedAdhoc", "taken", "availableBalance", "upcoming", "projectedBalance", "units", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        engagement: typing.Union['TimeOffEngagementDetails', schemas.Unset] = schemas.unset,
        annualEntitlement: typing.Union[MetaOapg.properties.annualEntitlement, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        accrued: typing.Union[MetaOapg.properties.accrued, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        carried: typing.Union[MetaOapg.properties.carried, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        adjustedAdhoc: typing.Union[MetaOapg.properties.adjustedAdhoc, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        taken: typing.Union[MetaOapg.properties.taken, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        availableBalance: typing.Union[MetaOapg.properties.availableBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        upcoming: typing.Union[MetaOapg.properties.upcoming, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        projectedBalance: typing.Union[MetaOapg.properties.projectedBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        units: typing.Union[MetaOapg.properties.units, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffEntitlementsItem':
        return super().__new__(
            cls,
            *args,
            engagement=engagement,
            annualEntitlement=annualEntitlement,
            accrued=accrued,
            carried=carried,
            adjustedAdhoc=adjustedAdhoc,
            taken=taken,
            availableBalance=availableBalance,
            upcoming=upcoming,
            projectedBalance=projectedBalance,
            units=units,
            _configuration=_configuration,
            **kwargs,
        )

from oyster_python_sdk.model.time_off_engagement_details import TimeOffEngagementDetails
