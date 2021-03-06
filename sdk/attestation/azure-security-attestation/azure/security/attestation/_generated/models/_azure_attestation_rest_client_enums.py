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


class AttestationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Intel Software Guard eXtensions.
    SGX_ENCLAVE = "SgxEnclave"
    #: OpenEnclave extensions to SGX.
    OPEN_ENCLAVE = "OpenEnclave"
    #: Edge TPM Virtualization Based Security.
    TPM = "Tpm"

class CertificateModification(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The result of the operation
    """

    #: After the operation was performed, the certificate is in the set of certificates.
    IS_PRESENT = "IsPresent"
    #: After the operation was performed, the certificate is no longer present in the set of
    #: certificates.
    IS_ABSENT = "IsAbsent"

class DataType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the type of the data encoded contained within the "data" field of a "RuntimeData" or
    "InitTimeData" object
    """

    #: The contents of the field should be treated as binary and not interpreted by MAA.
    BINARY = "Binary"
    #: The contents of the field should be treated as a JSON object and may be further interpreted by
    #: MAA.
    JSON = "JSON"

class PolicyModification(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The result of the operation
    """

    #: The specified policy object was updated.
    UPDATED = "Updated"
    #: The specified policy object was removed.
    REMOVED = "Removed"
