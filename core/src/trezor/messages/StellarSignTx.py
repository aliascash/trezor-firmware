# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class StellarSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 202

    def __init__(
        self,
        *,
        address_n: List[int] = None,
        network_passphrase: str = None,
        source_account: str = None,
        fee: int = None,
        sequence_number: int = None,
        timebounds_start: int = None,
        timebounds_end: int = None,
        memo_type: int = None,
        memo_text: str = None,
        memo_id: int = None,
        memo_hash: bytes = None,
        num_operations: int = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.network_passphrase = network_passphrase
        self.source_account = source_account
        self.fee = fee
        self.sequence_number = sequence_number
        self.timebounds_start = timebounds_start
        self.timebounds_end = timebounds_end
        self.memo_type = memo_type
        self.memo_text = memo_text
        self.memo_id = memo_id
        self.memo_hash = memo_hash
        self.num_operations = num_operations

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            3: ('network_passphrase', p.UnicodeType, None),
            4: ('source_account', p.UnicodeType, None),
            5: ('fee', p.UVarintType, None),
            6: ('sequence_number', p.UVarintType, None),
            8: ('timebounds_start', p.UVarintType, None),
            9: ('timebounds_end', p.UVarintType, None),
            10: ('memo_type', p.UVarintType, None),
            11: ('memo_text', p.UnicodeType, None),
            12: ('memo_id', p.UVarintType, None),
            13: ('memo_hash', p.BytesType, None),
            14: ('num_operations', p.UVarintType, None),
        }
