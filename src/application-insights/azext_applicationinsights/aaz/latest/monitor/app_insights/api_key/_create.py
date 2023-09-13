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
    "monitor app-insights api-key create",
)
class Create(AAZCommand):
    """Create an API Key of an Application Insights component.

    :example: Create a component with kind web and location.
        az monitor app-insights api-key create --api-key cli-demo --read-properties ReadTelemetry --write-properties WriteAnnotations -g demoRg --app testApp

    :example: Create a component with kind web and location without any permission
        az monitor app-insights api-key create --api-key cli-demo --read-properties '""' --write-properties '""' -g demoRg --app testApp
    """

    _aaz_info = {
        "version": "2015-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/components/{}/apikeys", "2015-05-01"],
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
        _args_schema.read_properties = AAZListArg(
            options=["--read-properties"],
            help="A space-separated list of names of read Roles for this API key                                      to inherit.",
        )
        _args_schema.write_properties = AAZListArg(
            options=["--write-properties"],
            help="A space-separated list of names of write Roles for this API key                                      to inherit.",
        )
        _args_schema.api_key = AAZStrArg(
            options=["--api-key"],
            help="Name of the API key to create.",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.app = AAZStrArg(
            options=["-a", "--app"],
            help="GUID, app name, or fully-qualified Azure resource name of                                      Application Insights component. The application GUID may be                                      acquired from the API Access menu item on any Application                                      Insights resource in the Azure portal. If using an application                                      name, please specify resource group.",
            required=True,
        )

        read_properties = cls._args_schema.read_properties
        read_properties.Element = AAZStrArg()

        write_properties = cls._args_schema.write_properties
        write_properties.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.APIKeysCreate(ctx=self.ctx)()
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

    class APIKeysCreate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ApiKeys",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.app,
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
                    "api-version", "2015-05-01",
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
            _builder.set_prop("linkedReadProperties", AAZListType, ".read_properties")
            _builder.set_prop("linkedWriteProperties", AAZListType, ".write_properties")
            _builder.set_prop("name", AAZStrType, ".api_key")

            linked_read_properties = _builder.get(".linkedReadProperties")
            if linked_read_properties is not None:
                linked_read_properties.set_elements(AAZStrType, ".")

            linked_write_properties = _builder.get(".linkedWriteProperties")
            if linked_write_properties is not None:
                linked_write_properties.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.api_key = AAZStrType(
                serialized_name="apiKey",
                flags={"read_only": True},
            )
            _schema_on_200.created_date = AAZStrType(
                serialized_name="createdDate",
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.linked_read_properties = AAZListType(
                serialized_name="linkedReadProperties",
            )
            _schema_on_200.linked_write_properties = AAZListType(
                serialized_name="linkedWriteProperties",
            )
            _schema_on_200.name = AAZStrType()

            linked_read_properties = cls._schema_on_200.linked_read_properties
            linked_read_properties.Element = AAZStrType()

            linked_write_properties = cls._schema_on_200.linked_write_properties
            linked_write_properties.Element = AAZStrType()

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]