#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-28 17:18:45
# @Author  : Jun Jiang (flametest@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import aiohttp
import asyncio
import time


async def async_get_statuses(websites):
    async with aiohttp.ClientSession() as session:
        statuses = {}
        tasks = [get_status(website, session) for website in websites]
        for status in await asyncio.gather(*tasks):
            statuses.setdefault(status, 0)
            statuses[status] += 1
        return statuses


async def get_status(website, session):
    async with session.get(website) as response:
        return response.status


if __name__ == '__main__':
    start = time.time()
    websites = [
        "http://www.163.com/",
        "https://www.baidu.com/",
        "http://www.sina.com.cn/",
        "https://www.taobao.com/",
        "https://github.com/"
    ]
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(async_get_statuses(websites)))
    loop.close()
    time_taken = time.time() - start
    print("takes %f seconds" % time_taken)
