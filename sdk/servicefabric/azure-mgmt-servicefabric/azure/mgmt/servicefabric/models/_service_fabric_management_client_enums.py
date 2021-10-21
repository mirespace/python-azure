# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AddOnFeatures(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Available cluster add-on features
    """

    REPAIR_MANAGER = "RepairManager"
    DNS_SERVICE = "DnsService"
    BACKUP_RESTORE_SERVICE = "BackupRestoreService"
    RESOURCE_MONITOR_SERVICE = "ResourceMonitorService"

class ArmServicePackageActivationMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The activation Mode of the service package
    """

    #: Indicates the application package activation mode will use shared process.
    SHARED_PROCESS = "SharedProcess"
    #: Indicates the application package activation mode will use exclusive process.
    EXCLUSIVE_PROCESS = "ExclusiveProcess"

class ArmUpgradeFailureAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The activation Mode of the service package
    """

    #: Indicates that a rollback of the upgrade will be performed by Service Fabric if the upgrade
    #: fails.
    ROLLBACK = "Rollback"
    #: Indicates that a manual repair will need to be performed by the administrator if the upgrade
    #: fails. Service Fabric will not proceed to the next upgrade domain automatically.
    MANUAL = "Manual"

class ClusterEnvironment(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Cluster operating system, the default will be Windows
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class ClusterState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of the cluster.
    
    
    * WaitingForNodes - Indicates that the cluster resource is created and the resource provider is
    waiting for Service Fabric VM extension to boot up and report to it.
    * Deploying - Indicates that the Service Fabric runtime is being installed on the VMs. Cluster
    resource will be in this state until the cluster boots up and system services are up.
    * BaselineUpgrade - Indicates that the cluster is upgrading to establishes the cluster version.
    This upgrade is automatically initiated when the cluster boots up for the first time.
    * UpdatingUserConfiguration - Indicates that the cluster is being upgraded with the user
    provided configuration.
    * UpdatingUserCertificate - Indicates that the cluster is being upgraded with the user provided
    certificate.
    * UpdatingInfrastructure - Indicates that the cluster is being upgraded with the latest Service
    Fabric runtime version. This happens only when the **upgradeMode** is set to 'Automatic'.
    * EnforcingClusterVersion - Indicates that cluster is on a different version than expected and
    the cluster is being upgraded to the expected version.
    * UpgradeServiceUnreachable - Indicates that the system service in the cluster is no longer
    polling the Resource Provider. Clusters in this state cannot be managed by the Resource
    Provider.
    * AutoScale - Indicates that the ReliabilityLevel of the cluster is being adjusted.
    * Ready - Indicates that the cluster is in a stable state.
    """

    WAITING_FOR_NODES = "WaitingForNodes"
    DEPLOYING = "Deploying"
    BASELINE_UPGRADE = "BaselineUpgrade"
    UPDATING_USER_CONFIGURATION = "UpdatingUserConfiguration"
    UPDATING_USER_CERTIFICATE = "UpdatingUserCertificate"
    UPDATING_INFRASTRUCTURE = "UpdatingInfrastructure"
    ENFORCING_CLUSTER_VERSION = "EnforcingClusterVersion"
    UPGRADE_SERVICE_UNREACHABLE = "UpgradeServiceUnreachable"
    AUTO_SCALE = "AutoScale"
    READY = "Ready"

class ClusterUpgradeCadence(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates when new cluster runtime version upgrades will be applied after they are released. By
    default is Wave0.
    """

    #: Cluster upgrade starts immediately after a new version is rolled out. Recommended for Test/Dev
    #: clusters.
    WAVE0 = "Wave0"
    #: Cluster upgrade starts 7 days after a new version is rolled out. Recommended for Pre-prod
    #: clusters.
    WAVE1 = "Wave1"
    #: Cluster upgrade starts 14 days after a new version is rolled out. Recommended for Production
    #: clusters.
    WAVE2 = "Wave2"

class DurabilityLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The durability level of the node type. Learn about `DurabilityLevel
    <https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-capacity>`_.
    
    
    * Bronze - No privileges. This is the default.
    * Silver - The infrastructure jobs can be paused for a duration of 10 minutes per UD.
    * Gold - The infrastructure jobs can be paused for a duration of 2 hours per UD. Gold
    durability can be enabled only on full node VM skus like D15_V2, G5 etc.
    """

    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"

class Enum14(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    WINDOWS = "Windows"
    LINUX = "Linux"

class ManagedIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of managed identity for the resource.
    """

    #: Indicates that system assigned identity is associated with the resource.
    SYSTEM_ASSIGNED = "SystemAssigned"
    #: Indicates that user assigned identity is associated with the resource.
    USER_ASSIGNED = "UserAssigned"
    #: Indicates that both system assigned and user assigned identity are associated with the
    #: resource.
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    #: Indicates that no identity is associated with the resource.
    NONE = "None"

class MoveCost(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the move cost for the service.
    """

    #: Zero move cost. This value is zero.
    ZERO = "Zero"
    #: Specifies the move cost of the service as Low. The value is 1.
    LOW = "Low"
    #: Specifies the move cost of the service as Medium. The value is 2.
    MEDIUM = "Medium"
    #: Specifies the move cost of the service as High. The value is 3.
    HIGH = "High"

class NotificationCategory(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The category of notification.
    """

    #: Notification will be regarding wave progress.
    WAVE_PROGRESS = "WaveProgress"

class NotificationChannel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The notification channel indicates the type of receivers subscribed to the notification, either
    user or subscription.
    """

    #: For email user receivers. In this case, the parameter receivers should be a list of email
    #: addresses that will receive the notifications.
    EMAIL_USER = "EmailUser"
    #: For subscription receivers. In this case, the parameter receivers should be a list of roles of
    #: the subscription for the cluster (eg. Owner, AccountAdmin, etc) that will receive the
    #: notifications.
    EMAIL_SUBSCRIPTION = "EmailSubscription"

class NotificationLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The level of notification.
    """

    #: Receive only critical notifications.
    CRITICAL = "Critical"
    #: Receive all notifications.
    ALL = "All"

class PartitionScheme(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enumerates the ways that a service can be partitioned.
    """

    #: Indicates the partition kind is invalid. All Service Fabric enumerations have the invalid type.
    #: The value is zero.
    INVALID = "Invalid"
    #: Indicates that the partition is based on string names, and is a
    #: SingletonPartitionSchemeDescription object, The value is 1.
    SINGLETON = "Singleton"
    #: Indicates that the partition is based on Int64 key ranges, and is a
    #: UniformInt64RangePartitionSchemeDescription object. The value is 2.
    UNIFORM_INT64_RANGE = "UniformInt64Range"
    #: Indicates that the partition is based on string names, and is a NamedPartitionSchemeDescription
    #: object. The value is 3.
    NAMED = "Named"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state of the cluster resource.
    """

    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"

class ReliabilityLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reliability level sets the replica set size of system services. Learn about
    `ReliabilityLevel
    <https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-capacity>`_.
    
    
    * None - Run the System services with a target replica set count of 1. This should only be used
    for test clusters.
    * Bronze - Run the System services with a target replica set count of 3. This should only be
    used for test clusters.
    * Silver - Run the System services with a target replica set count of 5.
    * Gold - Run the System services with a target replica set count of 7.
    * Platinum - Run the System services with a target replica set count of 9.
    """

    NONE = "None"
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

class RollingUpgradeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The mode used to monitor health during a rolling upgrade. The values are UnmonitoredAuto,
    UnmonitoredManual, and Monitored.
    """

    #: Indicates the upgrade mode is invalid. All Service Fabric enumerations have the invalid type.
    #: The value is zero.
    INVALID = "Invalid"
    #: The upgrade will proceed automatically without performing any health monitoring. The value is
    #: 1.
    UNMONITORED_AUTO = "UnmonitoredAuto"
    #: The upgrade will stop after completing each upgrade domain, giving the opportunity to manually
    #: monitor health before proceeding. The value is 2.
    UNMONITORED_MANUAL = "UnmonitoredManual"
    #: The upgrade will stop after completing each upgrade domain and automatically monitor health
    #: before proceeding. The value is 3.
    MONITORED = "Monitored"

class ServiceCorrelationScheme(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The service correlation scheme.
    """

    #: An invalid correlation scheme. Cannot be used. The value is zero.
    INVALID = "Invalid"
    #: Indicates that this service has an affinity relationship with another service. Provided for
    #: backwards compatibility, consider preferring the Aligned or NonAlignedAffinity options. The
    #: value is 1.
    AFFINITY = "Affinity"
    #: Aligned affinity ensures that the primaries of the partitions of the affinitized services are
    #: collocated on the same nodes. This is the default and is the same as selecting the Affinity
    #: scheme. The value is 2.
    ALIGNED_AFFINITY = "AlignedAffinity"
    #: Non-Aligned affinity guarantees that all replicas of each service will be placed on the same
    #: nodes. Unlike Aligned Affinity, this does not guarantee that replicas of particular role will
    #: be collocated. The value is 3.
    NON_ALIGNED_AFFINITY = "NonAlignedAffinity"

class ServiceKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of service (Stateless or Stateful).
    """

    #: Indicates the service kind is invalid. All Service Fabric enumerations have the invalid type.
    #: The value is zero.
    INVALID = "Invalid"
    #: Does not use Service Fabric to make its state highly available or reliable. The value is 1.
    STATELESS = "Stateless"
    #: Uses Service Fabric to make its state or part of its state highly available and reliable. The
    #: value is 2.
    STATEFUL = "Stateful"

class ServiceLoadMetricWeight(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Determines the metric weight relative to the other metrics that are configured for this
    service. During runtime, if two metrics end up in conflict, the Cluster Resource Manager
    prefers the metric with the higher weight.
    """

    #: Disables resource balancing for this metric. This value is zero.
    ZERO = "Zero"
    #: Specifies the metric weight of the service load as Low. The value is 1.
    LOW = "Low"
    #: Specifies the metric weight of the service load as Medium. The value is 2.
    MEDIUM = "Medium"
    #: Specifies the metric weight of the service load as High. The value is 3.
    HIGH = "High"

class ServicePlacementPolicyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of placement policy for a service fabric service. Following are the possible values.
    """

    #: Indicates the type of the placement policy is invalid. All Service Fabric enumerations have the
    #: invalid type. The value is zero.
    INVALID = "Invalid"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementInvalidDomainPolicyDescription, which indicates that a particular fault or
    #: upgrade domain cannot be used for placement of this service. The value is 1.
    INVALID_DOMAIN = "InvalidDomain"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementRequireDomainDistributionPolicyDescription indicating that the replicas of the
    #: service must be placed in a specific domain. The value is 2.
    REQUIRED_DOMAIN = "RequiredDomain"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementPreferPrimaryDomainPolicyDescription, which indicates that if possible the
    #: Primary replica for the partitions of the service should be located in a particular domain as
    #: an optimization. The value is 3.
    PREFERRED_PRIMARY_DOMAIN = "PreferredPrimaryDomain"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementRequireDomainDistributionPolicyDescription, indicating that the system will
    #: disallow placement of any two replicas from the same partition in the same domain at any time.
    #: The value is 4.
    REQUIRED_DOMAIN_DISTRIBUTION = "RequiredDomainDistribution"
    #: Indicates that the ServicePlacementPolicyDescription is of type
    #: ServicePlacementNonPartiallyPlaceServicePolicyDescription, which indicates that if possible all
    #: replicas of a particular partition of the service should be placed atomically. The value is 5.
    NON_PARTIALLY_PLACE_SERVICE = "NonPartiallyPlaceService"

class SfZonalUpgradeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """This property controls the logical grouping of VMs in upgrade domains (UDs). This property
    can't be modified if a node type with multiple Availability Zones is already present in the
    cluster.
    """

    #: VMs under the node type are grouped into UDs and ignore the zone info in five UDs. This setting
    #: causes UDs across all zones to be upgraded at the same time. This deployment mode is faster for
    #: upgrades, we don't recommend it because it goes against the SDP guidelines, which state that
    #: the updates should be applied to one zone at a time.
    PARALLEL = "Parallel"
    #: If this value is omitted or set to Hierarchical, VMs are grouped to reflect the zonal
    #: distribution in up to 15 UDs. Each of the three zones has five UDs. This ensures that the zones
    #: are updated one at a time, moving to next zone only after completing five UDs within the first
    #: zone. This update process is safer for the cluster and the user application.
    HIERARCHICAL = "Hierarchical"

class StoreName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The local certificate store location.
    """

    ADDRESS_BOOK = "AddressBook"
    AUTH_ROOT = "AuthRoot"
    CERTIFICATE_AUTHORITY = "CertificateAuthority"
    DISALLOWED = "Disallowed"
    MY = "My"
    ROOT = "Root"
    TRUSTED_PEOPLE = "TrustedPeople"
    TRUSTED_PUBLISHER = "TrustedPublisher"

class UpgradeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The upgrade mode of the cluster when new Service Fabric runtime version is available.
    """

    #: The cluster will be automatically upgraded to the latest Service Fabric runtime version,
    #: **upgradeWave** will determine when the upgrade starts after the new version becomes available.
    AUTOMATIC = "Automatic"
    #: The cluster will not be automatically upgraded to the latest Service Fabric runtime version.
    #: The cluster is upgraded by setting the **clusterCodeVersion** property in the cluster resource.
    MANUAL = "Manual"

class VmssZonalUpgradeMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """This property defines the upgrade mode for the virtual machine scale set, it is mandatory if a
    node type with multiple Availability Zones is added.
    """

    #: Updates will happen in all Availability Zones at once for the virtual machine scale sets.
    PARALLEL = "Parallel"
    #: VMs are grouped to reflect the zonal distribution in up to 15 UDs. Each of the three zones has
    #: five UDs. This ensures that the zones are updated one at a time, moving to next zone only after
    #: completing five UDs within the first zone.
    HIERARCHICAL = "Hierarchical"
