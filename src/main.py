import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import os
import datetime


def main():
    start = datetime.datetime.now()
    root_path = Path(__file__).resolve(strict=True).parent.parent
    data = pd.read_csv(os.path.join(root_path, Path("data/data.txt")), sep=";", header=None)
    data.columns = ["domain", "init_date"]

    data["title"] = ""
    data["description"] = ""

    counter = 0
    # for domain in data["domain"]:
    for index, row in data.iterrows():
        len_description = 0
        len_title = 0
        domain = row["domain"]
        url = "http://" + domain
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features="lxml")
            metas = soup.find_all('meta')
            attr_names = [m.get('name') for m in metas]
            if 'description' in attr_names:
                for m in metas:
                    if m.get('name') == 'description':
                        desc = m.get('content')
                        len_description = len(desc)
            else:
                len_description = 0

            if 'title' in attr_names:
                for m in metas:
                    if m.get('name') == 'title':
                        title = m.get('content')
                        len_title = len(title)
            else:
                len_title = 0
        except:
            len_title = 0
            len_description = 0

        data.loc[index, "title"] = len_title
        data.loc[index, "description"] = len_description

        if counter > 150:
            break
        counter += 1

    data.to_csv(os.path.join(root_path, Path("data/result.csv")), index=False, header=False, sep=";")
    print(data[data['title'] != 0])


if __name__ == "__main__":
    main()
