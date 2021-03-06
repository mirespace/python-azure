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

from ._configuration import WebPubSubManagementClientConfiguration
from .operations import Operations
from .operations import WebPubSubOperations
from .operations import UsagesOperations
from .operations import WebPubSubHubsOperations
from .operations import WebPubSubPrivateEndpointConnectionsOperations
from .operations import WebPubSubPrivateLinkResourcesOperations
from .operations import WebPubSubSharedPrivateLinkResourcesOperations
from .. import models


class WebPubSubManagementClient(object):
    """REST API for Azure WebPubSub Service.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.webpubsub.aio.operations.Operations
    :ivar web_pub_sub: WebPubSubOperations operations
    :vartype web_pub_sub: azure.mgmt.webpubsub.aio.operations.WebPubSubOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.webpubsub.aio.operations.UsagesOperations
    :ivar web_pub_sub_hubs: WebPubSubHubsOperations operations
    :vartype web_pub_sub_hubs: azure.mgmt.webpubsub.aio.operations.WebPubSubHubsOperations
    :ivar web_pub_sub_private_endpoint_connections: WebPubSubPrivateEndpointConnectionsOperations operations
    :vartype web_pub_sub_private_endpoint_connections: azure.mgmt.webpubsub.aio.operations.WebPubSubPrivateEndpointConnectionsOperations
    :ivar web_pub_sub_private_link_resources: WebPubSubPrivateLinkResourcesOperations operations
    :vartype web_pub_sub_private_link_resources: azure.mgmt.webpubsub.aio.operations.WebPubSubPrivateLinkResourcesOperations
    :ivar web_pub_sub_shared_private_link_resources: WebPubSubSharedPrivateLinkResourcesOperations operations
    :vartype web_pub_sub_shared_private_link_resources: azure.mgmt.webpubsub.aio.operations.WebPubSubSharedPrivateLinkResourcesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
        self._config = WebPubSubManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub = WebPubSubOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_hubs = WebPubSubHubsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_private_endpoint_connections = WebPubSubPrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_private_link_resources = WebPubSubPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.web_pub_sub_shared_private_link_resources = WebPubSubSharedPrivateLinkResourcesOperations(
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

    async def __aenter__(self) -> "WebPubSubManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
