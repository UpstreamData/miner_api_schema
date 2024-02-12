from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    """
    :param status: The status of the request.
    :param message: The result message or an error message if the request failed.
    :param command: The command that was sent.
    :param result: The result of the command.  Type overridden by subclasses.
    """

    status: bool
    message: str
    command: str
    result: Any
