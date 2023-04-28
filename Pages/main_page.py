import time

from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import MainPageLocators, YandexIDPageLocators, DiskPageLocators, get_folder_locator, get_file_locator
from faker import Faker


def generate_folder_name():
    fake = Faker()
    new_folder_name = fake.bothify(text='Folder:????-########', letters='ABCDE')
    return new_folder_name


def generate_file_name():
    fake = Faker()
    new_file_name = fake.bothify(text='File:????-########', letters='ABCDE')
    print(new_file_name)
    return new_file_name


class MainPage(BasePage):
    def user_authorization(self):
        login_button = self.browser.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()
        login_input = self.browser.find_element(*YandexIDPageLocators.LOGIN_INPUT)
        login_input.send_keys("Simbirtest2704")
        sing_in_button = self.browser.find_element(*YandexIDPageLocators.SING_IN_BUTTON)
        sing_in_button.click()
        time.sleep(2)
        password_input = self.browser.find_element(*YandexIDPageLocators.PASSWORD_INPUT)
        password_input.send_keys("Simbirtest270423")
        sing_in_button = self.browser.find_element(*YandexIDPageLocators.SING_IN_BUTTON)
        sing_in_button.click()
        time.sleep(5)

    def go_to_yadisk_page(self):
        time.sleep(2)
        account_button = self.browser.find_element(*MainPageLocators.ACCOUNT_BUTTON)
        account_button.click()
        time.sleep(2)
        iframe = self.browser.find_element(*MainPageLocators.ACCOUNT_IFRAME)
        self.browser.switch_to.frame(iframe)
        disk_button = self.browser.find_element(*MainPageLocators.DISK_BUTTON)
        disk_button.click()
        self.browser.switch_to.default_content()
        time.sleep(3)

    def create_new_disk_folder(self, folder_name):
        create_button = self.browser.find_element(*DiskPageLocators.CREATE_BUTTON)
        create_button.click()
        add_folder_button = self.browser.find_element(*DiskPageLocators.ADD_FOLDER_BUTTON)
        add_folder_button.click()
        folder_name_input = self.browser.find_element(*DiskPageLocators.FOLDER_NAME_INPUT)
        folder_name_input.send_keys(Keys.CONTROL, 'a')
        folder_name_input.send_keys(Keys.BACKSPACE)
        folder_name_input.send_keys(folder_name)
        submit_button = self.browser.find_element(*DiskPageLocators.SAVE_BUTTON)
        submit_button.click()
        time.sleep(3)

    def create_new_disk_file(self, file_name):
        create_button = self.browser.find_element(*DiskPageLocators.CREATE_BUTTON)
        create_button.click()
        add_doc_file_button = self.browser.find_element(*DiskPageLocators.ADD_DOC_FILE_BUTTON)
        add_doc_file_button.click()
        file_name_input = self.browser.find_element(*DiskPageLocators.FILE_NAME_INPUT)
        file_name_input.send_keys(Keys.CONTROL, 'a')
        file_name_input.send_keys(Keys.BACKSPACE)
        file_name_input.send_keys(file_name)
        submit_button = self.browser.find_element(*DiskPageLocators.SAVE_BUTTON)
        submit_button.click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[2])
        self.browser.close()

    def open_disk_folder(self, folder_name):
        folder = self.browser.find_element(*get_folder_locator(folder_name))
        folder.click()

    def check_file(self, file_name):
        assert self.is_element_present(*get_file_locator(file_name)), "File not found"

    def user_logout(self):
        account_button = self.browser.find_element(*DiskPageLocators.ACCOUNT_BUTTON)
        account_button.click()
        logout_button = self.browser.find_element(*MainPageLocators.LOGOUT_BUTTON)
        logout_button.click()