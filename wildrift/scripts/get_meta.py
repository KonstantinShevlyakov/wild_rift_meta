#!usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re


def get_response():
    response = requests.get('https://www.wildriftfire.com/tier-list')
    meta_file = open('wildrift/meta_files/meta.txt', 'w')
    return meta_file.write(response.text)


def get_meta(text):
    roles_list = []
    champions_list = []
    jungle, mid, solo, duo, support = [], [], [], [], []
    roles = text.findAll("a", attrs={"class": "ico-holder"})
    for elem in roles:
        roles_list.append(
            re.search(r"Jungle|Solo|Support|Mid|Duo", str(elem)).group(0)
        )
    champions = text.findAll("span")
    for elem in champions:
        champions_list.append(elem.text.strip())
    meta_list = list(zip(roles_list, champions_list))
    for elem in meta_list:
        if elem[0] == 'Jungle':
            jungle.append(elem[1])
        elif elem[0] == 'Solo':
            solo.append(elem[1])
        elif elem[0] == 'Mid':
            mid.append(elem[1])
        elif elem[0] == 'Duo':
            duo.append(elem[1])
        elif elem[0] == 'Support':
            support.append(elem[1])
        else:
            raise TypeError
    meta_file = open('wildrift/meta_files/s_tier.txt', 'w')
    meta_file.write(f'Jungle: {jungle}\nSupport: {support}\n'
                    f'Solo: {solo}\nDuo:{duo}\n'
                    f'Mid: {mid}')
    pass


def get_splus_tier():
    get_response()
    with open('wildrift/meta_files/meta.txt', 'r') as meta:
        contents = meta.read()
        soup = BeautifulSoup(contents, 'html.parser')
        splus = soup.find("div", attrs={"class": "tier splus"})
    return get_meta(splus)


def main():
    get_splus_tier()


if __name__ == '__main__':
    main()

print('Done')