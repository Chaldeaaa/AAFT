#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import concurrent.futures

def fetch_user_info(user_id):
    url = f"https://www.xinghun.love/home/{user_id}.html"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print(f"Failed to retrieve page for user ID {user_id}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    divinfo = soup.find('div', class_='divinfo')
    if not divinfo:
        print(f"No profile found for user ID {user_id}")
        return None

    def extract_info(divinfo, keyword):
        box = divinfo.find('div', string=lambda x: x and keyword in x)
        if box:
            return box.get_text(strip=True).split('：')[1]
        return 'NA'

    def extract_li_info(keyword):
        li = soup.find('li', string=lambda x: x and keyword in x)
        if li:
            return li.find('label').get_text(strip=True)
        return 'NA'

    gender = extract_info(divinfo, '性别')
    age = extract_info(divinfo, '年龄')
    income = extract_info(divinfo, '收入')
    marital_status = extract_info(divinfo, '婚况')
    occupation = extract_info(divinfo, '职业')
    location = extract_info(divinfo, '所在地')

    home_intro_elements = soup.find_all('div', class_='home_intro')
    hope_for_marriage = home_intro_elements[0].find('div', class_='intro').get_text(strip=True) if len(home_intro_elements) > 0 else '未知'
    hope_for_partner = home_intro_elements[1].find('div', class_='intro').get_text(strip=True) if len(home_intro_elements) > 1 else '未知'

    marriage_type = extract_li_info('婚姻类型')
    has_children = extract_li_info('有无小孩')
    wants_children = extract_li_info('婚后是否要孩子')
    certificate = extract_li_info('是否领证')
    live_together = extract_li_info('婚后是否同住')
    job_nature = extract_li_info('工作性质')
    accept_long_distance = extract_li_info('是否接受异地')
    stable_same_sex_partner = extract_li_info('是否有稳定同性对象')
    look_for_same_sex_partner = extract_li_info('是否想找同性伴侣')
    come_out = extract_li_info('是否出柜')
    education = extract_li_info('学历')

    return {
        'ID': user_id,
        '性别': gender,
        '年龄': age,
        '收入': income,
        '婚况': marital_status,
        '职业': occupation,
        '所在地': location,
        '形婚期望': hope_for_marriage,
        '对象期望': hope_for_partner,
        '婚姻类型': marriage_type,
        '有无小孩': has_children,
        '婚后是否要孩子': wants_children,
        '是否领证': certificate,
        '婚后是否同住': live_together,
        '工作性质': job_nature,
        '是否接受异地': accept_long_distance,
        '是否有稳定同性对象': stable_same_sex_partner,
        '是否想找同性伴侣': look_for_same_sex_partner,
        '是否出柜': come_out,
        '学历': education
    }

def main():
    user_id_start = 85000
    user_id_end = 88000
    processed_ids = set()

    if os.path.isfile('profiles.csv'):
        with open('profiles.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                processed_ids.add(int(row['ID']))

    def process_user_id(user_id):
        if user_id in processed_ids:
            return None
        return fetch_user_info(user_id)

    with open('profiles.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'ID', '性别', '年龄', '收入', '婚况', '职业', '所在地', '形婚期望', '对象期望',
            '婚姻类型', '有无小孩', '婚后是否要孩子', '是否领证', '婚后是否同住', '工作性质',
            '是否接受异地', '是否有稳定同性对象', '是否想找同性伴侣', '是否出柜', '学历'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not processed_ids:
            writer.writeheader()

        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            future_to_user_id = {executor.submit(process_user_id, user_id): user_id for user_id in range(user_id_start, user_id_end + 1)}
            for future in concurrent.futures.as_completed(future_to_user_id):
                user_id = future_to_user_id[future]
                try:
                    user_data = future.result()
                    if user_data:
                        writer.writerow(user_data)
                        print(f"Written data for user ID {user_id}")
                except Exception as exc:
                    print(f"User ID {user_id} generated an exception: {exc}")

    print("用户信息已保存到 profiles.csv 文件中。")

if __name__ == "__main__":
    main()


# In[ ]:


from google.colab import drive
drive.mount('/content/drive')

