
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import random
import os
import pandas as pd



def get_group_member(driver = None):
    driver.refresh()
    elem_end = WebDriverWait(driver = driver ,timeout = 100).until \
        (EC.presence_of_element_located((By.XPATH ,'//td[@class="td-user-nick"]/img')))
    for i in range(40):
        time.sleep(0.5)
        driver.execute_script("var action=document.documentElement.scrollTop=10000")
        print(f'加载中,第{i}次加载······')
    group_members = driver.find_elements_by_xpath('//tr[contains(@class,"mb")]')

    for group_member in group_members:
        try:
            print(type(group_member.text))
            print(group_member.text)
            number = group_member.text.split('\n')[2].split(' ')[0]
            id_ = group_member.text.split('\n')[0].split(' ')[0]
            nickName = group_member.text.split('\n')[1].split(' ')[0]
            dat a =get_group_member.text
            print(nickName)
            dic t ={
                '编号' :id_,
                '昵称' :nickName,
                'qq号' :number
            }
            d f =pd.DataFrame(dict)
            print(dict)
            print(df)
            #             if data.isdigit() == True:
            with open('./recordppp.txt' ,'a' ,encoding = 'utf-8') as record:
                record.write(data)
                record.write('\n')
        except:
            continue
    print('Loaded')


def get_group_number(driver = None):
    group_number_dic = {}
    my_group_list = WebDriverWait(driver = driver ,timeout = 100).until \
        (EC.presence_of_all_elements_located((By.XPATH ,'//ul[@class="my-group-list"]/li')))
    print('在以下群中选择：')
    i = 1
    for my_group in my_group_list:
        try:
            group_number_dic[str(i)] = my_group
            print('第 %s 个---  ' %str(i) + my_group.get_attribute('title') + ' ' + my_group.get_attribute('data-id'))
            i += 1
        except:
            continue
    group = input('获取群编号 : ')
    group_number_dic[group].click()

    return driver

def login(driver = None):
    already_dic = {}
    login_button = WebDriverWait(driver = driver ,timeout = 100).until \
        (EC.presence_of_element_located((By.XPATH ,'//p[@class="user-info"]/a')))
    login_button.click()
    already_login_number = WebDriverWait(driver = driver ,timeout = 100).until \
        (EC.presence_of_element_located((By.XPATH ,'//div[@id="loginWin"]/iframe')))
    driver.get(url = already_login_number.get_attribute('src'))
    already_login_numbers = WebDriverWait(driver = driver ,timeout = 100).until \
        (EC.presence_of_all_elements_located((By.XPATH ,'//span[contains(@class,"nick")]')))
    print('在以下账号中选择所需账号')
    for already_login_number in already_login_numbers:
        already_dic[already_login_number.get_attribute('innerText')] = already_login_number
        print(already_login_number.get_attribute('innerText'))
    QQ_NeedToLogin = input('需要登陆: ')
    already_dic[QQ_NeedToLogin].click()
    time.sleep(1)


def start(driver = None ,url = None):

    print('Please wait for loading\n')
    driver.get(url = url)
    driver = get_group_number(driver=driver)

    print('Please wait for loading\n')
    get_group_member(driver=driver)
if __name__ == '__main__':
    print('Please wait for loading')
    chrome_option s =Options()
    chrome_options.add_argument('--headless')
    try:
        random.seed(time.time())
        QQ_number = '398435916'
        start_url = 'https://qun.qq.com/index.html#click'
        member_url = 'https://qun.qq.com/member.html#gid=%s ' %QQ_number
        member_url_test = 'https://qun.qq.com/member.html'
        driver = webdriver.Chrome()
        try:
            driver.get(url=start_url)
            login(driver=driver)
            while True:
                start(driver = driver ,url = member_url_test)
                flag = input('是否继续爬取？ yes or no : ')
                if flag == 'no':
                    break
                os.system('cls')
            driver.quit()
        except:
            print('Something wrong')
            driver.quit()
    except:
        print('Something wrong!!!!!!')
        os.system('pause')