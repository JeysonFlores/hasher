#!@PYTHON@
from enum import Enum
import hashlib
from fastlogging import LogInit
from asyncio import get_event_loop
from sdbus import (
    DbusInterfaceCommonAsync,
    DbusFailedError,
    dbus_method_async,
    dbus_property_async,
    request_default_bus_name_async,
)


SERVICE_VERSION = "@VERSION@"
BLOCK_SIZE = 65536

logger = LogInit(pathName="./tmp/logs.log", console=True, colors=True)


class HashType(Enum):
    MD5 = 0
    SHA1 = 1
    SHA224 = 2
    SHA256 = 3
    SHA384 = 4
    SHA512 = 5
    BLAKE2B = 6
    BLAKE2S = 7
    SHA3_224 = 8
    SHA3_256 = 9
    SHA3_384 = 10
    SHA3_512 = 11


class HasherInterface(
    DbusInterfaceCommonAsync, interface_name="com.github.jeysonflores.hasher.Service"
):
    def get_hash(self, filepath, file_hash):
        with open(filepath, "rb") as file:
            file_buffer = file.read(BLOCK_SIZE)
            while len(file_buffer) > 0:
                file_hash.update(file_buffer)
                file_buffer = file.read(BLOCK_SIZE)

        return file_hash.hexdigest()

    @dbus_method_async(
        input_signature="si",
        result_signature="s",
        input_args_names=["filepath", "algorithm"],
        result_args_names=["hash_digest"],
    )
    async def hash(self, filepath: str, algorithm: int) -> str:
        logger.info("Hash method called...")

        try:
            hash_type = HashType(algorithm)

            if hash_type == HashType.MD5:
                hash = hashlib.md5()
            elif hash_type == HashType.SHA1:
                hash = hashlib.sha1()
            elif hash_type == HashType.SHA224:
                hash = hashlib.sha224()
            elif hash_type == HashType.SHA256:
                hash = hashlib.sha256()
            elif hash_type == HashType.SHA384:
                hash = hashlib.sha384()
            elif hash_type == HashType.SHA512:
                hash = hashlib.sha512()
            elif hash_type == HashType.BLAKE2B:
                hash = hashlib.blake2b()
            elif hash_type == HashType.BLAKE2S:
                hash = hashlib.blake2s()
            elif hash_type == HashType.SHA3_224:
                hash = hashlib.sha3_224()
            elif hash_type == HashType.SHA3_256:
                hash = hashlib.sha3_256()
            elif hash_type == HashType.SHA3_384:
                hash = hashlib.sha3_384()
            elif hash_type == HashType.SHA3_512:
                hash = hashlib.sha3_512()

            return self.get_hash(filepath, hash)

        except ValueError as e:
            logger.error("Unknown Hash Algorithm")
            raise DbusFailedError

        except Exception as e:
            logger.error("There was an error")
            raise DbusFailedError

    @dbus_property_async(
        property_signature="s",
        property_name="service_version",
    )
    def service_version(self) -> str:
        return SERVICE_VERSION


loop = get_event_loop()
hasher_object = HasherInterface()


async def startup() -> None:
    logger.info("Starting D-Bus Service...")
 
    await request_default_bus_name_async("com.github.jeysonflores.hasher.Service")
    hasher_object.export_to_dbus("/com/github/jeysonflores/hasher/Service")
    
    logger.info("D-Bus Service started")


loop.run_until_complete(startup())
loop.run_forever()
