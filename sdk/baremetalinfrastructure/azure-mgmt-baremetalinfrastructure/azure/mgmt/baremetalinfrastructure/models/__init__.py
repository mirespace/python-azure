# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AzureBareMetalInstance
    from ._models_py3 import AzureBareMetalInstancesListResult
    from ._models_py3 import Disk
    from ._models_py3 import Display
    from ._models_py3 import ErrorDefinition
    from ._models_py3 import ErrorResponse
    from ._models_py3 import HardwareProfile
    from ._models_py3 import IpAddress
    from ._models_py3 import NetworkProfile
    from ._models_py3 import OSProfile
    from ._models_py3 import Operation
    from ._models_py3 import OperationList
    from ._models_py3 import Resource
    from ._models_py3 import Result
    from ._models_py3 import StorageProfile
    from ._models_py3 import SystemData
    from ._models_py3 import Tags
    from ._models_py3 import TrackedResource
except (SyntaxError, ImportError):
    from ._models import AzureBareMetalInstance  # type: ignore
    from ._models import AzureBareMetalInstancesListResult  # type: ignore
    from ._models import Disk  # type: ignore
    from ._models import Display  # type: ignore
    from ._models import ErrorDefinition  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import HardwareProfile  # type: ignore
    from ._models import IpAddress  # type: ignore
    from ._models import NetworkProfile  # type: ignore
    from ._models import OSProfile  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationList  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Result  # type: ignore
    from ._models import StorageProfile  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import Tags  # type: ignore
    from ._models import TrackedResource  # type: ignore

from ._bare_metal_infrastructure_client_enums import (
    AzureBareMetalHardwareTypeNamesEnum,
    AzureBareMetalInstancePowerStateEnum,
    AzureBareMetalInstanceSizeNamesEnum,
    AzureBareMetalProvisioningStatesEnum,
    CreatedByType,
)

__all__ = [
    'AzureBareMetalInstance',
    'AzureBareMetalInstancesListResult',
    'Disk',
    'Display',
    'ErrorDefinition',
    'ErrorResponse',
    'HardwareProfile',
    'IpAddress',
    'NetworkProfile',
    'OSProfile',
    'Operation',
    'OperationList',
    'Resource',
    'Result',
    'StorageProfile',
    'SystemData',
    'Tags',
    'TrackedResource',
    'AzureBareMetalHardwareTypeNamesEnum',
    'AzureBareMetalInstancePowerStateEnum',
    'AzureBareMetalInstanceSizeNamesEnum',
    'AzureBareMetalProvisioningStatesEnum',
    'CreatedByType',
]
