# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import ServiceBusManagementClientConfiguration
from .operations import NamespacesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import Operations
from .operations import DisasterRecoveryConfigsOperations
from .operations import MigrationConfigsOperations
from .operations import QueuesOperations
from .operations import TopicsOperations
from .operations import RulesOperations
from .operations import SubscriptionsOperations
from . import models


class ServiceBusManagementClient(object):
    """Azure Service Bus client for managing Namespace.

    :ivar namespaces: NamespacesOperations operations
    :vartype namespaces: azure.mgmt.servicebus.v2021_01_01_preview.operations.NamespacesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.servicebus.v2021_01_01_preview.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.servicebus.v2021_01_01_preview.operations.PrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.servicebus.v2021_01_01_preview.operations.Operations
    :ivar disaster_recovery_configs: DisasterRecoveryConfigsOperations operations
    :vartype disaster_recovery_configs: azure.mgmt.servicebus.v2021_01_01_preview.operations.DisasterRecoveryConfigsOperations
    :ivar migration_configs: MigrationConfigsOperations operations
    :vartype migration_configs: azure.mgmt.servicebus.v2021_01_01_preview.operations.MigrationConfigsOperations
    :ivar queues: QueuesOperations operations
    :vartype queues: azure.mgmt.servicebus.v2021_01_01_preview.operations.QueuesOperations
    :ivar topics: TopicsOperations operations
    :vartype topics: azure.mgmt.servicebus.v2021_01_01_preview.operations.TopicsOperations
    :ivar rules: RulesOperations operations
    :vartype rules: azure.mgmt.servicebus.v2021_01_01_preview.operations.RulesOperations
    :ivar subscriptions: SubscriptionsOperations operations
    :vartype subscriptions: azure.mgmt.servicebus.v2021_01_01_preview.operations.SubscriptionsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ServiceBusManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.namespaces = NamespacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disaster_recovery_configs = DisasterRecoveryConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.migration_configs = MigrationConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queues = QueuesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.topics = TopicsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.rules = RulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscriptions = SubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ServiceBusManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
