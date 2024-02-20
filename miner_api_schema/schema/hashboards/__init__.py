from __future__ import annotations

from pydantic import BaseModel

from miner_api_schema.schema.base import BaseResponse


class HashBoardData(BaseModel):
    """
    :param slot: The physical slot of the board, indexed from 0.  For a 3 board machine, should be 0, 1, or 2.
    :param id: The internal ID of the board.  For S9s, this would be 6, 7, 8.
    :param enabled: Whether the board is enabled.
    :param working: Whether the board is working (non-broken).  Should not be affected by enabled.
    :param avg_hashrate: The average hashrate of the board across the uptime of the miner.
    :param avg_hashrate_5s: THe average hashrate of the board in the past 5 seconds.
    :param avg_hashrate_1m: THe average hashrate of the board in the past minute.
    :param avg_hashrate_5m: THe average hashrate of the board in the past 5 minutes.
    :param hashrate_unit: The unit of measurement for the hashrate.
    :param working_chips: The number of chips on the board that are working (non-broken).
    :param expected_chips: The number of chips that are expected to be working on the board.
    :param wattage: The power consumption of the board.
    :param avg_pcb_temperature: The average temperature of the PCB sensors.
    :param avg_chip_temperature: The average temperature of the chip sensors.
    :param max_chip_temperature: The highest temperature of the chip sensors.
    :param min_chip_temperature: The lowest temperature of the chip sensors.
    :param serial_number: The serial number of the hashboard.
    """

    slot: int
    id: int
    enabled: bool
    working: bool
    avg_hashrate: float
    avg_hashrate_5s: float
    avg_hashrate_1m: float
    avg_hashrate_5m: float
    hashrate_unit: str
    working_chips: int
    expected_chips: int
    wattage: int
    avg_pcb_temperature: float
    avg_chip_temperature: float
    max_chip_temperature: float
    min_chip_temperature: float
    serial_number: str


class ASICChipData(BaseModel):
    """
    :param id: The chip ID on the board.
    :param enabled: Whether the chip is enabled.
    :param working: Whether the chip is a working chip (non-broken).  Should not be affected by enabled.
    :param temperature: The temperature reading of the chip.
    :param hashrate: The hashrate of the chip.  Should use the same unit as the enclosing class.
    :param voltage: The voltage on the chip.
    :param frequency: The frequency on the chip.
    :param hardware_errors: The number of hardware errors on this chip.
    """

    id: int
    enabled: bool
    working: bool
    temperature: float
    hashrate: float
    voltage: float
    frequency: float
    hardware_errors: int


class AdvancedHashBoardData(HashBoardData):
    """
    :param chips: A list of chip data.
    :param chip_type: The chip type on the board, such as '0x1930' or '0x1968'.
    :param hardware_errors: The number of hardware errors on this board.
    """

    chips: list[ASICChipData]
    chip_type: str
    hardware_errors: int


class HashBoardsResult(BaseModel):
    """
    :param count: The number of boards in the response.
    :param expected_count: The nominal number of boards in this machine.
    :param advanced: Whether the hashboards list contains `AdvancedHashBoardData`.
    :param hashboards: A list of `HashBoardData` or `AdvancedHashBoardData` if advanced is True.
    """

    count: int
    expected_count: int
    advanced: bool
    hashboards: list[HashBoardData | AdvancedHashBoardData]


class HashBoardsResponse(BaseResponse):
    result: HashBoardsResult
