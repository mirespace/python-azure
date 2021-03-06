# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, Optional

import msrest.serialization


class CloudEvent(msrest.serialization.Model):
    """Properties of an event published to an Event Grid topic using the CloudEvent 1.0 Schema.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param id: Required. An identifier for the event. The combination of id and source must be
     unique for each distinct event.
    :type id: str
    :param source: Required. Identifies the context in which an event happened. The combination of
     id and source must be unique for each distinct event.
    :type source: str
    :param data: Event data specific to the event type.
    :type data: object
    :param data_base64: Event data specific to the event type, encoded as a base64 string.
    :type data_base64: bytearray
    :param type: Required. Type of event related to the originating occurrence.
    :type type: str
    :param time: The time (in UTC) the event was generated, in RFC3339 format.
    :type time: ~datetime.datetime
    :param specversion: Required. The version of the CloudEvents specification which the event
     uses.
    :type specversion: str
    :param dataschema: Identifies the schema that data adheres to.
    :type dataschema: str
    :param datacontenttype: Content type of data value.
    :type datacontenttype: str
    :param subject: This describes the subject of the event in the context of the event producer
     (identified by source).
    :type subject: str
    """

    _validation = {
        'id': {'required': True},
        'source': {'required': True},
        'type': {'required': True},
        'specversion': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'data_base64': {'key': 'data_base64', 'type': 'bytearray'},
        'type': {'key': 'type', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
        'specversion': {'key': 'specversion', 'type': 'str'},
        'dataschema': {'key': 'dataschema', 'type': 'str'},
        'datacontenttype': {'key': 'datacontenttype', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: str,
        source: str,
        type: str,
        specversion: str,
        additional_properties: Optional[Dict[str, object]] = None,
        data: Optional[object] = None,
        data_base64: Optional[bytearray] = None,
        time: Optional[datetime.datetime] = None,
        dataschema: Optional[str] = None,
        datacontenttype: Optional[str] = None,
        subject: Optional[str] = None,
        **kwargs
    ):
        super(CloudEvent, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.source = source
        self.data = data
        self.data_base64 = data_base64
        self.type = type
        self.time = time
        self.specversion = specversion
        self.dataschema = dataschema
        self.datacontenttype = datacontenttype
        self.subject = subject


class EventGridEvent(msrest.serialization.Model):
    """Properties of an event published to an Event Grid topic using the EventGrid Schema.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. An unique identifier for the event.
    :type id: str
    :param topic: The resource path of the event source.
    :type topic: str
    :param subject: Required. A resource path relative to the topic path.
    :type subject: str
    :param data: Required. Event data specific to the event type.
    :type data: object
    :param event_type: Required. The type of the event that occurred.
    :type event_type: str
    :param event_time: Required. The time (in UTC) the event was generated.
    :type event_time: ~datetime.datetime
    :ivar metadata_version: The schema version of the event metadata.
    :vartype metadata_version: str
    :param data_version: Required. The schema version of the data object.
    :type data_version: str
    """

    _validation = {
        'id': {'required': True},
        'subject': {'required': True},
        'data': {'required': True},
        'event_type': {'required': True},
        'event_time': {'required': True},
        'metadata_version': {'readonly': True},
        'data_version': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'topic': {'key': 'topic', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'event_time': {'key': 'eventTime', 'type': 'iso-8601'},
        'metadata_version': {'key': 'metadataVersion', 'type': 'str'},
        'data_version': {'key': 'dataVersion', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: str,
        subject: str,
        data: object,
        event_type: str,
        event_time: datetime.datetime,
        data_version: str,
        topic: Optional[str] = None,
        **kwargs
    ):
        super(EventGridEvent, self).__init__(**kwargs)
        self.id = id
        self.topic = topic
        self.subject = subject
        self.data = data
        self.event_type = event_type
        self.event_time = event_time
        self.metadata_version = None
        self.data_version = data_version
