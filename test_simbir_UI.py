import time
from Pages.main_page import MainPage, generate_folder_name, generate_file_name


def test_new_file_upload(browser):
    link = "https://ya.ru/"
    page = MainPage(browser, link)
    page.open(link)
    time.sleep(5)
    page.user_authorization()
    page.go_to_yadisk_page()
    browser.switch_to.window(browser.window_handles[1])
    folder_name = generate_folder_name()
    page.create_new_disk_folder(folder_name)
    page.open_disk_folder(folder_name)
    file_name = generate_file_name()
    page.create_new_disk_file(file_name)
    browser.switch_to.window(browser.window_handles[1])
    page.check_file(file_name)
    page.user_logout()