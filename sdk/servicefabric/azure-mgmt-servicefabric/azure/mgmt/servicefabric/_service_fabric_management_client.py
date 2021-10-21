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

from ._configuration import ServiceFabricManagementClientConfiguration
from .operations import ClustersOperations
from .operations import ClusterVersionsOperations
from .operations import Operations
from .operations import ApplicationTypesOperations
from .operations import ApplicationTypeVersionsOperations
from .operations import ApplicationsOperations
from .operations import ServicesOperations
from . import models


class ServiceFabricManagementClient(object):
    """Service Fabric Management Client.

    :ivar clusters: ClustersOperations operations
    :vartype clusters: azure.mgmt.servicefabric.operations.ClustersOperations
    :ivar cluster_versions: ClusterVersionsOperations operations
    :vartype cluster_versions: azure.mgmt.servicefabric.operations.ClusterVersionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.servicefabric.operations.Operations
    :ivar application_types: ApplicationTypesOperations operations
    :vartype application_types: azure.mgmt.servicefabric.operations.ApplicationTypesOperations
    :ivar application_type_versions: ApplicationTypeVersionsOperations operations
    :vartype application_type_versions: azure.mgmt.servicefabric.operations.ApplicationTypeVersionsOperations
    :ivar applications: ApplicationsOperations operations
    :vartype applications: azure.mgmt.servicefabric.operations.ApplicationsOperations
    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.servicefabric.operations.ServicesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The customer subscription identifier.
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
        self._config = ServiceFabricManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.clusters = ClustersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cluster_versions = ClusterVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_types = ApplicationTypesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_type_versions = ApplicationTypeVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.applications = ApplicationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.services = ServicesOperations(
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
        # type: () -> ServiceFabricManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
