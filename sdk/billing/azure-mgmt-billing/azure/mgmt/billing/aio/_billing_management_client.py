# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import BillingManagementClientConfiguration
from .operations import BillingAccountsOperations
from .operations import AddressOperations
from .operations import AvailableBalancesOperations
from .operations import InstructionsOperations
from .operations import BillingProfilesOperations
from .operations import CustomersOperations
from .operations import InvoiceSectionsOperations
from .operations import BillingPermissionsOperations
from .operations import BillingSubscriptionsOperations
from .operations import ProductsOperations
from .operations import InvoicesOperations
from .operations import TransactionsOperations
from .operations import PoliciesOperations
from .operations import BillingPropertyOperations
from .operations import Operations
from .operations import BillingRoleDefinitionsOperations
from .operations import BillingRoleAssignmentsOperations
from .operations import AgreementsOperations
from .operations import ReservationsOperations
from .operations import EnrollmentAccountsOperations
from .operations import BillingPeriodsOperations
from .. import models


class BillingManagementClient(object):
    """Billing client provides access to billing resources for Azure subscriptions.

    :ivar billing_accounts: BillingAccountsOperations operations
    :vartype billing_accounts: azure.mgmt.billing.aio.operations.BillingAccountsOperations
    :ivar address: AddressOperations operations
    :vartype address: azure.mgmt.billing.aio.operations.AddressOperations
    :ivar available_balances: AvailableBalancesOperations operations
    :vartype available_balances: azure.mgmt.billing.aio.operations.AvailableBalancesOperations
    :ivar instructions: InstructionsOperations operations
    :vartype instructions: azure.mgmt.billing.aio.operations.InstructionsOperations
    :ivar billing_profiles: BillingProfilesOperations operations
    :vartype billing_profiles: azure.mgmt.billing.aio.operations.BillingProfilesOperations
    :ivar customers: CustomersOperations operations
    :vartype customers: azure.mgmt.billing.aio.operations.CustomersOperations
    :ivar invoice_sections: InvoiceSectionsOperations operations
    :vartype invoice_sections: azure.mgmt.billing.aio.operations.InvoiceSectionsOperations
    :ivar billing_permissions: BillingPermissionsOperations operations
    :vartype billing_permissions: azure.mgmt.billing.aio.operations.BillingPermissionsOperations
    :ivar billing_subscriptions: BillingSubscriptionsOperations operations
    :vartype billing_subscriptions: azure.mgmt.billing.aio.operations.BillingSubscriptionsOperations
    :ivar products: ProductsOperations operations
    :vartype products: azure.mgmt.billing.aio.operations.ProductsOperations
    :ivar invoices: InvoicesOperations operations
    :vartype invoices: azure.mgmt.billing.aio.operations.InvoicesOperations
    :ivar transactions: TransactionsOperations operations
    :vartype transactions: azure.mgmt.billing.aio.operations.TransactionsOperations
    :ivar policies: PoliciesOperations operations
    :vartype policies: azure.mgmt.billing.aio.operations.PoliciesOperations
    :ivar billing_property: BillingPropertyOperations operations
    :vartype billing_property: azure.mgmt.billing.aio.operations.BillingPropertyOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.billing.aio.operations.Operations
    :ivar billing_role_definitions: BillingRoleDefinitionsOperations operations
    :vartype billing_role_definitions: azure.mgmt.billing.aio.operations.BillingRoleDefinitionsOperations
    :ivar billing_role_assignments: BillingRoleAssignmentsOperations operations
    :vartype billing_role_assignments: azure.mgmt.billing.aio.operations.BillingRoleAssignmentsOperations
    :ivar agreements: AgreementsOperations operations
    :vartype agreements: azure.mgmt.billing.aio.operations.AgreementsOperations
    :ivar reservations: ReservationsOperations operations
    :vartype reservations: azure.mgmt.billing.aio.operations.ReservationsOperations
    :ivar enrollment_accounts: EnrollmentAccountsOperations operations
    :vartype enrollment_accounts: azure.mgmt.billing.aio.operations.EnrollmentAccountsOperations
    :ivar billing_periods: BillingPeriodsOperations operations
    :vartype billing_periods: azure.mgmt.billing.aio.operations.BillingPeriodsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID that uniquely identifies an Azure subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = BillingManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.billing_accounts = BillingAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.address = AddressOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.available_balances = AvailableBalancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.instructions = InstructionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_profiles = BillingProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.customers = CustomersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invoice_sections = InvoiceSectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_permissions = BillingPermissionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_subscriptions = BillingSubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.products = ProductsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invoices = InvoicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.transactions = TransactionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_property = BillingPropertyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_role_definitions = BillingRoleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_role_assignments = BillingRoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.agreements = AgreementsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.reservations = ReservationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.enrollment_accounts = EnrollmentAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_periods = BillingPeriodsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "BillingManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
