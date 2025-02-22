# coding: utf-8

"""
    Endpoints

    Oyster uses OAuth2 to enable customers to grant access to their data to third party applications. Customers also need to use this API to authenticate themselves when making API requests.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from oyster_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from oyster_python_sdk.api_response import AsyncGeneratorResponse
from oyster_python_sdk import api_client, exceptions
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

from oyster_python_sdk.model.async_response import AsyncResponse as AsyncResponseSchema
from oyster_python_sdk.model.error import Error as ErrorSchema
from oyster_python_sdk.model.expenses_create_operation_key_request_receipt_amount import ExpensesCreateOperationKeyRequestReceiptAmount as ExpensesCreateOperationKeyRequestReceiptAmountSchema
from oyster_python_sdk.model.expenses_create_operation_key_request import ExpensesCreateOperationKeyRequest as ExpensesCreateOperationKeyRequestSchema
from oyster_python_sdk.model.field_errors import FieldErrors as FieldErrorsSchema

from oyster_python_sdk.type.expenses_create_operation_key_request import ExpensesCreateOperationKeyRequest
from oyster_python_sdk.type.field_errors import FieldErrors
from oyster_python_sdk.type.async_response import AsyncResponse
from oyster_python_sdk.type.error import Error
from oyster_python_sdk.type.expenses_create_operation_key_request_receipt_amount import ExpensesCreateOperationKeyRequestReceiptAmount

from ...api_client import Dictionary
from oyster_python_sdk.pydantic.field_errors import FieldErrors as FieldErrorsPydantic
from oyster_python_sdk.pydantic.error import Error as ErrorPydantic
from oyster_python_sdk.pydantic.expenses_create_operation_key_request import ExpensesCreateOperationKeyRequest as ExpensesCreateOperationKeyRequestPydantic
from oyster_python_sdk.pydantic.expenses_create_operation_key_request_receipt_amount import ExpensesCreateOperationKeyRequestReceiptAmount as ExpensesCreateOperationKeyRequestReceiptAmountPydantic
from oyster_python_sdk.pydantic.async_response import AsyncResponse as AsyncResponsePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ExpensesCreateOperationKeyRequestSchema


request_body_expenses_create_operation_key_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'bearer_auth',
]
SchemaFor202ResponseBodyApplicationJson = AsyncResponseSchema


@dataclass
class ApiResponseFor202(api_client.ApiResponse):
    body: AsyncResponse


@dataclass
class ApiResponseFor202Async(api_client.AsyncApiResponse):
    body: AsyncResponse


_response_for_202 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor202,
    response_cls_async=ApiResponseFor202Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor202ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = FieldErrorsSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: FieldErrors


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: FieldErrors


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: Error


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = FieldErrorsSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: FieldErrors


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: FieldErrors


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '202': _response_for_202,
    '400': _response_for_400,
    '403': _response_for_403,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_operation_key_mapped_args(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if engagement_id is not None:
            _body["engagementId"] = engagement_id
        if name is not None:
            _body["name"] = name
        if incurred_on is not None:
            _body["incurredOn"] = incurred_on
        if category is not None:
            _body["category"] = category
        if receipt_url is not None:
            _body["receiptUrl"] = receipt_url
        if receipt_amount is not None:
            _body["receiptAmount"] = receipt_amount
        args.body = _body
        return args

    async def _acreate_operation_key_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create expense
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/expenses',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_expenses_create_operation_key_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_operation_key_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create expense
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/expenses',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_expenses_create_operation_key_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateOperationKeyRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_operation_key(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_operation_key_mapped_args(
            engagement_id=engagement_id,
            name=name,
            incurred_on=incurred_on,
            category=category,
            receipt_url=receipt_url,
            receipt_amount=receipt_amount,
            description=description,
        )
        return await self._acreate_operation_key_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_operation_key(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_operation_key_mapped_args(
            engagement_id=engagement_id,
            name=name,
            incurred_on=incurred_on,
            category=category,
            receipt_url=receipt_url,
            receipt_amount=receipt_amount,
            description=description,
        )
        return self._create_operation_key_oapg(
            body=args.body,
        )

class CreateOperationKey(BaseApi):

    async def acreate_operation_key(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AsyncResponsePydantic:
        raw_response = await self.raw.acreate_operation_key(
            engagement_id=engagement_id,
            name=name,
            incurred_on=incurred_on,
            category=category,
            receipt_url=receipt_url,
            receipt_amount=receipt_amount,
            description=description,
            **kwargs,
        )
        if validate:
            return AsyncResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AsyncResponsePydantic, raw_response.body)
    
    
    def create_operation_key(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AsyncResponsePydantic:
        raw_response = self.raw.create_operation_key(
            engagement_id=engagement_id,
            name=name,
            incurred_on=incurred_on,
            category=category,
            receipt_url=receipt_url,
            receipt_amount=receipt_amount,
            description=description,
        )
        if validate:
            return AsyncResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AsyncResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor202Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_operation_key_mapped_args(
            engagement_id=engagement_id,
            name=name,
            incurred_on=incurred_on,
            category=category,
            receipt_url=receipt_url,
            receipt_amount=receipt_amount,
            description=description,
        )
        return await self._acreate_operation_key_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        engagement_id: str,
        name: str,
        incurred_on: date,
        category: str,
        receipt_url: str,
        receipt_amount: ExpensesCreateOperationKeyRequestReceiptAmount,
        description: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor202,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_operation_key_mapped_args(
            engagement_id=engagement_id,
            name=name,
            incurred_on=incurred_on,
            category=category,
            receipt_url=receipt_url,
            receipt_amount=receipt_amount,
            description=description,
        )
        return self._create_operation_key_oapg(
            body=args.body,
        )

