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


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class CallSummaryInstance(InstanceResource):
    class AnsweredBy(object):
        UNKNOWN = "unknown"
        MACHINE_START = "machine_start"
        MACHINE_END_BEEP = "machine_end_beep"
        MACHINE_END_SILENCE = "machine_end_silence"
        MACHINE_END_OTHER = "machine_end_other"
        HUMAN = "human"
        FAX = "fax"

    class CallState(object):
        RINGING = "ringing"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        CANCELED = "canceled"
        ANSWERED = "answered"
        UNDIALED = "undialed"

    class CallType(object):
        CARRIER = "carrier"
        SIP = "sip"
        TRUNKING = "trunking"
        CLIENT = "client"

    class ProcessingState(object):
        COMPLETE = "complete"
        PARTIAL = "partial"

    """
    :ivar account_sid: 
    :ivar call_sid: 
    :ivar call_type: 
    :ivar call_state: 
    :ivar answered_by: 
    :ivar processing_state: 
    :ivar created_time: 
    :ivar start_time: 
    :ivar end_time: 
    :ivar duration: 
    :ivar connect_duration: 
    :ivar _from: 
    :ivar to: 
    :ivar carrier_edge: 
    :ivar client_edge: 
    :ivar sdk_edge: 
    :ivar sip_edge: 
    :ivar tags: 
    :ivar url: 
    :ivar attributes: 
    :ivar properties: 
    :ivar trust: 
    :ivar annotation: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], call_sid: str):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.call_type: Optional["CallSummaryInstance.CallType"] = payload.get(
            "call_type"
        )
        self.call_state: Optional["CallSummaryInstance.CallState"] = payload.get(
            "call_state"
        )
        self.answered_by: Optional["CallSummaryInstance.AnsweredBy"] = payload.get(
            "answered_by"
        )
        self.processing_state: Optional[
            "CallSummaryInstance.ProcessingState"
        ] = payload.get("processing_state")
        self.created_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("created_time")
        )
        self.start_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("start_time")
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.connect_duration: Optional[int] = deserialize.integer(
            payload.get("connect_duration")
        )
        self._from: Optional[Dict[str, object]] = payload.get("from")
        self.to: Optional[Dict[str, object]] = payload.get("to")
        self.carrier_edge: Optional[Dict[str, object]] = payload.get("carrier_edge")
        self.client_edge: Optional[Dict[str, object]] = payload.get("client_edge")
        self.sdk_edge: Optional[Dict[str, object]] = payload.get("sdk_edge")
        self.sip_edge: Optional[Dict[str, object]] = payload.get("sip_edge")
        self.tags: Optional[List[str]] = payload.get("tags")
        self.url: Optional[str] = payload.get("url")
        self.attributes: Optional[Dict[str, object]] = payload.get("attributes")
        self.properties: Optional[Dict[str, object]] = payload.get("properties")
        self.trust: Optional[Dict[str, object]] = payload.get("trust")
        self.annotation: Optional[Dict[str, object]] = payload.get("annotation")

        self._solution = {
            "call_sid": call_sid,
        }
        self._context: Optional[CallSummaryContext] = None

    @property
    def _proxy(self) -> "CallSummaryContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CallSummaryContext for this CallSummaryInstance
        """
        if self._context is None:
            self._context = CallSummaryContext(
                self._version,
                call_sid=self._solution["call_sid"],
            )
        return self._context

    def fetch(
        self,
        processing_state: Union[
            "CallSummaryInstance.ProcessingState", object
        ] = values.unset,
    ) -> "CallSummaryInstance":
        """
        Fetch the CallSummaryInstance

        :param processing_state:

        :returns: The fetched CallSummaryInstance
        """
        return self._proxy.fetch(
            processing_state=processing_state,
        )

    async def fetch_async(
        self,
        processing_state: Union[
            "CallSummaryInstance.ProcessingState", object
        ] = values.unset,
    ) -> "CallSummaryInstance":
        """
        Asynchronous coroutine to fetch the CallSummaryInstance

        :param processing_state:

        :returns: The fetched CallSummaryInstance
        """
        return await self._proxy.fetch_async(
            processing_state=processing_state,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.CallSummaryInstance {}>".format(context)


class CallSummaryContext(InstanceContext):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the CallSummaryContext

        :param version: Version that contains the resource
        :param call_sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }
        self._uri = "/Voice/{call_sid}/Summary".format(**self._solution)

    def fetch(
        self,
        processing_state: Union[
            "CallSummaryInstance.ProcessingState", object
        ] = values.unset,
    ) -> CallSummaryInstance:
        """
        Fetch the CallSummaryInstance

        :param processing_state:

        :returns: The fetched CallSummaryInstance
        """

        data = values.of(
            {
                "ProcessingState": processing_state,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return CallSummaryInstance(
            self._version,
            payload,
            call_sid=self._solution["call_sid"],
        )

    async def fetch_async(
        self,
        processing_state: Union[
            "CallSummaryInstance.ProcessingState", object
        ] = values.unset,
    ) -> CallSummaryInstance:
        """
        Asynchronous coroutine to fetch the CallSummaryInstance

        :param processing_state:

        :returns: The fetched CallSummaryInstance
        """

        data = values.of(
            {
                "ProcessingState": processing_state,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return CallSummaryInstance(
            self._version,
            payload,
            call_sid=self._solution["call_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.CallSummaryContext {}>".format(context)


class CallSummaryList(ListResource):
    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the CallSummaryList

        :param version: Version that contains the resource
        :param call_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "call_sid": call_sid,
        }

    def get(self) -> CallSummaryContext:
        """
        Constructs a CallSummaryContext

        """
        return CallSummaryContext(self._version, call_sid=self._solution["call_sid"])

    def __call__(self) -> CallSummaryContext:
        """
        Constructs a CallSummaryContext

        """
        return CallSummaryContext(self._version, call_sid=self._solution["call_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.CallSummaryList>"