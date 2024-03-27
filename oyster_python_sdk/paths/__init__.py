# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from oyster_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    OAUTH2_TOKEN = "/oauth2/token"
    V1_EXPENSES_ID_APPROVE = "/v1/expenses/{id}/approve"
    V1_EXPENSES_ID_DECLINE = "/v1/expenses/{id}/decline"
    V1_EXPENSES_ID = "/v1/expenses/{id}"
    V1_EXPENSES = "/v1/expenses"
    V1_COMPANY = "/v1/company"
    V1_DEPARTMENTS = "/v1/departments"
    V1_ENGAGEMENTS_ID = "/v1/engagements/{id}"
    V1_ENGAGEMENTS = "/v1/engagements"
    V1_META_OPERATIONS_OPERATION_KEY = "/v1/meta/operations/{operation_key}"
    V1_PAYROLL_ID = "/v1/payroll/{id}"
    V1_PAYROLL = "/v1/payroll"
    V1_TIME_OFF_ENTITLEMENTS = "/v1/time_off/entitlements"
    V1_TIME_OFF_REQUESTS_ID_APPROVE = "/v1/time_off/requests/{id}/approve"
    V1_TIME_OFF_REQUESTS_ID_REJECT = "/v1/time_off/requests/{id}/reject"
    V1_TIME_OFF_REQUESTS_ID = "/v1/time_off/requests/{id}"
    V1_TIME_OFF_REQUESTS = "/v1/time_off/requests"
