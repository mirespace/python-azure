# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AddRemoveIncrementalNamedPartitionScalingMechanism
    from ._models_py3 import ApplicationHealthPolicy
    from ._models_py3 import ApplicationResource
    from ._models_py3 import ApplicationResourceList
    from ._models_py3 import ApplicationTypeResource
    from ._models_py3 import ApplicationTypeResourceList
    from ._models_py3 import ApplicationTypeUpdateParameters
    from ._models_py3 import ApplicationTypeVersionResource
    from ._models_py3 import ApplicationTypeVersionResourceList
    from ._models_py3 import ApplicationTypeVersionUpdateParameters
    from ._models_py3 import ApplicationTypeVersionsCleanupPolicy
    from ._models_py3 import ApplicationUpdateParameters
    from ._models_py3 import ApplicationUpgradePolicy
    from ._models_py3 import ApplicationUserAssignedIdentity
    from ._models_py3 import AvailableOperationDisplay
    from ._models_py3 import AveragePartitionLoadScalingTrigger
    from ._models_py3 import AverageServiceLoadScalingTrigger
    from ._models_py3 import AzureActiveDirectory
    from ._models_py3 import ClientCertificate
    from ._models_py3 import EndpointRangeDescription
    from ._models_py3 import ErrorModel
    from ._models_py3 import ErrorModelError
    from ._models_py3 import LoadBalancingRule
    from ._models_py3 import ManagedCluster
    from ._models_py3 import ManagedClusterCodeVersionResult
    from ._models_py3 import ManagedClusterListResult
    from ._models_py3 import ManagedClusterUpdateParameters
    from ._models_py3 import ManagedIdentity
    from ._models_py3 import ManagedProxyResource
    from ._models_py3 import NamedPartitionScheme
    from ._models_py3 import NetworkSecurityRule
    from ._models_py3 import NodeType
    from ._models_py3 import NodeTypeActionParameters
    from ._models_py3 import NodeTypeListResult
    from ._models_py3 import NodeTypeUpdateParameters
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationResult
    from ._models_py3 import Partition
    from ._models_py3 import PartitionInstanceCountScaleMechanism
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import RollingUpgradeMonitoringPolicy
    from ._models_py3 import ScalingMechanism
    from ._models_py3 import ScalingPolicy
    from ._models_py3 import ScalingTrigger
    from ._models_py3 import ServiceCorrelation
    from ._models_py3 import ServiceLoadMetric
    from ._models_py3 import ServicePlacementInvalidDomainPolicy
    from ._models_py3 import ServicePlacementNonPartiallyPlaceServicePolicy
    from ._models_py3 import ServicePlacementPolicy
    from ._models_py3 import ServicePlacementPreferPrimaryDomainPolicy
    from ._models_py3 import ServicePlacementRequireDomainDistributionPolicy
    from ._models_py3 import ServicePlacementRequiredDomainPolicy
    from ._models_py3 import ServiceResource
    from ._models_py3 import ServiceResourceList
    from ._models_py3 import ServiceResourceProperties
    from ._models_py3 import ServiceResourcePropertiesBase
    from ._models_py3 import ServiceTypeHealthPolicy
    from ._models_py3 import ServiceUpdateParameters
    from ._models_py3 import SettingsParameterDescription
    from ._models_py3 import SettingsSectionDescription
    from ._models_py3 import SingletonPartitionScheme
    from ._models_py3 import Sku
    from ._models_py3 import StatefulServiceProperties
    from ._models_py3 import StatelessServiceProperties
    from ._models_py3 import SubResource
    from ._models_py3 import SystemData
    from ._models_py3 import UniformInt64RangePartitionScheme
    from ._models_py3 import UserAssignedIdentity
    from ._models_py3 import VMSSExtension
    from ._models_py3 import VaultCertificate
    from ._models_py3 import VaultSecretGroup
    from ._models_py3 import VmManagedIdentity
except (SyntaxError, ImportError):
    from ._models import AddRemoveIncrementalNamedPartitionScalingMechanism  # type: ignore
    from ._models import ApplicationHealthPolicy  # type: ignore
    from ._models import ApplicationResource  # type: ignore
    from ._models import ApplicationResourceList  # type: ignore
    from ._models import ApplicationTypeResource  # type: ignore
    from ._models import ApplicationTypeResourceList  # type: ignore
    from ._models import ApplicationTypeUpdateParameters  # type: ignore
    from ._models import ApplicationTypeVersionResource  # type: ignore
    from ._models import ApplicationTypeVersionResourceList  # type: ignore
    from ._models import ApplicationTypeVersionUpdateParameters  # type: ignore
    from ._models import ApplicationTypeVersionsCleanupPolicy  # type: ignore
    from ._models import ApplicationUpdateParameters  # type: ignore
    from ._models import ApplicationUpgradePolicy  # type: ignore
    from ._models import ApplicationUserAssignedIdentity  # type: ignore
    from ._models import AvailableOperationDisplay  # type: ignore
    from ._models import AveragePartitionLoadScalingTrigger  # type: ignore
    from ._models import AverageServiceLoadScalingTrigger  # type: ignore
    from ._models import AzureActiveDirectory  # type: ignore
    from ._models import ClientCertificate  # type: ignore
    from ._models import EndpointRangeDescription  # type: ignore
    from ._models import ErrorModel  # type: ignore
    from ._models import ErrorModelError  # type: ignore
    from ._models import LoadBalancingRule  # type: ignore
    from ._models import ManagedCluster  # type: ignore
    from ._models import ManagedClusterCodeVersionResult  # type: ignore
    from ._models import ManagedClusterListResult  # type: ignore
    from ._models import ManagedClusterUpdateParameters  # type: ignore
    from ._models import ManagedIdentity  # type: ignore
    from ._models import ManagedProxyResource  # type: ignore
    from ._models import NamedPartitionScheme  # type: ignore
    from ._models import NetworkSecurityRule  # type: ignore
    from ._models import NodeType  # type: ignore
    from ._models import NodeTypeActionParameters  # type: ignore
    from ._models import NodeTypeListResult  # type: ignore
    from ._models import NodeTypeUpdateParameters  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationResult  # type: ignore
    from ._models import Partition  # type: ignore
    from ._models import PartitionInstanceCountScaleMechanism  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RollingUpgradeMonitoringPolicy  # type: ignore
    from ._models import ScalingMechanism  # type: ignore
    from ._models import ScalingPolicy  # type: ignore
    from ._models import ScalingTrigger  # type: ignore
    from ._models import ServiceCorrelation  # type: ignore
    from ._models import ServiceLoadMetric  # type: ignore
    from ._models import ServicePlacementInvalidDomainPolicy  # type: ignore
    from ._models import ServicePlacementNonPartiallyPlaceServicePolicy  # type: ignore
    from ._models import ServicePlacementPolicy  # type: ignore
    from ._models import ServicePlacementPreferPrimaryDomainPolicy  # type: ignore
    from ._models import ServicePlacementRequireDomainDistributionPolicy  # type: ignore
    from ._models import ServicePlacementRequiredDomainPolicy  # type: ignore
    from ._models import ServiceResource  # type: ignore
    from ._models import ServiceResourceList  # type: ignore
    from ._models import ServiceResourceProperties  # type: ignore
    from ._models import ServiceResourcePropertiesBase  # type: ignore
    from ._models import ServiceTypeHealthPolicy  # type: ignore
    from ._models import ServiceUpdateParameters  # type: ignore
    from ._models import SettingsParameterDescription  # type: ignore
    from ._models import SettingsSectionDescription  # type: ignore
    from ._models import SingletonPartitionScheme  # type: ignore
    from ._models import Sku  # type: ignore
    from ._models import StatefulServiceProperties  # type: ignore
    from ._models import StatelessServiceProperties  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import UniformInt64RangePartitionScheme  # type: ignore
    from ._models import UserAssignedIdentity  # type: ignore
    from ._models import VMSSExtension  # type: ignore
    from ._models import VaultCertificate  # type: ignore
    from ._models import VaultSecretGroup  # type: ignore
    from ._models import VmManagedIdentity  # type: ignore

from ._service_fabric_managed_clusters_management_client_enums import (
    Access,
    ClusterState,
    ClusterUpgradeCadence,
    ClusterUpgradeMode,
    Direction,
    DiskType,
    FailureAction,
    ManagedClusterAddOnFeature,
    ManagedIdentityType,
    ManagedResourceProvisioningState,
    MoveCost,
    NsgProtocol,
    PartitionScheme,
    ProbeProtocol,
    Protocol,
    RollingUpgradeMode,
    ServiceCorrelationScheme,
    ServiceKind,
    ServiceLoadMetricWeight,
    ServicePackageActivationMode,
    ServicePlacementPolicyType,
    ServiceScalingMechanismKind,
    ServiceScalingTriggerKind,
    SkuName,
)

__all__ = [
    'AddRemoveIncrementalNamedPartitionScalingMechanism',
    'ApplicationHealthPolicy',
    'ApplicationResource',
    'ApplicationResourceList',
    'ApplicationTypeResource',
    'ApplicationTypeResourceList',
    'ApplicationTypeUpdateParameters',
    'ApplicationTypeVersionResource',
    'ApplicationTypeVersionResourceList',
    'ApplicationTypeVersionUpdateParameters',
    'ApplicationTypeVersionsCleanupPolicy',
    'ApplicationUpdateParameters',
    'ApplicationUpgradePolicy',
    'ApplicationUserAssignedIdentity',
    'AvailableOperationDisplay',
    'AveragePartitionLoadScalingTrigger',
    'AverageServiceLoadScalingTrigger',
    'AzureActiveDirectory',
    'ClientCertificate',
    'EndpointRangeDescription',
    'ErrorModel',
    'ErrorModelError',
    'LoadBalancingRule',
    'ManagedCluster',
    'ManagedClusterCodeVersionResult',
    'ManagedClusterListResult',
    'ManagedClusterUpdateParameters',
    'ManagedIdentity',
    'ManagedProxyResource',
    'NamedPartitionScheme',
    'NetworkSecurityRule',
    'NodeType',
    'NodeTypeActionParameters',
    'NodeTypeListResult',
    'NodeTypeUpdateParameters',
    'OperationListResult',
    'OperationResult',
    'Partition',
    'PartitionInstanceCountScaleMechanism',
    'ProxyResource',
    'Resource',
    'RollingUpgradeMonitoringPolicy',
    'ScalingMechanism',
    'ScalingPolicy',
    'ScalingTrigger',
    'ServiceCorrelation',
    'ServiceLoadMetric',
    'ServicePlacementInvalidDomainPolicy',
    'ServicePlacementNonPartiallyPlaceServicePolicy',
    'ServicePlacementPolicy',
    'ServicePlacementPreferPrimaryDomainPolicy',
    'ServicePlacementRequireDomainDistributionPolicy',
    'ServicePlacementRequiredDomainPolicy',
    'ServiceResource',
    'ServiceResourceList',
    'ServiceResourceProperties',
    'ServiceResourcePropertiesBase',
    'ServiceTypeHealthPolicy',
    'ServiceUpdateParameters',
    'SettingsParameterDescription',
    'SettingsSectionDescription',
    'SingletonPartitionScheme',
    'Sku',
    'StatefulServiceProperties',
    'StatelessServiceProperties',
    'SubResource',
    'SystemData',
    'UniformInt64RangePartitionScheme',
    'UserAssignedIdentity',
    'VMSSExtension',
    'VaultCertificate',
    'VaultSecretGroup',
    'VmManagedIdentity',
    'Access',
    'ClusterState',
    'ClusterUpgradeCadence',
    'ClusterUpgradeMode',
    'Direction',
    'DiskType',
    'FailureAction',
    'ManagedClusterAddOnFeature',
    'ManagedIdentityType',
    'ManagedResourceProvisioningState',
    'MoveCost',
    'NsgProtocol',
    'PartitionScheme',
    'ProbeProtocol',
    'Protocol',
    'RollingUpgradeMode',
    'ServiceCorrelationScheme',
    'ServiceKind',
    'ServiceLoadMetricWeight',
    'ServicePackageActivationMode',
    'ServicePlacementPolicyType',
    'ServiceScalingMechanismKind',
    'ServiceScalingTriggerKind',
    'SkuName',
]