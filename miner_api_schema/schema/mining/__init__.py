from __future__ import annotations

from enum import IntFlag
from typing import Any, Optional

from pydantic import BaseModel

from miner_api_schema.schema.base import BaseResponse


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

    def __str__(self):
        if self.value == self.normal:
            return "Normal"
        if self.value == self.sleep:
            return "Sleep"
        if self.value == self.low:
            return "Low"
        if self.value == self.high:
            return "High"
        if self.value == self.power_tune:
            return "Power Tuning"
        if self.value == self.hashrate_tune:
            return "Hashrate Tuning"

class MiningModeDescription(BaseModel):
    """
    :param mode: The mining mode the miner is currently using.  May be extended with additional values as needed.
    :param name: The internal name of the mining mode the miner is using.
    """

    mode: MiningMode
    name: str


class MiningModeResult(MiningModeDescription):
    """
    :param target: The target of the mining mode. Hashrate tuning uses this for hashrate, power tuning for power.  Can be set to 0, or used to communicate expected hashrate for other modes.
    :param available: The available mining modes on this machine..
    """

    target: Any = 0
    available: list[MiningModeDescription]


class MiningModeResponse(BaseResponse):
    result: MiningModeResult


class SetMiningModeParams(BaseModel):
    """
    :param mode: The mining mode to set the miner to use.
    :param target: The target of the mining mode. Hashrate tuning uses this for hashrate, power tuning for power.  May be excluded for modes that don't use a target.
    """

    mode: MiningMode | int
    target: Optional[Any]


class SetMiningModeRequest(BaseModel):
    param: SetMiningModeParams
