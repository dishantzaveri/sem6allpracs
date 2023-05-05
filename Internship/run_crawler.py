import os
import traceback
import argparse

import pandas as pd

from tqdm.auto import tqdm
from selenium import webdriver

class ACLAnthologyCrawler(object):
    def __init__(self, chrome_driver_path="D:/"):
        self.chrome_driver_path = chrome_driver_path

        self.web_driver = webdriver.Chrome(executable_path=r'D:/chromedriver.exe')
        # driver = webdriver.Chrome(executable_path=r'C:/path/to/chromedriver.exe')
        self.web_driver.implicitly_wait(10)

    def generate_url(self, event_name, year):
        if event_name == "acl":
            url = f"https://www.aclweb.org/anthology/volumes/{year}.{event_name.lower()}-main/"
        elif event_name == "conll":
            url = f"https://www.aclweb.org/anthology/volumes/{year}.{event_name.lower()}-1/"
        elif event_name == "emnlp":
            url = f"https://www.aclweb.org/anthology/volumes/{year}.{event_name.lower()}-main/"
        elif event_name == "coling":
            url = f"https://www.aclweb.org/anthology/volumes/{year}.{event_name}-main/"
        else:
            raise NotImplementedError(event_name)
        return url

    def crawling(self, event_name, year):

        crawled_papers = {
            "title": [],
            "authors" : [],
            "paper_url" : [],
            "year" : [],
            "conference" : []
        }

        try:
            conference_url = self.generate_url(event_name, year)
            print(conference_url)
            self.web_driver.get(conference_url)

            paper_list = self.web_driver.find_elements_by_xpath("//*[@class='d-sm-flex align-items-stretch']/span[2]")
            paper_list = paper_list[1:]

            paper_iterator = tqdm(paper_list, desc="Iteration")

            for paper in paper_iterator:
                paper_text = paper.text.split("\n")

                title = paper_text[0]
                authors = paper_text[1].replace(" |", ",")
                paper_url = paper.find_element_by_class_name("align-middle").get_attribute("href")

                crawled_papers["title"].append(title)
                crawled_papers["authors"].append(authors)
                crawled_papers["paper_url"].append(paper_url)
                crawled_papers["year"].append(year)
                crawled_papers["conference"].append(event_name)

        except:
            traceback.print_exc()

        finally:
            self.web_driver.quit()

        df = pd.DataFrame(crawled_papers)
        return df


def prepare_dir(dir_name):
    if not os.path.exists(dir_name): os.makedirs(dir_name)


if __name__ == '__main__':
    event_names = ["acl", "conll", "coling", "emnlp"]

    parser = argparse.ArgumentParser()

    parser.add_argument("--event_name", type=str, required=True,
                         help="event name(specify an event name listed in https://aclweb.org/anthology/)"
                              "[Examples] acl, conll, coling, emnlp, etc...")
    parser.add_argument("--year", type=str, required=True,
                        help="year (yyyy)")
    parser.add_argument("--output_dir", type=str, default="./output",
                        help="path to output directory")
    parser.add_argument("--chrome_driver_path", type=str, default="./chromedriver.exe",
                        help="path to ChromeDriver")

    args = parser.parse_args()

    prepare_dir(args.output_dir)
    fn = os.path.join(args.output_dir, "papers.csv")

    df_list = []
    for event_name in event_names:
        crawler = ACLAnthologyCrawler()
        df_list.append(crawler.crawling(event_name=event_name, year=args.year))

    result = pd.concat(df_list, ignore_index=True)

    result.to_excel(fn, index=False)
    result.to_csv(fn, index=False)
    print("All paper Info is dumped at {}".format(fn))
