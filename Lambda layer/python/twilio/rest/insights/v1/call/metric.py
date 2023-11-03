r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MetricInstance(InstanceResource):
    class StreamDirection(object):
        UNKNOWN = "unknown"
        INBOUND = "inbound"
        OUTBOUND = "outbound"
        BOTH = "both"

    class TwilioEdge(object):
        UNKNOWN_EDGE = "unknown_edge"
        CARRIER_EDGE = "carrier_edge"
        SIP_EDGE = "sip_edge"
        SDK_EDGE = "sdk_edge"
        CLIENT_EDGE = "client_edge"

    """
    :ivar timestamp: 
    :ivar call_sid: 
    :ivar account_sid: 
    :ivar edge: 
    :ivar direction: 
    :ivar carrier_edge: 
    :ivar sip_edge: 
    :ivar sdk_edge: 
    :ivar client_edge: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], call_sid: str):
        super().__init__(version)

        self.timestamp: Optional[str] = payload.get("timestamp")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.edge: Optional["MetricInstance.TwilioEdge"] = payload.get("edge")
        self.direction: Optional["MetricInstance.StreamDirection"] = payload.get(
            "direction"
        )
        self.carrier_edge: Optional[Dict[str, object]] = payload.get("carrier_edge")
        self.sip_edge: Optional[Dict[str, object]] = payload.get("sip_edge")
        self.sdk_edge: Optional[Dict[str, object]] = payload.get("sdk_edge")
        self.client_edge: Optional[Dict[str, object]] = payload.get("client_edge")

        self._solution = {
            "call_sid": call_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.MetricInstance {}>".format(context)


class MetricPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> MetricInstance:
        """
        Build an instance of MetricInstance

        :param payload: Payload response from the API
        """
        return MetricInstance(
            self._version, payload, call_sid=self._solution["call_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.MetricPage>"


class MetricList(ListResource):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the MetricList

        :param version: Version that contains the resource
        :param call_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }
        self._uri = "/Voice/{call_sid}/Metrics".format(**self._solution)

    def stream(
        self,
        edge: Union["MetricInstance.TwilioEdge", object] = values.unset,
        direction: Union["MetricInstance.StreamDirection", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[MetricInstance]:
        """
        Streams MetricInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MetricInstance.TwilioEdge&quot; edge:
        :param &quot;MetricInstance.StreamDirection&quot; direction:
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(edge=edge, direction=direction, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        edge: Union["MetricInstance.TwilioEdge", object] = values.unset,
        direction: Union["MetricInstance.StreamDirection", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[MetricInstance]:
        """
        Asynchronously streams MetricInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;MetricInstance.TwilioEdge&quot; edge:
        :param &quot;MetricInstance.StreamDirection&quot; direction:
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            edge=edge, direction=direction, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        edge: Union["MetricInstance.TwilioEdge", object] = values.unset,
        direction: Union["MetricInstance.StreamDirection", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MetricInstance]:
        """
        Lists MetricInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MetricInstance.TwilioEdge&quot; edge:
        :param &quot;MetricInstance.StreamDirection&quot; direction:
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
                edge=edge,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        edge: Union["MetricInstance.TwilioEdge", object] = values.unset,
        direction: Union["MetricInstance.StreamDirection", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MetricInstance]:
        """
        Asynchronously lists MetricInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;MetricInstance.TwilioEdge&quot; edge:
        :param &quot;MetricInstance.StreamDirection&quot; direction:
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
                edge=edge,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        edge: Union["MetricInstance.TwilioEdge", object] = values.unset,
        direction: Union["MetricInstance.StreamDirection", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MetricPage:
        """
        Retrieve a single page of MetricInstance records from the API.
        Request is executed immediately

        :param edge:
        :param direction:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MetricInstance
        """
        data = values.of(
            {
                "Edge": edge,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MetricPage(self._version, response, self._solution)

    async def page_async(
        self,
        edge: Union["MetricInstance.TwilioEdge", object] = values.unset,
        direction: Union["MetricInstance.StreamDirection", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> MetricPage:
        """
        Asynchronously retrieve a single page of MetricInstance records from the API.
        Request is executed immediately

        :param edge:
        :param direction:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MetricInstance
        """
        data = values.of(
            {
                "Edge": edge,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MetricPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> MetricPage:
        """
        Retrieve a specific page of MetricInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MetricInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MetricPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> MetricPage:
        """
        Asynchronously retrieve a specific page of MetricInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MetricInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MetricPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.MetricList>"
