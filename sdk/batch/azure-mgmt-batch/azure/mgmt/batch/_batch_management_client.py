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
from . import models


class BatchManagementClient(object):
    """Batch Client.

    :ivar batch_account: BatchAccountOperations operations
    :vartype batch_account: azure.mgmt.batch.operations.BatchAccountOperations
    :ivar application_package: ApplicationPackageOperations operations
    :vartype application_package: azure.mgmt.batch.operations.ApplicationPackageOperations
    :ivar application: ApplicationOperations operations
    :vartype application: azure.mgmt.batch.operations.ApplicationOperations
    :ivar location: LocationOperations operations
    :vartype location: azure.mgmt.batch.operations.LocationOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.batch.operations.Operations
    :ivar certificate: CertificateOperations operations
    :vartype certificate: azure.mgmt.batch.operations.CertificateOperations
    :ivar private_link_resource: PrivateLinkResourceOperations operations
    :vartype private_link_resource: azure.mgmt.batch.operations.PrivateLinkResourceOperations
    :ivar private_endpoint_connection: PrivateEndpointConnectionOperations operations
    :vartype private_endpoint_connection: azure.mgmt.batch.operations.PrivateEndpointConnectionOperations
    :ivar pool: PoolOperations operations
    :vartype pool: azure.mgmt.batch.operations.PoolOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
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
        self._config = BatchManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

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
        # type: () -> BatchManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
