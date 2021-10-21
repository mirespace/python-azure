# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class ApplicationSummaryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationSummary <azure.batch.models.ApplicationSummary>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationSummary]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationSummaryPaged, self).__init__(*args, **kwargs)
class PoolUsageMetricsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PoolUsageMetrics <azure.batch.models.PoolUsageMetrics>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PoolUsageMetrics]'}
    }

    def __init__(self, *args, **kwargs):

        super(PoolUsageMetricsPaged, self).__init__(*args, **kwargs)
class CloudPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CloudPool <azure.batch.models.CloudPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CloudPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(CloudPoolPaged, self).__init__(*args, **kwargs)
class ImageInformationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ImageInformation <azure.batch.models.ImageInformation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ImageInformation]'}
    }

    def __init__(self, *args, **kwargs):

        super(ImageInformationPaged, self).__init__(*args, **kwargs)
class PoolNodeCountsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PoolNodeCounts <azure.batch.models.PoolNodeCounts>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PoolNodeCounts]'}
    }

    def __init__(self, *args, **kwargs):

        super(PoolNodeCountsPaged, self).__init__(*args, **kwargs)
class CloudJobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CloudJob <azure.batch.models.CloudJob>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CloudJob]'}
    }

    def __init__(self, *args, **kwargs):

        super(CloudJobPaged, self).__init__(*args, **kwargs)
class JobPreparationAndReleaseTaskExecutionInformationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobPreparationAndReleaseTaskExecutionInformation <azure.batch.models.JobPreparationAndReleaseTaskExecutionInformation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobPreparationAndReleaseTaskExecutionInformation]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobPreparationAndReleaseTaskExecutionInformationPaged, self).__init__(*args, **kwargs)
class CertificatePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Certificate <azure.batch.models.Certificate>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Certificate]'}
    }

    def __init__(self, *args, **kwargs):

        super(CertificatePaged, self).__init__(*args, **kwargs)
class NodeFilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`NodeFile <azure.batch.models.NodeFile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NodeFile]'}
    }

    def __init__(self, *args, **kwargs):

        super(NodeFilePaged, self).__init__(*args, **kwargs)
class CloudJobSchedulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`CloudJobSchedule <azure.batch.models.CloudJobSchedule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CloudJobSchedule]'}
    }

    def __init__(self, *args, **kwargs):

        super(CloudJobSchedulePaged, self).__init__(*args, **kwargs)
class CloudTaskPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CloudTask <azure.batch.models.CloudTask>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CloudTask]'}
    }

    def __init__(self, *args, **kwargs):

        super(CloudTaskPaged, self).__init__(*args, **kwargs)
class ComputeNodePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ComputeNode <azure.batch.models.ComputeNode>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ComputeNode]'}
    }

    def __init__(self, *args, **kwargs):

        super(ComputeNodePaged, self).__init__(*args, **kwargs)
class NodeVMExtensionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NodeVMExtension <azure.batch.models.NodeVMExtension>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NodeVMExtension]'}
    }

    def __init__(self, *args, **kwargs):

        super(NodeVMExtensionPaged, self).__init__(*args, **kwargs)
