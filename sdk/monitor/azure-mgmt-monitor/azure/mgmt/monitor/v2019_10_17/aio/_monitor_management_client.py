# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import MonitorManagementClientConfiguration
from .operations import PrivateLinkScopesOperations
from .operations import PrivateLinkScopeOperationStatusOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkScopedResourcesOperations
from .. import models


class MonitorManagementClient(object):
    """Monitor Management Client.

    :ivar private_link_scopes: PrivateLinkScopesOperations operations
    :vartype private_link_scopes: $(python-base-namespace).v2019_10_17.aio.operations.PrivateLinkScopesOperations
    :ivar private_link_scope_operation_status: PrivateLinkScopeOperationStatusOperations operations
    :vartype private_link_scope_operation_status: $(python-base-namespace).v2019_10_17.aio.operations.PrivateLinkScopeOperationStatusOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: $(python-base-namespace).v2019_10_17.aio.operations.PrivateLinkResourcesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: $(python-base-namespace).v2019_10_17.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_scoped_resources: PrivateLinkScopedResourcesOperations operations
    :vartype private_link_scoped_resources: $(python-base-namespace).v2019_10_17.aio.operations.PrivateLinkScopedResourcesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Azure subscription Id.
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
        self._config = MonitorManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.private_link_scopes = PrivateLinkScopesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_scope_operation_status = PrivateLinkScopeOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_scoped_resources = PrivateLinkScopedResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "MonitorManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
