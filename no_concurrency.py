#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 15:47:00
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


import time
import requests


def get_statuses(websites):
    statuses = {}
    for website in websites:
        response = requests.get(website)
        status = response.status_code
        statuses.setdefault(status, 0)
        statuses[status] += 1
    return statuses


if __name__ == '__main__':
    start = time.time()
    websites = [
        "http://www.163.com/",
        "https://www.baidu.com/",
        "http://www.sina.com.cn/",
        "https://www.taobao.com/",
        "https://github.com/"
    ]
    print(get_statuses(websites))
    time_taken = time.time() - start
    print("takes %f seconds" % time_taken)
