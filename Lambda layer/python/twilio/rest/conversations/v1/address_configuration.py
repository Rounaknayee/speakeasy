r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AddressConfigurationInstance(InstanceResource):
    class AutoCreationType(object):
        WEBHOOK = "webhook"
        STUDIO = "studio"
        DEFAULT = "default"

    class Method(object):
        GET = "GET"
        POST = "POST"

    class Type(object):
        SMS = "sms"
        WHATSAPP = "whatsapp"
        MESSENGER = "messenger"
        GBM = "gbm"

    """
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) the address belongs to
    :ivar type: Type of Address, value can be `whatsapp` or `sms`.
    :ivar address: The unique address to be configured. The address can be a whatsapp address or phone number
    :ivar friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
    :ivar auto_creation: Auto Creation configuration for the address.
    :ivar date_created: The date that this resource was created.
    :ivar date_updated: The date that this resource was last updated.
    :ivar url: An absolute API resource URL for this address configuration.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.type: Optional[str] = payload.get("type")
        self.address: Optional[str] = payload.get("address")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.auto_creation: Optional[Dict[str, object]] = payload.get("auto_creation")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[AddressConfigurationContext] = None

    @property
    def _proxy(self) -> "AddressConfigurationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AddressConfigurationContext for this AddressConfigurationInstance
        """
        if self._context is None:
            self._context = AddressConfigurationContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AddressConfigurationInstance":
        """
        Fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AddressConfigurationInstance":
        """
        Asynchronous coroutine to fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        auto_creation_enabled: Union[bool, object] = values.unset,
        auto_creation_type: Union[
            "AddressConfigurationInstance.AutoCreationType", object
        ] = values.unset,
        auto_creation_conversation_service_sid: Union[str, object] = values.unset,
        auto_creation_webhook_url: Union[str, object] = values.unset,
        auto_creation_webhook_method: Union[
            "AddressConfigurationInstance.Method", object
        ] = values.unset,
        auto_creation_webhook_filters: Union[List[str], object] = values.unset,
        auto_creation_studio_flow_sid: Union[str, object] = values.unset,
        auto_creation_studio_retry_count: Union[int, object] = values.unset,
    ) -> "AddressConfigurationInstance":
        """
        Update the AddressConfigurationInstance

        :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param auto_creation_type:
        :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param auto_creation_webhook_method:
        :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            auto_creation_enabled=auto_creation_enabled,
            auto_creation_type=auto_creation_type,
            auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
            auto_creation_webhook_url=auto_creation_webhook_url,
            auto_creation_webhook_method=auto_creation_webhook_method,
            auto_creation_webhook_filters=auto_creation_webhook_filters,
            auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
            auto_creation_studio_retry_count=auto_creation_studio_retry_count,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        auto_creation_enabled: Union[bool, object] = values.unset,
        auto_creation_type: Union[
            "AddressConfigurationInstance.AutoCreationType", object
        ] = values.unset,
        auto_creation_conversation_service_sid: Union[str, object] = values.unset,
        auto_creation_webhook_url: Union[str, object] = values.unset,
        auto_creation_webhook_method: Union[
            "AddressConfigurationInstance.Method", object
        ] = values.unset,
        auto_creation_webhook_filters: Union[List[str], object] = values.unset,
        auto_creation_studio_flow_sid: Union[str, object] = values.unset,
        auto_creation_studio_retry_count: Union[int, object] = values.unset,
    ) -> "AddressConfigurationInstance":
        """
        Asynchronous coroutine to update the AddressConfigurationInstance

        :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param auto_creation_type:
        :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param auto_creation_webhook_method:
        :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            auto_creation_enabled=auto_creation_enabled,
            auto_creation_type=auto_creation_type,
            auto_creation_conversation_service_sid=auto_creation_conversation_service_sid,
            auto_creation_webhook_url=auto_creation_webhook_url,
            auto_creation_webhook_method=auto_creation_webhook_method,
            auto_creation_webhook_filters=auto_creation_webhook_filters,
            auto_creation_studio_flow_sid=auto_creation_studio_flow_sid,
            auto_creation_studio_retry_count=auto_creation_studio_retry_count,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.AddressConfigurationInstance {}>".format(
            context
        )


class AddressConfigurationContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AddressConfigurationContext

        :param version: Version that contains the resource
        :param sid: The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Configuration/Addresses/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AddressConfigurationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AddressConfigurationInstance:
        """
        Fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AddressConfigurationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AddressConfigurationInstance:
        """
        Asynchronous coroutine to fetch the AddressConfigurationInstance


        :returns: The fetched AddressConfigurationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AddressConfigurationInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        auto_creation_enabled: Union[bool, object] = values.unset,
        auto_creation_type: Union[
            "AddressConfigurationInstance.AutoCreationType", object
        ] = values.unset,
        auto_creation_conversation_service_sid: Union[str, object] = values.unset,
        auto_creation_webhook_url: Union[str, object] = values.unset,
        auto_creation_webhook_method: Union[
            "AddressConfigurationInstance.Method", object
        ] = values.unset,
        auto_creation_webhook_filters: Union[List[str], object] = values.unset,
        auto_creation_studio_flow_sid: Union[str, object] = values.unset,
        auto_creation_studio_retry_count: Union[int, object] = values.unset,
    ) -> AddressConfigurationInstance:
        """
        Update the AddressConfigurationInstance

        :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param auto_creation_type:
        :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param auto_creation_webhook_method:
        :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        auto_creation_enabled: Union[bool, object] = values.unset,
        auto_creation_type: Union[
            "AddressConfigurationInstance.AutoCreationType", object
        ] = values.unset,
        auto_creation_conversation_service_sid: Union[str, object] = values.unset,
        auto_creation_webhook_url: Union[str, object] = values.unset,
        auto_creation_webhook_method: Union[
            "AddressConfigurationInstance.Method", object
        ] = values.unset,
        auto_creation_webhook_filters: Union[List[str], object] = values.unset,
        auto_creation_studio_flow_sid: Union[str, object] = values.unset,
        auto_creation_studio_retry_count: Union[int, object] = values.unset,
    ) -> AddressConfigurationInstance:
        """
        Asynchronous coroutine to update the AddressConfigurationInstance

        :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param auto_creation_type:
        :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param auto_creation_webhook_method:
        :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The updated AddressConfigurationInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.AddressConfigurationContext {}>".format(
            context
        )


class AddressConfigurationPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AddressConfigurationInstance:
        """
        Build an instance of AddressConfigurationInstance

        :param payload: Payload response from the API
        """
        return AddressConfigurationInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.AddressConfigurationPage>"


class AddressConfigurationList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AddressConfigurationList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Configuration/Addresses"

    def create(
        self,
        type: "AddressConfigurationInstance.Type",
        address: str,
        friendly_name: Union[str, object] = values.unset,
        auto_creation_enabled: Union[bool, object] = values.unset,
        auto_creation_type: Union[
            "AddressConfigurationInstance.AutoCreationType", object
        ] = values.unset,
        auto_creation_conversation_service_sid: Union[str, object] = values.unset,
        auto_creation_webhook_url: Union[str, object] = values.unset,
        auto_creation_webhook_method: Union[
            "AddressConfigurationInstance.Method", object
        ] = values.unset,
        auto_creation_webhook_filters: Union[List[str], object] = values.unset,
        auto_creation_studio_flow_sid: Union[str, object] = values.unset,
        auto_creation_studio_retry_count: Union[int, object] = values.unset,
    ) -> AddressConfigurationInstance:
        """
        Create the AddressConfigurationInstance

        :param type:
        :param address: The unique address to be configured. The address can be a whatsapp address or phone number
        :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param auto_creation_type:
        :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param auto_creation_webhook_method:
        :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The created AddressConfigurationInstance
        """
        data = values.of(
            {
                "Type": type,
                "Address": address,
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(self._version, payload)

    async def create_async(
        self,
        type: "AddressConfigurationInstance.Type",
        address: str,
        friendly_name: Union[str, object] = values.unset,
        auto_creation_enabled: Union[bool, object] = values.unset,
        auto_creation_type: Union[
            "AddressConfigurationInstance.AutoCreationType", object
        ] = values.unset,
        auto_creation_conversation_service_sid: Union[str, object] = values.unset,
        auto_creation_webhook_url: Union[str, object] = values.unset,
        auto_creation_webhook_method: Union[
            "AddressConfigurationInstance.Method", object
        ] = values.unset,
        auto_creation_webhook_filters: Union[List[str], object] = values.unset,
        auto_creation_studio_flow_sid: Union[str, object] = values.unset,
        auto_creation_studio_retry_count: Union[int, object] = values.unset,
    ) -> AddressConfigurationInstance:
        """
        Asynchronously create the AddressConfigurationInstance

        :param type:
        :param address: The unique address to be configured. The address can be a whatsapp address or phone number
        :param friendly_name: The human-readable name of this configuration, limited to 256 characters. Optional.
        :param auto_creation_enabled: Enable/Disable auto-creating conversations for messages to this address
        :param auto_creation_type:
        :param auto_creation_conversation_service_sid: Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
        :param auto_creation_webhook_url: For type `webhook`, the url for the webhook request.
        :param auto_creation_webhook_method:
        :param auto_creation_webhook_filters: The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
        :param auto_creation_studio_flow_sid: For type `studio`, the studio flow SID where the webhook should be sent to.
        :param auto_creation_studio_retry_count: For type `studio`, number of times to retry the webhook request

        :returns: The created AddressConfigurationInstance
        """
        data = values.of(
            {
                "Type": type,
                "Address": address,
                "FriendlyName": friendly_name,
                "AutoCreation.Enabled": auto_creation_enabled,
                "AutoCreation.Type": auto_creation_type,
                "AutoCreation.ConversationServiceSid": auto_creation_conversation_service_sid,
                "AutoCreation.WebhookUrl": auto_creation_webhook_url,
                "AutoCreation.WebhookMethod": auto_creation_webhook_method,
                "AutoCreation.WebhookFilters": serialize.map(
                    auto_creation_webhook_filters, lambda e: e
                ),
                "AutoCreation.StudioFlowSid": auto_creation_studio_flow_sid,
                "AutoCreation.StudioRetryCount": auto_creation_studio_retry_count,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressConfigurationInstance(self._version, payload)

    def stream(
        self,
        type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AddressConfigurationInstance]:
        """
        Streams AddressConfigurationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(type=type, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AddressConfigurationInstance]:
        """
        Asynchronously streams AddressConfigurationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(type=type, page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AddressConfigurationInstance]:
        """
        Lists AddressConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        type: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AddressConfigurationInstance]:
        """
        Asynchronously lists AddressConfigurationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                type=type,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        type: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AddressConfigurationPage:
        """
        Retrieve a single page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AddressConfigurationInstance
        """
        data = values.of(
            {
                "Type": type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AddressConfigurationPage(self._version, response)

    async def page_async(
        self,
        type: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AddressConfigurationPage:
        """
        Asynchronously retrieve a single page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param type: Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AddressConfigurationInstance
        """
        data = values.of(
            {
                "Type": type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AddressConfigurationPage(self._version, response)

    def get_page(self, target_url: str) -> AddressConfigurationPage:
        """
        Retrieve a specific page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AddressConfigurationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AddressConfigurationPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AddressConfigurationPage:
        """
        Asynchronously retrieve a specific page of AddressConfigurationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AddressConfigurationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AddressConfigurationPage(self._version, response)

    def get(self, sid: str) -> AddressConfigurationContext:
        """
        Constructs a AddressConfigurationContext

        :param sid: The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
        """
        return AddressConfigurationContext(self._version, sid=sid)

    def __call__(self, sid: str) -> AddressConfigurationContext:
        """
        Constructs a AddressConfigurationContext

        :param sid: The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
        """
        return AddressConfigurationContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.AddressConfigurationList>"