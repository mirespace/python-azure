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

from ._configuration import PrivateDnsManagementClientConfiguration
from .operations import PrivateZonesOperations
from .operations import VirtualNetworkLinksOperations
from .operations import RecordSetsOperations
from . import models


class PrivateDnsManagementClient(object):
    """The Private DNS Management Client.

    :ivar private_zones: PrivateZonesOperations operations
    :vartype private_zones: azure.mgmt.privatedns.operations.PrivateZonesOperations
    :ivar virtual_network_links: VirtualNetworkLinksOperations operations
    :vartype virtual_network_links: azure.mgmt.privatedns.operations.VirtualNetworkLinksOperations
    :ivar record_sets: RecordSetsOperations operations
    :vartype record_sets: azure.mgmt.privatedns.operations.RecordSetsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
        self._config = PrivateDnsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.private_zones = PrivateZonesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_links = VirtualNetworkLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.record_sets = RecordSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> PrivateDnsManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
