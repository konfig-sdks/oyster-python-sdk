import typing_extensions

from oyster_python_sdk.apis.tags import TagValues
from oyster_python_sdk.apis.tags.time_off_api import TimeOffApi
from oyster_python_sdk.apis.tags.expenses_api import ExpensesApi
from oyster_python_sdk.apis.tags.engagements_api import EngagementsApi
from oyster_python_sdk.apis.tags.payroll_api import PayrollApi
from oyster_python_sdk.apis.tags.authentication_api import AuthenticationApi
from oyster_python_sdk.apis.tags.company_api import CompanyApi
from oyster_python_sdk.apis.tags.departments_api import DepartmentsApi
from oyster_python_sdk.apis.tags.operations_api import OperationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.EXPENSES: ExpensesApi,
        TagValues.ENGAGEMENTS: EngagementsApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.OPERATIONS: OperationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.EXPENSES: ExpensesApi,
        TagValues.ENGAGEMENTS: EngagementsApi,
        TagValues.PAYROLL: PayrollApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.COMPANY: CompanyApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.OPERATIONS: OperationsApi,
    }
)
