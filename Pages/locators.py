from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@data-statlog='headline.avatar']")
    ACCOUNT_IFRAME = (By.TAG_NAME, 'iframe')
    DISK_BUTTON = (By.XPATH, "/html/body/div/div/div/div/div[2]/a[4]")
    LOGOUT_BUTTON = (By.XPATH, "//span[text()='Выйти']")


class YandexIDPageLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@data-t='field:input-login']")
    PASSWORD_INPUT = (By.XPATH, "//input[@data-t='field:input-passwd']")
    SING_IN_BUTTON = (By.XPATH, "//button[@data-t='button:action:passp:sign-in']")


def get_folder_locator(folder_name):
    folder = (By.XPATH, ".//*[contains(text(),'" + folder_name + "')]")
    return folder


def get_file_locator(file_name):
    file = (By.XPATH, "//div[@aria-label='" + file_name + ".docx" + "']")
    print(*file)
    return file


class DiskPageLocators:
    CREATE_BUTTON = (By.XPATH, "//span[@class='create-resource-popup-with-anchor']")
    ADD_FOLDER_BUTTON = (By.XPATH, "//span[text()='Папку']")
    FOLDER_NAME_INPUT = (By.XPATH, "//input[@text='Новая папка']")
    SAVE_BUTTON = (By.XPATH,
                   "//button[@class='Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit ']")
    ADD_DOC_FILE_BUTTON = (By.XPATH, "//span[text()='Текстовый документ']")
    FILE_NAME_INPUT = (By.XPATH, "//input[@text='Новый документ']")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@aria-label='Аккаунт']")
