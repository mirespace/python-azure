# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Column(msrest.serialization.Model):
    """Query result column descriptor.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Column name.
    :type name: str
    :param type: Required. Column data type. Possible values include: "string", "integer",
     "number", "boolean", "object".
    :type type: str or ~resource_graph_client.models.ColumnDataType
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Column, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.type = kwargs['type']


class DateTimeInterval(msrest.serialization.Model):
    """An interval in time specifying the date and time for the inclusive start and exclusive end, i.e. ``[start, end)``.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. A datetime indicating the inclusive/closed start of the time interval,
     i.e. ``[``\ **\ ``start``\ **\ ``, end)``. Specifying a ``start`` that occurs chronologically
     after ``end`` will result in an error.
    :type start: ~datetime.datetime
    :param end: Required. A datetime indicating the exclusive/open end of the time interval, i.e.
     ``[start,``\ **\ ``end``\ **\ ``)``. Specifying an ``end`` that occurs chronologically before
     ``start`` will result in an error.
    :type end: ~datetime.datetime
    """

    _validation = {
        'start': {'required': True},
        'end': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'start', 'type': 'iso-8601'},
        'end': {'key': 'end', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DateTimeInterval, self).__init__(**kwargs)
        self.start = kwargs['start']
        self.end = kwargs['end']


class Error(msrest.serialization.Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. Error code identifying the specific error.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    :param details: Error details.
    :type details: list[~resource_graph_client.models.ErrorDetails]
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetails]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.details = kwargs.get('details', None)


class ErrorDetails(msrest.serialization.Model):
    """Error details.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param code: Required. Error code identifying the specific error.
    :type code: str
    :param message: Required. A human readable error message.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.code = kwargs['code']
        self.message = kwargs['message']


class ErrorResponse(msrest.serialization.Model):
    """An error response from the API.

    All required parameters must be populated in order to send to Azure.

    :param error: Required. Error information.
    :type error: ~resource_graph_client.models.Error
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs['error']


class Facet(msrest.serialization.Model):
    """A facet containing additional statistics on the response of a query. Can be either FacetResult or FacetError.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: FacetError, FacetResult.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. Facet expression, same as in the corresponding facet request.
    :type expression: str
    :param result_type: Required. Result type.Constant filled by server.
    :type result_type: str
    """

    _validation = {
        'expression': {'required': True},
        'result_type': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
    }

    _subtype_map = {
        'result_type': {'FacetError': 'FacetError', 'FacetResult': 'FacetResult'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Facet, self).__init__(**kwargs)
        self.expression = kwargs['expression']
        self.result_type = None  # type: Optional[str]


class FacetError(Facet):
    """A facet whose execution resulted in an error.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. Facet expression, same as in the corresponding facet request.
    :type expression: str
    :param result_type: Required. Result type.Constant filled by server.
    :type result_type: str
    :param errors: Required. An array containing detected facet errors with details.
    :type errors: list[~resource_graph_client.models.ErrorDetails]
    """

    _validation = {
        'expression': {'required': True},
        'result_type': {'required': True},
        'errors': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'errors': {'key': 'errors', 'type': '[ErrorDetails]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FacetError, self).__init__(**kwargs)
        self.result_type = 'FacetError'  # type: str
        self.errors = kwargs['errors']


class FacetRequest(msrest.serialization.Model):
    """A request to compute additional statistics (facets) over the query results.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. The column or list of columns to summarize by.
    :type expression: str
    :param options: The options for facet evaluation.
    :type options: ~resource_graph_client.models.FacetRequestOptions
    """

    _validation = {
        'expression': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'options': {'key': 'options', 'type': 'FacetRequestOptions'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FacetRequest, self).__init__(**kwargs)
        self.expression = kwargs['expression']
        self.options = kwargs.get('options', None)


class FacetRequestOptions(msrest.serialization.Model):
    """The options for facet evaluation.

    :param sort_by: The column name or query expression to sort on. Defaults to count if not
     present.
    :type sort_by: str
    :param sort_order: The sorting order by the selected column (count by default). Possible values
     include: "asc", "desc". Default value: "desc".
    :type sort_order: str or ~resource_graph_client.models.FacetSortOrder
    :param filter: Specifies the filter condition for the 'where' clause which will be run on main
     query's result, just before the actual faceting.
    :type filter: str
    :param top: The maximum number of facet rows that should be returned.
    :type top: int
    """

    _validation = {
        'top': {'maximum': 1000, 'minimum': 1},
    }

    _attribute_map = {
        'sort_by': {'key': 'sortBy', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'str'},
        'top': {'key': '$top', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FacetRequestOptions, self).__init__(**kwargs)
        self.sort_by = kwargs.get('sort_by', None)
        self.sort_order = kwargs.get('sort_order', "desc")
        self.filter = kwargs.get('filter', None)
        self.top = kwargs.get('top', None)


class FacetResult(Facet):
    """Successfully executed facet containing additional statistics on the response of a query.

    All required parameters must be populated in order to send to Azure.

    :param expression: Required. Facet expression, same as in the corresponding facet request.
    :type expression: str
    :param result_type: Required. Result type.Constant filled by server.
    :type result_type: str
    :param total_records: Required. Number of total records in the facet results.
    :type total_records: long
    :param count: Required. Number of records returned in the facet response.
    :type count: int
    :param data: Required. A table containing the desired facets. Only present if the facet is
     valid.
    :type data: object
    """

    _validation = {
        'expression': {'required': True},
        'result_type': {'required': True},
        'total_records': {'required': True},
        'count': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'total_records': {'key': 'totalRecords', 'type': 'long'},
        'count': {'key': 'count', 'type': 'int'},
        'data': {'key': 'data', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(FacetResult, self).__init__(**kwargs)
        self.result_type = 'FacetResult'  # type: str
        self.total_records = kwargs['total_records']
        self.count = kwargs['count']
        self.data = kwargs['data']


class Operation(msrest.serialization.Model):
    """Resource Graph REST API operation definition.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~resource_graph_client.models.OperationDisplay
    :param origin: The origin of operations.
    :type origin: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)


class OperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Service provider: Microsoft Resource Graph.
    :type provider: str
    :param resource: Resource on which the operation is performed etc.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description for the operation.
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
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationListResult(msrest.serialization.Model):
    """Result of the request to list Resource Graph operations. It contains a list of operations and a URL link to get the next set of results.

    :param value: List of Resource Graph operations supported by the Resource Graph resource
     provider.
    :type value: list[~resource_graph_client.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class QueryRequest(msrest.serialization.Model):
    """Describes a query to be executed.

    All required parameters must be populated in order to send to Azure.

    :param subscriptions: Azure subscriptions against which to execute the query.
    :type subscriptions: list[str]
    :param management_group_id: The management group identifier.
    :type management_group_id: str
    :param query: Required. The resources query.
    :type query: str
    :param options: The query evaluation options.
    :type options: ~resource_graph_client.models.QueryRequestOptions
    :param facets: An array of facet requests to be computed against the query result.
    :type facets: list[~resource_graph_client.models.FacetRequest]
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'subscriptions': {'key': 'subscriptions', 'type': '[str]'},
        'management_group_id': {'key': 'managementGroupId', 'type': 'str'},
        'query': {'key': 'query', 'type': 'str'},
        'options': {'key': 'options', 'type': 'QueryRequestOptions'},
        'facets': {'key': 'facets', 'type': '[FacetRequest]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueryRequest, self).__init__(**kwargs)
        self.subscriptions = kwargs.get('subscriptions', None)
        self.management_group_id = kwargs.get('management_group_id', None)
        self.query = kwargs['query']
        self.options = kwargs.get('options', None)
        self.facets = kwargs.get('facets', None)


class QueryRequestOptions(msrest.serialization.Model):
    """The options for query evaluation.

    :param skip_token: Continuation token for pagination, capturing the next page size and offset,
     as well as the context of the query.
    :type skip_token: str
    :param top: The maximum number of rows that the query should return. Overrides the page size
     when ``$skipToken`` property is present.
    :type top: int
    :param skip: The number of rows to skip from the beginning of the results. Overrides the next
     page offset when ``$skipToken`` property is present.
    :type skip: int
    :param result_format: Defines in which format query result returned. Possible values include:
     "table", "objectArray".
    :type result_format: str or ~resource_graph_client.models.ResultFormat
    """

    _validation = {
        'top': {'maximum': 1000, 'minimum': 1},
        'skip': {'minimum': 0},
    }

    _attribute_map = {
        'skip_token': {'key': '$skipToken', 'type': 'str'},
        'top': {'key': '$top', 'type': 'int'},
        'skip': {'key': '$skip', 'type': 'int'},
        'result_format': {'key': 'resultFormat', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueryRequestOptions, self).__init__(**kwargs)
        self.skip_token = kwargs.get('skip_token', None)
        self.top = kwargs.get('top', None)
        self.skip = kwargs.get('skip', None)
        self.result_format = kwargs.get('result_format', None)


class QueryResponse(msrest.serialization.Model):
    """Query result.

    All required parameters must be populated in order to send to Azure.

    :param total_records: Required. Number of total records matching the query.
    :type total_records: long
    :param count: Required. Number of records returned in the current response. In the case of
     paging, this is the number of records in the current page.
    :type count: long
    :param result_truncated: Required. Indicates whether the query results are truncated. Possible
     values include: "true", "false".
    :type result_truncated: str or ~resource_graph_client.models.ResultTruncated
    :param skip_token: When present, the value can be passed to a subsequent query call (together
     with the same query and subscriptions used in the current request) to retrieve the next page of
     data.
    :type skip_token: str
    :param data: Required. Query output in tabular format.
    :type data: object
    :param facets: Query facets.
    :type facets: list[~resource_graph_client.models.Facet]
    """

    _validation = {
        'total_records': {'required': True},
        'count': {'required': True},
        'result_truncated': {'required': True},
        'data': {'required': True},
    }

    _attribute_map = {
        'total_records': {'key': 'totalRecords', 'type': 'long'},
        'count': {'key': 'count', 'type': 'long'},
        'result_truncated': {'key': 'resultTruncated', 'type': 'str'},
        'skip_token': {'key': '$skipToken', 'type': 'str'},
        'data': {'key': 'data', 'type': 'object'},
        'facets': {'key': 'facets', 'type': '[Facet]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueryResponse, self).__init__(**kwargs)
        self.total_records = kwargs['total_records']
        self.count = kwargs['count']
        self.result_truncated = kwargs['result_truncated']
        self.skip_token = kwargs.get('skip_token', None)
        self.data = kwargs['data']
        self.facets = kwargs.get('facets', None)


class ResourceChangeData(msrest.serialization.Model):
    """Data on a specific change, represented by a pair of before and after resource snapshots.

    All required parameters must be populated in order to send to Azure.

    :param change_id: Required. The change ID. Valid and unique within the specified resource only.
    :type change_id: str
    :param before_snapshot: Required. The snapshot before the change.
    :type before_snapshot: ~resource_graph_client.models.ResourceSnapshotData
    :param after_snapshot: Required. The snapshot after the change.
    :type after_snapshot: ~resource_graph_client.models.ResourceSnapshotData
    :param change_type: The change type for snapshot. PropertyChanges will be provided in case of
     Update change type. Possible values include: "Create", "Update", "Delete".
    :type change_type: str or ~resource_graph_client.models.ChangeType
    :param property_changes: An array of resource property change.
    :type property_changes: list[~resource_graph_client.models.ResourcePropertyChange]
    """

    _validation = {
        'change_id': {'required': True},
        'before_snapshot': {'required': True},
        'after_snapshot': {'required': True},
    }

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'str'},
        'before_snapshot': {'key': 'beforeSnapshot', 'type': 'ResourceSnapshotData'},
        'after_snapshot': {'key': 'afterSnapshot', 'type': 'ResourceSnapshotData'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'property_changes': {'key': 'propertyChanges', 'type': '[ResourcePropertyChange]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangeData, self).__init__(**kwargs)
        self.change_id = kwargs['change_id']
        self.before_snapshot = kwargs['before_snapshot']
        self.after_snapshot = kwargs['after_snapshot']
        self.change_type = kwargs.get('change_type', None)
        self.property_changes = kwargs.get('property_changes', None)


class ResourceSnapshotData(msrest.serialization.Model):
    """Data on a specific resource snapshot.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. The time when the snapshot was created.
     The snapshot timestamp provides an approximation as to when a modification to a resource was
     detected.  There can be a difference between the actual modification time and the detection
     time.  This is due to differences in how operations that modify a resource are processed,
     versus how operation that record resource snapshots are processed.
    :type timestamp: ~datetime.datetime
    :param content: The resource snapshot content (in resourceChangeDetails response only).
    :type content: object
    """

    _validation = {
        'timestamp': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'content': {'key': 'content', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceSnapshotData, self).__init__(**kwargs)
        self.timestamp = kwargs['timestamp']
        self.content = kwargs.get('content', None)


class ResourceChangeDataAfterSnapshot(ResourceSnapshotData):
    """The snapshot after the change.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. The time when the snapshot was created.
     The snapshot timestamp provides an approximation as to when a modification to a resource was
     detected.  There can be a difference between the actual modification time and the detection
     time.  This is due to differences in how operations that modify a resource are processed,
     versus how operation that record resource snapshots are processed.
    :type timestamp: ~datetime.datetime
    :param content: The resource snapshot content (in resourceChangeDetails response only).
    :type content: object
    """

    _validation = {
        'timestamp': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'content': {'key': 'content', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangeDataAfterSnapshot, self).__init__(**kwargs)


class ResourceChangeDataBeforeSnapshot(ResourceSnapshotData):
    """The snapshot before the change.

    All required parameters must be populated in order to send to Azure.

    :param timestamp: Required. The time when the snapshot was created.
     The snapshot timestamp provides an approximation as to when a modification to a resource was
     detected.  There can be a difference between the actual modification time and the detection
     time.  This is due to differences in how operations that modify a resource are processed,
     versus how operation that record resource snapshots are processed.
    :type timestamp: ~datetime.datetime
    :param content: The resource snapshot content (in resourceChangeDetails response only).
    :type content: object
    """

    _validation = {
        'timestamp': {'required': True},
    }

    _attribute_map = {
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'content': {'key': 'content', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangeDataBeforeSnapshot, self).__init__(**kwargs)


class ResourceChangeDetailsRequestParameters(msrest.serialization.Model):
    """The parameters for a specific change details request.

    All required parameters must be populated in order to send to Azure.

    :param resource_id: Required. Specifies the resource for a change details request.
    :type resource_id: str
    :param change_id: Required. Specifies the change ID.
    :type change_id: str
    """

    _validation = {
        'resource_id': {'required': True},
        'change_id': {'required': True},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'change_id': {'key': 'changeId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangeDetailsRequestParameters, self).__init__(**kwargs)
        self.resource_id = kwargs['resource_id']
        self.change_id = kwargs['change_id']


class ResourceChangeList(msrest.serialization.Model):
    """A list of changes associated with a resource over a specific time interval.

    :param changes: The pageable value returned by the operation, i.e. a list of changes to the
     resource.
    
    
     * The list is ordered from the most recent changes to the least recent changes.
     * This list will be empty if there were no changes during the requested interval.
     * The ``Before`` snapshot timestamp value of the oldest change can be outside of the specified
     time interval.
    :type changes: list[~resource_graph_client.models.ResourceChangeData]
    :param skip_token: Skip token that encodes the skip information while executing the current
     request.
    :type skip_token: object
    """

    _attribute_map = {
        'changes': {'key': 'changes', 'type': '[ResourceChangeData]'},
        'skip_token': {'key': '$skipToken', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangeList, self).__init__(**kwargs)
        self.changes = kwargs.get('changes', None)
        self.skip_token = kwargs.get('skip_token', None)


class ResourceChangesRequestParameters(msrest.serialization.Model):
    """The parameters for a specific changes request.

    All required parameters must be populated in order to send to Azure.

    :param resource_id: Required. Specifies the resource for a changes request.
    :type resource_id: str
    :param interval: Required. Specifies the date and time interval for a changes request.
    :type interval: ~resource_graph_client.models.DateTimeInterval
    :param skip_token: Acts as the continuation token for paged responses.
    :type skip_token: str
    :param top: The maximum number of changes the client can accept in a paged response.
    :type top: int
    :param fetch_property_changes: The flag if set to true will fetch property changes.
    :type fetch_property_changes: bool
    """

    _validation = {
        'resource_id': {'required': True},
        'interval': {'required': True},
        'top': {'maximum': 1000, 'minimum': 1},
    }

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'interval': {'key': 'interval', 'type': 'DateTimeInterval'},
        'skip_token': {'key': '$skipToken', 'type': 'str'},
        'top': {'key': '$top', 'type': 'int'},
        'fetch_property_changes': {'key': 'fetchPropertyChanges', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangesRequestParameters, self).__init__(**kwargs)
        self.resource_id = kwargs['resource_id']
        self.interval = kwargs['interval']
        self.skip_token = kwargs.get('skip_token', None)
        self.top = kwargs.get('top', None)
        self.fetch_property_changes = kwargs.get('fetch_property_changes', None)


class ResourceChangesRequestParametersInterval(DateTimeInterval):
    """Specifies the date and time interval for a changes request.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. A datetime indicating the inclusive/closed start of the time interval,
     i.e. ``[``\ **\ ``start``\ **\ ``, end)``. Specifying a ``start`` that occurs chronologically
     after ``end`` will result in an error.
    :type start: ~datetime.datetime
    :param end: Required. A datetime indicating the exclusive/open end of the time interval, i.e.
     ``[start,``\ **\ ``end``\ **\ ``)``. Specifying an ``end`` that occurs chronologically before
     ``start`` will result in an error.
    :type end: ~datetime.datetime
    """

    _validation = {
        'start': {'required': True},
        'end': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'start', 'type': 'iso-8601'},
        'end': {'key': 'end', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceChangesRequestParametersInterval, self).__init__(**kwargs)


class ResourcePropertyChange(msrest.serialization.Model):
    """The resource property change.

    All required parameters must be populated in order to send to Azure.

    :param property_name: Required. The property name.
    :type property_name: str
    :param before_value: The property value in before snapshot.
    :type before_value: str
    :param after_value: The property value in after snapshot.
    :type after_value: str
    :param change_category: Required. The change category. Possible values include: "User",
     "System".
    :type change_category: str or ~resource_graph_client.models.ChangeCategory
    :param property_change_type: Required. The property change Type. Possible values include:
     "Insert", "Update", "Remove".
    :type property_change_type: str or ~resource_graph_client.models.PropertyChangeType
    """

    _validation = {
        'property_name': {'required': True},
        'change_category': {'required': True},
        'property_change_type': {'required': True},
    }

    _attribute_map = {
        'property_name': {'key': 'propertyName', 'type': 'str'},
        'before_value': {'key': 'beforeValue', 'type': 'str'},
        'after_value': {'key': 'afterValue', 'type': 'str'},
        'change_category': {'key': 'changeCategory', 'type': 'str'},
        'property_change_type': {'key': 'propertyChangeType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourcePropertyChange, self).__init__(**kwargs)
        self.property_name = kwargs['property_name']
        self.before_value = kwargs.get('before_value', None)
        self.after_value = kwargs.get('after_value', None)
        self.change_category = kwargs['change_category']
        self.property_change_type = kwargs['property_change_type']


class Table(msrest.serialization.Model):
    """Query output in tabular format.

    All required parameters must be populated in order to send to Azure.

    :param columns: Required. Query result column descriptors.
    :type columns: list[~resource_graph_client.models.Column]
    :param rows: Required. Query result rows.
    :type rows: list[list[object]]
    """

    _validation = {
        'columns': {'required': True},
        'rows': {'required': True},
    }

    _attribute_map = {
        'columns': {'key': 'columns', 'type': '[Column]'},
        'rows': {'key': 'rows', 'type': '[[object]]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Table, self).__init__(**kwargs)
        self.columns = kwargs['columns']
        self.rows = kwargs['rows']