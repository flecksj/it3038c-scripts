from urllib.request import urlopen

page = urlopen('https://webscraper.io/test-sites/e-commerce/allinone/phones')
html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)