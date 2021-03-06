# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from ._models import DeletedSecret, KeyVaultSecret, KeyVaultSecretIdentifier, SecretProperties
from ._shared.client_base import ApiVersion
from ._client import SecretClient

__all__ = [
    "ApiVersion",
    "SecretClient",
    "KeyVaultSecret",
    "KeyVaultSecretIdentifier",
    "SecretProperties",
    "DeletedSecret"
]

from ._version import VERSION
__version__ = VERSION
