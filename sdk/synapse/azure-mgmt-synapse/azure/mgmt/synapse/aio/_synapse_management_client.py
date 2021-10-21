# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import SynapseManagementClientConfiguration
from .operations import AzureADOnlyAuthenticationsOperations
from .operations import Operations
from .operations import IpFirewallRulesOperations
from .operations import KeysOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import PrivateLinkHubPrivateLinkResourcesOperations
from .operations import PrivateLinkHubsOperations
from .operations import PrivateEndpointConnectionsPrivateLinkHubOperations
from .operations import SqlPoolsOperations
from .operations import SqlPoolMetadataSyncConfigsOperations
from .operations import SqlPoolOperationResultsOperations
from .operations import SqlPoolGeoBackupPoliciesOperations
from .operations import SqlPoolDataWarehouseUserActivitiesOperations
from .operations import SqlPoolRestorePointsOperations
from .operations import SqlPoolReplicationLinksOperations
from .operations import SqlPoolMaintenanceWindowsOperations
from .operations import SqlPoolMaintenanceWindowOptionsOperations
from .operations import SqlPoolTransparentDataEncryptionsOperations
from .operations import SqlPoolBlobAuditingPoliciesOperations
from .operations import SqlPoolOperationsOperations
from .operations import SqlPoolUsagesOperations
from .operations import SqlPoolSensitivityLabelsOperations
from .operations import SqlPoolRecommendedSensitivityLabelsOperations
from .operations import SqlPoolSchemasOperations
from .operations import SqlPoolTablesOperations
from .operations import SqlPoolTableColumnsOperations
from .operations import SqlPoolConnectionPoliciesOperations
from .operations import SqlPoolVulnerabilityAssessmentsOperations
from .operations import SqlPoolVulnerabilityAssessmentScansOperations
from .operations import SqlPoolSecurityAlertPoliciesOperations
from .operations import SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
from .operations import ExtendedSqlPoolBlobAuditingPoliciesOperations
from .operations import DataMaskingPoliciesOperations
from .operations import DataMaskingRulesOperations
from .operations import SqlPoolColumnsOperations
from .operations import SqlPoolWorkloadGroupOperations
from .operations import SqlPoolWorkloadClassifierOperations
from .operations import WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
from .operations import WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
from .operations import WorkspaceManagedSqlServerSecurityAlertPolicyOperations
from .operations import WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
from .operations import WorkspaceManagedSqlServerEncryptionProtectorOperations
from .operations import WorkspaceManagedSqlServerUsagesOperations
from .operations import WorkspaceManagedSqlServerRecoverableSqlPoolsOperations
from .operations import WorkspacesOperations
from .operations import WorkspaceAadAdminsOperations
from .operations import WorkspaceSqlAadAdminsOperations
from .operations import WorkspaceManagedIdentitySqlControlSettingsOperations
from .operations import RestorableDroppedSqlPoolsOperations
from .operations import BigDataPoolsOperations
from .operations import LibraryOperations
from .operations import LibrariesOperations
from .operations import IntegrationRuntimesOperations
from .operations import IntegrationRuntimeNodeIpAddressOperations
from .operations import IntegrationRuntimeObjectMetadataOperations
from .operations import IntegrationRuntimeNodesOperations
from .operations import IntegrationRuntimeCredentialsOperations
from .operations import IntegrationRuntimeConnectionInfosOperations
from .operations import IntegrationRuntimeAuthKeysOperations
from .operations import IntegrationRuntimeMonitoringDataOperations
from .operations import IntegrationRuntimeStatusOperations
from .operations import SparkConfigurationOperations
from .operations import SparkConfigurationsOperations
from .operations import KustoOperationsOperations
from .operations import KustoPoolOperations
from .operations import KustoPoolsOperations
from .operations import KustoPoolChildResourceOperations
from .operations import KustoPoolAttachedDatabaseConfigurationsOperations
from .operations import KustoPoolDatabasesOperations
from .operations import KustoPoolDataConnectionsOperations
from .operations import KustoPoolPrincipalAssignmentsOperations
from .operations import KustoPoolDatabasePrincipalAssignmentsOperations
from .. import models


class SynapseManagementClient(object):
    """Azure Synapse Analytics Management Client.

    :ivar azure_ad_only_authentications: AzureADOnlyAuthenticationsOperations operations
    :vartype azure_ad_only_authentications: azure.mgmt.synapse.aio.operations.AzureADOnlyAuthenticationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.synapse.aio.operations.Operations
    :ivar ip_firewall_rules: IpFirewallRulesOperations operations
    :vartype ip_firewall_rules: azure.mgmt.synapse.aio.operations.IpFirewallRulesOperations
    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.synapse.aio.operations.KeysOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.synapse.aio.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.synapse.aio.operations.PrivateLinkResourcesOperations
    :ivar private_link_hub_private_link_resources: PrivateLinkHubPrivateLinkResourcesOperations operations
    :vartype private_link_hub_private_link_resources: azure.mgmt.synapse.aio.operations.PrivateLinkHubPrivateLinkResourcesOperations
    :ivar private_link_hubs: PrivateLinkHubsOperations operations
    :vartype private_link_hubs: azure.mgmt.synapse.aio.operations.PrivateLinkHubsOperations
    :ivar private_endpoint_connections_private_link_hub: PrivateEndpointConnectionsPrivateLinkHubOperations operations
    :vartype private_endpoint_connections_private_link_hub: azure.mgmt.synapse.aio.operations.PrivateEndpointConnectionsPrivateLinkHubOperations
    :ivar sql_pools: SqlPoolsOperations operations
    :vartype sql_pools: azure.mgmt.synapse.aio.operations.SqlPoolsOperations
    :ivar sql_pool_metadata_sync_configs: SqlPoolMetadataSyncConfigsOperations operations
    :vartype sql_pool_metadata_sync_configs: azure.mgmt.synapse.aio.operations.SqlPoolMetadataSyncConfigsOperations
    :ivar sql_pool_operation_results: SqlPoolOperationResultsOperations operations
    :vartype sql_pool_operation_results: azure.mgmt.synapse.aio.operations.SqlPoolOperationResultsOperations
    :ivar sql_pool_geo_backup_policies: SqlPoolGeoBackupPoliciesOperations operations
    :vartype sql_pool_geo_backup_policies: azure.mgmt.synapse.aio.operations.SqlPoolGeoBackupPoliciesOperations
    :ivar sql_pool_data_warehouse_user_activities: SqlPoolDataWarehouseUserActivitiesOperations operations
    :vartype sql_pool_data_warehouse_user_activities: azure.mgmt.synapse.aio.operations.SqlPoolDataWarehouseUserActivitiesOperations
    :ivar sql_pool_restore_points: SqlPoolRestorePointsOperations operations
    :vartype sql_pool_restore_points: azure.mgmt.synapse.aio.operations.SqlPoolRestorePointsOperations
    :ivar sql_pool_replication_links: SqlPoolReplicationLinksOperations operations
    :vartype sql_pool_replication_links: azure.mgmt.synapse.aio.operations.SqlPoolReplicationLinksOperations
    :ivar sql_pool_maintenance_windows: SqlPoolMaintenanceWindowsOperations operations
    :vartype sql_pool_maintenance_windows: azure.mgmt.synapse.aio.operations.SqlPoolMaintenanceWindowsOperations
    :ivar sql_pool_maintenance_window_options: SqlPoolMaintenanceWindowOptionsOperations operations
    :vartype sql_pool_maintenance_window_options: azure.mgmt.synapse.aio.operations.SqlPoolMaintenanceWindowOptionsOperations
    :ivar sql_pool_transparent_data_encryptions: SqlPoolTransparentDataEncryptionsOperations operations
    :vartype sql_pool_transparent_data_encryptions: azure.mgmt.synapse.aio.operations.SqlPoolTransparentDataEncryptionsOperations
    :ivar sql_pool_blob_auditing_policies: SqlPoolBlobAuditingPoliciesOperations operations
    :vartype sql_pool_blob_auditing_policies: azure.mgmt.synapse.aio.operations.SqlPoolBlobAuditingPoliciesOperations
    :ivar sql_pool_operations: SqlPoolOperationsOperations operations
    :vartype sql_pool_operations: azure.mgmt.synapse.aio.operations.SqlPoolOperationsOperations
    :ivar sql_pool_usages: SqlPoolUsagesOperations operations
    :vartype sql_pool_usages: azure.mgmt.synapse.aio.operations.SqlPoolUsagesOperations
    :ivar sql_pool_sensitivity_labels: SqlPoolSensitivityLabelsOperations operations
    :vartype sql_pool_sensitivity_labels: azure.mgmt.synapse.aio.operations.SqlPoolSensitivityLabelsOperations
    :ivar sql_pool_recommended_sensitivity_labels: SqlPoolRecommendedSensitivityLabelsOperations operations
    :vartype sql_pool_recommended_sensitivity_labels: azure.mgmt.synapse.aio.operations.SqlPoolRecommendedSensitivityLabelsOperations
    :ivar sql_pool_schemas: SqlPoolSchemasOperations operations
    :vartype sql_pool_schemas: azure.mgmt.synapse.aio.operations.SqlPoolSchemasOperations
    :ivar sql_pool_tables: SqlPoolTablesOperations operations
    :vartype sql_pool_tables: azure.mgmt.synapse.aio.operations.SqlPoolTablesOperations
    :ivar sql_pool_table_columns: SqlPoolTableColumnsOperations operations
    :vartype sql_pool_table_columns: azure.mgmt.synapse.aio.operations.SqlPoolTableColumnsOperations
    :ivar sql_pool_connection_policies: SqlPoolConnectionPoliciesOperations operations
    :vartype sql_pool_connection_policies: azure.mgmt.synapse.aio.operations.SqlPoolConnectionPoliciesOperations
    :ivar sql_pool_vulnerability_assessments: SqlPoolVulnerabilityAssessmentsOperations operations
    :vartype sql_pool_vulnerability_assessments: azure.mgmt.synapse.aio.operations.SqlPoolVulnerabilityAssessmentsOperations
    :ivar sql_pool_vulnerability_assessment_scans: SqlPoolVulnerabilityAssessmentScansOperations operations
    :vartype sql_pool_vulnerability_assessment_scans: azure.mgmt.synapse.aio.operations.SqlPoolVulnerabilityAssessmentScansOperations
    :ivar sql_pool_security_alert_policies: SqlPoolSecurityAlertPoliciesOperations operations
    :vartype sql_pool_security_alert_policies: azure.mgmt.synapse.aio.operations.SqlPoolSecurityAlertPoliciesOperations
    :ivar sql_pool_vulnerability_assessment_rule_baselines: SqlPoolVulnerabilityAssessmentRuleBaselinesOperations operations
    :vartype sql_pool_vulnerability_assessment_rule_baselines: azure.mgmt.synapse.aio.operations.SqlPoolVulnerabilityAssessmentRuleBaselinesOperations
    :ivar extended_sql_pool_blob_auditing_policies: ExtendedSqlPoolBlobAuditingPoliciesOperations operations
    :vartype extended_sql_pool_blob_auditing_policies: azure.mgmt.synapse.aio.operations.ExtendedSqlPoolBlobAuditingPoliciesOperations
    :ivar data_masking_policies: DataMaskingPoliciesOperations operations
    :vartype data_masking_policies: azure.mgmt.synapse.aio.operations.DataMaskingPoliciesOperations
    :ivar data_masking_rules: DataMaskingRulesOperations operations
    :vartype data_masking_rules: azure.mgmt.synapse.aio.operations.DataMaskingRulesOperations
    :ivar sql_pool_columns: SqlPoolColumnsOperations operations
    :vartype sql_pool_columns: azure.mgmt.synapse.aio.operations.SqlPoolColumnsOperations
    :ivar sql_pool_workload_group: SqlPoolWorkloadGroupOperations operations
    :vartype sql_pool_workload_group: azure.mgmt.synapse.aio.operations.SqlPoolWorkloadGroupOperations
    :ivar sql_pool_workload_classifier: SqlPoolWorkloadClassifierOperations operations
    :vartype sql_pool_workload_classifier: azure.mgmt.synapse.aio.operations.SqlPoolWorkloadClassifierOperations
    :ivar workspace_managed_sql_server_blob_auditing_policies: WorkspaceManagedSqlServerBlobAuditingPoliciesOperations operations
    :vartype workspace_managed_sql_server_blob_auditing_policies: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_extended_blob_auditing_policies: WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations operations
    :vartype workspace_managed_sql_server_extended_blob_auditing_policies: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations
    :ivar workspace_managed_sql_server_security_alert_policy: WorkspaceManagedSqlServerSecurityAlertPolicyOperations operations
    :vartype workspace_managed_sql_server_security_alert_policy: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerSecurityAlertPolicyOperations
    :ivar workspace_managed_sql_server_vulnerability_assessments: WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations operations
    :vartype workspace_managed_sql_server_vulnerability_assessments: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations
    :ivar workspace_managed_sql_server_encryption_protector: WorkspaceManagedSqlServerEncryptionProtectorOperations operations
    :vartype workspace_managed_sql_server_encryption_protector: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerEncryptionProtectorOperations
    :ivar workspace_managed_sql_server_usages: WorkspaceManagedSqlServerUsagesOperations operations
    :vartype workspace_managed_sql_server_usages: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerUsagesOperations
    :ivar workspace_managed_sql_server_recoverable_sql_pools: WorkspaceManagedSqlServerRecoverableSqlPoolsOperations operations
    :vartype workspace_managed_sql_server_recoverable_sql_pools: azure.mgmt.synapse.aio.operations.WorkspaceManagedSqlServerRecoverableSqlPoolsOperations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.synapse.aio.operations.WorkspacesOperations
    :ivar workspace_aad_admins: WorkspaceAadAdminsOperations operations
    :vartype workspace_aad_admins: azure.mgmt.synapse.aio.operations.WorkspaceAadAdminsOperations
    :ivar workspace_sql_aad_admins: WorkspaceSqlAadAdminsOperations operations
    :vartype workspace_sql_aad_admins: azure.mgmt.synapse.aio.operations.WorkspaceSqlAadAdminsOperations
    :ivar workspace_managed_identity_sql_control_settings: WorkspaceManagedIdentitySqlControlSettingsOperations operations
    :vartype workspace_managed_identity_sql_control_settings: azure.mgmt.synapse.aio.operations.WorkspaceManagedIdentitySqlControlSettingsOperations
    :ivar restorable_dropped_sql_pools: RestorableDroppedSqlPoolsOperations operations
    :vartype restorable_dropped_sql_pools: azure.mgmt.synapse.aio.operations.RestorableDroppedSqlPoolsOperations
    :ivar big_data_pools: BigDataPoolsOperations operations
    :vartype big_data_pools: azure.mgmt.synapse.aio.operations.BigDataPoolsOperations
    :ivar library: LibraryOperations operations
    :vartype library: azure.mgmt.synapse.aio.operations.LibraryOperations
    :ivar libraries: LibrariesOperations operations
    :vartype libraries: azure.mgmt.synapse.aio.operations.LibrariesOperations
    :ivar integration_runtimes: IntegrationRuntimesOperations operations
    :vartype integration_runtimes: azure.mgmt.synapse.aio.operations.IntegrationRuntimesOperations
    :ivar integration_runtime_node_ip_address: IntegrationRuntimeNodeIpAddressOperations operations
    :vartype integration_runtime_node_ip_address: azure.mgmt.synapse.aio.operations.IntegrationRuntimeNodeIpAddressOperations
    :ivar integration_runtime_object_metadata: IntegrationRuntimeObjectMetadataOperations operations
    :vartype integration_runtime_object_metadata: azure.mgmt.synapse.aio.operations.IntegrationRuntimeObjectMetadataOperations
    :ivar integration_runtime_nodes: IntegrationRuntimeNodesOperations operations
    :vartype integration_runtime_nodes: azure.mgmt.synapse.aio.operations.IntegrationRuntimeNodesOperations
    :ivar integration_runtime_credentials: IntegrationRuntimeCredentialsOperations operations
    :vartype integration_runtime_credentials: azure.mgmt.synapse.aio.operations.IntegrationRuntimeCredentialsOperations
    :ivar integration_runtime_connection_infos: IntegrationRuntimeConnectionInfosOperations operations
    :vartype integration_runtime_connection_infos: azure.mgmt.synapse.aio.operations.IntegrationRuntimeConnectionInfosOperations
    :ivar integration_runtime_auth_keys: IntegrationRuntimeAuthKeysOperations operations
    :vartype integration_runtime_auth_keys: azure.mgmt.synapse.aio.operations.IntegrationRuntimeAuthKeysOperations
    :ivar integration_runtime_monitoring_data: IntegrationRuntimeMonitoringDataOperations operations
    :vartype integration_runtime_monitoring_data: azure.mgmt.synapse.aio.operations.IntegrationRuntimeMonitoringDataOperations
    :ivar integration_runtime_status: IntegrationRuntimeStatusOperations operations
    :vartype integration_runtime_status: azure.mgmt.synapse.aio.operations.IntegrationRuntimeStatusOperations
    :ivar spark_configuration: SparkConfigurationOperations operations
    :vartype spark_configuration: azure.mgmt.synapse.aio.operations.SparkConfigurationOperations
    :ivar spark_configurations: SparkConfigurationsOperations operations
    :vartype spark_configurations: azure.mgmt.synapse.aio.operations.SparkConfigurationsOperations
    :ivar kusto_operations: KustoOperationsOperations operations
    :vartype kusto_operations: azure.mgmt.synapse.aio.operations.KustoOperationsOperations
    :ivar kusto_pool: KustoPoolOperations operations
    :vartype kusto_pool: azure.mgmt.synapse.aio.operations.KustoPoolOperations
    :ivar kusto_pools: KustoPoolsOperations operations
    :vartype kusto_pools: azure.mgmt.synapse.aio.operations.KustoPoolsOperations
    :ivar kusto_pool_child_resource: KustoPoolChildResourceOperations operations
    :vartype kusto_pool_child_resource: azure.mgmt.synapse.aio.operations.KustoPoolChildResourceOperations
    :ivar kusto_pool_attached_database_configurations: KustoPoolAttachedDatabaseConfigurationsOperations operations
    :vartype kusto_pool_attached_database_configurations: azure.mgmt.synapse.aio.operations.KustoPoolAttachedDatabaseConfigurationsOperations
    :ivar kusto_pool_databases: KustoPoolDatabasesOperations operations
    :vartype kusto_pool_databases: azure.mgmt.synapse.aio.operations.KustoPoolDatabasesOperations
    :ivar kusto_pool_data_connections: KustoPoolDataConnectionsOperations operations
    :vartype kusto_pool_data_connections: azure.mgmt.synapse.aio.operations.KustoPoolDataConnectionsOperations
    :ivar kusto_pool_principal_assignments: KustoPoolPrincipalAssignmentsOperations operations
    :vartype kusto_pool_principal_assignments: azure.mgmt.synapse.aio.operations.KustoPoolPrincipalAssignmentsOperations
    :ivar kusto_pool_database_principal_assignments: KustoPoolDatabasePrincipalAssignmentsOperations operations
    :vartype kusto_pool_database_principal_assignments: azure.mgmt.synapse.aio.operations.KustoPoolDatabasePrincipalAssignmentsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SynapseManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.azure_ad_only_authentications = AzureADOnlyAuthenticationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.ip_firewall_rules = IpFirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.keys = KeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_hub_private_link_resources = PrivateLinkHubPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_hubs = PrivateLinkHubsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections_private_link_hub = PrivateEndpointConnectionsPrivateLinkHubOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pools = SqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_metadata_sync_configs = SqlPoolMetadataSyncConfigsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_operation_results = SqlPoolOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_geo_backup_policies = SqlPoolGeoBackupPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_data_warehouse_user_activities = SqlPoolDataWarehouseUserActivitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_restore_points = SqlPoolRestorePointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_replication_links = SqlPoolReplicationLinksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_maintenance_windows = SqlPoolMaintenanceWindowsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_maintenance_window_options = SqlPoolMaintenanceWindowOptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_transparent_data_encryptions = SqlPoolTransparentDataEncryptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_blob_auditing_policies = SqlPoolBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_operations = SqlPoolOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_usages = SqlPoolUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_sensitivity_labels = SqlPoolSensitivityLabelsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_recommended_sensitivity_labels = SqlPoolRecommendedSensitivityLabelsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_schemas = SqlPoolSchemasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_tables = SqlPoolTablesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_table_columns = SqlPoolTableColumnsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_connection_policies = SqlPoolConnectionPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessments = SqlPoolVulnerabilityAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessment_scans = SqlPoolVulnerabilityAssessmentScansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_security_alert_policies = SqlPoolSecurityAlertPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_vulnerability_assessment_rule_baselines = SqlPoolVulnerabilityAssessmentRuleBaselinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.extended_sql_pool_blob_auditing_policies = ExtendedSqlPoolBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_masking_policies = DataMaskingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_masking_rules = DataMaskingRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_columns = SqlPoolColumnsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_workload_group = SqlPoolWorkloadGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_pool_workload_classifier = SqlPoolWorkloadClassifierOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_blob_auditing_policies = WorkspaceManagedSqlServerBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_extended_blob_auditing_policies = WorkspaceManagedSqlServerExtendedBlobAuditingPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_security_alert_policy = WorkspaceManagedSqlServerSecurityAlertPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_vulnerability_assessments = WorkspaceManagedSqlServerVulnerabilityAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_encryption_protector = WorkspaceManagedSqlServerEncryptionProtectorOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_usages = WorkspaceManagedSqlServerUsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_sql_server_recoverable_sql_pools = WorkspaceManagedSqlServerRecoverableSqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_aad_admins = WorkspaceAadAdminsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_sql_aad_admins = WorkspaceSqlAadAdminsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_managed_identity_sql_control_settings = WorkspaceManagedIdentitySqlControlSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.restorable_dropped_sql_pools = RestorableDroppedSqlPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.big_data_pools = BigDataPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.library = LibraryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.libraries = LibrariesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtimes = IntegrationRuntimesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_node_ip_address = IntegrationRuntimeNodeIpAddressOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_object_metadata = IntegrationRuntimeObjectMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_nodes = IntegrationRuntimeNodesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_credentials = IntegrationRuntimeCredentialsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_connection_infos = IntegrationRuntimeConnectionInfosOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_auth_keys = IntegrationRuntimeAuthKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_monitoring_data = IntegrationRuntimeMonitoringDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_runtime_status = IntegrationRuntimeStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_configuration = SparkConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.spark_configurations = SparkConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_operations = KustoOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool = KustoPoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pools = KustoPoolsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_child_resource = KustoPoolChildResourceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_attached_database_configurations = KustoPoolAttachedDatabaseConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_databases = KustoPoolDatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_data_connections = KustoPoolDataConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_principal_assignments = KustoPoolPrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.kusto_pool_database_principal_assignments = KustoPoolDatabasePrincipalAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SynapseManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)