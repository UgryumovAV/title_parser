import requests
from bs4 import BeautifulSoup
import datetime
import lxml
import metadata_parser


def main():
    start_time = datetime.datetime.now()
    url = "http://" + "Domen.ru"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    metas = soup.find_all('meta')
    # print([meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description'])
    # print(meta.attrs['name'] == 'description' for meta in metas)
    # for m in metas:
    #     if m.get('name') == 'description':
    #         desc = m.get('content')
    #         print(desc)
    #         print(type(desc))
    #         print(len(desc))
    # end_time = datetime.datetime.now()
    # print(end_time - start_time)

    for m in metas:
        print(m.get('name'))
        # if m.get('name') == 'title':
        #     desc = m.get('content')
        #     print(desc)

# def main():
#     html_content = "http://" + "Domen.ru"
#     doc = lxml.html.document_fromstring(html_content)
#     title_element = doc.xpath("//title")
#     website_title = title_element[0].text_content().strip()
#     print(website_title)
#     meta_description_element = doc.xpath("//meta[@property='description']")
#     website_meta_description = meta_description_element[0].text_content().strip()
#     print(website_meta_description)

# def main():
#     url = "http://" + "Domen.ru"
#     page = metadata_parser.MetadataParser(url=url)
#     meta_desc = page.metadata['og']['title']
#     print(meta_desc)


if __name__ == "__main__":
    main()
