from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Elvis</li>
    <li>Cosmin</li>
    <li>Jenuta</li>
    <li>Jean</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser') # initiate the parser


def find_title():
    """find the title using the h1 tag"""
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    """find all the elements that have the 'li' tag and print them"""
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)


def find_subtitle():
    """Find the paragraph that has the subtitle class"""
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    """Find the other paragraphs that do not have the subtitle class"""
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)

find_title()
find_list_items()
find_subtitle()
find_other_paragraph()
