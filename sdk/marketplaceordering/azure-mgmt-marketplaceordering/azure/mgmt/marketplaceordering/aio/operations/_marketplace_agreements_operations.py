# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MarketplaceAgreementsOperations:
    """MarketplaceAgreementsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.marketplaceordering.models
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
        offer_type: Union[str, "_models.OfferType"],
        publisher_id: str,
        offer_id: str,
        plan_id: str,
        **kwargs
    ) -> "_models.AgreementTerms":
        """Get marketplace terms.

        :param offer_type: Offer Type, currently only virtualmachine type is supported.
        :type offer_type: str or ~azure.mgmt.marketplaceordering.models.OfferType
        :param publisher_id: Publisher identifier string of image being deployed.
        :type publisher_id: str
        :param offer_id: Offer identifier string of image being deployed.
        :type offer_id: str
        :param plan_id: Plan identifier string of image being deployed.
        :type plan_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AgreementTerms, or the result of cls(response)
        :rtype: ~azure.mgmt.marketplaceordering.models.AgreementTerms
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AgreementTerms"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'offerType': self._serialize.url("offer_type", offer_type, 'str'),
            'publisherId': self._serialize.url("publisher_id", publisher_id, 'str'),
            'offerId': self._serialize.url("offer_id", offer_id, 'str'),
            'planId': self._serialize.url("plan_id", plan_id, 'str'),
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
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AgreementTerms', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offerType}/publishers/{publisherId}/offers/{offerId}/plans/{planId}/agreements/current'}  # type: ignore

    async def create(
        self,
        offer_type: Union[str, "_models.OfferType"],
        publisher_id: str,
        offer_id: str,
        plan_id: str,
        parameters: "_models.AgreementTerms",
        **kwargs
    ) -> "_models.AgreementTerms":
        """Save marketplace terms.

        :param offer_type: Offer Type, currently only virtualmachine type is supported.
        :type offer_type: str or ~azure.mgmt.marketplaceordering.models.OfferType
        :param publisher_id: Publisher identifier string of image being deployed.
        :type publisher_id: str
        :param offer_id: Offer identifier string of image being deployed.
        :type offer_id: str
        :param plan_id: Plan identifier string of image being deployed.
        :type plan_id: str
        :param parameters: Parameters supplied to the Create Marketplace Terms operation.
        :type parameters: ~azure.mgmt.marketplaceordering.models.AgreementTerms
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AgreementTerms, or the result of cls(response)
        :rtype: ~azure.mgmt.marketplaceordering.models.AgreementTerms
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AgreementTerms"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create.metadata['url']  # type: ignore
        path_format_arguments = {
            'offerType': self._serialize.url("offer_type", offer_type, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'publisherId': self._serialize.url("publisher_id", publisher_id, 'str'),
            'offerId': self._serialize.url("offer_id", offer_id, 'str'),
            'planId': self._serialize.url("plan_id", plan_id, 'str'),
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
        body_content = self._serialize.body(parameters, 'AgreementTerms')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AgreementTerms', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offerType}/publishers/{publisherId}/offers/{offerId}/plans/{planId}/agreements/current'}  # type: ignore

    async def sign(
        self,
        publisher_id: str,
        offer_id: str,
        plan_id: str,
        **kwargs
    ) -> "_models.AgreementTerms":
        """Sign marketplace terms.

        :param publisher_id: Publisher identifier string of image being deployed.
        :type publisher_id: str
        :param offer_id: Offer identifier string of image being deployed.
        :type offer_id: str
        :param plan_id: Plan identifier string of image being deployed.
        :type plan_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AgreementTerms, or the result of cls(response)
        :rtype: ~azure.mgmt.marketplaceordering.models.AgreementTerms
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AgreementTerms"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.sign.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'publisherId': self._serialize.url("publisher_id", publisher_id, 'str'),
            'offerId': self._serialize.url("offer_id", offer_id, 'str'),
            'planId': self._serialize.url("plan_id", plan_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AgreementTerms', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    sign.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}/sign'}  # type: ignore

    async def cancel(
        self,
        publisher_id: str,
        offer_id: str,
        plan_id: str,
        **kwargs
    ) -> "_models.AgreementTerms":
        """Cancel marketplace terms.

        :param publisher_id: Publisher identifier string of image being deployed.
        :type publisher_id: str
        :param offer_id: Offer identifier string of image being deployed.
        :type offer_id: str
        :param plan_id: Plan identifier string of image being deployed.
        :type plan_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AgreementTerms, or the result of cls(response)
        :rtype: ~azure.mgmt.marketplaceordering.models.AgreementTerms
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AgreementTerms"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.cancel.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'publisherId': self._serialize.url("publisher_id", publisher_id, 'str'),
            'offerId': self._serialize.url("offer_id", offer_id, 'str'),
            'planId': self._serialize.url("plan_id", plan_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AgreementTerms', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}/cancel'}  # type: ignore

    async def get_agreement(
        self,
        publisher_id: str,
        offer_id: str,
        plan_id: str,
        **kwargs
    ) -> "_models.AgreementTerms":
        """Get marketplace agreement.

        :param publisher_id: Publisher identifier string of image being deployed.
        :type publisher_id: str
        :param offer_id: Offer identifier string of image being deployed.
        :type offer_id: str
        :param plan_id: Plan identifier string of image being deployed.
        :type plan_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AgreementTerms, or the result of cls(response)
        :rtype: ~azure.mgmt.marketplaceordering.models.AgreementTerms
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AgreementTerms"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_agreement.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'publisherId': self._serialize.url("publisher_id", publisher_id, 'str'),
            'offerId': self._serialize.url("offer_id", offer_id, 'str'),
            'planId': self._serialize.url("plan_id", plan_id, 'str'),
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
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AgreementTerms', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_agreement.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}'}  # type: ignore

    async def list(
        self,
        **kwargs
    ) -> List["_models.AgreementTerms"]:
        """List marketplace agreements in the subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of AgreementTerms, or the result of cls(response)
        :rtype: list[~azure.mgmt.marketplaceordering.models.AgreementTerms]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.AgreementTerms"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.list.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
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
            error = self._deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[AgreementTerms]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements'}  # type: ignore
