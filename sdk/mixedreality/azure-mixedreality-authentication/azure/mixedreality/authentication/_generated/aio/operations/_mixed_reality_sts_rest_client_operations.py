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

class MixedRealityStsRestClientOperationsMixin:

    async def get_token(
        self,
        account_id: str,
        api_version: Optional[str] = "2019-02-28-preview",
        token_request_options: Optional["_models.TokenRequestOptions"] = None,
        **kwargs
    ) -> "_models.StsTokenResponseMessage":
        """Gets an access token to be used with Mixed Reality services.

        Gets an access token to be used with Mixed Reality services.

        :param account_id: The Mixed Reality account identifier.
        :type account_id: str
        :param api_version: Api Version.
        :type api_version: str
        :param token_request_options: Parameter group.
        :type token_request_options: ~azure.mixedreality.authentication._generated.models.TokenRequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StsTokenResponseMessage, or the result of cls(response)
        :rtype: ~azure.mixedreality.authentication._generated.models.StsTokenResponseMessage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.StsTokenResponseMessage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _client_request_id = None
        if token_request_options is not None:
            _client_request_id = token_request_options.client_request_id
        accept = "application/json"

        # Construct URL
        url = self.get_token.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountId': self._serialize.url("account_id", account_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _client_request_id is not None:
            header_parameters['X-MRC-CV'] = self._serialize.header("client_request_id", _client_request_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['MS-CV']=self._deserialize('str', response.headers.get('MS-CV'))
        deserialized = self._deserialize('StsTokenResponseMessage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_token.metadata = {'url': '/Accounts/{accountId}/token'}  # type: ignore
