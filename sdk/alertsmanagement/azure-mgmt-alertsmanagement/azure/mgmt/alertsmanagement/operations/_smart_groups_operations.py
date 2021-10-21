# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SmartGroupsOperations(object):
    """SmartGroupsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.alertsmanagement.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_all(
        self,
        target_resource=None,  # type: Optional[str]
        target_resource_group=None,  # type: Optional[str]
        target_resource_type=None,  # type: Optional[str]
        monitor_service=None,  # type: Optional[Union[str, "_models.MonitorService"]]
        monitor_condition=None,  # type: Optional[Union[str, "_models.MonitorCondition"]]
        severity=None,  # type: Optional[Union[str, "_models.Severity"]]
        smart_group_state=None,  # type: Optional[Union[str, "_models.AlertState"]]
        time_range=None,  # type: Optional[Union[str, "_models.TimeRange"]]
        page_count=None,  # type: Optional[int]
        sort_by=None,  # type: Optional[Union[str, "_models.SmartGroupsSortByFields"]]
        sort_order=None,  # type: Optional[Union[str, "_models.Enum11"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.SmartGroupsList"]
        """Get all Smart Groups within a specified subscription.

        List all the Smart Groups within a specified subscription.

        :param target_resource: Filter by target resource( which is full ARM ID) Default value is
         select all.
        :type target_resource: str
        :param target_resource_group: Filter by target resource group name. Default value is select
         all.
        :type target_resource_group: str
        :param target_resource_type: Filter by target resource type. Default value is select all.
        :type target_resource_type: str
        :param monitor_service: Filter by monitor service which generates the alert instance. Default
         value is select all.
        :type monitor_service: str or ~azure.mgmt.alertsmanagement.models.MonitorService
        :param monitor_condition: Filter by monitor condition which is either 'Fired' or 'Resolved'.
         Default value is to select all.
        :type monitor_condition: str or ~azure.mgmt.alertsmanagement.models.MonitorCondition
        :param severity: Filter by severity.  Default value is select all.
        :type severity: str or ~azure.mgmt.alertsmanagement.models.Severity
        :param smart_group_state: Filter by state of the smart group. Default value is to select all.
        :type smart_group_state: str or ~azure.mgmt.alertsmanagement.models.AlertState
        :param time_range: Filter by time range by below listed values. Default value is 1 day.
        :type time_range: str or ~azure.mgmt.alertsmanagement.models.TimeRange
        :param page_count: Determines number of alerts returned per page in response. Permissible value
         is between 1 to 250. When the "includeContent"  filter is selected, maximum value allowed is
         25. Default value is 25.
        :type page_count: int
        :param sort_by: Sort the query results by input field. Default value is sort by
         'lastModifiedDateTime'.
        :type sort_by: str or ~azure.mgmt.alertsmanagement.models.SmartGroupsSortByFields
        :param sort_order: Sort the query results order in either ascending or descending.  Default
         value is 'desc' for time fields and 'asc' for others.
        :type sort_order: str or ~azure.mgmt.alertsmanagement.models.Enum11
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SmartGroupsList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.alertsmanagement.models.SmartGroupsList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SmartGroupsList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-05-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_all.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if target_resource is not None:
                    query_parameters['targetResource'] = self._serialize.query("target_resource", target_resource, 'str')
                if target_resource_group is not None:
                    query_parameters['targetResourceGroup'] = self._serialize.query("target_resource_group", target_resource_group, 'str')
                if target_resource_type is not None:
                    query_parameters['targetResourceType'] = self._serialize.query("target_resource_type", target_resource_type, 'str')
                if monitor_service is not None:
                    query_parameters['monitorService'] = self._serialize.query("monitor_service", monitor_service, 'str')
                if monitor_condition is not None:
                    query_parameters['monitorCondition'] = self._serialize.query("monitor_condition", monitor_condition, 'str')
                if severity is not None:
                    query_parameters['severity'] = self._serialize.query("severity", severity, 'str')
                if smart_group_state is not None:
                    query_parameters['smartGroupState'] = self._serialize.query("smart_group_state", smart_group_state, 'str')
                if time_range is not None:
                    query_parameters['timeRange'] = self._serialize.query("time_range", time_range, 'str')
                if page_count is not None:
                    query_parameters['pageCount'] = self._serialize.query("page_count", page_count, 'int')
                if sort_by is not None:
                    query_parameters['sortBy'] = self._serialize.query("sort_by", sort_by, 'str')
                if sort_order is not None:
                    query_parameters['sortOrder'] = self._serialize.query("sort_order", sort_order, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('SmartGroupsList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(_models.ErrorResponseAutoGenerated2, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    get_all.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups'}  # type: ignore

    def get_by_id(
        self,
        smart_group_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SmartGroup"
        """Get information related to a specific Smart Group.

        Get information related to a specific Smart Group.

        :param smart_group_id: Smart group unique id.
        :type smart_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SmartGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SmartGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-05-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_by_id.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'smartGroupId': self._serialize.url("smart_group_id", smart_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponseAutoGenerated2, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('SmartGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_by_id.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}'}  # type: ignore

    def change_state(
        self,
        smart_group_id,  # type: str
        new_state,  # type: Union[str, "_models.AlertState"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SmartGroup"
        """Change the state of a Smart Group.

        :param smart_group_id: Smart group unique id.
        :type smart_group_id: str
        :param new_state: New state of the alert.
        :type new_state: str or ~azure.mgmt.alertsmanagement.models.AlertState
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SmartGroup, or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroup
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SmartGroup"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-05-preview"
        accept = "application/json"

        # Construct URL
        url = self.change_state.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'smartGroupId': self._serialize.url("smart_group_id", smart_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        query_parameters['newState'] = self._serialize.query("new_state", new_state, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponseAutoGenerated2, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers['x-ms-request-id']=self._deserialize('str', response.headers.get('x-ms-request-id'))
        deserialized = self._deserialize('SmartGroup', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    change_state.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState'}  # type: ignore

    def get_history(
        self,
        smart_group_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SmartGroupModification"
        """Get the history a smart group, which captures any Smart Group state changes
        (New/Acknowledged/Closed) .

        :param smart_group_id: Smart group unique id.
        :type smart_group_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SmartGroupModification, or the result of cls(response)
        :rtype: ~azure.mgmt.alertsmanagement.models.SmartGroupModification
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.SmartGroupModification"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-05-preview"
        accept = "application/json"

        # Construct URL
        url = self.get_history.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'smartGroupId': self._serialize.url("smart_group_id", smart_group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(_models.ErrorResponseAutoGenerated2, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SmartGroupModification', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_history.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history'}  # type: ignore