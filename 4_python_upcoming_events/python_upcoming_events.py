from bs4 import BeautifulSoup
from urllib.request import urlopen


URL = 'https://www.python.org/events/python-events'


def find_bs_objects(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    bs_objects = soup.find('ul', {'class': 'list-recent-events'}).findAll('li')
    return bs_objects


def get_events_list(bs_objects):
    events_list = []
    for object in bs_objects:
        title = object.find('h3').text
        date = object.find('time').text
        location = object.find('span', {'class': 'event-location'}).text
        events_list.append([title, date, location])
    return events_list


def show_events_info(events):
    for event in events[0:4]:
        print('Upcoming event: %s' % ', '.join(event))


def main(url):
    bs_objects = find_bs_objects(url)
    events = get_events_list(bs_objects)
    show_events_info(events)


if __name__ == '__main__':
    main(URL)
