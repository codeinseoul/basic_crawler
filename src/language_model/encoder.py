from language_model.token import Token
from typing import Set, List
from database.match import Match
import datetime as dt


class Encoder:
    def __init__(self, date: dt.date):
        self._date: dt.date = date

    def encode(self, sentences: List[str]) -> Set[Match]:
        matches = set()

        for sentence in sentences:
            if "베이스볼" not in sentence:
                try:
                    match = self.encode_match(sentence)
                    matches.add(match)
                except Exception as e:
                    continue

        return matches

    def encode_match(self, sentence: str) -> Match:
        pos = 0

        away_team = self.encode_team(sentence[pos:])
        pos += len(str(away_team))

        away_result = self.encode_result(sentence[pos:])
        pos += len(str(away_result))

        away_pitcher = self.encode_pitcher(sentence[pos:])
        pos += len(str(away_pitcher)) + len("스코어")

        away_score = self.encode_score(sentence[pos:])
        pos += len(str(away_score))

        home_team = self.encode_team(sentence[pos:])
        pos += len(str(home_team))

        assert sentence[pos] == "홈"
        pos += len("홈")

        home_result = self.encode_result(sentence[pos:])
        pos += len(str(home_result))

        home_pitcher = self.encode_pitcher(sentence[pos:])
        pos += len(str(home_pitcher)) + len("스코어")

        home_score = self.encode_score(sentence[pos:])
        pos += len(str(home_score))

        return Match(self._date, home_team, home_result, home_pitcher, home_score, away_team, away_result, away_pitcher, away_score)

    def encode_team(self, sentence: str) -> Token:
        if "LG" == sentence[:2]:
            return Token(Token.TokenType.KT)
        elif "KT" == sentence[:2]:
            return Token(Token.TokenType.KT)
        elif "SSG" == sentence[:3]:
            return Token(Token.TokenType.SSG)
        elif "NC" == sentence[:2]:
            return Token(Token.TokenType.NC)
        elif "두산" == sentence[:2]:
            return Token(Token.TokenType.DOOSAN)
        elif "KIA" == sentence[:3]:
            return Token(Token.TokenType.KIA)
        elif "롯데" == sentence[:2]:
            return Token(Token.TokenType.LOTTE)
        elif "삼성" == sentence[:2]:
            return Token(Token.TokenType.SAMSUNG)
        elif "한화" == sentence[:2]:
            return Token(Token.TokenType.HANHWA)
        elif "키움" == sentence[:2]:
            return Token(Token.TokenType.KIWOOM)
        else:
            raise ValueError("team is invalid")

    def encode_result(self, sentence: str) -> Token:
        if sentence[0] == "승":
            return Token(Token.TokenType.WIN)
        elif sentence[0] == "패":
            return Token(Token.TokenType.LOSE)
        else:
            raise ValueError("result is invalid")

    def encode_pitcher(self, sentence: str) -> str:
        index = sentence.find("스코어")

        return sentence[:index]

    def encode_score(self, sentence: str) -> int:
        for i in range(1, len(sentence)):
            word = sentence[:i]
            if not word.isdigit():
                return int(sentence[:i-1])