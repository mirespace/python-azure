# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from json import loads as _loads
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async

from ..._vendor import _convert_request
from ...operations._operations import build_metadata_policy_get_request, build_metadata_policy_list_all_request, build_metadata_policy_update_request, build_metadata_roles_list_request

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MetadataRolesOperations:
    """MetadataRolesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> AsyncIterable[Any]:
        """Lists roles for Purview Account.

        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.async_paging.AsyncItemPaged[Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "nextLink": "str",  # Optional.
                    "values": [
                        {
                            "id": "str",  # Optional. The Id of role.
                            "name": "str",  # Optional. The name of role.
                            "properties": {
                                "cnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "description": "str",  # Optional. The description of role.
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "friendlyName": "str",  # Optional. The friendly name of role.
                                "provisioningState": "str",  # Optional. The provisioningState of role.
                                "roleType": "str",  # Optional. The type of role.
                                "version": 0.0  # Optional. The version of role.
                            },
                            "type": "str"  # Optional. The type of role.
                        }
                    ]
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_metadata_roles_list_request(
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_metadata_roles_list_request(
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = _loads(pipeline_response.http_response.body())
            list_of_elem = deserialized["values"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/metadataRoles'}  # type: ignore
class MetadataPolicyOperations:
    """MetadataPolicyOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_all(
        self,
        *,
        collection_name: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable[Any]:
        """List or Get metadata policies.

        :keyword collection_name: The name of an existing collection for which one policy needs to be
         fetched.
        :paramtype collection_name: str
        :return: An iterator like instance of JSON object
        :rtype: ~azure.core.async_paging.AsyncItemPaged[Any]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "nextLink": "str",  # Optional.
                    "values": [
                        {
                            "id": "str",  # Optional. The id of policy.
                            "name": "str",  # Optional. The name of policy.
                            "properties": {
                                "attributeRules": [
                                    {
                                        "dnfCondition": [
                                            [
                                                {
                                                    "attributeName": "str",  # Optional. AttributeName.
                                                    "attributeValueExcludedIn": [
                                                        "str"  # Optional. List of values excluded for attribute.
                                                    ],
                                                    "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                                    "attributeValueIncludedIn": [
                                                        "str"  # Optional. List of values for attribute.
                                                    ],
                                                    "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                                }
                                            ]
                                        ],
                                        "id": "str",  # Optional. The id for rule.
                                        "kind": "str",  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                                        "name": "str"  # Optional. The name for rule.
                                    }
                                ],
                                "collection": {
                                    "referenceName": "str",  # Optional. The name of reference.
                                    "type": "CollectionReference"  # Optional. Default value is "CollectionReference". The type of reference.
                                },
                                "decisionRules": [
                                    {
                                        "dnfCondition": [
                                            [
                                                {
                                                    "attributeName": "str",  # Optional. AttributeName.
                                                    "attributeValueExcludedIn": [
                                                        "str"  # Optional. List of values excluded for attribute.
                                                    ],
                                                    "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                                    "attributeValueIncludedIn": [
                                                        "str"  # Optional. List of values for attribute.
                                                    ],
                                                    "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                                }
                                            ]
                                        ],
                                        "effect": "str",  # Optional. The effect for rule. Possible values include: "Deny", "Permit".
                                        "kind": "str"  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                                    }
                                ],
                                "description": "str",  # Optional. The description of policy.
                                "parentCollectionName": "str"  # Optional. The parent collection of the policy.
                            },
                            "version": 0  # Optional. The version of policy.
                        }
                    ]
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_metadata_policy_list_all_request(
                    collection_name=collection_name,
                    template_url=self.list_all.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_metadata_policy_list_all_request(
                    collection_name=collection_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = _loads(pipeline_response.http_response.body())
            list_of_elem = deserialized["values"]
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.get("nextLink", None), AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_all.metadata = {'url': '/metadataPolicies'}  # type: ignore

    @distributed_trace_async
    async def update(
        self,
        policy_id: str,
        body: Any = None,
        **kwargs: Any
    ) -> Any:
        """Updates a metadata policy.

        :param policy_id: Unique policy id.
        :type policy_id: str
        :param body: Policy to be updated.
        :type body: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "id": "str",  # Optional. The id of policy.
                    "name": "str",  # Optional. The name of policy.
                    "properties": {
                        "attributeRules": [
                            {
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "id": "str",  # Optional. The id for rule.
                                "kind": "str",  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                                "name": "str"  # Optional. The name for rule.
                            }
                        ],
                        "collection": {
                            "referenceName": "str",  # Optional. The name of reference.
                            "type": "CollectionReference"  # Optional. Default value is "CollectionReference". The type of reference.
                        },
                        "decisionRules": [
                            {
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "effect": "str",  # Optional. The effect for rule. Possible values include: "Deny", "Permit".
                                "kind": "str"  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                            }
                        ],
                        "description": "str",  # Optional. The description of policy.
                        "parentCollectionName": "str"  # Optional. The parent collection of the policy.
                    },
                    "version": 0  # Optional. The version of policy.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": "str",  # Optional. The id of policy.
                    "name": "str",  # Optional. The name of policy.
                    "properties": {
                        "attributeRules": [
                            {
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "id": "str",  # Optional. The id for rule.
                                "kind": "str",  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                                "name": "str"  # Optional. The name for rule.
                            }
                        ],
                        "collection": {
                            "referenceName": "str",  # Optional. The name of reference.
                            "type": "CollectionReference"  # Optional. Default value is "CollectionReference". The type of reference.
                        },
                        "decisionRules": [
                            {
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "effect": "str",  # Optional. The effect for rule. Possible values include: "Deny", "Permit".
                                "kind": "str"  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                            }
                        ],
                        "description": "str",  # Optional. The description of policy.
                        "parentCollectionName": "str"  # Optional. The parent collection of the policy.
                    },
                    "version": 0  # Optional. The version of policy.
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if body is not None:
            json = body
        else:
            json = None

        request = build_metadata_policy_update_request(
            policy_id=policy_id,
            content_type=content_type,
            json=json,
            template_url=self.update.metadata['url'],
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/metadataPolicies/{policyId}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        policy_id: str,
        **kwargs: Any
    ) -> Any:
        """Gets a metadata policy.

        :param policy_id: Id of an existing policy that needs to be fetched.
        :type policy_id: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": "str",  # Optional. The id of policy.
                    "name": "str",  # Optional. The name of policy.
                    "properties": {
                        "attributeRules": [
                            {
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "id": "str",  # Optional. The id for rule.
                                "kind": "str",  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                                "name": "str"  # Optional. The name for rule.
                            }
                        ],
                        "collection": {
                            "referenceName": "str",  # Optional. The name of reference.
                            "type": "CollectionReference"  # Optional. Default value is "CollectionReference". The type of reference.
                        },
                        "decisionRules": [
                            {
                                "dnfCondition": [
                                    [
                                        {
                                            "attributeName": "str",  # Optional. AttributeName.
                                            "attributeValueExcludedIn": [
                                                "str"  # Optional. List of values excluded for attribute.
                                            ],
                                            "attributeValueExcludes": "str",  # Optional. Value excluded for attribute.
                                            "attributeValueIncludedIn": [
                                                "str"  # Optional. List of values for attribute.
                                            ],
                                            "attributeValueIncludes": "str"  # Optional. Value for attribute.
                                        }
                                    ]
                                ],
                                "effect": "str",  # Optional. The effect for rule. Possible values include: "Deny", "Permit".
                                "kind": "str"  # Optional. The kind of rule. Possible values include: "decisionrule", "attributerule".
                            }
                        ],
                        "description": "str",  # Optional. The description of policy.
                        "parentCollectionName": "str"  # Optional. The parent collection of the policy.
                    },
                    "version": 0  # Optional. The version of policy.
                }
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Any]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_metadata_policy_get_request(
            policy_id=policy_id,
            template_url=self.get.metadata['url'],
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/metadataPolicies/{policyId}'}  # type: ignore

