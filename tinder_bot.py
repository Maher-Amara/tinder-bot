from selenium import webdriver
from time import sleep


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://tinder.com')
        sleep(2)

    def login(self):
        # login_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        # login_btn.click()
        # sleep(2)
        #
        # fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        # fb_btn.click()
        # sleep(2)
        #
        # base_window = self.driver.window_handles[0]
        # self.driver.switch_to.window(self.driver.window_handles[1])
        #
        #
        # email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        # email_in.send_keys('maheramara32@yahoo.fr')
        #
        # pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        # pw_in.send_keys('GoToHellMariem9800')
        #
        # login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        # login_btn.click()
        #
        #
        # self.driver.switch_to.window(base_window)
        input("continue login then press a key")
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')  # not sure
        dislike_btn.click()

    def close_popup1(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')  # super like popup
        popup_3.click()

    def close_popup2(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')  # super like popup
        popup_4.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')  # not sure
        match_popup.click()

    def auto_swipe(self):
        input("press a key when ready to swipe")
        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup1()
                except Exception:
                    try:
                        self.close_popup2()
                    except Exception:
                        try:
                            self.close_match()
                        except Exception:
                            sleep(3)


bot = TinderBot()
bot.login()
bot.auto_swipe()
