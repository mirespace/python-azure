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

from ._configuration import BatchManagementClientConfiguration
from .operations import BatchAccountOperations
from .operations import ApplicationPackageOperations
from .operations import ApplicationOperations
from .operations import LocationOperations
from .operations import Operations
from .operations import CertificateOperations
from .operations import PrivateLinkResourceOperations
from .operations import PrivateEndpointConnectionOperations
from .operations import PoolOperations
from .. import models


class BatchManagementClient(object):
    """Batch Client.

    :ivar batch_account: BatchAccountOperations operations
    :vartype batch_account: azure.mgmt.batch.aio.operations.BatchAccountOperations
    :ivar application_package: ApplicationPackageOperations operations
    :vartype application_package: azure.mgmt.batch.aio.operations.ApplicationPackageOperations
    :ivar application: ApplicationOperations operations
    :vartype application: azure.mgmt.batch.aio.operations.ApplicationOperations
    :ivar location: LocationOperations operations
    :vartype location: azure.mgmt.batch.aio.operations.LocationOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.batch.aio.operations.Operations
    :ivar certificate: CertificateOperations operations
    :vartype certificate: azure.mgmt.batch.aio.operations.CertificateOperations
    :ivar private_link_resource: PrivateLinkResourceOperations operations
    :vartype private_link_resource: azure.mgmt.batch.aio.operations.PrivateLinkResourceOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection: azure.mgmt.batch.aio.operations.PrivateEndpointConnectionOperations
    :ivar pool: PoolOperations operations
    :vartype pool: azure.mgmt.batch.aio.operations.PoolOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
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
        self._config = BatchManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.batch_account = BatchAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_package = ApplicationPackageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application = ApplicationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location = LocationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.certificate = CertificateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resource = PrivateLinkResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connection = PrivateEndpointConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pool = PoolOperations(
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

    async def __aenter__(self) -> "BatchManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
