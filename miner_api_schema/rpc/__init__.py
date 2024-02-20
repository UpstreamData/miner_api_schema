from __future__ import annotations

import asyncio
import json
from typing import Callable, Optional, Any

from miner_api_schema.schema.base import BaseResponse
from miner_api_schema.schema.fans import (
    FansResponse,
    FansResult,
    AdvancedFanData,
    FanData,
)
from miner_api_schema.schema.mining import MiningModeResponse, MiningModeResult, MiningMode, \
    MiningModeDescription
from miner_api_schema.schema.multi import MultiResponse


class MinerSchemaRPCHandler:
    def __init__(self):
        self.commands: dict[str, Callable] = {
            "fans": self.fans,
            "mining_mode": self.mining_mode,
        }

    async def run(self):
        server = await asyncio.start_server(self._handle_client, "0.0.0.0", 4028)
        async with server:
            await server.serve_forever()

    async def _handle_client(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ):
        raw_data = await reader.read(4096)
        str_data = raw_data.decode()
        try:
            data = json.loads(str_data)
        except json.JSONDecodeError:
            writer.write(
                json.dumps(
                    self._handle_failure(
                        message="Unable to decode JSON.  It may be invalid."
                    ).dict()
                ).encode()
            )
            await writer.drain()
            writer.close()
            return

        result = self._handle_command(data)

        writer.write(json.dumps(result.dict()).encode())
        await writer.drain()
        writer.close()

    @staticmethod
    def _handle_failure(message: str, command: Optional[str] = None) -> BaseResponse:
        return BaseResponse(status=False, message=message, command=command)

    def _handle_command(self, data: dict) -> BaseResponse | MultiResponse:
        if "command" in data.keys():
            if "+" in data["command"]:
                return MultiResponse(
                    multi_result={
                        cmd: self.commands[cmd](**data.get("param", {}))
                        for cmd in data["command"].split("+")
                    }
                )
            return self.commands[data["command"]](**data.get("param", {}))
        elif "cmd" in data.keys():
            if "+" in data["cmd"]:
                return MultiResponse(
                    multi_result={
                        cmd: self.commands[cmd](**data.get("param", {}))
                        for cmd in data["cmd"].split("+")
                    }
                )
            return self.commands[data["cmd"]](**data.get("param", {}))
        return self._handle_failure(f"No command found in {data}.")

    def fans(self, **param: Any) -> FansResponse:
        if param.get("advanced"):
            return self.advanced_fans()

        fan_data = []

        for fan in range(2):
            fan_data.append(
                FanData(
                    id=fan,
                    speed=100,
                    rpm=6000,
                    max_rpm=6000,
                )
            )

        return FansResponse(
            status=True,
            message="Fan data.",
            command="fans",
            result=FansResult(
                count=2,
                expected_count=2,
                advanced=False,
                fans=fan_data,
            ),
        )

    def advanced_fans(self) -> FansResponse:
        fan_data = []

        for fan in range(2):
            fan_data.append(
                AdvancedFanData(
                    id=fan,
                    speed=100,
                    rpm=6000,
                    max_rpm=6000,
                )
            )

        return FansResponse(
            status=True,
            message="Fan data.",
            command="fans",
            result=FansResult(
                count=2,
                expected_count=2,
                advanced=False,
                fans=fan_data,
            ),
        )

    def mining_mode(self, **param: Any) -> MiningModeResponse:
        return MiningModeResponse(
            status=True,
            message="Mining mode data.",
            command="mining_mode",
            result=MiningModeResult(
            mode=MiningMode.normal,
            name=str(MiningMode.normal),
            available=[MiningModeDescription(mode=val, name=str(val)) for val in MiningMode]
        ))
