from pydantic import BaseModel

from miner_api_schema.base import BaseResponse


class MultiResponse(BaseModel):
    """
    Handler for multi-commands.

    A multicommand is a list of commands joined on a `+`.  For example, `summary+hashboards` would return the result
    of board `summary` and `hashboards` in the format `{"multi_result": {"hashboards": result, "summary": result}}

    :param multi_result: The result from multiple commands.  Each item uses the command as the key.
    """

    multi_result: dict[str, BaseResponse]
