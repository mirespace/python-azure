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

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import AzureDigitalTwinsManagementClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class AzureDigitalTwinsManagementClient(MultiApiClientMixin, _SDKClient):
    """Azure Digital Twins Client for managing DigitalTwinsInstance.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2020-12-01'
    _PROFILE_TAG = "azure.mgmt.digitaltwins.AzureDigitalTwinsManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url=None,  # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureDigitalTwinsManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(AzureDigitalTwinsManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2020-03-01-preview: :mod:`v2020_03_01_preview.models<azure.mgmt.digitaltwins.v2020_03_01_preview.models>`
           * 2020-10-31: :mod:`v2020_10_31.models<azure.mgmt.digitaltwins.v2020_10_31.models>`
           * 2020-12-01: :mod:`v2020_12_01.models<azure.mgmt.digitaltwins.v2020_12_01.models>`
        """
        if api_version == '2020-03-01-preview':
            from .v2020_03_01_preview import models
            return models
        elif api_version == '2020-10-31':
            from .v2020_10_31 import models
            return models
        elif api_version == '2020-12-01':
            from .v2020_12_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def digital_twins(self):
        """Instance depends on the API version:

           * 2020-03-01-preview: :class:`DigitalTwinsOperations<azure.mgmt.digitaltwins.v2020_03_01_preview.operations.DigitalTwinsOperations>`
           * 2020-10-31: :class:`DigitalTwinsOperations<azure.mgmt.digitaltwins.v2020_10_31.operations.DigitalTwinsOperations>`
           * 2020-12-01: :class:`DigitalTwinsOperations<azure.mgmt.digitaltwins.v2020_12_01.operations.DigitalTwinsOperations>`
        """
        api_version = self._get_api_version('digital_twins')
        if api_version == '2020-03-01-preview':
            from .v2020_03_01_preview.operations import DigitalTwinsOperations as OperationClass
        elif api_version == '2020-10-31':
            from .v2020_10_31.operations import DigitalTwinsOperations as OperationClass
        elif api_version == '2020-12-01':
            from .v2020_12_01.operations import DigitalTwinsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'digital_twins'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def digital_twins_endpoint(self):
        """Instance depends on the API version:

           * 2020-03-01-preview: :class:`DigitalTwinsEndpointOperations<azure.mgmt.digitaltwins.v2020_03_01_preview.operations.DigitalTwinsEndpointOperations>`
           * 2020-10-31: :class:`DigitalTwinsEndpointOperations<azure.mgmt.digitaltwins.v2020_10_31.operations.DigitalTwinsEndpointOperations>`
           * 2020-12-01: :class:`DigitalTwinsEndpointOperations<azure.mgmt.digitaltwins.v2020_12_01.operations.DigitalTwinsEndpointOperations>`
        """
        api_version = self._get_api_version('digital_twins_endpoint')
        if api_version == '2020-03-01-preview':
            from .v2020_03_01_preview.operations import DigitalTwinsEndpointOperations as OperationClass
        elif api_version == '2020-10-31':
            from .v2020_10_31.operations import DigitalTwinsEndpointOperations as OperationClass
        elif api_version == '2020-12-01':
            from .v2020_12_01.operations import DigitalTwinsEndpointOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'digital_twins_endpoint'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2020-03-01-preview: :class:`Operations<azure.mgmt.digitaltwins.v2020_03_01_preview.operations.Operations>`
           * 2020-10-31: :class:`Operations<azure.mgmt.digitaltwins.v2020_10_31.operations.Operations>`
           * 2020-12-01: :class:`Operations<azure.mgmt.digitaltwins.v2020_12_01.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2020-03-01-preview':
            from .v2020_03_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-10-31':
            from .v2020_10_31.operations import Operations as OperationClass
        elif api_version == '2020-12-01':
            from .v2020_12_01.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2020-12-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.digitaltwins.v2020_12_01.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2020-12-01':
            from .v2020_12_01.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2020-12-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.digitaltwins.v2020_12_01.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2020-12-01':
            from .v2020_12_01.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
