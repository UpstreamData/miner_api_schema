from __future__ import annotations

from pydantic import BaseModel

from miner_api_schema.schema.base import BaseResponse


class FanData(BaseModel):
    """
    :param id: The ID of the fan.  Should always index from 0, for a 2 fan machine it should be 0 or 1.
    :param speed: The speed of the fan in %, from 0-100.
    :param rpm: The RPM of the fan.
    :param max_rpm: The maximum RPM of the attached fan.
    """

    id: int
    speed: float
    rpm: int
    max_rpm: int


class AdvancedFanData(FanData):
    """
    :param max_speed_set: The maximum speed of the fan as set by the user.  Defaults to 100.
    :param min_speed_set: The minimum speed fo the fan as set by the user.  Defaults to 0.
    :param: pid_mode: The PID mode being used.  Defaults to 0.
    """

    max_speed_set: int = 100
    min_speed_set: int = 0
    pid_mode: int = 0


class FansResult(BaseModel):
    """
    :param count: The number of fans in the response.
    :param expected_count: The nominal number of fans in this machine.
    :param advanced: Whether the fans list contains `AdvancedFanData`.
    :param fans: A list of `FanData` or `AdvancedFanData` if advanced is True.
    """

    count: int
    expected_count: int
    advanced: bool
    fans: list[FanData | AdvancedFanData]


class FansResponse(BaseResponse):
    result: FansResult
