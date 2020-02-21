import time
import sys
import threading

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class CourseSelect(object):
    def __init__(
        self,
        driver_path: str = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe",
    ):
        option = webdriver.ChromeOptions()
        option.add_argument(
            r"user-data-dir=C:\Users\yulin\AppData\Local\Google\Chrome\User Data"
        )
        # option.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.browser = webdriver.Chrome(driver_path, options=option)

    def selectCourse(self, *, course_nums):
        browser = self.browser
        browser.get("http://yjsjy.uestc.edu.cn/pyxx/pygl/pyjhxk/wsxk")
        browser.switch_to.frame(
            browser.find_element_by_xpath('//iframe[@id="allSubjectIframe"]')
        )
        for course_num in course_nums:
            xpath = "//*[text()='{}']".format(course_num)
            try:
                course = browser.find_element_by_xpath(xpath).find_element_by_xpath(
                    ".."
                )
                course_btn = course.find_element_by_xpath(".//a[@id='jhnxkBtn']")
                course_btn.click()
                time.sleep(1)
                browser.switch_to.alert.accept()
            except Exception:
                print(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                    "无人退课",
                )


if __name__ == "__main__":
    xk = CourseSelect()
    while True:
        xk.selectCourse(course_nums=["0808126006", "0808126007"])
        time.sleep(3)
