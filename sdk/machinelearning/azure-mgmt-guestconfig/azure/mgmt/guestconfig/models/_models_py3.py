# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._guest_configuration_client_enums import *


class AssignmentInfo(msrest.serialization.Model):
    """Information about the guest configuration assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the guest configuration assignment.
    :vartype name: str
    :param configuration: Information about the configuration.
    :type configuration: ~azure.mgmt.guestconfig.models.ConfigurationInfo
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ConfigurationInfo'},
    }

    def __init__(
        self,
        *,
        configuration: Optional["ConfigurationInfo"] = None,
        **kwargs
    ):
        super(AssignmentInfo, self).__init__(**kwargs)
        self.name = None
        self.configuration = configuration


class AssignmentReport(msrest.serialization.Model):
    """AssignmentReport.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the report for the guest configuration assignment.
    :vartype id: str
    :ivar report_id: GUID that identifies the guest configuration assignment report under a
     subscription, resource group.
    :vartype report_id: str
    :param assignment: Configuration details of the guest configuration assignment.
    :type assignment: ~azure.mgmt.guestconfig.models.AssignmentInfo
    :param vm: Information about the VM.
    :type vm: ~azure.mgmt.guestconfig.models.VMInfo
    :ivar start_time: Start date and time of the guest configuration assignment compliance status
     check.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: End date and time of the guest configuration assignment compliance status
     check.
    :vartype end_time: ~datetime.datetime
    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~azure.mgmt.guestconfig.models.ComplianceStatus
    :ivar operation_type: Type of report, Consistency or Initial. Possible values include:
     "Consistency", "Initial".
    :vartype operation_type: str or ~azure.mgmt.guestconfig.models.Type
    :param resources: The list of resources for which guest configuration assignment compliance is
     checked.
    :type resources: list[~azure.mgmt.guestconfig.models.AssignmentReportResource]
    """

    _validation = {
        'id': {'readonly': True},
        'report_id': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'compliance_status': {'readonly': True},
        'operation_type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'report_id': {'key': 'reportId', 'type': 'str'},
        'assignment': {'key': 'assignment', 'type': 'AssignmentInfo'},
        'vm': {'key': 'vm', 'type': 'VMInfo'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[AssignmentReportResource]'},
    }

    def __init__(
        self,
        *,
        assignment: Optional["AssignmentInfo"] = None,
        vm: Optional["VMInfo"] = None,
        resources: Optional[List["AssignmentReportResource"]] = None,
        **kwargs
    ):
        super(AssignmentReport, self).__init__(**kwargs)
        self.id = None
        self.report_id = None
        self.assignment = assignment
        self.vm = vm
        self.start_time = None
        self.end_time = None
        self.compliance_status = None
        self.operation_type = None
        self.resources = resources


class AssignmentReportDetails(msrest.serialization.Model):
    """Details of the guest configuration assignment report.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~azure.mgmt.guestconfig.models.ComplianceStatus
    :ivar start_time: Start date and time of the guest configuration assignment compliance status
     check.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: End date and time of the guest configuration assignment compliance status
     check.
    :vartype end_time: ~datetime.datetime
    :ivar job_id: GUID of the report.
    :vartype job_id: str
    :ivar operation_type: Type of report, Consistency or Initial. Possible values include:
     "Consistency", "Initial".
    :vartype operation_type: str or ~azure.mgmt.guestconfig.models.Type
    :param resources: The list of resources for which guest configuration assignment compliance is
     checked.
    :type resources: list[~azure.mgmt.guestconfig.models.AssignmentReportResource]
    """

    _validation = {
        'compliance_status': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'job_id': {'readonly': True},
        'operation_type': {'readonly': True},
    }

    _attribute_map = {
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[AssignmentReportResource]'},
    }

    def __init__(
        self,
        *,
        resources: Optional[List["AssignmentReportResource"]] = None,
        **kwargs
    ):
        super(AssignmentReportDetails, self).__init__(**kwargs)
        self.compliance_status = None
        self.start_time = None
        self.end_time = None
        self.job_id = None
        self.operation_type = None
        self.resources = resources


class AssignmentReportResource(msrest.serialization.Model):
    """The guest configuration assignment resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~azure.mgmt.guestconfig.models.ComplianceStatus
    :ivar resource_id: Name of the guest configuration assignment resource setting.
    :vartype resource_id: str
    :param reasons: Compliance reason and reason code for a resource.
    :type reasons: list[~azure.mgmt.guestconfig.models.AssignmentReportResourceComplianceReason]
    :ivar properties: Properties of a guest configuration assignment resource.
    :vartype properties: any
    """

    _validation = {
        'compliance_status': {'readonly': True},
        'resource_id': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'reasons': {'key': 'reasons', 'type': '[AssignmentReportResourceComplianceReason]'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        *,
        reasons: Optional[List["AssignmentReportResourceComplianceReason"]] = None,
        **kwargs
    ):
        super(AssignmentReportResource, self).__init__(**kwargs)
        self.compliance_status = None
        self.resource_id = None
        self.reasons = reasons
        self.properties = None


class AssignmentReportResourceComplianceReason(msrest.serialization.Model):
    """Reason and code for the compliance of the guest configuration assignment resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar phrase: Reason for the compliance of the guest configuration assignment resource.
    :vartype phrase: str
    :ivar code: Code for the compliance of the guest configuration assignment resource.
    :vartype code: str
    """

    _validation = {
        'phrase': {'readonly': True},
        'code': {'readonly': True},
    }

    _attribute_map = {
        'phrase': {'key': 'phrase', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AssignmentReportResourceComplianceReason, self).__init__(**kwargs)
        self.phrase = None
        self.code = None


class ConfigurationInfo(msrest.serialization.Model):
    """Information about the configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the configuration.
    :vartype name: str
    :ivar version: Version of the configuration.
    :vartype version: str
    """

    _validation = {
        'name': {'readonly': True},
        'version': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationInfo, self).__init__(**kwargs)
        self.name = None
        self.version = None


class ConfigurationParameter(msrest.serialization.Model):
    """Represents a configuration parameter.

    :param name: Name of the configuration parameter.
    :type name: str
    :param value: Value of the configuration parameter.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ):
        super(ConfigurationParameter, self).__init__(**kwargs)
        self.name = name
        self.value = value


class ConfigurationSetting(msrest.serialization.Model):
    """Configuration setting of LCM (Local Configuration Manager).

    :param configuration_mode: Specifies how the LCM(Local Configuration Manager) actually applies
     the configuration to the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and
     ApplyAndAutoCorrect. Possible values include: "ApplyOnly", "ApplyAndMonitor",
     "ApplyAndAutoCorrect".
    :type configuration_mode: str or ~azure.mgmt.guestconfig.models.ConfigurationMode
    :param allow_module_overwrite: If true - new configurations downloaded from the pull service
     are allowed to overwrite the old ones on the target node. Otherwise, false.
    :type allow_module_overwrite: bool
    :param action_after_reboot: Specifies what happens after a reboot during the application of a
     configuration. The possible values are ContinueConfiguration and StopConfiguration. Possible
     values include: "ContinueConfiguration", "StopConfiguration".
    :type action_after_reboot: str or ~azure.mgmt.guestconfig.models.ActionAfterReboot
    :param refresh_frequency_mins: The time interval, in minutes, at which the LCM checks a pull
     service to get updated configurations. This value is ignored if the LCM is not configured in
     pull mode. The default value is 30.
    :type refresh_frequency_mins: float
    :param reboot_if_needed: Set this to true to automatically reboot the node after a
     configuration that requires reboot is applied. Otherwise, you will have to manually reboot the
     node for any configuration that requires it. The default value is false. To use this setting
     when a reboot condition is enacted by something other than DSC (such as Windows Installer),
     combine this setting with the xPendingReboot module.
    :type reboot_if_needed: bool
    :param configuration_mode_frequency_mins: How often, in minutes, the current configuration is
     checked and applied. This property is ignored if the ConfigurationMode property is set to
     ApplyOnly. The default value is 15.
    :type configuration_mode_frequency_mins: float
    """

    _attribute_map = {
        'configuration_mode': {'key': 'configurationMode', 'type': 'str'},
        'allow_module_overwrite': {'key': 'allowModuleOverwrite', 'type': 'bool'},
        'action_after_reboot': {'key': 'actionAfterReboot', 'type': 'str'},
        'refresh_frequency_mins': {'key': 'refreshFrequencyMins', 'type': 'float'},
        'reboot_if_needed': {'key': 'rebootIfNeeded', 'type': 'bool'},
        'configuration_mode_frequency_mins': {'key': 'configurationModeFrequencyMins', 'type': 'float'},
    }

    def __init__(
        self,
        *,
        configuration_mode: Optional[Union[str, "ConfigurationMode"]] = None,
        allow_module_overwrite: Optional[bool] = None,
        action_after_reboot: Optional[Union[str, "ActionAfterReboot"]] = None,
        refresh_frequency_mins: Optional[float] = 30,
        reboot_if_needed: Optional[bool] = None,
        configuration_mode_frequency_mins: Optional[float] = 15,
        **kwargs
    ):
        super(ConfigurationSetting, self).__init__(**kwargs)
        self.configuration_mode = configuration_mode
        self.allow_module_overwrite = allow_module_overwrite
        self.action_after_reboot = action_after_reboot
        self.refresh_frequency_mins = refresh_frequency_mins
        self.reboot_if_needed = reboot_if_needed
        self.configuration_mode_frequency_mins = configuration_mode_frequency_mins


class ErrorResponse(msrest.serialization.Model):
    """Error response of an operation failure.

    :param error:
    :type error: ~azure.mgmt.guestconfig.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponseError"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ErrorResponseError(msrest.serialization.Model):
    """ErrorResponseError.

    :param code: Error code.
    :type code: str
    :param message: Detail error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = code
        self.message = message


class Resource(msrest.serialization.Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the guest configuration assignment.
    :vartype id: str
    :param name: Name of the guest configuration assignment.
    :type name: str
    :param location: Region where the VM is located.
    :type location: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        location: Optional[str] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = name
        self.location = location
        self.type = None


class ProxyResource(Resource):
    """ARM proxy resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the guest configuration assignment.
    :vartype id: str
    :param name: Name of the guest configuration assignment.
    :type name: str
    :param location: Region where the VM is located.
    :type location: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        location: Optional[str] = None,
        **kwargs
    ):
        super(ProxyResource, self).__init__(name=name, location=location, **kwargs)


class GuestConfigurationAssignment(ProxyResource):
    """Guest configuration assignment is an association between a machine and guest configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the guest configuration assignment.
    :vartype id: str
    :param name: Name of the guest configuration assignment.
    :type name: str
    :param location: Region where the VM is located.
    :type location: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param properties: Properties of the Guest configuration assignment.
    :type properties: ~azure.mgmt.guestconfig.models.GuestConfigurationAssignmentProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'GuestConfigurationAssignmentProperties'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        location: Optional[str] = None,
        properties: Optional["GuestConfigurationAssignmentProperties"] = None,
        **kwargs
    ):
        super(GuestConfigurationAssignment, self).__init__(name=name, location=location, **kwargs)
        self.properties = properties


class GuestConfigurationAssignmentList(msrest.serialization.Model):
    """The response of the list guest configuration assignment operation.

    :param value: Result of the list guest configuration assignment operation.
    :type value: list[~azure.mgmt.guestconfig.models.GuestConfigurationAssignment]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[GuestConfigurationAssignment]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["GuestConfigurationAssignment"]] = None,
        **kwargs
    ):
        super(GuestConfigurationAssignmentList, self).__init__(**kwargs)
        self.value = value


class GuestConfigurationAssignmentProperties(msrest.serialization.Model):
    """Guest configuration assignment properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar target_resource_id: VM resource Id.
    :vartype target_resource_id: str
    :param guest_configuration: The guest configuration to assign.
    :type guest_configuration: ~azure.mgmt.guestconfig.models.GuestConfigurationNavigation
    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~azure.mgmt.guestconfig.models.ComplianceStatus
    :ivar last_compliance_status_checked: Date and time when last compliance status was checked.
    :vartype last_compliance_status_checked: ~datetime.datetime
    :ivar latest_report_id: Id of the latest report for the guest configuration assignment.
    :vartype latest_report_id: str
    :param latest_assignment_report: Last reported guest configuration assignment report.
    :type latest_assignment_report: ~azure.mgmt.guestconfig.models.AssignmentReport
    :param context: The source which initiated the guest configuration assignment. Ex: Azure
     Policy.
    :type context: str
    :ivar assignment_hash: Combined hash of the configuration package and parameters.
    :vartype assignment_hash: str
    :ivar provisioning_state: The provisioning state, which only appears in the response. Possible
     values include: "Succeeded", "Failed", "Canceled", "Created".
    :vartype provisioning_state: str or ~azure.mgmt.guestconfig.models.ProvisioningState
    """

    _validation = {
        'target_resource_id': {'readonly': True},
        'compliance_status': {'readonly': True},
        'last_compliance_status_checked': {'readonly': True},
        'latest_report_id': {'readonly': True},
        'assignment_hash': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'guest_configuration': {'key': 'guestConfiguration', 'type': 'GuestConfigurationNavigation'},
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'last_compliance_status_checked': {'key': 'lastComplianceStatusChecked', 'type': 'iso-8601'},
        'latest_report_id': {'key': 'latestReportId', 'type': 'str'},
        'latest_assignment_report': {'key': 'latestAssignmentReport', 'type': 'AssignmentReport'},
        'context': {'key': 'context', 'type': 'str'},
        'assignment_hash': {'key': 'assignmentHash', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        guest_configuration: Optional["GuestConfigurationNavigation"] = None,
        latest_assignment_report: Optional["AssignmentReport"] = None,
        context: Optional[str] = None,
        **kwargs
    ):
        super(GuestConfigurationAssignmentProperties, self).__init__(**kwargs)
        self.target_resource_id = None
        self.guest_configuration = guest_configuration
        self.compliance_status = None
        self.last_compliance_status_checked = None
        self.latest_report_id = None
        self.latest_assignment_report = latest_assignment_report
        self.context = context
        self.assignment_hash = None
        self.provisioning_state = None


class GuestConfigurationAssignmentReport(msrest.serialization.Model):
    """Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the report for the guest configuration assignment.
    :vartype id: str
    :ivar name: GUID that identifies the guest configuration assignment report under a
     subscription, resource group.
    :vartype name: str
    :param properties: Properties of the guest configuration report.
    :type properties: ~azure.mgmt.guestconfig.models.GuestConfigurationAssignmentReportProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'GuestConfigurationAssignmentReportProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["GuestConfigurationAssignmentReportProperties"] = None,
        **kwargs
    ):
        super(GuestConfigurationAssignmentReport, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.properties = properties


class GuestConfigurationAssignmentReportList(msrest.serialization.Model):
    """List of guest configuration assignment reports.

    :param value: List of reports for the guest configuration. Report contains information such as
     compliance status, reason and more.
    :type value: list[~azure.mgmt.guestconfig.models.GuestConfigurationAssignmentReport]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[GuestConfigurationAssignmentReport]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["GuestConfigurationAssignmentReport"]] = None,
        **kwargs
    ):
        super(GuestConfigurationAssignmentReportList, self).__init__(**kwargs)
        self.value = value


class GuestConfigurationAssignmentReportProperties(msrest.serialization.Model):
    """Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~azure.mgmt.guestconfig.models.ComplianceStatus
    :ivar report_id: GUID that identifies the guest configuration assignment report under a
     subscription, resource group.
    :vartype report_id: str
    :param assignment: Configuration details of the guest configuration assignment.
    :type assignment: ~azure.mgmt.guestconfig.models.AssignmentInfo
    :param vm: Information about the VM.
    :type vm: ~azure.mgmt.guestconfig.models.VMInfo
    :ivar start_time: Start date and time of the guest configuration assignment compliance status
     check.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: End date and time of the guest configuration assignment compliance status
     check.
    :vartype end_time: ~datetime.datetime
    :param details: Details of the assignment report.
    :type details: ~azure.mgmt.guestconfig.models.AssignmentReportDetails
    """

    _validation = {
        'compliance_status': {'readonly': True},
        'report_id': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
    }

    _attribute_map = {
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'report_id': {'key': 'reportId', 'type': 'str'},
        'assignment': {'key': 'assignment', 'type': 'AssignmentInfo'},
        'vm': {'key': 'vm', 'type': 'VMInfo'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'details': {'key': 'details', 'type': 'AssignmentReportDetails'},
    }

    def __init__(
        self,
        *,
        assignment: Optional["AssignmentInfo"] = None,
        vm: Optional["VMInfo"] = None,
        details: Optional["AssignmentReportDetails"] = None,
        **kwargs
    ):
        super(GuestConfigurationAssignmentReportProperties, self).__init__(**kwargs)
        self.compliance_status = None
        self.report_id = None
        self.assignment = assignment
        self.vm = vm
        self.start_time = None
        self.end_time = None
        self.details = details


class GuestConfigurationNavigation(msrest.serialization.Model):
    """Guest configuration is an artifact that encapsulates DSC configuration and its dependencies. The artifact is a zip file containing DSC configuration (as MOF) and dependent resources and other dependencies like modules.

    :param kind: Kind of the guest configuration. For example:DSC. Possible values include: "DSC".
    :type kind: str or ~azure.mgmt.guestconfig.models.Kind
    :param name: Name of the guest configuration.
    :type name: str
    :param version: Version of the guest configuration.
    :type version: str
    :param content_uri: Uri of the storage where guest configuration package is uploaded.
    :type content_uri: str
    :param content_hash: Combined hash of the guest configuration package and configuration
     parameters.
    :type content_hash: str
    :param assignment_type: Specifies the assignment type and execution of the configuration.
     Possible values are Audit, DeployAndAutoCorrect, ApplyAndAutoCorrect and ApplyAndMonitor.
     Possible values include: "Audit", "DeployAndAutoCorrect", "ApplyAndAutoCorrect",
     "ApplyAndMonitor".
    :type assignment_type: str or ~azure.mgmt.guestconfig.models.AssignmentType
    :param configuration_parameter: The configuration parameters for the guest configuration.
    :type configuration_parameter: list[~azure.mgmt.guestconfig.models.ConfigurationParameter]
    :param configuration_setting: The configuration setting for the guest configuration.
    :type configuration_setting: ~azure.mgmt.guestconfig.models.ConfigurationSetting
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'content_hash': {'key': 'contentHash', 'type': 'str'},
        'assignment_type': {'key': 'assignmentType', 'type': 'str'},
        'configuration_parameter': {'key': 'configurationParameter', 'type': '[ConfigurationParameter]'},
        'configuration_setting': {'key': 'configurationSetting', 'type': 'ConfigurationSetting'},
    }

    def __init__(
        self,
        *,
        kind: Optional[Union[str, "Kind"]] = None,
        name: Optional[str] = None,
        version: Optional[str] = None,
        content_uri: Optional[str] = None,
        content_hash: Optional[str] = None,
        assignment_type: Optional[Union[str, "AssignmentType"]] = None,
        configuration_parameter: Optional[List["ConfigurationParameter"]] = None,
        configuration_setting: Optional["ConfigurationSetting"] = None,
        **kwargs
    ):
        super(GuestConfigurationNavigation, self).__init__(**kwargs)
        self.kind = kind
        self.name = name
        self.version = version
        self.content_uri = content_uri
        self.content_hash = content_hash
        self.assignment_type = assignment_type
        self.configuration_parameter = configuration_parameter
        self.configuration_setting = configuration_setting


class Operation(msrest.serialization.Model):
    """GuestConfiguration REST API operation.

    :param name: Operation name: For ex.
     providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/write or read.
    :type name: str
    :param display: Provider, Resource, Operation and description values.
    :type display: ~azure.mgmt.guestconfig.models.OperationDisplay
    :param status_code: Service provider: Microsoft.GuestConfiguration.
    :type status_code: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'status_code': {'key': 'properties.statusCode', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        status_code: Optional[str] = None,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.status_code = status_code


class OperationDisplay(msrest.serialization.Model):
    """Provider, Resource, Operation and description values.

    :param provider: Service provider: Microsoft.GuestConfiguration.
    :type provider: str
    :param resource: Resource on which the operation is performed:  For ex.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description about operation.
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
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationList(msrest.serialization.Model):
    """The response model for the list of Automation operations.

    :param value: List of Automation operations supported by the Automation resource provider.
    :type value: list[~azure.mgmt.guestconfig.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Operation"]] = None,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = value


class VMInfo(msrest.serialization.Model):
    """Information about the VM.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id of the VM.
    :vartype id: str
    :ivar uuid: UUID(Universally Unique Identifier) of the VM.
    :vartype uuid: str
    """

    _validation = {
        'id': {'readonly': True},
        'uuid': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'uuid': {'key': 'uuid', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(VMInfo, self).__init__(**kwargs)
        self.id = None
        self.uuid = None
