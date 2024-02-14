from __future__ import annotations
from pydantic import BaseModel

from miner_api_schema.base import BaseResponse
from miner_api_schema.fans import FanData


class PowerData(BaseModel):
    """
    :param psu_fan: Fan data for the PSU fan.
    :param power: The current power usage of the miner.
    :param max_power: The maximum rated output of the PSU.
    """
    psu_fan: FanData
    power: int
    max_power: int

class AdvancedPowerData(PowerData):
    """
    :param voltage_in: The current input voltage.
    :param voltage_out: The current output voltage.
    :param min_voltage: The minimum allowed input voltage.
    :param max_voltage: The maximum allowed input voltage.
    :param amperage_in: The current input amperage.
    :param amperage_out: The current output amperage.
    :param max_amperage: The maximum allowed input amperage.
    """
    voltage_in: float
    voltage_out: float
    min_voltage: float
    max_voltage: float
    amperage_in: float
    amperage_out: float
    max_amperage: float

class PowerResult(BaseModel):
    power: PowerData | AdvancedPowerData

class PowerResponse(BaseResponse):
    result: PowerResponse
