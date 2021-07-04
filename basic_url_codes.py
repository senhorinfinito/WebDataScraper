def urls(base_url,start_page, last_page):
    """
    Urls fuction take single url as type string & number of total pages  as int.
    as return a list of urls
    :param base_url:  string
    :param start_page: int
    :param last_page: int
    :return: list of urls
    """
    url = str(base_url)
    page_urls = []
    for pages_url_number in range(int(start_page), int(last_page)):
        pages_url = url + str(pages_url_number)
        page_urls.append(pages_url)
    return page_urls

if __name__ == "__main__":
    urls()



