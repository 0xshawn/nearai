# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from nearai.openapi_client.models.entry_location import EntryLocation
from nearai.openapi_client.models.entry_metadata_input import EntryMetadataInput
from typing import Optional, Set
from typing_extensions import Self

class BodyUploadMetadataV1RegistryUploadMetadataPost(BaseModel):
    """
    BodyUploadMetadataV1RegistryUploadMetadataPost
    """ # noqa: E501
    metadata: EntryMetadataInput
    entry_location: EntryLocation
    __properties: ClassVar[List[str]] = ["metadata", "entry_location"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BodyUploadMetadataV1RegistryUploadMetadataPost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entry_location
        if self.entry_location:
            _dict['entry_location'] = self.entry_location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BodyUploadMetadataV1RegistryUploadMetadataPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "metadata": EntryMetadataInput.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "entry_location": EntryLocation.from_dict(obj["entry_location"]) if obj.get("entry_location") is not None else None
        })
        return _obj

