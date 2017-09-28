#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 16:26:17
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$


import time
import multiprocessing
import requests
from collections import Counter


def multi_process_get_statuses(websites):
    statuses = Counter({})
    with multiprocessing.Pool(processes=5) as pool:
        for website in websites:
            try:
                res = pool.apply_async(get_status, args=(website, ),)
                status = res.get(timeout=10)
                statuses += Counter(status)
            except multiprocessing.TimeoutError:
                print("timeout error, website: %s" % website)
        pool.close()
        pool.join()
    return dict(statuses)


def get_status(website):
    statuses = {}
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
    print(multi_process_get_statuses(websites))
    time_taken = time.time() - start
    print("takes %f seconds" % time_taken)
