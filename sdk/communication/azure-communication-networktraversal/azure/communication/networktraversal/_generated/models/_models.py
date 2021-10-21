# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CommunicationError(msrest.serialization.Model):
    """The Communication Services error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar code: Required. The error code.
    :vartype code: str
    :ivar message: Required. The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: Further details about specific errors that led to this error.
    :vartype details: list[~azure.communication.networktraversal.models.CommunicationError]
    :ivar inner_error: The inner error if any.
    :vartype inner_error: ~azure.communication.networktraversal.models.CommunicationError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CommunicationError]'},
        'inner_error': {'key': 'innererror', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword code: Required. The error code.
        :paramtype code: str
        :keyword message: Required. The error message.
        :paramtype message: str
        """
        super(CommunicationError, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = None
        self.details = None
        self.inner_error = None


class CommunicationErrorResponse(msrest.serialization.Model):
    """The Communication Services error.

    All required parameters must be populated in order to send to Azure.

    :ivar error: Required. The Communication Services error.
    :vartype error: ~azure.communication.networktraversal.models.CommunicationError
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'CommunicationError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword error: Required. The Communication Services error.
        :paramtype error: ~azure.communication.networktraversal.models.CommunicationError
        """
        super(CommunicationErrorResponse, self).__init__(**kwargs)
        self.error = kwargs['error']


class CommunicationIceServer(msrest.serialization.Model):
    """An instance of a STUN/TURN server with credentials to be used for ICE negotiation.

    All required parameters must be populated in order to send to Azure.

    :ivar urls: Required. List of STUN/TURN server URLs.
    :vartype urls: list[str]
    :ivar username: Required. User account name which uniquely identifies the credentials.
    :vartype username: str
    :ivar credential: Required. Credential for the server.
    :vartype credential: str
    """

    _validation = {
        'urls': {'required': True},
        'username': {'required': True},
        'credential': {'required': True},
    }

    _attribute_map = {
        'urls': {'key': 'urls', 'type': '[str]'},
        'username': {'key': 'username', 'type': 'str'},
        'credential': {'key': 'credential', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword urls: Required. List of STUN/TURN server URLs.
        :paramtype urls: list[str]
        :keyword username: Required. User account name which uniquely identifies the credentials.
        :paramtype username: str
        :keyword credential: Required. Credential for the server.
        :paramtype credential: str
        """
        super(CommunicationIceServer, self).__init__(**kwargs)
        self.urls = kwargs['urls']
        self.username = kwargs['username']
        self.credential = kwargs['credential']


class CommunicationRelayConfiguration(msrest.serialization.Model):
    """A relay configuration containing the STUN/TURN URLs and credentials.

    All required parameters must be populated in order to send to Azure.

    :ivar expires_on: Required. The date for which the username and credentials are not longer
     valid.
    :vartype expires_on: ~datetime.datetime
    :ivar ice_servers: Required. An array representing the credentials and the STUN/TURN server
     URLs for use in ICE negotiations.
    :vartype ice_servers: list[~azure.communication.networktraversal.models.CommunicationIceServer]
    """

    _validation = {
        'expires_on': {'required': True},
        'ice_servers': {'required': True},
    }

    _attribute_map = {
        'expires_on': {'key': 'expiresOn', 'type': 'iso-8601'},
        'ice_servers': {'key': 'iceServers', 'type': '[CommunicationIceServer]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword expires_on: Required. The date for which the username and credentials are not longer
         valid.
        :paramtype expires_on: ~datetime.datetime
        :keyword ice_servers: Required. An array representing the credentials and the STUN/TURN server
         URLs for use in ICE negotiations.
        :paramtype ice_servers:
         list[~azure.communication.networktraversal.models.CommunicationIceServer]
        """
        super(CommunicationRelayConfiguration, self).__init__(**kwargs)
        self.expires_on = kwargs['expires_on']
        self.ice_servers = kwargs['ice_servers']


class CommunicationRelayConfigurationRequest(msrest.serialization.Model):
    """Request for a CommunicationRelayConfiguration.

    :ivar id: An existing ACS identity.
    :vartype id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword id: An existing ACS identity.
        :paramtype id: str
        """
        super(CommunicationRelayConfigurationRequest, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)