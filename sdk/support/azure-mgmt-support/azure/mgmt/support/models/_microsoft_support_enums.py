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


class CommunicationDirection(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Direction of communication.
    """

    INBOUND = "inbound"
    OUTBOUND = "outbound"

class CommunicationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Communication type.
    """

    WEB = "web"
    PHONE = "phone"

class PreferredContactMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Preferred contact method.
    """

    EMAIL = "email"
    PHONE = "phone"

class SeverityLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A value that indicates the urgency of the case, which in turn determines the response time
    according to the service level agreement of the technical support plan you have with Azure.
    Note: 'Highest critical impact', also known as the 'Emergency - Severe impact' level in the
    Azure portal is reserved only for our Premium customers.
    """

    MINIMAL = "minimal"
    MODERATE = "moderate"
    CRITICAL = "critical"
    HIGHESTCRITICALIMPACT = "highestcriticalimpact"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status to be updated on the ticket.
    """

    OPEN = "open"
    CLOSED = "closed"

class Type(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of resource.
    """

    MICROSOFT_SUPPORT_SUPPORT_TICKETS = "Microsoft.Support/supportTickets"
    MICROSOFT_SUPPORT_COMMUNICATIONS = "Microsoft.Support/communications"