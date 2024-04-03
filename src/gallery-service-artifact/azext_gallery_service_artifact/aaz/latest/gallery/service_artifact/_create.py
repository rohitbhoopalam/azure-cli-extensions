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
    "gallery service-artifact create",
)
class Create(AAZCommand):
    """Create a Service Artifact under a gallery.
    """

    _aaz_info = {
        "version": "2023-07-03",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.compute/galleries/{}/serviceartifacts/{}", "2023-07-03"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

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
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="The name of the resource group. The name is case insensitive.",
            required=True,
        )
        _args_schema.service_artifact_name = AAZStrArg(
            options=["-n", "--name", "--service-artifact-name"],
            help="The name of the Gallery Service Artifact.",
            required=True,
        )

        # define Arg Group "GalleryServiceArtifact"

        _args_schema = cls._args_schema
        _args_schema.location = AAZStrArg(
            options=["--location"],
            arg_group="GalleryServiceArtifact",
            help="The Azure region where Service Artifact is created",
            required=True,
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="GalleryServiceArtifact",
            help="Resource tags",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Description of the Service Artifact",
        )
        _args_schema.target_locations = AAZListArg(
            options=["--target-locations"],
            arg_group="Properties",
            help="List of target locations for the Service Artifact",
            required=True,
        )
        _args_schema.vm_artifacts_profiles = AAZListArg(
            options=["--vm-artifacts-profiles"],
            arg_group="Properties",
            help="VM Artifact Profile Definition",
            required=True,
        )

        target_locations = cls._args_schema.target_locations
        target_locations.Element = AAZObjectArg()

        _element = cls._args_schema.target_locations.Element
        _element.name = AAZStrArg(
            options=["name"],
            required=True,
        )
        _element.vm_artifacts_profiles = AAZListArg(
            options=["vm-artifacts-profiles"],
        )

        vm_artifacts_profiles = cls._args_schema.target_locations.Element.vm_artifacts_profiles
        vm_artifacts_profiles.Element = AAZObjectArg()
        cls._build_args_vm_artifacts_profile_create(vm_artifacts_profiles.Element)

        vm_artifacts_profiles = cls._args_schema.vm_artifacts_profiles
        vm_artifacts_profiles.Element = AAZObjectArg()
        cls._build_args_vm_artifacts_profile_create(vm_artifacts_profiles.Element)
        return cls._args_schema

    _args_vm_artifacts_profile_create = None

    @classmethod
    def _build_args_vm_artifacts_profile_create(cls, _schema):
        if cls._args_vm_artifacts_profile_create is not None:
            _schema.artifact_profiles = cls._args_vm_artifacts_profile_create.artifact_profiles
            _schema.description = cls._args_vm_artifacts_profile_create.description
            _schema.name = cls._args_vm_artifacts_profile_create.name
            _schema.upgrade_provider_info = cls._args_vm_artifacts_profile_create.upgrade_provider_info
            _schema.upgrade_sdp_policy = cls._args_vm_artifacts_profile_create.upgrade_sdp_policy
            return

        cls._args_vm_artifacts_profile_create = AAZObjectArg()

        vm_artifacts_profile_create = cls._args_vm_artifacts_profile_create
        vm_artifacts_profile_create.artifact_profiles = AAZListArg(
            options=["artifact-profiles"],
            help="Artifact Profile",
            required=True,
        )
        vm_artifacts_profile_create.description = AAZStrArg(
            options=["description"],
        )
        vm_artifacts_profile_create.name = AAZStrArg(
            options=["name"],
            help="Name of the VM Artifact Profile",
            required=True,
        )
        vm_artifacts_profile_create.upgrade_provider_info = AAZObjectArg(
            options=["upgrade-provider-info"],
        )
        vm_artifacts_profile_create.upgrade_sdp_policy = AAZObjectArg(
            options=["upgrade-sdp-policy"],
            required=True,
        )

        artifact_profiles = cls._args_vm_artifacts_profile_create.artifact_profiles
        artifact_profiles.Element = AAZObjectArg()

        _element = cls._args_vm_artifacts_profile_create.artifact_profiles.Element
        _element.description = AAZStrArg(
            options=["description"],
        )
        _element.image_reference = AAZObjectArg(
            options=["image-reference"],
        )

        image_reference = cls._args_vm_artifacts_profile_create.artifact_profiles.Element.image_reference
        image_reference.current_version = AAZStrArg(
            options=["current-version"],
            help="Current version of the Service Artifact image version",
        )
        image_reference.id = AAZStrArg(
            options=["id"],
            help="Reference to gallery image id",
        )
        image_reference.initial_version = AAZStrArg(
            options=["initial-version"],
            help="Initial version of the Service Artifact image version",
        )
        image_reference.offer = AAZStrArg(
            options=["offer"],
            help="PIR image offer name",
        )
        image_reference.publisher = AAZStrArg(
            options=["publisher"],
            help="PIR image publisher name",
        )
        image_reference.shared_gallery_image_id = AAZStrArg(
            options=["shared-gallery-image-id"],
            help="Reference to 1P gallery image id",
        )
        image_reference.sku = AAZStrArg(
            options=["sku"],
            help="PIR image SKU",
        )

        upgrade_provider_info = cls._args_vm_artifacts_profile_create.upgrade_provider_info
        upgrade_provider_info.enable_auto_trigger = AAZBoolArg(
            options=["enable-auto-trigger"],
        )
        upgrade_provider_info.upgrade_provider_parameters = AAZObjectArg(
            options=["upgrade-provider-parameters"],
        )

        upgrade_provider_parameters = cls._args_vm_artifacts_profile_create.upgrade_provider_info.upgrade_provider_parameters
        upgrade_provider_parameters.service_group = AAZStrArg(
            options=["service-group"],
            help="Service group parameter for Ev2",
        )
        upgrade_provider_parameters.service_identifier = AAZStrArg(
            options=["service-identifier"],
            help="Service identifier GUID for Ev2",
        )

        upgrade_sdp_policy = cls._args_vm_artifacts_profile_create.upgrade_sdp_policy
        upgrade_sdp_policy.scheduling_policy = AAZObjectArg(
            options=["scheduling-policy"],
        )
        upgrade_sdp_policy.type = AAZStrArg(
            options=["type"],
        )

        scheduling_policy = cls._args_vm_artifacts_profile_create.upgrade_sdp_policy.scheduling_policy
        scheduling_policy.disable_regular_upgrades = AAZBoolArg(
            options=["disable-regular-upgrades"],
        )
        scheduling_policy.max_concurrent_resource_count_per_region = AAZIntArg(
            options=["max-concurrent-resource-count-per-region"],
        )
        scheduling_policy.upgrade_window = AAZStrArg(
            options=["upgrade-window"],
        )

        _schema.artifact_profiles = cls._args_vm_artifacts_profile_create.artifact_profiles
        _schema.description = cls._args_vm_artifacts_profile_create.description
        _schema.name = cls._args_vm_artifacts_profile_create.name
        _schema.upgrade_provider_info = cls._args_vm_artifacts_profile_create.upgrade_provider_info
        _schema.upgrade_sdp_policy = cls._args_vm_artifacts_profile_create.upgrade_sdp_policy

    def _execute_operations(self):
        self.pre_operations()
        yield self.GalleryServiceArtifactCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class GalleryServiceArtifactCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/serviceArtifacts/{serviceArtifactName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

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
                    "api-version", "2023-07-03",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("name", AAZStrType, ".service_artifact_name", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("targetLocations", AAZListType, ".target_locations", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("vmArtifactsProfiles", AAZListType, ".vm_artifacts_profiles", typ_kwargs={"flags": {"required": True}})

            target_locations = _builder.get(".properties.targetLocations")
            if target_locations is not None:
                target_locations.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.targetLocations[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("vmArtifactsProfiles", AAZListType, ".vm_artifacts_profiles")

            vm_artifacts_profiles = _builder.get(".properties.targetLocations[].vmArtifactsProfiles")
            if vm_artifacts_profiles is not None:
                _CreateHelper._build_schema_vm_artifacts_profile_create(vm_artifacts_profiles.set_elements(AAZObjectType, "."))

            vm_artifacts_profiles = _builder.get(".properties.vmArtifactsProfiles")
            if vm_artifacts_profiles is not None:
                _CreateHelper._build_schema_vm_artifacts_profile_create(vm_artifacts_profiles.set_elements(AAZObjectType, "."))

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _CreateHelper._build_schema_gallery_service_artifact_read(cls._schema_on_200_201)

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_vm_artifacts_profile_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("artifactProfiles", AAZListType, ".artifact_profiles", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("description", AAZStrType, ".description")
        _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("upgradeProviderInfo", AAZObjectType, ".upgrade_provider_info")
        _builder.set_prop("upgradeSdpPolicy", AAZObjectType, ".upgrade_sdp_policy", typ_kwargs={"flags": {"required": True}})

        artifact_profiles = _builder.get(".artifactProfiles")
        if artifact_profiles is not None:
            artifact_profiles.set_elements(AAZObjectType, ".")

        _elements = _builder.get(".artifactProfiles[]")
        if _elements is not None:
            _elements.set_prop("description", AAZStrType, ".description")
            _elements.set_prop("imageReference", AAZObjectType, ".image_reference")

        image_reference = _builder.get(".artifactProfiles[].imageReference")
        if image_reference is not None:
            image_reference.set_prop("currentVersion", AAZStrType, ".current_version")
            image_reference.set_prop("id", AAZStrType, ".id")
            image_reference.set_prop("initialVersion", AAZStrType, ".initial_version")
            image_reference.set_prop("offer", AAZStrType, ".offer")
            image_reference.set_prop("publisher", AAZStrType, ".publisher")
            image_reference.set_prop("sharedGalleryImageId", AAZStrType, ".shared_gallery_image_id")
            image_reference.set_prop("sku", AAZStrType, ".sku")

        upgrade_provider_info = _builder.get(".upgradeProviderInfo")
        if upgrade_provider_info is not None:
            upgrade_provider_info.set_prop("enableAutoTrigger", AAZBoolType, ".enable_auto_trigger")
            upgrade_provider_info.set_prop("upgradeProviderParameters", AAZObjectType, ".upgrade_provider_parameters")

        upgrade_provider_parameters = _builder.get(".upgradeProviderInfo.upgradeProviderParameters")
        if upgrade_provider_parameters is not None:
            upgrade_provider_parameters.set_prop("ServiceGroup", AAZStrType, ".service_group")
            upgrade_provider_parameters.set_prop("ServiceIdentifier", AAZStrType, ".service_identifier")

        upgrade_sdp_policy = _builder.get(".upgradeSdpPolicy")
        if upgrade_sdp_policy is not None:
            upgrade_sdp_policy.set_prop("schedulingPolicy", AAZObjectType, ".scheduling_policy")
            upgrade_sdp_policy.set_prop("type", AAZStrType, ".type")

        scheduling_policy = _builder.get(".upgradeSdpPolicy.schedulingPolicy")
        if scheduling_policy is not None:
            scheduling_policy.set_prop("disableRegularUpgrades", AAZBoolType, ".disable_regular_upgrades")
            scheduling_policy.set_prop("maxConcurrentResourceCountPerRegion", AAZIntType, ".max_concurrent_resource_count_per_region")
            scheduling_policy.set_prop("upgradeWindow", AAZStrType, ".upgrade_window")

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


__all__ = ["Create"]
