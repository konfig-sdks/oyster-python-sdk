<div align="left">

[![Visit Oyster](./header.png)](https://oysterhr.com)

# Oyster<a id="oyster"></a>

Oyster uses OAuth2 to enable customers to grant access to their data to third party applications. Customers also need to use this API to authenticate themselves when making API requests.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`oyster.authentication.create_access_token`](#oysterauthenticationcreate_access_token)
  * [`oyster.company.details_retrieve`](#oystercompanydetails_retrieve)
  * [`oyster.departments.get_all`](#oysterdepartmentsget_all)
  * [`oyster.engagements.get_all`](#oysterengagementsget_all)
  * [`oyster.engagements.get_by_id`](#oysterengagementsget_by_id)
  * [`oyster.expenses.approve_expense`](#oysterexpensesapprove_expense)
  * [`oyster.expenses.create_operation_key`](#oysterexpensescreate_operation_key)
  * [`oyster.expenses.decline_expense`](#oysterexpensesdecline_expense)
  * [`oyster.expenses.get_by_id`](#oysterexpensesget_by_id)
  * [`oyster.operations.get_by_operation_key`](#oysteroperationsget_by_operation_key)
  * [`oyster.payroll.get_all_payrolls`](#oysterpayrollget_all_payrolls)
  * [`oyster.payroll.get_by_id`](#oysterpayrollget_by_id)
  * [`oyster.time_off.approve_request`](#oystertime_offapprove_request)
  * [`oyster.time_off.get_all_requests`](#oystertime_offget_all_requests)
  * [`oyster.time_off.get_entitlements`](#oystertime_offget_entitlements)
  * [`oyster.time_off.get_request`](#oystertime_offget_request)
  * [`oyster.time_off.reject_request`](#oystertime_offreject_request)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Oyster&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from oyster_python_sdk import Oyster, ApiException

oyster = Oyster()

try:
    # Create an access token
    create_access_token_response = oyster.authentication.create_access_token(
        client_id="1234ABCD",
        client_secret="1234ABCD",
        grant_type="authorization_code",
        code="1234ABCD",
        redirect_uri="https://example.com/inbound",
        refresh_token="https://example.com/inbound",
    )
    print(create_access_token_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi.create_access_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from oyster_python_sdk import Oyster, ApiException

oyster = Oyster()


async def main():
    try:
        # Create an access token
        create_access_token_response = await oyster.authentication.acreate_access_token(
            client_id="1234ABCD",
            client_secret="1234ABCD",
            grant_type="authorization_code",
            code="1234ABCD",
            redirect_uri="https://example.com/inbound",
            refresh_token="https://example.com/inbound",
        )
        print(create_access_token_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi.create_access_token: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from oyster_python_sdk import Oyster, ApiException

oyster = Oyster()

try:
    # Create an access token
    create_access_token_response = oyster.authentication.raw.create_access_token(
        client_id="1234ABCD",
        client_secret="1234ABCD",
        grant_type="authorization_code",
        code="1234ABCD",
        redirect_uri="https://example.com/inbound",
        refresh_token="https://example.com/inbound",
    )
    pprint(create_access_token_response.body)
    pprint(create_access_token_response.body["access_token"])
    pprint(create_access_token_response.body["token_type"])
    pprint(create_access_token_response.body["expires_in"])
    pprint(create_access_token_response.body["refresh_token"])
    pprint(create_access_token_response.body["scope"])
    pprint(create_access_token_response.body["created_at"])
    pprint(create_access_token_response.headers)
    pprint(create_access_token_response.status)
    pprint(create_access_token_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AuthenticationApi.create_access_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `oyster.authentication.create_access_token`<a id="oysterauthenticationcreate_access_token"></a>

Oyster grants access to API resources based on OAuth. This means that individual customers grant API access to Developer Apps that you create. This applies to both customers and partners. Follow these simple steps: <br><br> 1. [Create an Oyster account](https://app.oysterhr.com/sign_up) or [log in](https://app.oysterhr.com/users/sign_in) to your existing account. <br> <br> 2. Create an Oyster Developer App in the [Developer Tab](https://app.oysterhr.com/developer) (If you can't see the developer tab please contact us to enable it for your account). <br> Hint: If you are a customer doing this as a one time action you don't need to specify a functioning URL as step 3 will explain. <br> <br> 3. If you are a customer you can simply click on the "Authorization URL" and grant access to your own app. You will be redirected to the URL you specified when creating the Developer App. In the URL you will see that `?code=xxx` has been added to the URL. This is the `code` you need to create an access token. <br> If you are a partner add "Authorization URL to your application. The redirect_url should be a URL that goes back to your app and you're able to programmatically retrieve the URL query param of `?code=xxx` to then create an access token. <br> <br> 4. You need to first request an `authorization_code` with the API request detailed below. This will provide an `access_token` that is used as the Bearer Token for making API requests to Oyster. Ensure that you store the `refresh_token` for making future API requests. <br> <br> 5. If your `access_token` has expired then request a new one using your `refresh_token` that you have stored earlier. Ensure you store the new `refresh_token` each time as the previous ones will expire.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_access_token_response = oyster.authentication.create_access_token(
    client_id="1234ABCD",
    client_secret="1234ABCD",
    grant_type="authorization_code",
    code="1234ABCD",
    redirect_uri="https://example.com/inbound",
    refresh_token="https://example.com/inbound",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

The client_id of your Developer App. This can be found by visting https://app.oysterhr.com/developer

##### client_secret: `str`<a id="client_secret-str"></a>

The secret of your Developer App.

##### grant_type: `str`<a id="grant_type-str"></a>

First you need to request an `authorization_code`. Afterwards you can request a `refresh_token`.

##### code: `str`<a id="code-str"></a>

The code is required when requesting an `authorization_code`.

##### redirect_uri: `str`<a id="redirect_uri-str"></a>

The redirect_uri is required when requesting an `authorization_code`.

##### refresh_token: `str`<a id="refresh_token-str"></a>

A `refresh_token` is required when requesting a `refresh_token`. A `refresh_token` will be provided when requesting an `authorization_code`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationCreateAccessTokenRequest`](./oyster_python_sdk/type/authentication_create_access_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Token`](./oyster_python_sdk/pydantic/token.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/oauth2/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.company.details_retrieve`<a id="oystercompanydetails_retrieve"></a>

Returns details about the connected company

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
details_retrieve_response = oyster.company.details_retrieve()
```

#### 🔄 Return<a id="🔄-return"></a>

[`CompanyDetailsRetrieveResponse`](./oyster_python_sdk/pydantic/company_details_retrieve_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/company` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.departments.get_all`<a id="oysterdepartmentsget_all"></a>

Returns a list of departments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = oyster.departments.get_all(
    per_page=1,
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### page: `int`<a id="page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DepartmentsGetAllResponse`](./oyster_python_sdk/pydantic/departments_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.engagements.get_all`<a id="oysterengagementsget_all"></a>

Returns a list of engagements

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = oyster.engagements.get_all(
    per_page=1,
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### page: `int`<a id="page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EngagementsGetAllResponse`](./oyster_python_sdk/pydantic/engagements_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/engagements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.engagements.get_by_id`<a id="oysterengagementsget_by_id"></a>

Returns details for an engagement with a given engagement ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = oyster.engagements.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Engagement ID

#### 🔄 Return<a id="🔄-return"></a>

[`EngagementsGetByIdResponse`](./oyster_python_sdk/pydantic/engagements_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/engagements/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.expenses.approve_expense`<a id="oysterexpensesapprove_expense"></a>

Approves an expense.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
oyster.expenses.approve_expense(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Expense ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{id}/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.expenses.create_operation_key`<a id="oysterexpensescreate_operation_key"></a>

Creates a new expense for an engagement. This is an asynchronous operation. Returns operationKey that can be used to retrieve the operation to know if it's successfully completed

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_operation_key_response = oyster.expenses.create_operation_key(
    engagement_id="a",
    name="a",
    incurred_on="1970-01-01",
    category="a",
    receipt_url="a",
    receipt_amount={
        "decimal": "decimal_example",
        "currency_code": "currency_code_example",
    },
    description="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### engagement_id: `str`<a id="engagement_id-str"></a>

##### name: `str`<a id="name-str"></a>

##### incurred_on: `date`<a id="incurred_on-date"></a>

##### category: `str`<a id="category-str"></a>

##### receipt_url: `str`<a id="receipt_url-str"></a>

##### receipt_amount: [`ExpensesCreateOperationKeyRequestReceiptAmount`](./oyster_python_sdk/type/expenses_create_operation_key_request_receipt_amount.py)<a id="receipt_amount-expensescreateoperationkeyrequestreceiptamountoyster_python_sdktypeexpenses_create_operation_key_request_receipt_amountpy"></a>


##### description: `str`<a id="description-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpensesCreateOperationKeyRequest`](./oyster_python_sdk/type/expenses_create_operation_key_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AsyncResponse`](./oyster_python_sdk/pydantic/async_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.expenses.decline_expense`<a id="oysterexpensesdecline_expense"></a>

Declines an expense.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
oyster.expenses.decline_expense(
    id="id_example",
    reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Expense ID

##### reason: `str`<a id="reason-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExpensesDeclineExpenseRequest`](./oyster_python_sdk/type/expenses_decline_expense_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{id}/decline` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.expenses.get_by_id`<a id="oysterexpensesget_by_id"></a>

Returns details for an expense with a given expense ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = oyster.expenses.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Expense ID

#### 🔄 Return<a id="🔄-return"></a>

[`ExpensesGetByIdResponse`](./oyster_python_sdk/pydantic/expenses_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.operations.get_by_operation_key`<a id="oysteroperationsget_by_operation_key"></a>

Returns details for an operation with a given operation key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_operation_key_response = oyster.operations.get_by_operation_key(
    operation_key="operation_key_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### operation_key: `str`<a id="operation_key-str"></a>

Operation key

#### 🔄 Return<a id="🔄-return"></a>

[`OperationsGetByOperationKeyResponse`](./oyster_python_sdk/pydantic/operations_get_by_operation_key_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/meta/operations/{operation_key}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.payroll.get_all_payrolls`<a id="oysterpayrollget_all_payrolls"></a>

Returns a list of payrolls

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_payrolls_response = oyster.payroll.get_all_payrolls(
    per_page=1,
    page=1,
    _from="string_example",
    to="string_example",
    include_records=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### page: `int`<a id="page-int"></a>

##### _from: `str`<a id="_from-str"></a>

##### to: `str`<a id="to-str"></a>

##### include_records: `bool`<a id="include_records-bool"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollGetAllPayrollsResponse`](./oyster_python_sdk/pydantic/payroll_get_all_payrolls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.payroll.get_by_id`<a id="oysterpayrollget_by_id"></a>

Returns details for a payroll with a given payroll ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = oyster.payroll.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Payroll ID

#### 🔄 Return<a id="🔄-return"></a>

[`PayrollGetByIdResponse`](./oyster_python_sdk/pydantic/payroll_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/payroll/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.time_off.approve_request`<a id="oystertime_offapprove_request"></a>

Approves a time off request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
oyster.time_off.approve_request(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Time Off Request ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off/requests/{id}/approve` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.time_off.get_all_requests`<a id="oystertime_offget_all_requests"></a>

Returns all Time Off Requests for a company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_requests_response = oyster.time_off.get_all_requests(
    per_page=1,
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### page: `int`<a id="page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetAllRequestsResponse`](./oyster_python_sdk/pydantic/time_off_get_all_requests_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off/requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.time_off.get_entitlements`<a id="oystertime_offget_entitlements"></a>

Returns entitlements for each engagement of the company.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_entitlements_response = oyster.time_off.get_entitlements(
    per_page=1,
    page=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### per_page: `int`<a id="per_page-int"></a>

##### page: `int`<a id="page-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetEntitlementsResponse`](./oyster_python_sdk/pydantic/time_off_get_entitlements_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off/entitlements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.time_off.get_request`<a id="oystertime_offget_request"></a>

Returns details for a request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_request_response = oyster.time_off.get_request(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Time Off Request ID

#### 🔄 Return<a id="🔄-return"></a>

[`TimeOffGetRequestResponse`](./oyster_python_sdk/pydantic/time_off_get_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off/requests/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `oyster.time_off.reject_request`<a id="oystertime_offreject_request"></a>

Rejects a time off request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
oyster.time_off.reject_request(
    reason="string_example",
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reason: `str`<a id="reason-str"></a>

##### id: `str`<a id="id-str"></a>

Time Off Request ID

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TimeOffRejectRequestRequest`](./oyster_python_sdk/type/time_off_reject_request_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/time_off/requests/{id}/reject` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
