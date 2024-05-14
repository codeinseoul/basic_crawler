from enum import Enum, auto


class Token:
    class TokenType(Enum):
        LG = auto()
        KT = auto()
        SSG = auto()
        NC = auto()
        DOOSAN = auto()
        KIA = auto()
        LOTTE = auto()
        SAMSUNG = auto()
        HANHWA = auto()
        KIWOOM = auto()

        WIN = auto()
        LOSE = auto()

    def __init__(self, token_type: TokenType):
        self._token_type: Token.TokenType = token_type

    def __repr__(self) -> str:
        match self._token_type:
            case Token.TokenType.LG:
                return "LG"
            case Token.TokenType.KT:
                return "KT"
            case Token.TokenType.SSG:
                return "SSG"
            case Token.TokenType.NC:
                return "NC"
            case Token.TokenType.DOOSAN:
                return "두산"
            case Token.TokenType.KIA:
                return "KIA"
            case Token.TokenType.LOTTE:
                return "롯데"
            case Token.TokenType.SAMSUNG:
                return "삼성"
            case Token.TokenType.HANHWA:
                return "한화"
            case Token.TokenType.KIWOOM:
                return "키움"
            case Token.TokenType.WIN:
                return "승"
            case Token.TokenType.LOSE:
                return "패"
            case _:
                raise ValueError("token type is invalid")