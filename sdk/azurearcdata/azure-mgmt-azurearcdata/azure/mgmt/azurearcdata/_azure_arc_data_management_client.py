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

from ._configuration import AzureArcDataManagementClientConfiguration
from .operations import Operations
from .operations import SqlManagedInstancesOperations
from .operations import SqlServerInstancesOperations
from .operations import DataControllersOperations
from . import models


class AzureArcDataManagementClient(object):
    """The AzureArcData management API provides a RESTful set of web APIs to manage Azure Data Services on Azure Arc Resources.

    :ivar operations: Operations operations
    :vartype operations: azure_arc_data_management_client.operations.Operations
    :ivar sql_managed_instances: SqlManagedInstancesOperations operations
    :vartype sql_managed_instances: azure_arc_data_management_client.operations.SqlManagedInstancesOperations
    :ivar sql_server_instances: SqlServerInstancesOperations operations
    :vartype sql_server_instances: azure_arc_data_management_client.operations.SqlServerInstancesOperations
    :ivar data_controllers: DataControllersOperations operations
    :vartype data_controllers: azure_arc_data_management_client.operations.DataControllersOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the Azure subscription.
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
        self._config = AzureArcDataManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_managed_instances = SqlManagedInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_server_instances = SqlServerInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_controllers = DataControllersOperations(
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
        # type: () -> AzureArcDataManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
