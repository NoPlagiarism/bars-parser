import asyncio
import aiohttp
import uncurl
from datetime import datetime as dt
from collections import defaultdict
import json
from sys import exit

with open("curl.txt", "r") as f:
    curl = f.read()
print("Файл был открыт")

HOST = ""
if HOST != "":
    GetParentsUrl = HOST + "/api/MailBoxService/getParentUserProfiles"
else:
    GetParentsUrl = None

cookies = {

}

headers = {

}

GROUP_STUDENTS_BY_CLASS = True
FILE_TO_SAVE = "school_db.json"

kids = defaultdict(list)

if not curl and all((GetParentsUrl, headers, cookies)):
    pass
elif curl is not None:
    data = uncurl.parse_context(curl)
    if GetParentsUrl is None:
        HOST = '/'.join(data.url.split('/')[:3])
        GetParentsUrl = HOST + "/api/MailBoxService/getParentUserProfiles"
    cookies, headers = data.cookies, data.headers
elif not all((GetParentsUrl, headers, cookies)):
    print("Пожалуйста, введите данные в файле")
    exit(-1)

print("Данные для входа успешно получены")


def get_data(page_num):
    return {
        'fullname': '',
        'child_fullname': '',
        'study_level': '',
        'letter': '',
        "search_text": "",
        'page': page_num
    }


async def get_page(session: aiohttp.ClientSession, page_num):
    response = await session.get(GetParentsUrl, params=get_data(page_num))
    json_response = await response.json()
    return json_response


async def parse_page(session, page_num):
    global kids
    json_page = await get_page(session, page_num)
    for parent in json_page['items']:
        kids[(parent['child_fullname'], parent['class_name'])].append(parent['fullname'])
    return


async def main(main_loop):
    global kids

    session = aiohttp.ClientSession(cookies=cookies, headers=headers, loop=main_loop)
    before = dt.now()

    first_page = await get_page(session, 1)
    try:
        parents_per_page = len(first_page['items'])
    except KeyError:
        message = "Произошла ошибка"
        if first_page.get('faultcode', False) == "Server.UserNotAuthenticated":
            message += "\nПожалуйста, введите новые данные"
        print(message)
        return
    len_pages = first_page['count'] // parents_per_page

    await asyncio.gather(*[parse_page(session, page_num) for page_num in range(1, len_pages)])

    await session.close()

    after = dt.now()
    delta = after - before
    print(f"Parsing took {str(delta.total_seconds())} seconds:")

    if GROUP_STUDENTS_BY_CLASS:
        print("Группировка по классам включена")
        kids_grouped = defaultdict(dict)
        for kid, kid_class in kids:
            kids_grouped[kid_class][kid] = kids[(kid, kid_class)]
        kids = kids_grouped

    print("Сохраняю все данные в файл", FILE_TO_SAVE)
    with open(FILE_TO_SAVE, "w+", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in kids.items()}, f, ensure_ascii=False, indent=4)
    print("Все данные сохранены")


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
exit(0)
