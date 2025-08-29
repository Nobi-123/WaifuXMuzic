from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")

try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)

    # Use a specific database name instead of ".Anon"
    # You can rename "Anon" to any DB name you prefer
    db = _mongo_async_["Anon"]

    LOGGER(__name__).info("Connected to your Mongo Database.")

except Exception as e:
    LOGGER(__name__).error(f"Failed to connect to your Mongo Database: {e}")
    exit()
