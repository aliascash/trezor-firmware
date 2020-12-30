# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class IdentityType(p.MessageType):

    def __init__(
        self,
        *,
        proto: str = None,
        user: str = None,
        host: str = None,
        port: str = None,
        path: str = None,
        index: int = 0,
    ) -> None:
        self.proto = proto
        self.user = user
        self.host = host
        self.port = port
        self.path = path
        self.index = index

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('proto', p.UnicodeType, None),
            2: ('user', p.UnicodeType, None),
            3: ('host', p.UnicodeType, None),
            4: ('port', p.UnicodeType, None),
            5: ('path', p.UnicodeType, None),
            6: ('index', p.UVarintType, 0),  # default=0
        }
