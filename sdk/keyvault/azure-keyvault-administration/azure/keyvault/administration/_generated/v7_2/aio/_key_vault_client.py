# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

from ._configuration import KeyVaultClientConfiguration
from .operations import RoleDefinitionsOperations
from .operations import RoleAssignmentsOperations
from .operations import KeyVaultClientOperationsMixin
from .. import models


class KeyVaultClient(KeyVaultClientOperationsMixin):
    """The key vault client performs cryptographic key operations and vault operations against the Key Vault service.

    :ivar role_definitions: RoleDefinitionsOperations operations
    :vartype role_definitions: azure.keyvault.v7_2.aio.operations.RoleDefinitionsOperations
    :ivar role_assignments: RoleAssignmentsOperations operations
    :vartype role_assignments: azure.keyvault.v7_2.aio.operations.RoleAssignmentsOperations
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        **kwargs: Any
    ) -> None:
        base_url = '{vaultBaseUrl}'
        self._config = KeyVaultClientConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.role_definitions = RoleDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_assignments = RoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        http_request.url = self._client.format_url(http_request.url)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "KeyVaultClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
