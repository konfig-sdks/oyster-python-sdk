# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from oyster_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TIME_OFF = "Time Off"
    EXPENSES = "Expenses"
    ENGAGEMENTS = "Engagements"
    PAYROLL = "Payroll"
    AUTHENTICATION = "Authentication"
    COMPANY = "Company"
    DEPARTMENTS = "Departments"
    OPERATIONS = "Operations"
