import datetime as dt
from language_model.token import Token


class Match:
    def __init__(self, date: dt.date,
                 home_team: Token, home_result: Token, home_pitcher: str, home_score: int,
                 away_team: Token, away_result: Token, away_pitcher: str, away_score: int):
        self._date: dt.date = date

        self._home_team: Token = home_team
        self._home_result: Token = home_result
        self._home_pitcher: str = home_pitcher
        self._home_score: int = home_score

        self._away_team: Token = away_team
        self._away_result: Token = away_result
        self._away_pitcher: str = away_pitcher
        self._away_score: int = away_score

    def __repr__(self) -> str:
        return f"{self._date.year}-{self._date.month}-{self._date.day}: {self._home_team} {self._home_score} vs {self._away_team} {self._away_score}"

    def date(self) -> dt.date:
        return self._date

    def home_team(self) -> Token:
        return self._home_team

    def home_result(self) -> Token:
        return self._home_result

    def home_pitcher(self) -> str:
        return self._home_pitcher

    def home_score(self) -> int:
        return self._home_score

    def away_team(self) -> Token:
        return self._away_team

    def away_result(self) -> Token:
        return self._away_result

    def away_pitcher(self) -> str:
        return self._away_pitcher

    def away_score(self) -> int:
        return self._away_score

