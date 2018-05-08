# -*- coding:utf-8 -*-
"""
读取配置，配置文件用yaml，
也可以使用XML,INI等
需在file_reader中添加相应的Reader进行处理
"""
import os
import file_reader
#通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。这种方法可以支持linux和Windows等不同平台os.XXX比+'\\xxx\\ss'这种好的地方即在此处
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'config','config.yml')
DATA_PATH = os.path.join(BASE_PATH,'data')
DRIVER_PATH = os.path.join(BASE_PATH,'drivers')
LOG_PATH = os.path.join(BASE_PATH,'log')
REPORT_PATH = os.path.join(BASE_PATH,'report')
class Config:
    def __init__(self,config=CONFIG_FILE):
        self.config = file_reader.YamlReader(config).data
    def get(self,element,index=0):
        #yaml是可以通过‘---’分节的。用YamlReader读取返回的是一个list，第一项默认的节，如果有多个节，可以传入index来获取。这样我们可以把框架相关配置放在默认节，其他关于项目的配置放在其他节中，可以在框架中实现多个项目测试
        return self.config[index].get(element)

