# coding=utf-8
import requests
from bs4 import BeautifulSoup
from everyday_wechat.utils.common import SPIDER_HEADERS

def get_today_weather(cityname):
    """
        https://weather.mipang.com/rizhao获取特定城市今天天气
        """
    print('获取 米胖天气 信息...')
    weather_url = 'https://weather.mipang.com/{}'.format(cityname)
    try:
        resp = requests.get(weather_url, headers=SPIDER_HEADERS)
        if resp.status_code == 200:
            soup_texts = BeautifulSoup(resp.text, 'lxml')
            #取天气预报
            predict_msg = soup_texts.find('div', class_='row row1').text #只取当天的这句
            #取生活指数
            sweet_msg = soup_texts.find('div', class_='box box3').text.replace('\n', ':')
            return predict_msg + '\n' + sweet_msg
        print('获取 米胖天气 失败。')
    except Exception as exception:
        print(exception)
        return None
    return None


if __name__ == '__main__':
    cityname = 'guangzhou'
    print(get_today_weather(cityname))


