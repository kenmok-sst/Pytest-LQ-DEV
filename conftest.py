# coding=UTF-8
'''
Created on 2023.01.19
Updated on 2023.01.19
Author: Ken Mok
'''
# -*- coding: utf-8 -*-

import pytest
import os
import yaml
from appium import webdriver

CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\config\\"

@pytest.fixture
def input_value():
   input = 39
   return input

@pytest.fixture
def setup_method():

   conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
   desired_caps={}
   desired_caps['platformName'] = conf['platformName']
   desired_caps['platformVersion'] = conf['platformVersion']
   desired_caps['deviceName'] = conf['deviceName']
   desired_caps['udid'] = conf['udid']
   desired_caps['appPackage'] = conf['appPackage']
   desired_caps['appActivity'] = conf['appActivity']
   desired_caps['unicodeKeyboard'] = conf['unicodeKeyboard']
   desired_caps['resetKeyboard'] = conf['resetKeyboard']
   desired_caps['noReset'] = conf['noReset']
   desired_caps['newSessionWaitTimeout'] = conf['newSessionWaitTimeout']
   desired_caps['newCommandTimeout'] = conf['newCommandTimeout']
   desired_caps['endSessionWaitTimeout'] = conf['endSessionWaitTimeout']
   return desired_caps

        


