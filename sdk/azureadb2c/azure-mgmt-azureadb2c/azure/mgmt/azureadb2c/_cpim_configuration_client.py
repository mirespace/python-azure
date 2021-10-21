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

from azure.mgmt.core import ARMPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import CPIMConfigurationClientConfiguration

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class CPIMConfigurationClient(MultiApiClientMixin, _SDKClient):
    """CPIM Configuration Client.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2020-05-01-preview'
    _PROFILE_TAG = "azure.mgmt.azureadb2c.CPIMConfigurationClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'b2_ctenants': '2019-01-01-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None,
        base_url=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = CPIMConfigurationClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(CPIMConfigurationClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-01-01-preview: :mod:`v2019_01_01_preview.models<azure.mgmt.azureadb2c.v2019_01_01_preview.models>`
           * 2020-05-01-preview: :mod:`v2020_05_01_preview.models<azure.mgmt.azureadb2c.v2020_05_01_preview.models>`
        """
        if api_version == '2019-01-01-preview':
            from .v2019_01_01_preview import models
            return models
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def b2_ctenants(self):
        """Instance depends on the API version:

           * 2019-01-01-preview: :class:`B2CTenantsOperations<azure.mgmt.azureadb2c.v2019_01_01_preview.operations.B2CTenantsOperations>`
        """
        api_version = self._get_api_version('b2_ctenants')
        if api_version == '2019-01-01-preview':
            from .v2019_01_01_preview.operations import B2CTenantsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'b2_ctenants'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def guest_usages(self):
        """Instance depends on the API version:

           * 2020-05-01-preview: :class:`GuestUsagesOperations<azure.mgmt.azureadb2c.v2020_05_01_preview.operations.GuestUsagesOperations>`
        """
        api_version = self._get_api_version('guest_usages')
        if api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import GuestUsagesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'guest_usages'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2019-01-01-preview: :class:`Operations<azure.mgmt.azureadb2c.v2019_01_01_preview.operations.Operations>`
           * 2020-05-01-preview: :class:`Operations<azure.mgmt.azureadb2c.v2020_05_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2019-01-01-preview':
            from .v2019_01_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-05-01-preview':
            from .v2020_05_01_preview.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
