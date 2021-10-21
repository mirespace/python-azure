# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Advisor
    from ._models_py3 import AdvisorsResultList
    from ._models_py3 import CloudErrorAutoGenerated
    from ._models_py3 import Configuration
    from ._models_py3 import ConfigurationListResult
    from ._models_py3 import Database
    from ._models_py3 import DatabaseListResult
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorResponse
    from ._models_py3 import FirewallRule
    from ._models_py3 import FirewallRuleListResult
    from ._models_py3 import LogFile
    from ._models_py3 import LogFileListResult
    from ._models_py3 import NameAvailability
    from ._models_py3 import NameAvailabilityRequest
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import PerformanceTierListResult
    from ._models_py3 import PerformanceTierProperties
    from ._models_py3 import PerformanceTierServiceLevelObjectives
    from ._models_py3 import PrivateEndpointConnection
    from ._models_py3 import PrivateEndpointConnectionListResult
    from ._models_py3 import PrivateEndpointProperty
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceListResult
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ProxyResource
    from ._models_py3 import QueryStatistic
    from ._models_py3 import QueryText
    from ._models_py3 import QueryTextsResultList
    from ._models_py3 import RecommendationAction
    from ._models_py3 import RecommendationActionsResultList
    from ._models_py3 import RecommendedActionSessionsOperationStatus
    from ._models_py3 import Resource
    from ._models_py3 import Server
    from ._models_py3 import ServerForCreate
    from ._models_py3 import ServerListResult
    from ._models_py3 import ServerPrivateEndpointConnection
    from ._models_py3 import ServerPrivateEndpointConnectionProperties
    from ._models_py3 import ServerPrivateLinkServiceConnectionStateProperty
    from ._models_py3 import ServerPropertiesForCreate
    from ._models_py3 import ServerPropertiesForDefaultCreate
    from ._models_py3 import ServerPropertiesForGeoRestore
    from ._models_py3 import ServerPropertiesForReplica
    from ._models_py3 import ServerPropertiesForRestore
    from ._models_py3 import ServerSecurityAlertPolicy
    from ._models_py3 import ServerUpdateParameters
    from ._models_py3 import Sku
    from ._models_py3 import StorageProfile
    from ._models_py3 import TagsObject
    from ._models_py3 import TopQueryStatisticsInput
    from ._models_py3 import TopQueryStatisticsResultList
    from ._models_py3 import TrackedResource
    from ._models_py3 import VirtualNetworkRule
    from ._models_py3 import VirtualNetworkRuleListResult
    from ._models_py3 import WaitStatistic
    from ._models_py3 import WaitStatisticsInput
    from ._models_py3 import WaitStatisticsResultList
except (SyntaxError, ImportError):
    from ._models import Advisor  # type: ignore
    from ._models import AdvisorsResultList  # type: ignore
    from ._models import CloudErrorAutoGenerated  # type: ignore
    from ._models import Configuration  # type: ignore
    from ._models import ConfigurationListResult  # type: ignore
    from ._models import Database  # type: ignore
    from ._models import DatabaseListResult  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import FirewallRule  # type: ignore
    from ._models import FirewallRuleListResult  # type: ignore
    from ._models import LogFile  # type: ignore
    from ._models import LogFileListResult  # type: ignore
    from ._models import NameAvailability  # type: ignore
    from ._models import NameAvailabilityRequest  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import PerformanceTierListResult  # type: ignore
    from ._models import PerformanceTierProperties  # type: ignore
    from ._models import PerformanceTierServiceLevelObjectives  # type: ignore
    from ._models import PrivateEndpointConnection  # type: ignore
    from ._models import PrivateEndpointConnectionListResult  # type: ignore
    from ._models import PrivateEndpointProperty  # type: ignore
    from ._models import PrivateLinkResource  # type: ignore
    from ._models import PrivateLinkResourceListResult  # type: ignore
    from ._models import PrivateLinkResourceProperties  # type: ignore
    from ._models import PrivateLinkServiceConnectionStateProperty  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import QueryStatistic  # type: ignore
    from ._models import QueryText  # type: ignore
    from ._models import QueryTextsResultList  # type: ignore
    from ._models import RecommendationAction  # type: ignore
    from ._models import RecommendationActionsResultList  # type: ignore
    from ._models import RecommendedActionSessionsOperationStatus  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Server  # type: ignore
    from ._models import ServerForCreate  # type: ignore
    from ._models import ServerListResult  # type: ignore
    from ._models import ServerPrivateEndpointConnection  # type: ignore
    from ._models import ServerPrivateEndpointConnectionProperties  # type: ignore
    from ._models import ServerPrivateLinkServiceConnectionStateProperty  # type: ignore
    from ._models import ServerPropertiesForCreate  # type: ignore
    from ._models import ServerPropertiesForDefaultCreate  # type: ignore
    from ._models import ServerPropertiesForGeoRestore  # type: ignore
    from ._models import ServerPropertiesForReplica  # type: ignore
    from ._models import ServerPropertiesForRestore  # type: ignore
    from ._models import ServerSecurityAlertPolicy  # type: ignore
    from ._models import ServerUpdateParameters  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import TagsObject  # type: ignore
    from ._models import TopQueryStatisticsInput  # type: ignore
    from ._models import TopQueryStatisticsResultList  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import VirtualNetworkRule  # type: ignore
    from ._models import VirtualNetworkRuleListResult  # type: ignore
    from ._models import WaitStatistic  # type: ignore
    from ._models import WaitStatisticsInput  # type: ignore
    from ._models import WaitStatisticsResultList  # type: ignore

from ._maria_db_management_client_enums import (
    CreateMode,
    GeoRedundantBackup,
    OperationOrigin,
    PrivateEndpointProvisioningState,
    PrivateLinkServiceConnectionStateActionsRequire,
    PrivateLinkServiceConnectionStateStatus,
    PublicNetworkAccessEnum,
    SecurityAlertPolicyName,
    ServerSecurityAlertPolicyState,
    ServerState,
    ServerVersion,
    SkuTier,
    SslEnforcementEnum,
    StorageAutogrow,
    VirtualNetworkRuleState,
)

__all__ = [
    'Advisor',
    'AdvisorsResultList',
    'CloudErrorAutoGenerated',
    'Configuration',
    'ConfigurationListResult',
    'Database',
    'DatabaseListResult',
    'ErrorAdditionalInfo',
    'ErrorResponse',
    'FirewallRule',
    'FirewallRuleListResult',
    'LogFile',
    'LogFileListResult',
    'NameAvailability',
    'NameAvailabilityRequest',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PerformanceTierListResult',
    'PerformanceTierProperties',
    'PerformanceTierServiceLevelObjectives',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateEndpointProperty',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkResourceProperties',
    'PrivateLinkServiceConnectionStateProperty',
    'ProxyResource',
    'QueryStatistic',
    'QueryText',
    'QueryTextsResultList',
    'RecommendationAction',
    'RecommendationActionsResultList',
    'RecommendedActionSessionsOperationStatus',
    'Resource',
    'Server',
    'ServerForCreate',
    'ServerListResult',
    'ServerPrivateEndpointConnection',
    'ServerPrivateEndpointConnectionProperties',
    'ServerPrivateLinkServiceConnectionStateProperty',
    'ServerPropertiesForCreate',
    'ServerPropertiesForDefaultCreate',
    'ServerPropertiesForGeoRestore',
    'ServerPropertiesForReplica',
    'ServerPropertiesForRestore',
    'ServerSecurityAlertPolicy',
    'ServerUpdateParameters',
    'Sku',
    'StorageProfile',
    'TagsObject',
    'TopQueryStatisticsInput',
    'TopQueryStatisticsResultList',
    'TrackedResource',
    'VirtualNetworkRule',
    'VirtualNetworkRuleListResult',
    'WaitStatistic',
    'WaitStatisticsInput',
    'WaitStatisticsResultList',
    'CreateMode',
    'GeoRedundantBackup',
    'OperationOrigin',
    'PrivateEndpointProvisioningState',
    'PrivateLinkServiceConnectionStateActionsRequire',
    'PrivateLinkServiceConnectionStateStatus',
    'PublicNetworkAccessEnum',
    'SecurityAlertPolicyName',
    'ServerSecurityAlertPolicyState',
    'ServerState',
    'ServerVersion',
    'SkuTier',
    'SslEnforcementEnum',
    'StorageAutogrow',
    'VirtualNetworkRuleState',
]