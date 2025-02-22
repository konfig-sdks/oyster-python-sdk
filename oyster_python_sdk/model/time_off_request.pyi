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


class TimeOffRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            timeOffRequestId = schemas.StrSchema
        
            @staticmethod
            def engagement() -> typing.Type['TimeOffEngagementDetails']:
                return TimeOffEngagementDetails
            startDate = schemas.DateSchema
            endDate = schemas.DateSchema
            
            
            class firstDayDuration(
                schemas.StrSchema
            ):
                pass
            
            
            class lastDayDuration(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastDayDuration':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class state(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.StrSchema
            ):
                pass
            
            
            class requesterComments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'requesterComments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class rejectionReason(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rejectionReason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class reason(
                schemas.StrSchema
            ):
                pass
            periodInHours = schemas.Float32Schema
            __annotations__ = {
                "timeOffRequestId": timeOffRequestId,
                "engagement": engagement,
                "startDate": startDate,
                "endDate": endDate,
                "firstDayDuration": firstDayDuration,
                "lastDayDuration": lastDayDuration,
                "state": state,
                "type": type,
                "requesterComments": requesterComments,
                "rejectionReason": rejectionReason,
                "reason": reason,
                "periodInHours": periodInHours,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timeOffRequestId"]) -> MetaOapg.properties.timeOffRequestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["engagement"]) -> 'TimeOffEngagementDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startDate"]) -> MetaOapg.properties.startDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endDate"]) -> MetaOapg.properties.endDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstDayDuration"]) -> MetaOapg.properties.firstDayDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastDayDuration"]) -> MetaOapg.properties.lastDayDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requesterComments"]) -> MetaOapg.properties.requesterComments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rejectionReason"]) -> MetaOapg.properties.rejectionReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periodInHours"]) -> MetaOapg.properties.periodInHours: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["timeOffRequestId", "engagement", "startDate", "endDate", "firstDayDuration", "lastDayDuration", "state", "type", "requesterComments", "rejectionReason", "reason", "periodInHours", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timeOffRequestId"]) -> typing.Union[MetaOapg.properties.timeOffRequestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["engagement"]) -> typing.Union['TimeOffEngagementDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startDate"]) -> typing.Union[MetaOapg.properties.startDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endDate"]) -> typing.Union[MetaOapg.properties.endDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstDayDuration"]) -> typing.Union[MetaOapg.properties.firstDayDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastDayDuration"]) -> typing.Union[MetaOapg.properties.lastDayDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requesterComments"]) -> typing.Union[MetaOapg.properties.requesterComments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rejectionReason"]) -> typing.Union[MetaOapg.properties.rejectionReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periodInHours"]) -> typing.Union[MetaOapg.properties.periodInHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["timeOffRequestId", "engagement", "startDate", "endDate", "firstDayDuration", "lastDayDuration", "state", "type", "requesterComments", "rejectionReason", "reason", "periodInHours", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        timeOffRequestId: typing.Union[MetaOapg.properties.timeOffRequestId, str, schemas.Unset] = schemas.unset,
        engagement: typing.Union['TimeOffEngagementDetails', schemas.Unset] = schemas.unset,
        startDate: typing.Union[MetaOapg.properties.startDate, str, date, schemas.Unset] = schemas.unset,
        endDate: typing.Union[MetaOapg.properties.endDate, str, date, schemas.Unset] = schemas.unset,
        firstDayDuration: typing.Union[MetaOapg.properties.firstDayDuration, str, schemas.Unset] = schemas.unset,
        lastDayDuration: typing.Union[MetaOapg.properties.lastDayDuration, None, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        requesterComments: typing.Union[MetaOapg.properties.requesterComments, None, str, schemas.Unset] = schemas.unset,
        rejectionReason: typing.Union[MetaOapg.properties.rejectionReason, None, str, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        periodInHours: typing.Union[MetaOapg.properties.periodInHours, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffRequest':
        return super().__new__(
            cls,
            *args,
            timeOffRequestId=timeOffRequestId,
            engagement=engagement,
            startDate=startDate,
            endDate=endDate,
            firstDayDuration=firstDayDuration,
            lastDayDuration=lastDayDuration,
            state=state,
            type=type,
            requesterComments=requesterComments,
            rejectionReason=rejectionReason,
            reason=reason,
            periodInHours=periodInHours,
            _configuration=_configuration,
            **kwargs,
        )

from oyster_python_sdk.model.time_off_engagement_details import TimeOffEngagementDetails
