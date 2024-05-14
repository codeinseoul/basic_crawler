from urllib.error import HTTPError, URLError
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from language_model.encoder import Encoder
from parser.naver_sports_parser import NaverSportsParser
import datetime as dt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=str, default="2024-05-01")
    parser.add_argument("--end", type=str, default="2024-05-14")
    args = parser.parse_args()

    start_date = dt.datetime.strptime(args.start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(args.end, "%Y-%m-%d")
    delta = dt.timedelta(days=1)

    naver_sports_parser = NaverSportsParser()

    date = start_date
    while date <= end_date:
        encoder = Encoder(date)

        query = date.strftime("%Y-%m-%d")

        try:
            driver = webdriver.Chrome()
            driver.get(f"https://m.sports.naver.com/kbaseball/schedule/index?date={query}")

            html = driver.page_source
            bs = BeautifulSoup(html, "html.parser")
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        else:
            if bs is not None:
                match_elements = bs.find_all("div", {"class": naver_sports_parser.is_match})

                match_sentences = []
                for element in match_elements:
                    match_sentences.append(element.text)

                matches = encoder.encode(match_sentences)

                for match in matches:
                    print(match)

        date += delta
