import asyncio

from miner_api_schema.rpc import MinerSchemaRPCHandler

if __name__ == "__main__":
    asyncio.run(MinerSchemaRPCHandler().run())
