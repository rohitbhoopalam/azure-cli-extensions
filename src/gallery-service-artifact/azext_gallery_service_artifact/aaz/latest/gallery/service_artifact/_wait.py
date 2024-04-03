# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "gallery service-artifact wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/galleries/{}/serviceartifacts/{}", "2023-07-03"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.gallery_name = AAZStrArg(
            options=["--gallery-name"],
            help="The name of the Gallery under which the Service Artifact is created",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="The name of the resource group. The name is case insensitive.",
            required=True,
        )
        _args_schema.service_artifact_name = AAZStrArg(
            options=["-n", "--name", "--service-artifact-name"],
            help="The name of the Gallery Service Artifact.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="The expand expression to apply on the operation. Passing 'latestVersion' as value would return image reference from each region of the Service Artifact.",
            enum={"latestVersion": "latestVersion"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.GalleryServiceArtifactGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class GalleryServiceArtifactGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)
            if session.http_response.status_code in [202]:
                return self.on_202(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/serviceArtifacts/{serviceArtifactName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "galleryName", self.ctx.args.gallery_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceArtifactName", self.ctx.args.service_artifact_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2023-07-03",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _WaitHelper._build_schema_gallery_service_artifact_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

        def on_202(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_202
            )

        _schema_on_202 = None

        @classmethod
        def _build_schema_on_202(cls):
            if cls._schema_on_202 is not None:
                return cls._schema_on_202

            cls._schema_on_202 = AAZObjectType()
            _WaitHelper._build_schema_gallery_service_artifact_read(cls._schema_on_202)

            return cls._schema_on_202


class _WaitHelper:
    """Helper class for Wait"""

    _schema_gallery_service_artifact_read = None

    @classmethod
    def _build_schema_gallery_service_artifact_read(cls, _schema):
        if cls._schema_gallery_service_artifact_read is not None:
            _schema.id = cls._schema_gallery_service_artifact_read.id
            _schema.location = cls._schema_gallery_service_artifact_read.location
            _schema.name = cls._schema_gallery_service_artifact_read.name
            _schema.properties = cls._schema_gallery_service_artifact_read.properties
            _schema.tags = cls._schema_gallery_service_artifact_read.tags
            _schema.type = cls._schema_gallery_service_artifact_read.type
            return

        cls._schema_gallery_service_artifact_read = _schema_gallery_service_artifact_read = AAZObjectType()

        gallery_service_artifact_read = _schema_gallery_service_artifact_read
        gallery_service_artifact_read.id = AAZStrType()
        gallery_service_artifact_read.location = AAZStrType(
            flags={"required": True},
        )
        gallery_service_artifact_read.name = AAZStrType(
            flags={"required": True},
        )
        gallery_service_artifact_read.properties = AAZObjectType(
            flags={"required": True},
        )
        gallery_service_artifact_read.tags = AAZDictType()
        gallery_service_artifact_read.type = AAZStrType()

        properties = _schema_gallery_service_artifact_read.properties
        properties.description = AAZStrType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.target_locations = AAZListType(
            serialized_name="targetLocations",
            flags={"required": True},
        )
        properties.vm_artifacts_profiles = AAZListType(
            serialized_name="vmArtifactsProfiles",
            flags={"required": True},
        )

        target_locations = _schema_gallery_service_artifact_read.properties.target_locations
        target_locations.Element = AAZObjectType()

        _element = _schema_gallery_service_artifact_read.properties.target_locations.Element
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.vm_artifacts_profiles = AAZListType(
            serialized_name="vmArtifactsProfiles",
        )

        vm_artifacts_profiles = _schema_gallery_service_artifact_read.properties.target_locations.Element.vm_artifacts_profiles
        vm_artifacts_profiles.Element = AAZObjectType()
        cls._build_schema_vm_artifacts_profile_read(vm_artifacts_profiles.Element)

        vm_artifacts_profiles = _schema_gallery_service_artifact_read.properties.vm_artifacts_profiles
        vm_artifacts_profiles.Element = AAZObjectType()
        cls._build_schema_vm_artifacts_profile_read(vm_artifacts_profiles.Element)

        tags = _schema_gallery_service_artifact_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_gallery_service_artifact_read.id
        _schema.location = cls._schema_gallery_service_artifact_read.location
        _schema.name = cls._schema_gallery_service_artifact_read.name
        _schema.properties = cls._schema_gallery_service_artifact_read.properties
        _schema.tags = cls._schema_gallery_service_artifact_read.tags
        _schema.type = cls._schema_gallery_service_artifact_read.type

    _schema_vm_artifacts_profile_read = None

    @classmethod
    def _build_schema_vm_artifacts_profile_read(cls, _schema):
        if cls._schema_vm_artifacts_profile_read is not None:
            _schema.artifact_profiles = cls._schema_vm_artifacts_profile_read.artifact_profiles
            _schema.description = cls._schema_vm_artifacts_profile_read.description
            _schema.name = cls._schema_vm_artifacts_profile_read.name
            _schema.upgrade_provider_info = cls._schema_vm_artifacts_profile_read.upgrade_provider_info
            _schema.upgrade_sdp_policy = cls._schema_vm_artifacts_profile_read.upgrade_sdp_policy
            return

        cls._schema_vm_artifacts_profile_read = _schema_vm_artifacts_profile_read = AAZObjectType()

        vm_artifacts_profile_read = _schema_vm_artifacts_profile_read
        vm_artifacts_profile_read.artifact_profiles = AAZListType(
            serialized_name="artifactProfiles",
            flags={"required": True},
        )
        vm_artifacts_profile_read.description = AAZStrType()
        vm_artifacts_profile_read.name = AAZStrType(
            flags={"required": True},
        )
        vm_artifacts_profile_read.upgrade_provider_info = AAZObjectType(
            serialized_name="upgradeProviderInfo",
        )
        vm_artifacts_profile_read.upgrade_sdp_policy = AAZObjectType(
            serialized_name="upgradeSdpPolicy",
            flags={"required": True},
        )

        artifact_profiles = _schema_vm_artifacts_profile_read.artifact_profiles
        artifact_profiles.Element = AAZObjectType()

        _element = _schema_vm_artifacts_profile_read.artifact_profiles.Element
        _element.description = AAZStrType()
        _element.image_reference = AAZObjectType(
            serialized_name="imageReference",
        )

        image_reference = _schema_vm_artifacts_profile_read.artifact_profiles.Element.image_reference
        image_reference.current_version = AAZStrType(
            serialized_name="currentVersion",
        )
        image_reference.id = AAZStrType()
        image_reference.initial_version = AAZStrType(
            serialized_name="initialVersion",
        )
        image_reference.offer = AAZStrType()
        image_reference.publisher = AAZStrType()
        image_reference.shared_gallery_image_id = AAZStrType(
            serialized_name="sharedGalleryImageId",
        )
        image_reference.sku = AAZStrType()

        upgrade_provider_info = _schema_vm_artifacts_profile_read.upgrade_provider_info
        upgrade_provider_info.enable_auto_trigger = AAZBoolType(
            serialized_name="enableAutoTrigger",
        )
        upgrade_provider_info.upgrade_provider_parameters = AAZObjectType(
            serialized_name="upgradeProviderParameters",
        )

        upgrade_provider_parameters = _schema_vm_artifacts_profile_read.upgrade_provider_info.upgrade_provider_parameters
        upgrade_provider_parameters.service_group = AAZStrType(
            serialized_name="ServiceGroup",
        )
        upgrade_provider_parameters.service_identifier = AAZStrType(
            serialized_name="ServiceIdentifier",
        )

        upgrade_sdp_policy = _schema_vm_artifacts_profile_read.upgrade_sdp_policy
        upgrade_sdp_policy.scheduling_policy = AAZObjectType(
            serialized_name="schedulingPolicy",
        )
        upgrade_sdp_policy.type = AAZStrType()

        scheduling_policy = _schema_vm_artifacts_profile_read.upgrade_sdp_policy.scheduling_policy
        scheduling_policy.disable_regular_upgrades = AAZBoolType(
            serialized_name="disableRegularUpgrades",
        )
        scheduling_policy.max_concurrent_resource_count_per_region = AAZIntType(
            serialized_name="maxConcurrentResourceCountPerRegion",
        )
        scheduling_policy.upgrade_window = AAZStrType(
            serialized_name="upgradeWindow",
        )

        _schema.artifact_profiles = cls._schema_vm_artifacts_profile_read.artifact_profiles
        _schema.description = cls._schema_vm_artifacts_profile_read.description
        _schema.name = cls._schema_vm_artifacts_profile_read.name
        _schema.upgrade_provider_info = cls._schema_vm_artifacts_profile_read.upgrade_provider_info
        _schema.upgrade_sdp_policy = cls._schema_vm_artifacts_profile_read.upgrade_sdp_policy


__all__ = ["Wait"]
