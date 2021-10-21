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

from ._configuration import ResourceManagementClientConfiguration
from .operations import Operations
from .operations import DeploymentsOperations
from .operations import ProvidersOperations
from .operations import ResourcesOperations
from .operations import ResourceGroupsOperations
from .operations import TagsOperations
from .operations import DeploymentOperationsOperations
from . import models


class ResourceManagementClient(object):
    """Provides operations for working with resources and resource groups.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resource.resources.v2020_06_01.operations.Operations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments: azure.mgmt.resource.resources.v2020_06_01.operations.DeploymentsOperations
    :ivar providers: ProvidersOperations operations
    :vartype providers: azure.mgmt.resource.resources.v2020_06_01.operations.ProvidersOperations
    :ivar resources: ResourcesOperations operations
    :vartype resources: azure.mgmt.resource.resources.v2020_06_01.operations.ResourcesOperations
    :ivar resource_groups: ResourceGroupsOperations operations
    :vartype resource_groups: azure.mgmt.resource.resources.v2020_06_01.operations.ResourceGroupsOperations
    :ivar tags: TagsOperations operations
    :vartype tags: azure.mgmt.resource.resources.v2020_06_01.operations.TagsOperations
    :ivar deployment_operations: DeploymentOperationsOperations operations
    :vartype deployment_operations: azure.mgmt.resource.resources.v2020_06_01.operations.DeploymentOperationsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
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
        self._config = ResourceManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deployments = DeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.providers = ProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resources = ResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_groups = ResourceGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tags = TagsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.deployment_operations = DeploymentOperationsOperations(
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
        # type: () -> ResourceManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
