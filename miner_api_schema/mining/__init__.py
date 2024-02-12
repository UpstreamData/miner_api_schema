from __future__ import annotations

from enum import IntFlag
from typing import Any

from pydantic import BaseModel

from miner_api_schema.base import BaseResponse

class MiningMode(IntFlag):
    """
    :param normal: Normal mining mode.
    :param sleep: Sleep mode.
    :param low: Low power mode.
    :param high: High power mode.
    :param power_tune: Power tuning mode.  Paired with a wattage that it will optimize hashrate for.
    :param hashrate_tune: Hashrate tuning mode.  Paired with a hashrate that it will optimize power usage for.
    """
    normal = 0
    sleep = 1
    low = 2
    high = 3
    power_tune = 4
    hashrate_tune = 5


class MiningModeInfo(BaseModel):
    """
    :param mode: The mining mode the miner is currently using.  May be extended with additional values as needed.
    :param name: The internal name of the mining mode the miner is using.
    :param target: The target of the mining mode. Hashrate tuning uses this for hashrate, power tuning for power.  Can be set to 0, or used to communicate expected hashrate for other modes.
    """
    mode: MiningMode
    name: str
    target: Any

class MiningModeResponse(BaseResponse):
    result: MiningModeInfo
