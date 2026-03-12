from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome()
driver.get('https://vip.com')
driver.maximize_window()
# time.sleep(2)
driver.delete_all_cookies()
cookies = {
    'vip_address': '%257B%2522pid%2522%253A%2522102101%2522%252C%2522cid%2522%253A%2522102101105%2522%252C%2522pname%2522%253A%2522%255Cu8fbd%255Cu5b81%255Cu7701%2522%252C%2522cname%2522%253A%2522%255Cu672c%255Cu6eaa%255Cu5e02%2522%257D',
    'vip_province': '102101',
    'vip_province_name': '%E8%BE%BD%E5%AE%81%E7%9C%81',
    'vip_city_name': '%E6%9C%AC%E6%BA%AA%E5%B8%82',
    'vip_city_code': '102101105',
    'vip_wh': 'VIP_BJ',
    'vip_ipver': '31',
    'mars_cid': '1772412209598_6dc1a9c929615bd26ec05eea99f1c3c8',
    'mars_sid': '9f56dbec17714fa9908603d0f73cb966',
    'mst_area_code': '104104',
    'mars_pid': '0',
    'VIP_QR_FIRST': '1',
    'vip_sec_fp_vvid': 'ZTk4YzdjZTQtOThjNS00MTQ5LWJmMTAtZWUzZDc4ODdkN2YzMTc3MjQxMjIwOTUyMMl/Y2M=',
    'pc_fdc_area_id': '102101105',
    'pc_fdc_source_ip': '1',
    'is_default_area': '1',
    'smidV2': '20260302084341ca67355c54f9f01968bb8a071eca421400ceea543cfe14940',
    'VipRUID': '657722323',
    'VipRNAME': 'ph_*****************************10b',
    'VipDegree': 'D1',
    'user_class': 'b',
    'vip_sec_fp_vid': '657722323',
    'VipUINFO': 'luc%3Ab%7Csuc%3Ab%7Cbct%3Ac_new%7Chct%3Ac_new%7Cbdts%3A0%7Cbcts%3A0%7Ckfts%3A0%7Cc10%3A0%7Crcabt%3A0%7Cp2%3A0%7Cp3%3A1%7Cp4%3A0%7Cp5%3A0%7Cul%3A3105',
    'vip_tracker_source_from': '',
    'VipUID': '7a6d429fa3bd4407fcc5bdc5b874fa74',
    'vip_access_times': '%7B%22list%22%3A3%7D',
    '_jzqco': '%7C%7C%7C%7C%7C1.1233541264.1772412222102.1772413855733.1772443445996.1772413855733.1772443445996.0.0.0.4.4',
    'PASSPORT_ACCESS_TOKEN': '839D438C7BCEF05C2570A1F8AD878A1A6C1E6E8B',
    'VipLID': '0%7C1772443466%7Ccc2c49',
    'fe_global_sync': '1',
    '.thumbcache_f65dad1092aa9e66c73b4823b4493a2f': 'PgQ+YK+FMs2IzdCHxv9jeP56YeI+bO9nFiQCInWDqqEWqUw5z/HSQodaHFJQ3Dc6fcdzgprw3MD6b4x7nv4nvA%3D%3D',
    'vip_sec_fp_smtoken': 'BPgQ+YK+FMs2IzdCHxv9jeP56YeI+bO9nFiQCInWDqqEWqUw5z/HSQodaHFJQ3Dc6fcdzgprw3MD6b4x7nv4nvA==',
    'tfs_fp_token': 'BPgQ+YK+FMs2IzdCHxv9jeP56YeI+bO9nFiQCInWDqqEWqUw5z/HSQodaHFJQ3Dc6fcdzgprw3MD6b4x7nv4nvA%3D%3D',
    'vip_sec_fp_wtk': 'cwEAAzBqMdOi0sS9GRU1PK0pXb2dQOLVn443i7GESPAYK_zkTU-bZqa06-kHrB4dHEVfuEolSo4q3qkrUxE9agzUncN0dIE',
    'pg_session_no': '20',
    'tfs_fp_timestamp': '1772452944859',
    'waitlist': '%7B%22pollingId%22%3A%226818B461-1DD4-43D5-8B66-734F6CE40213%22%2C%22pollingStamp%22%3A1772453555511%7D',
}
for k, v in cookies.items():
    driver.add_cookie({'name': k, 'value': v, 'domain': '.vip.com', 'path': '/', 'secure': True})
driver.refresh()
# time.sleep(5)
# driver.get('https://vip.com')
time.sleep(5)
driver.get('https://category.vip.com/suggest.php?keyword=%E7%94%B5%E8%84%91')
while True:
    items = driver.find_elements(By.XPATH,
                                 '//div[@class="c-goods-item  J-goods-item c-goods-item--auto-width"]//div[@class="c-goods-item-bottom    "]/div[@class="c-goods-item__name  c-goods-item__name--two-line"]')
    list_data = []
    for item in items:
        list_data.append(item.text)
    print(len(list_data))
    print(list_data)
    # driver.refresh()
    # time.sleep(5)
    # driver.refresh()
    time.sleep(4)

    try:
        page = driver.find_element(By.ID, "J_nextPage_link")
        page.click()
        time.sleep(random.uniform(1, 1.5))
    except:
        print("没有下一页了")
        break
