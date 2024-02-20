from typing import Any, Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    :param status: The status of the request.
    :param message: The result message or an error message if the request failed.
    :param command: The command that was sent.  Set to None if the command cannot be loaded.
    :param result: The result of the command.  Type overridden by subclasses.
    """

    status: bool
    message: str
    command: Optional[str] = None
    result: Optional[Any] = None


class BaseRequest(BaseModel):
    """
    :param command: The command to use.  Interchangeable with `cmd`.
    :param cmd: The command to use.  Interchangeable with `command`.
    :param param: The parameters to use.  Used by set requests.
    """

    command: Optional[str] = None
    cmd: Optional[str] = None
    param: Optional[BaseModel] = None
