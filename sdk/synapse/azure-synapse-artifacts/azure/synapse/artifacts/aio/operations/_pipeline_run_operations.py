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

class PipelineRunOperations:
    """PipelineRunOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
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

    async def query_pipeline_runs_by_workspace(
        self,
        filter_parameters: "_models.RunFilterParameters",
        **kwargs: Any
    ) -> "_models.PipelineRunsQueryResponse":
        """Query pipeline runs in the workspace based on input filter conditions.

        :param filter_parameters: Parameters to filter the pipeline run.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineRunsQueryResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.PipelineRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PipelineRunsQueryResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.query_pipeline_runs_by_workspace.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
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
        body_content = self._serialize.body(filter_parameters, 'RunFilterParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PipelineRunsQueryResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    query_pipeline_runs_by_workspace.metadata = {'url': '/queryPipelineRuns'}  # type: ignore

    async def get_pipeline_run(
        self,
        run_id: str,
        **kwargs: Any
    ) -> "_models.PipelineRun":
        """Get a pipeline run by its run ID.

        :param run_id: The pipeline run identifier.
        :type run_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PipelineRun, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.PipelineRun
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PipelineRun"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-01"
        accept = "application/json"

        # Construct URL
        url = self.get_pipeline_run.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'runId': self._serialize.url("run_id", run_id, 'str'),
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
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PipelineRun', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_pipeline_run.metadata = {'url': '/pipelineruns/{runId}'}  # type: ignore

    async def query_activity_runs(
        self,
        pipeline_name: str,
        run_id: str,
        filter_parameters: "_models.RunFilterParameters",
        **kwargs: Any
    ) -> "_models.ActivityRunsQueryResponse":
        """Query activity runs based on input filter conditions.

        :param pipeline_name: The pipeline name.
        :type pipeline_name: str
        :param run_id: The pipeline run identifier.
        :type run_id: str
        :param filter_parameters: Parameters to filter the activity runs.
        :type filter_parameters: ~azure.synapse.artifacts.models.RunFilterParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ActivityRunsQueryResponse, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.ActivityRunsQueryResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ActivityRunsQueryResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-12-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.query_activity_runs.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str', max_length=260, min_length=1, pattern=r'^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$'),
            'runId': self._serialize.url("run_id", run_id, 'str'),
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
        body_content = self._serialize.body(filter_parameters, 'RunFilterParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ActivityRunsQueryResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    query_activity_runs.metadata = {'url': '/pipelines/{pipelineName}/pipelineruns/{runId}/queryActivityruns'}  # type: ignore

    async def cancel_pipeline_run(
        self,
        run_id: str,
        is_recursive: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """Cancel a pipeline run by its run ID.

        :param run_id: The pipeline run identifier.
        :type run_id: str
        :param is_recursive: If true, cancel all the Child pipelines that are triggered by the current
         pipeline.
        :type is_recursive: bool
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
        api_version = "2020-12-01"
        accept = "application/json"

        # Construct URL
        url = self.cancel_pipeline_run.metadata['url']  # type: ignore
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'runId': self._serialize.url("run_id", run_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if is_recursive is not None:
            query_parameters['isRecursive'] = self._serialize.query("is_recursive", is_recursive, 'bool')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    cancel_pipeline_run.metadata = {'url': '/pipelineruns/{runId}/cancel'}  # type: ignore
