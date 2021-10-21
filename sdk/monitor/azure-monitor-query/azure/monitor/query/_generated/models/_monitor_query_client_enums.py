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


class AggregationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the aggregation type of the metric.
    """

    NONE = "None"
    AVERAGE = "Average"
    COUNT = "Count"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"

class LogsColumnType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The data type of this column.
    """

    BOOL = "bool"
    DATETIME = "datetime"
    DYNAMIC = "dynamic"
    INT = "int"
    LONG = "long"
    REAL = "real"
    STRING = "string"
    GUID = "guid"
    DECIMAL = "decimal"
    TIMESPAN = "timespan"

class MetadataColumnDataType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The data type of the column
    """

    BOOL = "bool"
    DATETIME = "datetime"
    DYNAMIC = "dynamic"
    INT = "int"
    LONG = "long"
    REAL = "real"
    STRING = "string"
    GUID = "guid"
    DECIMAL = "decimal"
    TIMESPAN = "timespan"

class MetricClass(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The class of the metric.
    """

    AVAILABILITY = "Availability"
    TRANSACTIONS = "Transactions"
    ERRORS = "Errors"
    LATENCY = "Latency"
    SATURATION = "Saturation"

class MetricUnit(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The unit of the metric.
    """

    COUNT = "Count"
    BYTES = "Bytes"
    SECONDS = "Seconds"
    COUNT_PER_SECOND = "CountPerSecond"
    BYTES_PER_SECOND = "BytesPerSecond"
    PERCENT = "Percent"
    MILLI_SECONDS = "MilliSeconds"
    BYTE_SECONDS = "ByteSeconds"
    UNSPECIFIED = "Unspecified"
    CORES = "Cores"
    MILLI_CORES = "MilliCores"
    NANO_CORES = "NanoCores"
    BITS_PER_SECOND = "BitsPerSecond"

class NamespaceClassification(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of namespace
    """

    PLATFORM = "Platform"
    CUSTOM = "Custom"
    QOS = "Qos"

class ResultType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DATA = "Data"
    METADATA = "Metadata"
