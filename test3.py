# -*- coding: utf-8 -*-
import requests
headers = {
    'x-common-params-v2': 'ac=WIFI&aid=1128&app_name=aweme&app_version=14.7.1&build_number=147104&channel=App%20Store&device_id=53117787417&device_platform=iphone&device_type=iPhone10,2&idfa=F49C2EE4-0A12-4E58-A3E6-2803DD7D796B&js_sdk_version=1.99.0.3&os_api=18&os_version=13.6',
}
params = (
    ('tma_jssdk_version', '1.99.0.3'),
    ('minor_status', '0'),
    ('appTheme', 'dark'),
    ('is_vcd', '1'),
    ('keyword', '好医保'),
    ('from_group_id', '6930981942590573831'),
)
for i in range(100):
    response = requests.get('https://search5-search-lf.amemv.com/aweme/v1/search/sug/', headers=headers, params=params)
    print(response.text)