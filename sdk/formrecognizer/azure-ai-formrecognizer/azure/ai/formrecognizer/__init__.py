# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from ._version import VERSION
from ._form_recognizer_client import FormRecognizerClient
from ._form_training_client import FormTrainingClient
from ._document_analysis_client import DocumentAnalysisClient
from ._document_model_administration_client import DocumentModelAdministrationClient
from ._polling import DocumentModelAdministrationLROPoller
from ._models import (
    FormElement,
    LengthUnit,
    TrainingStatus,
    CustomFormModelStatus,
    FormContentType,
    FormTable,
    FormTableCell,
    TrainingDocumentInfo,
    FormRecognizerError,
    CustomFormModelInfo,
    AccountProperties,
    Point,
    FormPageRange,
    RecognizedForm,
    FormField,
    FieldData,
    FormPage,
    FormLine,
    FormWord,
    CustomFormModel,
    CustomFormSubmodel,
    CustomFormModelField,
    FieldValueType,
    CustomFormModelProperties,
    FormSelectionMark,
    TextAppearance,
    AnalyzeResult,
    AnalyzedDocument,
    BoundingRegion,
<<<<<<< HEAD
    DocumentElement,
=======
    DocumentContentElement,
>>>>>>> main
    DocumentEntity,
    DocumentField,
    DocumentKeyValuePair,
    DocumentKeyValueElement,
    DocumentLine,
    DocumentPage,
    DocumentSelectionMark,
    DocumentSpan,
    DocumentStyle,
    DocumentTable,
    DocumentTableCell,
    DocumentWord,
    ModelOperationInfo,
    ModelOperation,
    DocumentModel,
    DocumentModelInfo,
    DocTypeInfo,
    AccountInfo,
    DocumentAnalysisError,
    DocumentAnalysisInnerError,
)
from ._api_versions import FormRecognizerApiVersion, DocumentAnalysisApiVersion


__all__ = [
    "FormRecognizerApiVersion",
    "DocumentAnalysisClient",
    "DocumentModelAdministrationClient",
    "FormRecognizerClient",
    "FormTrainingClient",
    "LengthUnit",
    "TrainingStatus",
    "CustomFormModelStatus",
    "FormContentType",
    "FormElement",
    "FormTable",
    "FormTableCell",
    "TrainingDocumentInfo",
    "FormRecognizerError",
    "CustomFormModelInfo",
    "AccountProperties",
    "Point",
    "FormPageRange",
    "RecognizedForm",
    "FormField",
    "FieldData",
    "FormPage",
    "FormLine",
    "FormWord",
    "CustomFormModel",
    "CustomFormSubmodel",
    "CustomFormModelField",
    "FieldValueType",
    "CustomFormModelProperties",
    "FormSelectionMark",
    "TextAppearance",
    "AnalyzeResult",
    "AnalyzedDocument",
    "BoundingRegion",
<<<<<<< HEAD
    "DocumentElement",
=======
    "DocumentContentElement",
>>>>>>> main
    "DocumentEntity",
    "DocumentField",
    "DocumentKeyValueElement",
    "DocumentKeyValuePair",
    "DocumentLine",
    "DocumentPage",
    "DocumentSelectionMark",
    "DocumentSpan",
    "DocumentStyle",
    "DocumentTable",
    "DocumentTableCell",
    "DocumentWord",
    "DocumentModelAdministrationLROPoller",
    "ModelOperationInfo",
    "ModelOperation",
    "DocumentAnalysisApiVersion",
    "DocumentModel",
    "DocumentModelInfo",
    "DocTypeInfo",
    "AccountInfo",
    "DocumentAnalysisError",
    "DocumentAnalysisInnerError",
]

__VERSION__ = VERSION
