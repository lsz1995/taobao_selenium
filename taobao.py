#selenuim  获取淘宝信息

from selenium import webdriver
from lxml import etree
import time
#driver = webdriver.Chrome()

#'''#无头浏览
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(options=opt)
#driver.get('http://www.baidu.com/')
#'''
good_total =[]
def get_info(url,page):
    page =page+1
    driver.get(url)
    driver.implicitly_wait(10)
    selector = etree.HTML(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    #print(len(infos))
    for info in infos:
        name = info.xpath('div/div/div/a/img/@alt')
        good ={
            'goods':name
        }
        good_total.append(good)

    if page<=3:
        NextPage(url,page)
    else:
        pass









def NextPage(url,page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(2)

    get_info(driver.current_url,page)





if __name__ == '__main__':
    url = 'http://www.taobao.com'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('Ipad')
    driver.find_element_by_class_name('btn-search').click()
    #print(driver.current_url)#当前链接
    get_info(driver.current_url,1)


    print(good_total)
    print(len(good_total))