# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import AuthorizationManagementClientConfiguration
from .operations import RoleAssignmentsOperations
from .operations import EligibleChildResourcesOperations
from .operations import RoleAssignmentSchedulesOperations
from .operations import RoleAssignmentScheduleInstancesOperations
from .operations import RoleAssignmentScheduleRequestsOperations
from .operations import RoleEligibilitySchedulesOperations
from .operations import RoleEligibilityScheduleInstancesOperations
from .operations import RoleEligibilityScheduleRequestsOperations
from .operations import RoleManagementPoliciesOperations
from .operations import RoleManagementPolicyAssignmentsOperations
from . import models


class AuthorizationManagementClient(object):
    """Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role assignments. A role assignment grants access to Azure Active Directory users.

    :ivar role_assignments: RoleAssignmentsOperations operations
    :vartype role_assignments: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentsOperations
    :ivar eligible_child_resources: EligibleChildResourcesOperations operations
    :vartype eligible_child_resources: azure.mgmt.authorization.v2020_10_01_preview.operations.EligibleChildResourcesOperations
    :ivar role_assignment_schedules: RoleAssignmentSchedulesOperations operations
    :vartype role_assignment_schedules: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentSchedulesOperations
    :ivar role_assignment_schedule_instances: RoleAssignmentScheduleInstancesOperations operations
    :vartype role_assignment_schedule_instances: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentScheduleInstancesOperations
    :ivar role_assignment_schedule_requests: RoleAssignmentScheduleRequestsOperations operations
    :vartype role_assignment_schedule_requests: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleAssignmentScheduleRequestsOperations
    :ivar role_eligibility_schedules: RoleEligibilitySchedulesOperations operations
    :vartype role_eligibility_schedules: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleEligibilitySchedulesOperations
    :ivar role_eligibility_schedule_instances: RoleEligibilityScheduleInstancesOperations operations
    :vartype role_eligibility_schedule_instances: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleEligibilityScheduleInstancesOperations
    :ivar role_eligibility_schedule_requests: RoleEligibilityScheduleRequestsOperations operations
    :vartype role_eligibility_schedule_requests: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleEligibilityScheduleRequestsOperations
    :ivar role_management_policies: RoleManagementPoliciesOperations operations
    :vartype role_management_policies: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleManagementPoliciesOperations
    :ivar role_management_policy_assignments: RoleManagementPolicyAssignmentsOperations operations
    :vartype role_management_policy_assignments: azure.mgmt.authorization.v2020_10_01_preview.operations.RoleManagementPolicyAssignmentsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AuthorizationManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.role_assignments = RoleAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.eligible_child_resources = EligibleChildResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_assignment_schedules = RoleAssignmentSchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_assignment_schedule_instances = RoleAssignmentScheduleInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_assignment_schedule_requests = RoleAssignmentScheduleRequestsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_eligibility_schedules = RoleEligibilitySchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_eligibility_schedule_instances = RoleEligibilityScheduleInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_eligibility_schedule_requests = RoleEligibilityScheduleRequestsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_management_policies = RoleManagementPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.role_management_policy_assignments = RoleManagementPolicyAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AuthorizationManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
