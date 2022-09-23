import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from random import random
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver.v2 as uc

from SeleniumDTO import SeleniumDTO
from TargetDTO import TargetDTO


# Accept A SeleniumDTO object and an array of TargetDTO objects

class SeleniumAction:
    def __init__(self, selenium_dto: SeleniumDTO, target_dto_list: List[TargetDTO]):
        self.selenium_dto = selenium_dto
        self.target_dto_list = target_dto_list

    def run(self):
        options = uc.ChromeOptions()

        for argument in self.selenium_dto.arguments:
            options.add_argument(argument)

        driver = uc.Chrome(options=options)

        for target_dto in self.target_dto_list:

            if target_dto.wait_for_xpath_element is None:
                driver.implicitly_wait(target_dto.timeout)

            driver.get(target_dto.url)

            if target_dto.wait_for_xpath_element is not None:
                WebDriverWait(driver, target_dto.timeout).until(
                    EC.presence_of_element_located((By.XPATH, target_dto.wait_for_xpath_element))
                )

            if self.selenium_dto.fullscreen:
                s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
                driver.set_window_size(s('Width'), s('Height'))
                driver.save_screenshot(target_dto.screenshot_filename)
            else:
                driver.save_screenshot(target_dto.screenshot_filename)

            with open(target_dto.html_output_filename, "w") as f:
                f.write(driver.page_source)
