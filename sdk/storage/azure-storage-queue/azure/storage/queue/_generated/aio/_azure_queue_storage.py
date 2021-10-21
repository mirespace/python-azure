# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AzureQueueStorageConfiguration
from .operations import ServiceOperations
from .operations import QueueOperations
from .operations import MessagesOperations
from .operations import MessageIdOperations
from .. import models


class AzureQueueStorage(object):
    """AzureQueueStorage.

    :ivar service: ServiceOperations operations
    :vartype service: azure.storage.queue.aio.operations.ServiceOperations
    :ivar queue: QueueOperations operations
    :vartype queue: azure.storage.queue.aio.operations.QueueOperations
    :ivar messages: MessagesOperations operations
    :vartype messages: azure.storage.queue.aio.operations.MessagesOperations
    :ivar message_id: MessageIdOperations operations
    :vartype message_id: azure.storage.queue.aio.operations.MessageIdOperations
    :param url: The URL of the service account, queue or message that is the targe of the desired operation.
    :type url: str
    """

    def __init__(
        self,
        url: str,
        **kwargs: Any
    ) -> None:
        base_url = '{url}'
        self._config = AzureQueueStorageConfiguration(url, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.service = ServiceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queue = QueueOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.messages = MessagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.message_id = MessageIdOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureQueueStorage":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
