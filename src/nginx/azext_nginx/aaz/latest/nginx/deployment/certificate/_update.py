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
    "nginx deployment certificate update",
)
class Update(AAZCommand):
    """Update an NGINX deployment certificate

    :example: Update the certificate virtual path, key virtual path and certificate
        az nginx deployment certificate update --certificate-name myCertificate --deployment-name myDeployment --resource-group myResourceGroup --certificate-path /etc/nginx/testupdated.cert --key-path /etc/nginx/testupdated.key --key-vault-secret-id newKeyVaultSecretId
    """

    _aaz_info = {
        "version": "2024-01-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}/certificates/{}", "2024-01-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.certificate_name = AAZStrArg(
            options=["-n", "--name", "--certificate-name"],
            help="The name of certificate",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.deployment_name = AAZStrArg(
            options=["--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-z0-9A-Z][a-z0-9A-Z-]{0,28}[a-z0-9A-Z]|[a-z0-9A-Z])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            nullable=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.certificate_path = AAZStrArg(
            options=["--certificate-path"],
            arg_group="Properties",
            help={"short-summary": "Certificate path in Nginx configuration structure", "long-summary": "This path must match one or more ssl_certificate directive file argument in your Nginx configuration. This path must be unique between certificates within the same deployment"},
            nullable=True,
        )
        _args_schema.key_vault_secret_id = AAZStrArg(
            options=["--key-vault-secret-id"],
            arg_group="Properties",
            help="The secret ID for your certificate from Azure Key Vault",
            nullable=True,
        )
        _args_schema.key_path = AAZStrArg(
            options=["--key-path"],
            arg_group="Properties",
            help={"short-summary": "Key path in Nginx configuration structure", "long-summary": "This path must match one or more ssl_certificate_key directive file argument in your Nginx configuration. This path must be unique between certificates within the same deployment"},
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CertificatesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.CertificatesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CertificatesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/certificates/{certificateName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "certificateName", self.ctx.args.certificate_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2024-01-01-preview",
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

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_nginx_certificate_read(cls._schema_on_200)

            return cls._schema_on_200

    class CertificatesCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}/certificates/{certificateName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "certificateName", self.ctx.args.certificate_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2024-01-01-preview",
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
                value=self.ctx.vars.instance,
            )

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
            _UpdateHelper._build_schema_nginx_certificate_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("certificateVirtualPath", AAZStrType, ".certificate_path")
                properties.set_prop("keyVaultSecretId", AAZStrType, ".key_vault_secret_id")
                properties.set_prop("keyVirtualPath", AAZStrType, ".key_path")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_nginx_certificate_read = None

    @classmethod
    def _build_schema_nginx_certificate_read(cls, _schema):
        if cls._schema_nginx_certificate_read is not None:
            _schema.id = cls._schema_nginx_certificate_read.id
            _schema.location = cls._schema_nginx_certificate_read.location
            _schema.name = cls._schema_nginx_certificate_read.name
            _schema.properties = cls._schema_nginx_certificate_read.properties
            _schema.system_data = cls._schema_nginx_certificate_read.system_data
            _schema.type = cls._schema_nginx_certificate_read.type
            return

        cls._schema_nginx_certificate_read = _schema_nginx_certificate_read = AAZObjectType()

        nginx_certificate_read = _schema_nginx_certificate_read
        nginx_certificate_read.id = AAZStrType(
            flags={"read_only": True},
        )
        nginx_certificate_read.location = AAZStrType()
        nginx_certificate_read.name = AAZStrType(
            flags={"read_only": True},
        )
        nginx_certificate_read.properties = AAZObjectType()
        nginx_certificate_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        nginx_certificate_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_nginx_certificate_read.properties
        properties.certificate_error = AAZObjectType(
            serialized_name="certificateError",
        )
        properties.certificate_virtual_path = AAZStrType(
            serialized_name="certificateVirtualPath",
        )
        properties.key_vault_secret_created = AAZStrType(
            serialized_name="keyVaultSecretCreated",
            flags={"read_only": True},
        )
        properties.key_vault_secret_id = AAZStrType(
            serialized_name="keyVaultSecretId",
        )
        properties.key_vault_secret_version = AAZStrType(
            serialized_name="keyVaultSecretVersion",
            flags={"read_only": True},
        )
        properties.key_virtual_path = AAZStrType(
            serialized_name="keyVirtualPath",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.sha1_thumbprint = AAZStrType(
            serialized_name="sha1Thumbprint",
            flags={"read_only": True},
        )

        certificate_error = _schema_nginx_certificate_read.properties.certificate_error
        certificate_error.code = AAZStrType()
        certificate_error.message = AAZStrType()

        system_data = _schema_nginx_certificate_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        _schema.id = cls._schema_nginx_certificate_read.id
        _schema.location = cls._schema_nginx_certificate_read.location
        _schema.name = cls._schema_nginx_certificate_read.name
        _schema.properties = cls._schema_nginx_certificate_read.properties
        _schema.system_data = cls._schema_nginx_certificate_read.system_data
        _schema.type = cls._schema_nginx_certificate_read.type


__all__ = ["Update"]
