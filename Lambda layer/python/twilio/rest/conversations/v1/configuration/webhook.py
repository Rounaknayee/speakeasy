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


from typing import Any, Dict, List, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class WebhookInstance(InstanceResource):
    class Method(object):
        GET = "GET"
        POST = "POST"

    class Target(object):
        WEBHOOK = "webhook"
        FLEX = "flex"

    """
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
    :ivar method: 
    :ivar filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
    :ivar pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
    :ivar post_webhook_url: The absolute url the post-event webhook request should be sent to.
    :ivar target: 
    :ivar url: An absolute API resource API resource URL for this webhook.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.method: Optional["WebhookInstance.Method"] = payload.get("method")
        self.filters: Optional[List[str]] = payload.get("filters")
        self.pre_webhook_url: Optional[str] = payload.get("pre_webhook_url")
        self.post_webhook_url: Optional[str] = payload.get("post_webhook_url")
        self.target: Optional["WebhookInstance.Target"] = payload.get("target")
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[WebhookContext] = None

    @property
    def _proxy(self) -> "WebhookContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        """
        if self._context is None:
            self._context = WebhookContext(
                self._version,
            )
        return self._context

    def fetch(self) -> "WebhookInstance":
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "WebhookInstance":
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        method: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        target: Union["WebhookInstance.Target", object] = values.unset,
    ) -> "WebhookInstance":
        """
        Update the WebhookInstance

        :param method: The HTTP method to be used when sending a webhook request.
        :param filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param target:

        :returns: The updated WebhookInstance
        """
        return self._proxy.update(
            method=method,
            filters=filters,
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            target=target,
        )

    async def update_async(
        self,
        method: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        target: Union["WebhookInstance.Target", object] = values.unset,
    ) -> "WebhookInstance":
        """
        Asynchronous coroutine to update the WebhookInstance

        :param method: The HTTP method to be used when sending a webhook request.
        :param filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param target:

        :returns: The updated WebhookInstance
        """
        return await self._proxy.update_async(
            method=method,
            filters=filters,
            pre_webhook_url=pre_webhook_url,
            post_webhook_url=post_webhook_url,
            target=target,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Conversations.V1.WebhookInstance>"


class WebhookContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the WebhookContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/Configuration/Webhooks"

    def fetch(self) -> WebhookInstance:
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> WebhookInstance:
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
        )

    def update(
        self,
        method: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        target: Union["WebhookInstance.Target", object] = values.unset,
    ) -> WebhookInstance:
        """
        Update the WebhookInstance

        :param method: The HTTP method to be used when sending a webhook request.
        :param filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param target:

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "Method": method,
                "Filters": serialize.map(filters, lambda e: e),
                "PreWebhookUrl": pre_webhook_url,
                "PostWebhookUrl": post_webhook_url,
                "Target": target,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(self._version, payload)

    async def update_async(
        self,
        method: Union[str, object] = values.unset,
        filters: Union[List[str], object] = values.unset,
        pre_webhook_url: Union[str, object] = values.unset,
        post_webhook_url: Union[str, object] = values.unset,
        target: Union["WebhookInstance.Target", object] = values.unset,
    ) -> WebhookInstance:
        """
        Asynchronous coroutine to update the WebhookInstance

        :param method: The HTTP method to be used when sending a webhook request.
        :param filters: The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`
        :param pre_webhook_url: The absolute url the pre-event webhook request should be sent to.
        :param post_webhook_url: The absolute url the post-event webhook request should be sent to.
        :param target:

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "Method": method,
                "Filters": serialize.map(filters, lambda e: e),
                "PreWebhookUrl": pre_webhook_url,
                "PostWebhookUrl": post_webhook_url,
                "Target": target,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Conversations.V1.WebhookContext>"


class WebhookList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the WebhookList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> WebhookContext:
        """
        Constructs a WebhookContext

        """
        return WebhookContext(self._version)

    def __call__(self) -> WebhookContext:
        """
        Constructs a WebhookContext

        """
        return WebhookContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.WebhookList>"
