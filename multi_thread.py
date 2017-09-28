#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 16:18:38
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import time
import threading
import requests


def multi_thread_get_statuses(websites):
    threads = []
    statuses = {}
    for website in websites:
        t = threading.Thread(target=get_status, args=(website, statuses))
        threads.append(t)
    for i in threads:
        i.start()
    for j in threads:
        j.join()
    return statuses


def get_status(website, statuses):
    response = requests.get(website)
    status = response.status_code
    statuses.setdefault(status, 0)
    statuses[status] += 1


if __name__ == '__main__':
    start = time.time()
    websites = [
        "http://www.163.com/",
        "https://www.baidu.com/",
        "http://www.sina.com.cn/",
        "https://www.taobao.com/",
        "https://github.com/"
    ]
    print(multi_thread_get_statuses(websites))
    time_taken = time.time() - start
    print("takes %f seconds" % time_taken)
