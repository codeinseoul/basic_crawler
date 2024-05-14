class NaverSportsParser:
    def __init__(self):
        pass

    def is_match(self, x: str) -> bool:
        if isinstance(x, str):
            return "MatchBox_match_area" in x
        else:
            return False
