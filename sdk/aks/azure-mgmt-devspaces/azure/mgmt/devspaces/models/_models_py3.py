# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._dev_spaces_management_client_enums import *


class ContainerHostMapping(msrest.serialization.Model):
    """Container host mapping object specifying the Container host resource ID and its associated Controller resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param container_host_resource_id: ARM ID of the Container Host resource.
    :type container_host_resource_id: str
    :ivar mapped_controller_resource_id: ARM ID of the mapped Controller resource.
    :vartype mapped_controller_resource_id: str
    """

    _validation = {
        'mapped_controller_resource_id': {'readonly': True},
    }

    _attribute_map = {
        'container_host_resource_id': {'key': 'containerHostResourceId', 'type': 'str'},
        'mapped_controller_resource_id': {'key': 'mappedControllerResourceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        container_host_resource_id: Optional[str] = None,
        **kwargs
    ):
        super(ContainerHostMapping, self).__init__(**kwargs)
        self.container_host_resource_id = container_host_resource_id
        self.mapped_controller_resource_id = None


class Resource(msrest.serialization.Model):
    """An Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: A set of tags. Tags for the Azure resource.
    :type tags: dict[str, str]
    :param location: Region where the Azure resource is located.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Controller(TrackedResource):
    """Controller.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: A set of tags. Tags for the Azure resource.
    :type tags: dict[str, str]
    :param location: Region where the Azure resource is located.
    :type location: str
    :param sku: Required. Model representing SKU for Azure Dev Spaces Controller.
    :type sku: ~dev_spaces_management_client.models.Sku
    :ivar provisioning_state: Provisioning state of the Azure Dev Spaces Controller. Possible
     values include: "Succeeded", "Failed", "Canceled", "Updating", "Creating", "Deleting",
     "Deleted".
    :vartype provisioning_state: str or ~dev_spaces_management_client.models.ProvisioningState
    :ivar host_suffix: DNS suffix for public endpoints running in the Azure Dev Spaces Controller.
    :vartype host_suffix: str
    :ivar data_plane_fqdn: DNS name for accessing DataPlane services.
    :vartype data_plane_fqdn: str
    :ivar target_container_host_api_server_fqdn: DNS of the target container host's API server.
    :vartype target_container_host_api_server_fqdn: str
    :param target_container_host_resource_id: Required. Resource ID of the target container host.
    :type target_container_host_resource_id: str
    :param target_container_host_credentials_base64: Required. Credentials of the target container
     host (base64).
    :type target_container_host_credentials_base64: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'sku': {'required': True},
        'provisioning_state': {'readonly': True},
        'host_suffix': {'readonly': True},
        'data_plane_fqdn': {'readonly': True},
        'target_container_host_api_server_fqdn': {'readonly': True},
        'target_container_host_resource_id': {'required': True},
        'target_container_host_credentials_base64': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'host_suffix': {'key': 'properties.hostSuffix', 'type': 'str'},
        'data_plane_fqdn': {'key': 'properties.dataPlaneFqdn', 'type': 'str'},
        'target_container_host_api_server_fqdn': {'key': 'properties.targetContainerHostApiServerFqdn', 'type': 'str'},
        'target_container_host_resource_id': {'key': 'properties.targetContainerHostResourceId', 'type': 'str'},
        'target_container_host_credentials_base64': {'key': 'properties.targetContainerHostCredentialsBase64', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        sku: "Sku",
        target_container_host_resource_id: str,
        target_container_host_credentials_base64: str,
        tags: Optional[Dict[str, str]] = None,
        location: Optional[str] = None,
        **kwargs
    ):
        super(Controller, self).__init__(tags=tags, location=location, **kwargs)
        self.sku = sku
        self.provisioning_state = None
        self.host_suffix = None
        self.data_plane_fqdn = None
        self.target_container_host_api_server_fqdn = None
        self.target_container_host_resource_id = target_container_host_resource_id
        self.target_container_host_credentials_base64 = target_container_host_credentials_base64


class ControllerConnectionDetails(msrest.serialization.Model):
    """ControllerConnectionDetails.

    :param orchestrator_specific_connection_details: Base class for types that supply values used
     to connect to container orchestrators.
    :type orchestrator_specific_connection_details:
     ~dev_spaces_management_client.models.OrchestratorSpecificConnectionDetails
    """

    _attribute_map = {
        'orchestrator_specific_connection_details': {'key': 'orchestratorSpecificConnectionDetails', 'type': 'OrchestratorSpecificConnectionDetails'},
    }

    def __init__(
        self,
        *,
        orchestrator_specific_connection_details: Optional["OrchestratorSpecificConnectionDetails"] = None,
        **kwargs
    ):
        super(ControllerConnectionDetails, self).__init__(**kwargs)
        self.orchestrator_specific_connection_details = orchestrator_specific_connection_details


class ControllerConnectionDetailsList(msrest.serialization.Model):
    """ControllerConnectionDetailsList.

    :param connection_details_list: List of Azure Dev Spaces Controller connection details.
    :type connection_details_list:
     list[~dev_spaces_management_client.models.ControllerConnectionDetails]
    """

    _attribute_map = {
        'connection_details_list': {'key': 'connectionDetailsList', 'type': '[ControllerConnectionDetails]'},
    }

    def __init__(
        self,
        *,
        connection_details_list: Optional[List["ControllerConnectionDetails"]] = None,
        **kwargs
    ):
        super(ControllerConnectionDetailsList, self).__init__(**kwargs)
        self.connection_details_list = connection_details_list


class ControllerList(msrest.serialization.Model):
    """ControllerList.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: List of Azure Dev Spaces Controllers.
    :type value: list[~dev_spaces_management_client.models.Controller]
    :ivar next_link: The URI that can be used to request the next page for list of Azure Dev Spaces
     Controllers.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Controller]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Controller"]] = None,
        **kwargs
    ):
        super(ControllerList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class ControllerUpdateParameters(msrest.serialization.Model):
    """Parameters for updating an Azure Dev Spaces Controller.

    :param tags: A set of tags. Tags for the Azure Dev Spaces Controller.
    :type tags: dict[str, str]
    :param target_container_host_credentials_base64: Credentials of the target container host
     (base64).
    :type target_container_host_credentials_base64: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'target_container_host_credentials_base64': {'key': 'properties.targetContainerHostCredentialsBase64', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        target_container_host_credentials_base64: Optional[str] = None,
        **kwargs
    ):
        super(ControllerUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.target_container_host_credentials_base64 = target_container_host_credentials_base64


class DevSpacesErrorResponse(msrest.serialization.Model):
    """Error response indicates that the service is not able to process the incoming request. The reason is provided in the error message.

    :param error: The details of the error.
    :type error: ~dev_spaces_management_client.models.ErrorDetails
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetails'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDetails"] = None,
        **kwargs
    ):
        super(DevSpacesErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorDetails(msrest.serialization.Model):
    """ErrorDetails.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Status code for the error.
    :vartype code: str
    :ivar message: Error message describing the error in detail.
    :vartype message: str
    :ivar target: The target of the particular error.
    :vartype target: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None


class OrchestratorSpecificConnectionDetails(msrest.serialization.Model):
    """Base class for types that supply values used to connect to container orchestrators.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: KubernetesConnectionDetails.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar instance_type: Required. Gets the Instance type.Constant filled by server.
    :vartype instance_type: str
    """

    _validation = {
        'instance_type': {'required': True, 'readonly': True},
    }

    _attribute_map = {
        'instance_type': {'key': 'instanceType', 'type': 'str'},
    }

    _subtype_map = {
        'instance_type': {'Kubernetes': 'KubernetesConnectionDetails'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrchestratorSpecificConnectionDetails, self).__init__(**kwargs)
        self.instance_type = None  # type: Optional[str]


class KubernetesConnectionDetails(OrchestratorSpecificConnectionDetails):
    """Contains information used to connect to a Kubernetes cluster.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar instance_type: Required. Gets the Instance type.Constant filled by server.
    :vartype instance_type: str
    :param kube_config: Gets the kubeconfig for the cluster.
    :type kube_config: str
    """

    _validation = {
        'instance_type': {'required': True, 'readonly': True},
    }

    _attribute_map = {
        'instance_type': {'key': 'instanceType', 'type': 'str'},
        'kube_config': {'key': 'kubeConfig', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        kube_config: Optional[str] = None,
        **kwargs
    ):
        super(KubernetesConnectionDetails, self).__init__(**kwargs)
        self.instance_type = 'Kubernetes'  # type: str
        self.kube_config = kube_config


class ListConnectionDetailsParameters(msrest.serialization.Model):
    """Parameters for listing connection details of an Azure Dev Spaces Controller.

    All required parameters must be populated in order to send to Azure.

    :param target_container_host_resource_id: Required. Resource ID of the target container host
     mapped to the Azure Dev Spaces Controller.
    :type target_container_host_resource_id: str
    """

    _validation = {
        'target_container_host_resource_id': {'required': True},
    }

    _attribute_map = {
        'target_container_host_resource_id': {'key': 'targetContainerHostResourceId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        target_container_host_resource_id: str,
        **kwargs
    ):
        super(ListConnectionDetailsParameters, self).__init__(**kwargs)
        self.target_container_host_resource_id = target_container_host_resource_id


class ResourceProviderOperationDefinition(msrest.serialization.Model):
    """ResourceProviderOperationDefinition.

    :param name: Resource provider operation name.
    :type name: str
    :param display:
    :type display: ~dev_spaces_management_client.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["ResourceProviderOperationDisplay"] = None,
        **kwargs
    ):
        super(ResourceProviderOperationDefinition, self).__init__(**kwargs)
        self.name = name
        self.display = display


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """ResourceProviderOperationDisplay.

    :param provider: Name of the resource provider.
    :type provider: str
    :param resource: Name of the resource type.
    :type resource: str
    :param operation: Name of the resource provider operation.
    :type operation: str
    :param description: Description of the resource provider operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ResourceProviderOperationList(msrest.serialization.Model):
    """ResourceProviderOperationList.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param value: Resource provider operations list.
    :type value: list[~dev_spaces_management_client.models.ResourceProviderOperationDefinition]
    :ivar next_link: The URI that can be used to request the next page for list of Azure
     operations.
    :vartype next_link: str
    """

    _validation = {
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperationDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ResourceProviderOperationDefinition"]] = None,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = value
        self.next_link = None


class Sku(msrest.serialization.Model):
    """Model representing SKU for Azure Dev Spaces Controller.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU for Azure Dev Spaces Controller. Possible values
     include: "S1".
    :type name: str or ~dev_spaces_management_client.models.SkuName
    :param tier: The tier of the SKU for Azure Dev Spaces Controller. Possible values include:
     "Standard".
    :type tier: str or ~dev_spaces_management_client.models.SkuTier
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Union[str, "SkuName"],
        tier: Optional[Union[str, "SkuTier"]] = None,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
