# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .HDNodeType import HDNodeType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 306

    def __init__(
        self,
        xpub: str = None,
        node: HDNodeType = None,
    ) -> None:
        self.xpub = xpub
        self.node = node

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('xpub', p.UnicodeType, 0),
            2: ('node', HDNodeType, 0),
        }
