# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PolicyCertificatesOperations:
    """PolicyCertificatesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.security.attestation._generated.models
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

    async def get(
        self,
        **kwargs: Any
    ) -> "_models.PolicyCertificatesResponse":
        """Retrieves the set of certificates used to express policy for the current tenant.

        Retrieves the set of certificates used to express policy for the current tenant.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyCertificatesResponse, or the result of cls(response)
        :rtype: ~azure.security.attestation._generated.models.PolicyCertificatesResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyCertificatesResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'instanceUrl': self._serialize.url("self._config.instance_url", self._config.instance_url, 'str', skip_quote=True),
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
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PolicyCertificatesResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/certificates'}  # type: ignore

    async def add(
        self,
        policy_certificate_to_add: str,
        **kwargs: Any
    ) -> "_models.PolicyCertificatesModifyResponse":
        """Adds a new attestation policy certificate to the set of policy management certificates.

        Adds a new attestation policy certificate to the set of policy management certificates.

        :param policy_certificate_to_add: An RFC7519 JSON Web Token whose body is an RFC7517 JSON Web
         Key object. The RFC7519 JWT must be signed with one of the existing signing certificates.
        :type policy_certificate_to_add: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyCertificatesModifyResponse, or the result of cls(response)
        :rtype: ~azure.security.attestation._generated.models.PolicyCertificatesModifyResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyCertificatesModifyResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.add.metadata['url']  # type: ignore
        path_format_arguments = {
            'instanceUrl': self._serialize.url("self._config.instance_url", self._config.instance_url, 'str', skip_quote=True),
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
        body_content = self._serialize.body(policy_certificate_to_add, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PolicyCertificatesModifyResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    add.metadata = {'url': '/certificates:add'}  # type: ignore

    async def remove(
        self,
        policy_certificate_to_remove: str,
        **kwargs: Any
    ) -> "_models.PolicyCertificatesModifyResponse":
        """Removes the specified policy management certificate. Note that the final policy management certificate cannot be removed.

        Removes the specified policy management certificate. Note that the final policy management
        certificate cannot be removed.

        :param policy_certificate_to_remove: An RFC7519 JSON Web Token whose body is an
         AttestationCertificateManagementBody object. The RFC7519 JWT must be signed with one of the
         existing signing certificates.
        :type policy_certificate_to_remove: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyCertificatesModifyResponse, or the result of cls(response)
        :rtype: ~azure.security.attestation._generated.models.PolicyCertificatesModifyResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyCertificatesModifyResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-10-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.remove.metadata['url']  # type: ignore
        path_format_arguments = {
            'instanceUrl': self._serialize.url("self._config.instance_url", self._config.instance_url, 'str', skip_quote=True),
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
        body_content = self._serialize.body(policy_certificate_to_remove, 'str')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PolicyCertificatesModifyResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    remove.metadata = {'url': '/certificates:remove'}  # type: ignore
