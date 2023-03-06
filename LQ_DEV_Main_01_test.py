# coding=UTF-8
'''
Created on 2023.01.17
Updated on 2023.01.31
Author: Ken Mok
'''
# -*- coding: utf-8 -*-
import pytest
import os
import yaml
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "\\config\\"

class TestMainScreenClick:

    @pytest.mark.group2
    @pytest.mark.group1
    def test_football_click(self, setup_method):

        conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
        desired_caps={}
        desired_caps = setup_method
        self.driver = webdriver.Remote(conf['driver'], desired_caps)
        
        time.sleep(2)

        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='足球']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='篮球']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='主播']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='微头条']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='视频']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='锦囊']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='活动']]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
        time.sleep(2)
        '''
        # All of the latest Ace
        #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[1]")))
        self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[1]").click()

        # Click 推荐 to go back to Home
        #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]")))
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='推荐']]").click()
        time.sleep(2)

        # All of the Hot Live
        #WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,"((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[2]")))
        self.driver.find_element_by_xpath("((//*[@class='android.view.ViewGroup' and ./parent::*[@class='android.widget.ScrollView']]/*[@class='android.view.ViewGroup'])[2]/*/*[@text='全部'])[2]").click()
        time.sleep(4)

        # Click Back icon to go back to Home
        #WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@text='󰅁']")))
        self.driver.find_element_by_xpath("//*[@text='󰅁']").click()
        time.sleep(2)
        '''
        self.driver.quit()

    @pytest.mark.group2
    def test_initial_login(self, setup_method):

        conf = yaml.load(open(CONF_PATH + 'config.yml'), Loader=yaml.FullLoader)
        desired_caps={}
        desired_caps = setup_method
        self.driver = webdriver.Remote(conf['driver'], desired_caps)
        
        time.sleep(2)

        testdata = yaml.load(open(CONF_PATH + 'test_data.yml', encoding="utf-8"), Loader=yaml.FullLoader)
        login_member = testdata['login_dev_normal_user_02']
        login_member_username = login_member['username']
        login_member_password = login_member['pwd']

        self.driver.find_element_by_xpath("//*[@contentDescription='我的, tab, 4 of 4']").click()
        time.sleep(2)

        ## Click 登录 button
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='登录']]").click()
        time.sleep(2)

        ## Click 密码登录 button
        self.driver.find_element_by_link_text("密码登录").click()
        time.sleep(2)

        ## Input username
        self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.EditText").click()
        time.sleep(2)
        self.driver.execute_script("seetest:client.sendText(\""+ login_member_username +"\")")
        time.sleep(2)

        ## Input password
        self.driver.find_element_by_xpath("//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.EditText").click()
        time.sleep(2)
        self.driver.execute_script("seetest:client.sendText(\""+ login_member_password +"\")")
        time.sleep(2)

        ## Click Log-in key
        self.driver.find_element_by_xpath("//*[@class='android.view.ViewGroup' and ./*[@text='登录']]").click()

        self.driver.quit()

    @pytest.mark.group1
    def test_error_phone_shorter(self):
        print("\nhello01")
        print("hello02")
        print("hello03")
        print("hello04")
        print("hello05")
        print("hello06")
        assert 1 == 1

    @pytest.mark.group1
    def test_error_write_verification_code(self):
        assert 1 == 1

    @pytest.mark.group2
    def test_error_phone_format(self):
        assert 3 == 3

    @pytest.mark.xfail
    def test_fail(self):
        assert 1 == 2, "This should fail"

    def tearDown_method(self):
        self.driver.quit()