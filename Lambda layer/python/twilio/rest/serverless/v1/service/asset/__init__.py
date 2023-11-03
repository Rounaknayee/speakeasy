r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.serverless.v1.service.asset.asset_version import AssetVersionList


class AssetInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Asset resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Asset resource.
    :ivar service_sid: The SID of the Service that the Asset resource is associated with.
    :ivar friendly_name: The string that you assigned to describe the Asset resource. It can be a maximum of 255 characters.
    :ivar date_created: The date and time in GMT when the Asset resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Asset resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Asset resource.
    :ivar links: The URLs of the Asset resource's nested resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AssetContext] = None

    @property
    def _proxy(self) -> "AssetContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssetContext for this AssetInstance
        """
        if self._context is None:
            self._context = AssetContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AssetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AssetInstance":
        """
        Fetch the AssetInstance


        :returns: The fetched AssetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AssetInstance":
        """
        Asynchronous coroutine to fetch the AssetInstance


        :returns: The fetched AssetInstance
        """
        return await self._proxy.fetch_async()

    def update(self, friendly_name: str) -> "AssetInstance":
        """
        Update the AssetInstance

        :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    async def update_async(self, friendly_name: str) -> "AssetInstance":
        """
        Asynchronous coroutine to update the AssetInstance

        :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
        )

    @property
    def asset_versions(self) -> AssetVersionList:
        """
        Access the asset_versions
        """
        return self._proxy.asset_versions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.AssetInstance {}>".format(context)


class AssetContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the AssetContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to update the Asset resource from.
        :param sid: The SID that identifies the Asset resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Assets/{sid}".format(**self._solution)

        self._asset_versions: Optional[AssetVersionList] = None

    def delete(self) -> bool:
        """
        Deletes the AssetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssetInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AssetInstance:
        """
        Fetch the AssetInstance


        :returns: The fetched AssetInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AssetInstance:
        """
        Asynchronous coroutine to fetch the AssetInstance


        :returns: The fetched AssetInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, friendly_name: str) -> AssetInstance:
        """
        Update the AssetInstance

        :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, friendly_name: str) -> AssetInstance:
        """
        Asynchronous coroutine to update the AssetInstance

        :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The updated AssetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssetInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def asset_versions(self) -> AssetVersionList:
        """
        Access the asset_versions
        """
        if self._asset_versions is None:
            self._asset_versions = AssetVersionList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._asset_versions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.AssetContext {}>".format(context)


class AssetPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AssetInstance:
        """
        Build an instance of AssetInstance

        :param payload: Payload response from the API
        """
        return AssetInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.AssetPage>"


class AssetList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the AssetList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Asset resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Assets".format(**self._solution)

    def create(self, friendly_name: str) -> AssetInstance:
        """
        Create the AssetInstance

        :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The created AssetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssetInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, friendly_name: str) -> AssetInstance:
        """
        Asynchronously create the AssetInstance

        :param friendly_name: A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.

        :returns: The created AssetInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssetInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AssetInstance]:
        """
        Streams AssetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AssetInstance]:
        """
        Asynchronously streams AssetInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssetInstance]:
        """
        Lists AssetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssetInstance]:
        """
        Asynchronously lists AssetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssetPage:
        """
        Retrieve a single page of AssetInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssetInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssetPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssetPage:
        """
        Asynchronously retrieve a single page of AssetInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssetInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AssetPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AssetPage:
        """
        Retrieve a specific page of AssetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssetInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssetPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AssetPage:
        """
        Asynchronously retrieve a specific page of AssetInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssetInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssetPage(self._version, response, self._solution)

    def get(self, sid: str) -> AssetContext:
        """
        Constructs a AssetContext

        :param sid: The SID that identifies the Asset resource to update.
        """
        return AssetContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> AssetContext:
        """
        Constructs a AssetContext

        :param sid: The SID that identifies the Asset resource to update.
        """
        return AssetContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.AssetList>"
