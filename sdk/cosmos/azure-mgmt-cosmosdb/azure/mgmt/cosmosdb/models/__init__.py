# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ARMProxyResource
    from ._models_py3 import ARMResourceProperties
    from ._models_py3 import ApiProperties
    from ._models_py3 import AutoUpgradePolicyResource
    from ._models_py3 import AutoscaleSettings
    from ._models_py3 import AutoscaleSettingsResource
    from ._models_py3 import Capability
    from ._models_py3 import CassandraKeyspaceCreateUpdateParameters
    from ._models_py3 import CassandraKeyspaceGetPropertiesOptions
    from ._models_py3 import CassandraKeyspaceGetPropertiesResource
    from ._models_py3 import CassandraKeyspaceGetResults
    from ._models_py3 import CassandraKeyspaceListResult
    from ._models_py3 import CassandraKeyspaceResource
    from ._models_py3 import CassandraPartitionKey
    from ._models_py3 import CassandraSchema
    from ._models_py3 import CassandraTableCreateUpdateParameters
    from ._models_py3 import CassandraTableGetPropertiesOptions
    from ._models_py3 import CassandraTableGetPropertiesResource
    from ._models_py3 import CassandraTableGetResults
    from ._models_py3 import CassandraTableListResult
    from ._models_py3 import CassandraTableResource
    from ._models_py3 import ClusterKey
    from ._models_py3 import Column
    from ._models_py3 import CompositePath
    from ._models_py3 import ConflictResolutionPolicy
    from ._models_py3 import ConsistencyPolicy
    from ._models_py3 import ContainerPartitionKey
    from ._models_py3 import CorsPolicy
    from ._models_py3 import CreateUpdateOptions
    from ._models_py3 import DatabaseAccountConnectionString
    from ._models_py3 import DatabaseAccountCreateUpdateParameters
    from ._models_py3 import DatabaseAccountGetResults
    from ._models_py3 import DatabaseAccountListConnectionStringsResult
    from ._models_py3 import DatabaseAccountListKeysResult
    from ._models_py3 import DatabaseAccountListReadOnlyKeysResult
    from ._models_py3 import DatabaseAccountRegenerateKeyParameters
    from ._models_py3 import DatabaseAccountUpdateParameters
    from ._models_py3 import DatabaseAccountsListResult
    from ._models_py3 import ErrorResponse
    from ._models_py3 import ExcludedPath
    from ._models_py3 import ExtendedResourceProperties
    from ._models_py3 import FailoverPolicies
    from ._models_py3 import FailoverPolicy
    from ._models_py3 import GremlinDatabaseCreateUpdateParameters
    from ._models_py3 import GremlinDatabaseGetPropertiesOptions
    from ._models_py3 import GremlinDatabaseGetPropertiesResource
    from ._models_py3 import GremlinDatabaseGetResults
    from ._models_py3 import GremlinDatabaseListResult
    from ._models_py3 import GremlinDatabaseResource
    from ._models_py3 import GremlinGraphCreateUpdateParameters
    from ._models_py3 import GremlinGraphGetPropertiesOptions
    from ._models_py3 import GremlinGraphGetPropertiesResource
    from ._models_py3 import GremlinGraphGetResults
    from ._models_py3 import GremlinGraphListResult
    from ._models_py3 import GremlinGraphResource
    from ._models_py3 import IncludedPath
    from ._models_py3 import Indexes
    from ._models_py3 import IndexingPolicy
    from ._models_py3 import IpAddressOrRange
    from ._models_py3 import Location
    from ._models_py3 import Metric
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricDefinition
    from ._models_py3 import MetricDefinitionsListResult
    from ._models_py3 import MetricListResult
    from ._models_py3 import MetricName
    from ._models_py3 import MetricValue
    from ._models_py3 import MongoDBCollectionCreateUpdateParameters
    from ._models_py3 import MongoDBCollectionGetPropertiesOptions
    from ._models_py3 import MongoDBCollectionGetPropertiesResource
    from ._models_py3 import MongoDBCollectionGetResults
    from ._models_py3 import MongoDBCollectionListResult
    from ._models_py3 import MongoDBCollectionResource
    from ._models_py3 import MongoDBDatabaseCreateUpdateParameters
    from ._models_py3 import MongoDBDatabaseGetPropertiesOptions
    from ._models_py3 import MongoDBDatabaseGetPropertiesResource
    from ._models_py3 import MongoDBDatabaseGetResults
    from ._models_py3 import MongoDBDatabaseListResult
    from ._models_py3 import MongoDBDatabaseResource
    from ._models_py3 import MongoIndex
    from ._models_py3 import MongoIndexKeys
    from ._models_py3 import MongoIndexOptions
    from ._models_py3 import NotebookWorkspace
    from ._models_py3 import NotebookWorkspaceConnectionInfoResult
    from ._models_py3 import NotebookWorkspaceCreateUpdateParameters
    from ._models_py3 import NotebookWorkspaceListResult
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OptionsResource
    from ._models_py3 import PartitionMetric
    from ._models_py3 import PartitionMetricListResult
    from ._models_py3 import PartitionUsage
    from ._models_py3 import PartitionUsagesResult
    from ._models_py3 import PercentileMetric
    from ._models_py3 import PercentileMetricListResult
    from ._models_py3 import PercentileMetricValue
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionAutoGenerated
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import PrivateLinkServiceConnectionStatePropertyAutoGenerated
    from ._models_py3 import ProxyResource
    from ._models_py3 import RegionForOnlineOffline
    from ._models_py3 import Resource
    from ._models_py3 import SpatialSpec
    from ._models_py3 import SqlContainerCreateUpdateParameters
    from ._models_py3 import SqlContainerGetPropertiesOptions
    from ._models_py3 import SqlContainerGetPropertiesResource
    from ._models_py3 import SqlContainerGetResults
    from ._models_py3 import SqlContainerListResult
    from ._models_py3 import SqlContainerResource
    from ._models_py3 import SqlDatabaseCreateUpdateParameters
    from ._models_py3 import SqlDatabaseGetPropertiesOptions
    from ._models_py3 import SqlDatabaseGetPropertiesResource
    from ._models_py3 import SqlDatabaseGetResults
    from ._models_py3 import SqlDatabaseListResult
    from ._models_py3 import SqlDatabaseResource
    from ._models_py3 import SqlStoredProcedureCreateUpdateParameters
    from ._models_py3 import SqlStoredProcedureGetPropertiesResource
    from ._models_py3 import SqlStoredProcedureGetResults
    from ._models_py3 import SqlStoredProcedureListResult
    from ._models_py3 import SqlStoredProcedureResource
    from ._models_py3 import SqlTriggerCreateUpdateParameters
    from ._models_py3 import SqlTriggerGetPropertiesResource
    from ._models_py3 import SqlTriggerGetResults
    from ._models_py3 import SqlTriggerListResult
    from ._models_py3 import SqlTriggerResource
    from ._models_py3 import SqlUserDefinedFunctionCreateUpdateParameters
    from ._models_py3 import SqlUserDefinedFunctionGetPropertiesResource
    from ._models_py3 import SqlUserDefinedFunctionGetResults
    from ._models_py3 import SqlUserDefinedFunctionListResult
    from ._models_py3 import SqlUserDefinedFunctionResource
    from ._models_py3 import TableCreateUpdateParameters
    from ._models_py3 import TableGetPropertiesOptions
    from ._models_py3 import TableGetPropertiesResource
    from ._models_py3 import TableGetResults
    from ._models_py3 import TableListResult
    from ._models_py3 import TableResource
    from ._models_py3 import ThroughputPolicyResource
    from ._models_py3 import ThroughputSettingsGetPropertiesResource
    from ._models_py3 import ThroughputSettingsGetResults
    from ._models_py3 import ThroughputSettingsResource
    from ._models_py3 import ThroughputSettingsUpdateParameters
    from ._models_py3 import UniqueKey
    from ._models_py3 import UniqueKeyPolicy
    from ._models_py3 import Usage
    from ._models_py3 import UsagesResult
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import ARMProxyResource  # type: ignore
    from ._models import ARMResourceProperties  # type: ignore
    from ._models import ApiProperties  # type: ignore
    from ._models import AutoUpgradePolicyResource  # type: ignore
    from ._models import AutoscaleSettings  # type: ignore
    from ._models import AutoscaleSettingsResource  # type: ignore
    from ._models import Capability  # type: ignore
    from ._models import CassandraKeyspaceCreateUpdateParameters  # type: ignore
    from ._models import CassandraKeyspaceGetPropertiesOptions  # type: ignore
    from ._models import CassandraKeyspaceGetPropertiesResource  # type: ignore
    from ._models import CassandraKeyspaceGetResults  # type: ignore
    from ._models import CassandraKeyspaceListResult  # type: ignore
    from ._models import CassandraKeyspaceResource  # type: ignore
    from ._models import CassandraPartitionKey  # type: ignore
    from ._models import CassandraSchema  # type: ignore
    from ._models import CassandraTableCreateUpdateParameters  # type: ignore
    from ._models import CassandraTableGetPropertiesOptions  # type: ignore
    from ._models import CassandraTableGetPropertiesResource  # type: ignore
    from ._models import CassandraTableGetResults  # type: ignore
    from ._models import CassandraTableListResult  # type: ignore
    from ._models import CassandraTableResource  # type: ignore
    from ._models import ClusterKey  # type: ignore
    from ._models import Column  # type: ignore
    from ._models import CompositePath  # type: ignore
    from ._models import ConflictResolutionPolicy  # type: ignore
    from ._models import ConsistencyPolicy  # type: ignore
    from ._models import ContainerPartitionKey  # type: ignore
    from ._models import CorsPolicy  # type: ignore
    from ._models import CreateUpdateOptions  # type: ignore
    from ._models import DatabaseAccountConnectionString  # type: ignore
    from ._models import DatabaseAccountCreateUpdateParameters  # type: ignore
    from ._models import DatabaseAccountGetResults  # type: ignore
    from ._models import DatabaseAccountListConnectionStringsResult  # type: ignore
    from ._models import DatabaseAccountListKeysResult  # type: ignore
    from ._models import DatabaseAccountListReadOnlyKeysResult  # type: ignore
    from ._models import DatabaseAccountRegenerateKeyParameters  # type: ignore
    from ._models import DatabaseAccountUpdateParameters  # type: ignore
    from ._models import DatabaseAccountsListResult  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import ExcludedPath  # type: ignore
    from ._models import ExtendedResourceProperties  # type: ignore
    from ._models import FailoverPolicies  # type: ignore
    from ._models import FailoverPolicy  # type: ignore
    from ._models import GremlinDatabaseCreateUpdateParameters  # type: ignore
    from ._models import GremlinDatabaseGetPropertiesOptions  # type: ignore
    from ._models import GremlinDatabaseGetPropertiesResource  # type: ignore
    from ._models import GremlinDatabaseGetResults  # type: ignore
    from ._models import GremlinDatabaseListResult  # type: ignore
    from ._models import GremlinDatabaseResource  # type: ignore
    from ._models import GremlinGraphCreateUpdateParameters  # type: ignore
    from ._models import GremlinGraphGetPropertiesOptions  # type: ignore
    from ._models import GremlinGraphGetPropertiesResource  # type: ignore
    from ._models import GremlinGraphGetResults  # type: ignore
    from ._models import GremlinGraphListResult  # type: ignore
    from ._models import GremlinGraphResource  # type: ignore
    from ._models import IncludedPath  # type: ignore
    from ._models import Indexes  # type: ignore
    from ._models import IndexingPolicy  # type: ignore
    from ._models import IpAddressOrRange  # type: ignore
    from ._models import Location  # type: ignore
    from ._models import Metric  # type: ignore
    from ._models import MetricAvailability  # type: ignore
    from ._models import MetricDefinition  # type: ignore
    from ._models import MetricDefinitionsListResult  # type: ignore
    from ._models import MetricListResult  # type: ignore
    from ._models import MetricName  # type: ignore
    from ._models import MetricValue  # type: ignore
    from ._models import MongoDBCollectionCreateUpdateParameters  # type: ignore
    from ._models import MongoDBCollectionGetPropertiesOptions  # type: ignore
    from ._models import MongoDBCollectionGetPropertiesResource  # type: ignore
    from ._models import MongoDBCollectionGetResults  # type: ignore
    from ._models import MongoDBCollectionListResult  # type: ignore
    from ._models import MongoDBCollectionResource  # type: ignore
    from ._models import MongoDBDatabaseCreateUpdateParameters  # type: ignore
    from ._models import MongoDBDatabaseGetPropertiesOptions  # type: ignore
    from ._models import MongoDBDatabaseGetPropertiesResource  # type: ignore
    from ._models import MongoDBDatabaseGetResults  # type: ignore
    from ._models import MongoDBDatabaseListResult  # type: ignore
    from ._models import MongoDBDatabaseResource  # type: ignore
    from ._models import MongoIndex  # type: ignore
    from ._models import MongoIndexKeys  # type: ignore
    from ._models import MongoIndexOptions  # type: ignore
    from ._models import NotebookWorkspace  # type: ignore
    from ._models import NotebookWorkspaceConnectionInfoResult  # type: ignore
    from ._models import NotebookWorkspaceCreateUpdateParameters  # type: ignore
    from ._models import NotebookWorkspaceListResult  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OptionsResource  # type: ignore
    from ._models import PartitionMetric  # type: ignore
    from ._models import PartitionMetricListResult  # type: ignore
    from ._models import PartitionUsage  # type: ignore
    from ._models import PartitionUsagesResult  # type: ignore
    from ._models import PercentileMetric  # type: ignore
    from ._models import PercentileMetricListResult  # type: ignore
    from ._models import PercentileMetricValue  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionAutoGenerated  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateEndpointProperty  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkServiceConnectionStateProperty  # type: ignore
    from ._models import PrivateLinkServiceConnectionStatePropertyAutoGenerated  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import RegionForOnlineOffline  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SpatialSpec  # type: ignore
    from ._models import SqlContainerCreateUpdateParameters  # type: ignore
    from ._models import SqlContainerGetPropertiesOptions  # type: ignore
    from ._models import SqlContainerGetPropertiesResource  # type: ignore
    from ._models import SqlContainerGetResults  # type: ignore
    from ._models import SqlContainerListResult  # type: ignore
    from ._models import SqlContainerResource  # type: ignore
    from ._models import SqlDatabaseCreateUpdateParameters  # type: ignore
    from ._models import SqlDatabaseGetPropertiesOptions  # type: ignore
    from ._models import SqlDatabaseGetPropertiesResource  # type: ignore
    from ._models import SqlDatabaseGetResults  # type: ignore
    from ._models import SqlDatabaseListResult  # type: ignore
    from ._models import SqlDatabaseResource  # type: ignore
    from ._models import SqlStoredProcedureCreateUpdateParameters  # type: ignore
    from ._models import SqlStoredProcedureGetPropertiesResource  # type: ignore
    from ._models import SqlStoredProcedureGetResults  # type: ignore
    from ._models import SqlStoredProcedureListResult  # type: ignore
    from ._models import SqlStoredProcedureResource  # type: ignore
    from ._models import SqlTriggerCreateUpdateParameters  # type: ignore
    from ._models import SqlTriggerGetPropertiesResource  # type: ignore
    from ._models import SqlTriggerGetResults  # type: ignore
    from ._models import SqlTriggerListResult  # type: ignore
    from ._models import SqlTriggerResource  # type: ignore
    from ._models import SqlUserDefinedFunctionCreateUpdateParameters  # type: ignore
    from ._models import SqlUserDefinedFunctionGetPropertiesResource  # type: ignore
    from ._models import SqlUserDefinedFunctionGetResults  # type: ignore
    from ._models import SqlUserDefinedFunctionListResult  # type: ignore
    from ._models import SqlUserDefinedFunctionResource  # type: ignore
    from ._models import TableCreateUpdateParameters  # type: ignore
    from ._models import TableGetPropertiesOptions  # type: ignore
    from ._models import TableGetPropertiesResource  # type: ignore
    from ._models import TableGetResults  # type: ignore
    from ._models import TableListResult  # type: ignore
    from ._models import TableResource  # type: ignore
    from ._models import ThroughputPolicyResource  # type: ignore
    from ._models import ThroughputSettingsGetPropertiesResource  # type: ignore
    from ._models import ThroughputSettingsGetResults  # type: ignore
    from ._models import ThroughputSettingsResource  # type: ignore
    from ._models import ThroughputSettingsUpdateParameters  # type: ignore
    from ._models import UniqueKey  # type: ignore
    from ._models import UniqueKeyPolicy  # type: ignore
    from ._models import Usage  # type: ignore
    from ._models import UsagesResult  # type: ignore
    from ._models import VirtualNetworkRule  # type: ignore

from ._cosmos_db_management_client_enums import (
    CompositePathSortOrder,
    ConflictResolutionMode,
    ConnectorOffer,
    DataType,
    DatabaseAccountKind,
    DefaultConsistencyLevel,
    IndexKind,
    IndexingMode,
    KeyKind,
    NotebookWorkspaceName,
    PartitionKind,
    PrimaryAggregationType,
    PublicNetworkAccess,
    ServerVersion,
    SpatialType,
    TriggerOperation,
    TriggerType,
    UnitType,
)

__all__ = [
    'ARMProxyResource',
    'ARMResourceProperties',
    'ApiProperties',
    'AutoUpgradePolicyResource',
    'AutoscaleSettings',
    'AutoscaleSettingsResource',
    'Capability',
    'CassandraKeyspaceCreateUpdateParameters',
    'CassandraKeyspaceGetPropertiesOptions',
    'CassandraKeyspaceGetPropertiesResource',
    'CassandraKeyspaceGetResults',
    'CassandraKeyspaceListResult',
    'CassandraKeyspaceResource',
    'CassandraPartitionKey',
    'CassandraSchema',
    'CassandraTableCreateUpdateParameters',
    'CassandraTableGetPropertiesOptions',
    'CassandraTableGetPropertiesResource',
    'CassandraTableGetResults',
    'CassandraTableListResult',
    'CassandraTableResource',
    'ClusterKey',
    'Column',
    'CompositePath',
    'ConflictResolutionPolicy',
    'ConsistencyPolicy',
    'ContainerPartitionKey',
    'CorsPolicy',
    'CreateUpdateOptions',
    'DatabaseAccountConnectionString',
    'DatabaseAccountCreateUpdateParameters',
    'DatabaseAccountGetResults',
    'DatabaseAccountListConnectionStringsResult',
    'DatabaseAccountListKeysResult',
    'DatabaseAccountListReadOnlyKeysResult',
    'DatabaseAccountRegenerateKeyParameters',
    'DatabaseAccountUpdateParameters',
    'DatabaseAccountsListResult',
    'ErrorResponse',
    'ExcludedPath',
    'ExtendedResourceProperties',
    'FailoverPolicies',
    'FailoverPolicy',
    'GremlinDatabaseCreateUpdateParameters',
    'GremlinDatabaseGetPropertiesOptions',
    'GremlinDatabaseGetPropertiesResource',
    'GremlinDatabaseGetResults',
    'GremlinDatabaseListResult',
    'GremlinDatabaseResource',
    'GremlinGraphCreateUpdateParameters',
    'GremlinGraphGetPropertiesOptions',
    'GremlinGraphGetPropertiesResource',
    'GremlinGraphGetResults',
    'GremlinGraphListResult',
    'GremlinGraphResource',
    'IncludedPath',
    'Indexes',
    'IndexingPolicy',
    'IpAddressOrRange',
    'Location',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'MetricDefinitionsListResult',
    'MetricListResult',
    'MetricName',
    'MetricValue',
    'MongoDBCollectionCreateUpdateParameters',
    'MongoDBCollectionGetPropertiesOptions',
    'MongoDBCollectionGetPropertiesResource',
    'MongoDBCollectionGetResults',
    'MongoDBCollectionListResult',
    'MongoDBCollectionResource',
    'MongoDBDatabaseCreateUpdateParameters',
    'MongoDBDatabaseGetPropertiesOptions',
    'MongoDBDatabaseGetPropertiesResource',
    'MongoDBDatabaseGetResults',
    'MongoDBDatabaseListResult',
    'MongoDBDatabaseResource',
    'MongoIndex',
    'MongoIndexKeys',
    'MongoIndexOptions',
    'NotebookWorkspace',
    'NotebookWorkspaceConnectionInfoResult',
    'NotebookWorkspaceCreateUpdateParameters',
    'NotebookWorkspaceListResult',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OptionsResource',
    'PartitionMetric',
    'PartitionMetricListResult',
    'PartitionUsage',
    'PartitionUsagesResult',
    'PercentileMetric',
    'PercentileMetricListResult',
    'PercentileMetricValue',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionAutoGenerated',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionStateProperty',
    'PrivateLinkServiceConnectionStatePropertyAutoGenerated',
    'ProxyResource',
    'RegionForOnlineOffline',
    'Resource',
    'SpatialSpec',
    'SqlContainerCreateUpdateParameters',
    'SqlContainerGetPropertiesOptions',
    'SqlContainerGetPropertiesResource',
    'SqlContainerGetResults',
    'SqlContainerListResult',
    'SqlContainerResource',
    'SqlDatabaseCreateUpdateParameters',
    'SqlDatabaseGetPropertiesOptions',
    'SqlDatabaseGetPropertiesResource',
    'SqlDatabaseGetResults',
    'SqlDatabaseListResult',
    'SqlDatabaseResource',
    'SqlStoredProcedureCreateUpdateParameters',
    'SqlStoredProcedureGetPropertiesResource',
    'SqlStoredProcedureGetResults',
    'SqlStoredProcedureListResult',
    'SqlStoredProcedureResource',
    'SqlTriggerCreateUpdateParameters',
    'SqlTriggerGetPropertiesResource',
    'SqlTriggerGetResults',
    'SqlTriggerListResult',
    'SqlTriggerResource',
    'SqlUserDefinedFunctionCreateUpdateParameters',
    'SqlUserDefinedFunctionGetPropertiesResource',
    'SqlUserDefinedFunctionGetResults',
    'SqlUserDefinedFunctionListResult',
    'SqlUserDefinedFunctionResource',
    'TableCreateUpdateParameters',
    'TableGetPropertiesOptions',
    'TableGetPropertiesResource',
    'TableGetResults',
    'TableListResult',
    'TableResource',
    'ThroughputPolicyResource',
    'ThroughputSettingsGetPropertiesResource',
    'ThroughputSettingsGetResults',
    'ThroughputSettingsResource',
    'ThroughputSettingsUpdateParameters',
    'UniqueKey',
    'UniqueKeyPolicy',
    'Usage',
    'UsagesResult',
    'VirtualNetworkRule',
    'CompositePathSortOrder',
    'ConflictResolutionMode',
    'ConnectorOffer',
    'DataType',
    'DatabaseAccountKind',
    'DefaultConsistencyLevel',
    'IndexKind',
    'IndexingMode',
    'KeyKind',
    'NotebookWorkspaceName',
    'PartitionKind',
    'PrimaryAggregationType',
    'PublicNetworkAccess',
    'ServerVersion',
    'SpatialType',
    'TriggerOperation',
    'TriggerType',
    'UnitType',
]