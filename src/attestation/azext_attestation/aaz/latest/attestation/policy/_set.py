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
    "attestation policy set",
)
class Set(AAZCommand):
    """Sets the policy for a given kind of attestation type.

    :example: Sets the policy for a given kind of attestation type using JWT content.
        az attestation policy set -n "myattestationprovider" -g "MyResourceGroup" --attestation-type SGX-OpenEnclaveSDK --new-attestation-policy "{JWT}" --policy-format JWT

    :example: Sets the policy for a given kind of attestation type using Text content.
        az attestation policy set -n "myattestationprovider" -g "MyResourceGroup" --attestation-type SGX-OpenEnclaveSDK --new-attestation-policy "{json_text}"

    :example: Sets the policy for a given kind of attestation type using file name.
        az attestation policy set -n "myattestationprovider" -g "MyResourceGroup" --attestation-type SGX-OpenEnclaveSDK --new-attestation-policy-file "{file_name}" --policy- format JWT
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["data-plane:microsoft.attestation", "/policies/{}", "2022-08-01"],
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

        # define Arg Group "Client"

        _args_schema = cls._args_schema
        _args_schema.provider_name = AAZStrArg(
            options=["--provider-name"],
            arg_group="Client",
            help="Name of the attestation provider.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            arg_group="Client",
            help="Name of resource group. You can configure the default group using `az configure --defaults group=<name>`",
            required=True,
        )

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.attestation_type = AAZStrArg(
            options=["--attestation-type"],
            help="Type of the attestation.",
            required=True,
            enum={"OpenEnclave": "OpenEnclave", "SevSnpVm": "SevSnpVm", "SgxEnclave": "SgxEnclave", "Tpm": "Tpm"},
        )
        _args_schema.new_attestation_policy = AAZStrArg(
            options=["--new-attestation-policy"],
            help="Content of the new attestation policy (Text or JWT).",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="[A-Za-z0-9_-]+\.[A-Za-z0-9_-]*\.[A-Za-z0-9_-]*",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.PolicySet(ctx=self.ctx)()
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

    class PolicySet(AAZHttpOperation):
        CLIENT_TYPE = "AAZMicrosoftAttestationDataPlaneClient_attestation"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/policies/{attestationType}",
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
                    "attestationType", self.ctx.args.attestation_type,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
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
                self.ctx.args.new_attestation_policy,
                typ=AAZStrType,
                typ_kwargs={"flags": {"required": True}}
            )

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
            _schema_on_200.token = AAZStrType()

            return cls._schema_on_200


class _SetHelper:
    """Helper class for Set"""


__all__ = ["Set"]