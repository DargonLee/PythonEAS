# -*- coding: utf-8 -*-

"""
@author: harlan
@software: PyCharm
@file: loging.py
@time: 2023/2/16 11:33
"""

# import logging
# from logging import config


import logging.config
from conf import settings

logging.config.dictConfig(settings.LOGGING_DIC)
logger1 = logging.getLogger('logger2')

logger1.debug('调试日志')
logger1.info('消息日志')
logger1.warning('警告日志')
logger1.error('错误日志')
logger1.critical('严重错误日志')
