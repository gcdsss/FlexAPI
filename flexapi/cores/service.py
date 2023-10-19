import importlib

from pydantic import BaseModel, Field

from .request import Request
from .response import Response

from utils.consist_variable import ServiceType
from utils.types import ProcessMethod


class Service(BaseModel):
    name: str = Field(description="服务名称")
    type: ServiceType = Field(description="服务类型")
    save_log: bool = Field(description="是否保存服务日志", default=True)
    process_method_path: str = Field(
        description="服务处理方法 module.module1:method_name", default=True
    )

    def __init__(self) -> None:
        self.request = Request()
        self.response = Response()

    def _import_process_method(self) -> ProcessMethod:
        module_path, method_name = self.process_method_path.split(":")
        return getattr(
            importlib.import_module(module_path),
            method_name,
        )
