from requests import Session
from zeep import Client, Transport, Settings

from utils.types import Optional


class Request:
    def __init__(self) -> None:
        self.session = Session()

    def get(self, *args, **kwargs):
        return self.session.request(method="GET", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.session.request(method="POST", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.session.request(method="DELETE", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.session.request(method="PATCH", *args, **kwargs)

    def soap_client(
        self,
        wsdl_url: str,
        service_name: str,
        soap_post_url: Optional[str] = None,
        timeout: int = 10,
        *args,
        **kwargs
    ) -> str:
        transport = Transport(timeout=timeout, operation_timeout=timeout)
        settings = Settings(strict=True, raw_response=True)
        client = Client(wsdl_url, transport=transport, settings=settings)
        return getattr(client.service, service_name)(*args, **kwargs)
