# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CapabilitiesOperations:
    """CapabilitiesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
<<<<<<< HEAD
    :type models: ~microsoft_azure_chaos.models
=======
    :type models: ~chaos_management_client.models
>>>>>>> main
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        continuation_token_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.CapabilityListResult"]:
        """Get a list of Capability resources that extend a Target resource..

        :param resource_group_name: String that represents an Azure resource group.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name.
        :type target_name: str
        :param continuation_token_parameter: String that sets the continuation token.
        :type continuation_token_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CapabilityListResult or the result of cls(response)
<<<<<<< HEAD
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~microsoft_azure_chaos.models.CapabilityListResult]
=======
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~chaos_management_client.models.CapabilityListResult]
>>>>>>> main
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CapabilityListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-15-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$'),
                    'parentProviderNamespace': self._serialize.url("parent_provider_namespace", parent_provider_namespace, 'str', pattern=r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'),
                    'parentResourceType': self._serialize.url("parent_resource_type", parent_resource_type, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
                    'parentResourceName': self._serialize.url("parent_resource_name", parent_resource_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
                    'targetName': self._serialize.url("target_name", target_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if continuation_token_parameter is not None:
                    query_parameters['continuationToken'] = self._serialize.query("continuation_token_parameter", continuation_token_parameter, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CapabilityListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities'}  # type: ignore

    async def get(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        **kwargs: Any
    ) -> "_models.Capability":
        """Get a Capability resource that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name.
        :type capability_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability, or the result of cls(response)
<<<<<<< HEAD
        :rtype: ~microsoft_azure_chaos.models.Capability
=======
        :rtype: ~chaos_management_client.models.Capability
>>>>>>> main
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Capability"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-15-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$'),
            'parentProviderNamespace': self._serialize.url("parent_provider_namespace", parent_provider_namespace, 'str', pattern=r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'),
            'parentResourceType': self._serialize.url("parent_resource_type", parent_resource_type, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'parentResourceName': self._serialize.url("parent_resource_name", parent_resource_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'targetName': self._serialize.url("target_name", target_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'capabilityName': self._serialize.url("capability_name", capability_name, 'str', pattern=r'^[a-zA-Z0-9\-\.]+-\d\.\d$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Capability', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}'}  # type: ignore

    async def delete(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        **kwargs: Any
    ) -> None:
        """Delete a Capability that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name.
        :type capability_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-15-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$'),
            'parentProviderNamespace': self._serialize.url("parent_provider_namespace", parent_provider_namespace, 'str', pattern=r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'),
            'parentResourceType': self._serialize.url("parent_resource_type", parent_resource_type, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'parentResourceName': self._serialize.url("parent_resource_name", parent_resource_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'targetName': self._serialize.url("target_name", target_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'capabilityName': self._serialize.url("capability_name", capability_name, 'str', pattern=r'^[a-zA-Z0-9\-\.]+-\d\.\d$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}'}  # type: ignore

    async def create_or_update(
        self,
        resource_group_name: str,
        parent_provider_namespace: str,
        parent_resource_type: str,
        parent_resource_name: str,
        target_name: str,
        capability_name: str,
        capability: "_models.Capability",
        **kwargs: Any
    ) -> "_models.Capability":
        """Create or update a Capability resource that extends a Target resource.

        :param resource_group_name: String that represents an Azure resource group.
        :type resource_group_name: str
        :param parent_provider_namespace: String that represents a resource provider namespace.
        :type parent_provider_namespace: str
        :param parent_resource_type: String that represents a resource type.
        :type parent_resource_type: str
        :param parent_resource_name: String that represents a resource name.
        :type parent_resource_name: str
        :param target_name: String that represents a Target resource name.
        :type target_name: str
        :param capability_name: String that represents a Capability resource name.
        :type capability_name: str
        :param capability: Capability resource to be created or updated.
<<<<<<< HEAD
        :type capability: ~microsoft_azure_chaos.models.Capability
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability, or the result of cls(response)
        :rtype: ~microsoft_azure_chaos.models.Capability
=======
        :type capability: ~chaos_management_client.models.Capability
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Capability, or the result of cls(response)
        :rtype: ~chaos_management_client.models.Capability
>>>>>>> main
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Capability"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-09-15-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.\(\)]*[a-zA-Z0-9_\-\(\)]$'),
            'parentProviderNamespace': self._serialize.url("parent_provider_namespace", parent_provider_namespace, 'str', pattern=r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$'),
            'parentResourceType': self._serialize.url("parent_resource_type", parent_resource_type, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'parentResourceName': self._serialize.url("parent_resource_name", parent_resource_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'targetName': self._serialize.url("target_name", target_name, 'str', pattern=r'^[a-zA-Z0-9_\-\.]+$'),
            'capabilityName': self._serialize.url("capability_name", capability_name, 'str', pattern=r'^[a-zA-Z0-9\-\.]+-\d\.\d$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(capability, 'Capability')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Capability', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{parentProviderNamespace}/{parentResourceType}/{parentResourceName}/providers/Microsoft.Chaos/targets/{targetName}/capabilities/{capabilityName}'}  # type: ignore
