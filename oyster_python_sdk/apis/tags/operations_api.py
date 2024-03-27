# coding: utf-8

"""
    Endpoints

    Oyster uses OAuth2 to enable customers to grant access to their data to third party applications. Customers also need to use this API to authenticate themselves when making API requests.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from oyster_python_sdk.paths.v1_meta_operations_operation_key.get import GetByOperationKey
from oyster_python_sdk.apis.tags.operations_api_raw import OperationsApiRaw


class OperationsApi(
    GetByOperationKey,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: OperationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = OperationsApiRaw(api_client)
