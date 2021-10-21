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

from ._configuration import HybridNetworkManagementClientConfiguration
from .operations import NetworkFunctionsOperations
from .operations import DevicesOperations
from .operations import Operations
from .operations import VendorsOperations
from .operations import VendorSkusOperations
from .operations import VendorSkuPreviewOperations
from .operations import NetworkFunctionVendorsOperations
from .operations import NetworkFunctionVendorSkusOperations
from .operations import VendorNetworkFunctionsOperations
from .operations import RoleInstancesOperations
from .. import models


class HybridNetworkManagementClient(object):
    """The definitions in this swagger specification will be used to manage the Hybrid Network resources.

    :ivar network_functions: NetworkFunctionsOperations operations
    :vartype network_functions: hybrid_network_management_client.aio.operations.NetworkFunctionsOperations
    :ivar devices: DevicesOperations operations
    :vartype devices: hybrid_network_management_client.aio.operations.DevicesOperations
    :ivar operations: Operations operations
    :vartype operations: hybrid_network_management_client.aio.operations.Operations
    :ivar vendors: VendorsOperations operations
    :vartype vendors: hybrid_network_management_client.aio.operations.VendorsOperations
    :ivar vendor_skus: VendorSkusOperations operations
    :vartype vendor_skus: hybrid_network_management_client.aio.operations.VendorSkusOperations
    :ivar vendor_sku_preview: VendorSkuPreviewOperations operations
    :vartype vendor_sku_preview: hybrid_network_management_client.aio.operations.VendorSkuPreviewOperations
    :ivar network_function_vendors: NetworkFunctionVendorsOperations operations
    :vartype network_function_vendors: hybrid_network_management_client.aio.operations.NetworkFunctionVendorsOperations
    :ivar network_function_vendor_skus: NetworkFunctionVendorSkusOperations operations
    :vartype network_function_vendor_skus: hybrid_network_management_client.aio.operations.NetworkFunctionVendorSkusOperations
    :ivar vendor_network_functions: VendorNetworkFunctionsOperations operations
    :vartype vendor_network_functions: hybrid_network_management_client.aio.operations.VendorNetworkFunctionsOperations
    :ivar role_instances: RoleInstancesOperations operations
    :vartype role_instances: hybrid_network_management_client.aio.operations.RoleInstancesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
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
        self._config = HybridNetworkManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.network_functions = NetworkFunctionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vendors = VendorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vendor_skus = VendorSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vendor_sku_preview = VendorSkuPreviewOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_function_vendors = NetworkFunctionVendorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_function_vendor_skus = NetworkFunctionVendorSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.vendor_network_functions = VendorNetworkFunctionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_instances = RoleInstancesOperations(
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
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "HybridNetworkManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
