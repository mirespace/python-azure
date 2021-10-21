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

from ._configuration import MixedRealityClientConfiguration
from .operations import Operations
from .operations import MixedRealityClientOperationsMixin
from .operations import SpatialAnchorsAccountsOperations
from .operations import RemoteRenderingAccountsOperations
from .operations import ObjectAnchorsAccountsOperations
from . import models


class MixedRealityClient(MixedRealityClientOperationsMixin):
    """Mixed Reality Client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.mixedreality.operations.Operations
    :ivar spatial_anchors_accounts: SpatialAnchorsAccountsOperations operations
    :vartype spatial_anchors_accounts: azure.mgmt.mixedreality.operations.SpatialAnchorsAccountsOperations
    :ivar remote_rendering_accounts: RemoteRenderingAccountsOperations operations
    :vartype remote_rendering_accounts: azure.mgmt.mixedreality.operations.RemoteRenderingAccountsOperations
    :ivar object_anchors_accounts: ObjectAnchorsAccountsOperations operations
    :vartype object_anchors_accounts: azure.mgmt.mixedreality.operations.ObjectAnchorsAccountsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
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
        self._config = MixedRealityClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spatial_anchors_accounts = SpatialAnchorsAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.remote_rendering_accounts = RemoteRenderingAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.object_anchors_accounts = ObjectAnchorsAccountsOperations(
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
        # type: () -> MixedRealityClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
