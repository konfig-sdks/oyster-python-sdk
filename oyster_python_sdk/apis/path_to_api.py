import typing_extensions

from oyster_python_sdk.paths import PathValues
from oyster_python_sdk.apis.paths.oauth2_token import Oauth2Token
from oyster_python_sdk.apis.paths.v1_expenses_id_approve import V1ExpensesIdApprove
from oyster_python_sdk.apis.paths.v1_expenses_id_decline import V1ExpensesIdDecline
from oyster_python_sdk.apis.paths.v1_expenses_id import V1ExpensesId
from oyster_python_sdk.apis.paths.v1_expenses import V1Expenses
from oyster_python_sdk.apis.paths.v1_company import V1Company
from oyster_python_sdk.apis.paths.v1_departments import V1Departments
from oyster_python_sdk.apis.paths.v1_engagements_id import V1EngagementsId
from oyster_python_sdk.apis.paths.v1_engagements import V1Engagements
from oyster_python_sdk.apis.paths.v1_meta_operations_operation_key import V1MetaOperationsOperationKey
from oyster_python_sdk.apis.paths.v1_payroll_id import V1PayrollId
from oyster_python_sdk.apis.paths.v1_payroll import V1Payroll
from oyster_python_sdk.apis.paths.v1_time_off_entitlements import V1TimeOffEntitlements
from oyster_python_sdk.apis.paths.v1_time_off_requests_id_approve import V1TimeOffRequestsIdApprove
from oyster_python_sdk.apis.paths.v1_time_off_requests_id_reject import V1TimeOffRequestsIdReject
from oyster_python_sdk.apis.paths.v1_time_off_requests_id import V1TimeOffRequestsId
from oyster_python_sdk.apis.paths.v1_time_off_requests import V1TimeOffRequests

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.V1_EXPENSES_ID_APPROVE: V1ExpensesIdApprove,
        PathValues.V1_EXPENSES_ID_DECLINE: V1ExpensesIdDecline,
        PathValues.V1_EXPENSES_ID: V1ExpensesId,
        PathValues.V1_EXPENSES: V1Expenses,
        PathValues.V1_COMPANY: V1Company,
        PathValues.V1_DEPARTMENTS: V1Departments,
        PathValues.V1_ENGAGEMENTS_ID: V1EngagementsId,
        PathValues.V1_ENGAGEMENTS: V1Engagements,
        PathValues.V1_META_OPERATIONS_OPERATION_KEY: V1MetaOperationsOperationKey,
        PathValues.V1_PAYROLL_ID: V1PayrollId,
        PathValues.V1_PAYROLL: V1Payroll,
        PathValues.V1_TIME_OFF_ENTITLEMENTS: V1TimeOffEntitlements,
        PathValues.V1_TIME_OFF_REQUESTS_ID_APPROVE: V1TimeOffRequestsIdApprove,
        PathValues.V1_TIME_OFF_REQUESTS_ID_REJECT: V1TimeOffRequestsIdReject,
        PathValues.V1_TIME_OFF_REQUESTS_ID: V1TimeOffRequestsId,
        PathValues.V1_TIME_OFF_REQUESTS: V1TimeOffRequests,
    }
)

path_to_api = PathToApi(
    {
        PathValues.OAUTH2_TOKEN: Oauth2Token,
        PathValues.V1_EXPENSES_ID_APPROVE: V1ExpensesIdApprove,
        PathValues.V1_EXPENSES_ID_DECLINE: V1ExpensesIdDecline,
        PathValues.V1_EXPENSES_ID: V1ExpensesId,
        PathValues.V1_EXPENSES: V1Expenses,
        PathValues.V1_COMPANY: V1Company,
        PathValues.V1_DEPARTMENTS: V1Departments,
        PathValues.V1_ENGAGEMENTS_ID: V1EngagementsId,
        PathValues.V1_ENGAGEMENTS: V1Engagements,
        PathValues.V1_META_OPERATIONS_OPERATION_KEY: V1MetaOperationsOperationKey,
        PathValues.V1_PAYROLL_ID: V1PayrollId,
        PathValues.V1_PAYROLL: V1Payroll,
        PathValues.V1_TIME_OFF_ENTITLEMENTS: V1TimeOffEntitlements,
        PathValues.V1_TIME_OFF_REQUESTS_ID_APPROVE: V1TimeOffRequestsIdApprove,
        PathValues.V1_TIME_OFF_REQUESTS_ID_REJECT: V1TimeOffRequestsIdReject,
        PathValues.V1_TIME_OFF_REQUESTS_ID: V1TimeOffRequestsId,
        PathValues.V1_TIME_OFF_REQUESTS: V1TimeOffRequests,
    }
)
