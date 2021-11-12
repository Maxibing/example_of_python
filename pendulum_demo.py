#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description     :Usage of pendulum
@Date     :2021/11/12 07:46:21
@Author      :xbMa
'''

import pendulum

from datetime import datetime

# 1.获取当前时刻、今天、明天、昨天
print(f"pendulum.now(): {pendulum.now()}")
print(f"pendulum.today(): {pendulum.today()}")
print(f"pendulum.tomorrow(): {pendulum.tomorrow()}")
print(f"pendulum.yesterday(): {pendulum.yesterday()}")

# 2.字符转换
print(f"pendulum.now().to_datetime_string(): {pendulum.now().to_datetime_string()}")
print(f"pendulum.now().to_date_string(): {pendulum.now().to_date_string()}")
print(f"pendulum.now().to_time_string(): {pendulum.now().to_time_string()}")
print(f"pendulum.now().format(\"%Y-%m-%D\"): {pendulum.now().format('Y-m-D')}")

# 3.类型测试
print(f"isinstance(pendulum.datetime(2015, 3, 5), datetime) : {isinstance(pendulum.datetime(2015, 3, 5), datetime)}")

# 4.解析规范时间
print(f"pendulum.parse('2019-12-12'): {pendulum.parse('2019-12-12')}")

# 5.属性
print(f"pendulum.now().year: {pendulum.now().year}")
print(f"pendulum.now().month: {pendulum.now().month}")
print(f"pendulum.now().day: {pendulum.now().day}")
print(f"pendulum.now().hour: {pendulum.now().hour}")
print(f"pendulum.now().second: {pendulum.now().second}")

# 6.时间加减
print(f"pendulum.now().add(years=1): {pendulum.now().add(years=1)}")
print(f"pendulum.now().subtract(years=1): {pendulum.now().subtract(years=1)}")

# 7.时间跨度计算
print(f"pendulum.now().diff(pendulum.now().add(years=1)).in_years(): {pendulum.now().diff(pendulum.now().add(years=1)).in_years()}")
print(f"pendulum.now().diff(pendulum.now().add(years=1)).in_seconds(): {pendulum.now().diff(pendulum.now().add(years=1)).in_seconds()}")

# 8.设置语言地区
pendulum.set_locale("en")
print(f'pendulum.set_locale("en")')
print(f"pendulum.now().subtract(days=1).diff_for_humans(): {pendulum.now().subtract(days=1).diff_for_humans()}")
pendulum.set_locale("zh")
print(f'pendulum.set_locale("zh")')
print(f"pendulum.now().subtract(hours=1).diff_for_humans(): {pendulum.now().subtract(hours=1).diff_for_humans()}")

# 9.生成时间序列
periods = pendulum.period(pendulum.now(), pendulum.now().add(days=3))
print(f"periods = pendulum.period(pendulum.now(), pendulum.now().add(days=3))")
print('for dt in  periods.range("days"):')
print('    print(dt)')
for dt in  periods.range("days"):
    print(dt)

# 10.获取本周的周一和周日
print(f"pendulum.now().to_date_string(): {pendulum.now().to_date_string()}")
print(f"pendulum.now().to_date_string(): {pendulum.now().to_date_string()}")
print(f"pendulum.now().start_of('week').to_date_string(): {pendulum.now().start_of('week').to_date_string()}")
print(f"pendulum.now().end_of('week').to_date_string(): {pendulum.now().end_of('week').to_date_string()}")