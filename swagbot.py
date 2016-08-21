import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *


class PythonOrgSearch(unittest.TestCase):
    #Implemented ChromeDriver, firefoxdriver is outdated and now called marionettedriver, also known as GeckoDriver
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

    def test_search(self):
        driver = self.driver
        driver.implicitly_wait(10)
        accounts = {'youremail': 'yourpass'}
        for emaila, passw in accounts.items():
            driver.get("http://www.swagbucks.com/p/login")
            driver.maximize_window()
            getemail = driver.find_element_by_name("emailAddress")
            getemail.clear()
            getemail.send_keys(emaila)
            time.sleep(1)
            getpassword = driver.find_element_by_name("password")
            getpassword.clear()
            getpassword.send_keys(passw)
            getpassword.send_keys(Keys.RETURN)
            driver.get("http://www.swagbucks.com/watch/playlists/111/editors-pick")
            while "Swagbucks" in driver.title:
                driver.implicitly_wait(10000)
                driver.switch_to.window(driver.window_handles[0])
                i = 0
                listhead = driver.find_elements_by_xpath(".//*[contains(@id,'sbHomeCard')]")
                for head in listhead:
                    if head != listhead[len(listhead)-1]:
                        i += 1
                        print(str(head.text) + '\n' + "_" * 15)
                        limit = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/main/div[2]/div[1]/section[{}]/span/var".format(i))
                        vidcount = int(limit.text)
                        ActionChains(driver).move_to_element(head).perform()
                        time.sleep(1)
                        driver.find_element_by_xpath("/html/body/aside/article[{}]/ul/li[1]/a".format(i)).send_keys(Keys.CONTROL + Keys.ENTER)
                        ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.TAB).key_up(Keys.CONTROL).perform()
                        driver.switch_to.window(driver.window_handles[1])
                        totalchecks = driver.find_elements_by_class_name('iconCheckmark')
                        if vidcount != len(totalchecks):
                            driver.find_element_by_id('wayToGo') or driver.find_element_by_id('vdb_501707fc-4361-4b38-912e-0df55098fb15') or driver.find_element_by_class_name('ulive-error-container')
                        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
                        time.sleep(3)
                        driver.switch_to.window(driver.window_handles[0])
                        logo = driver.find_element_by_id("sbLogo")
                        ActionChains(driver).move_to_element(logo).perform()
                        time.sleep(3)
                    else:
                        driver.switch_to.window(driver.window_handles[0])
                        listhead.clear()
                        menu = driver.find_elements_by_xpath(".//*[contains(@id,'sbMainNavSectionListItemWatchCategory')]")
                        for category in menu[1::len(menu)-1]:
                            category.click()
                            time.sleep(1)

if __name__ == "__main__":
    unittest.main()
