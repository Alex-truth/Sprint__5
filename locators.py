from selenium.webdriver.common.by import By

class Locators:
    LOG_IN_MAIN_PAGE_BUTN = ("//*[@id='root']/div/main/section[2]/div/button")  # войти в акк на главной
    REGISTRATION_BUTN = ('//*[@id="root"]/div/main/div/form/button')  # кнопка Регистрации
    INPUT_NAME = ("//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")  # страница регистрации ввoд имени
    INPUT_EMAIL = ("//label[text()='Email']/../input")  # страница регистрации ввод email
    INPUT_PASSWORD = ("//label[text()='Пароль']/../input")  # страница регистрации ввод пароль
    INVALID_PWD_ERR = ("//div[@class='input__container']/p[text()='Некорректный пароль']")
    INPUT_AUTH_LOGIN = ('//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input') # логин авторизация
    INPUT_AUTH_PASS = ("*//form/fieldset[2]/div/div/input") # пароль авторизация
    ENTER_BUTN = ("//button[text()='Войти']") # кнопка Войти
    ORDER_BUTN = ("//button[text()='Оформить заказ']") # кнопка Оформить заказ
    LK_BUTN = ("//*[@id='root']/div/header/nav/a/p") # кнопка лк
    LOGIN_REG_BUTN = ('//*[@id="root"]/div/main/div/div/p/a') # кнопка войти в форме регистрации
    RECOVERY_BUTN = ('//*[@id="root"]/div/main/div/div/p[2]/a') # кнопка забыли пароль
    DESIGNER_BUTN = ('//*[@id="root"]/div/header/nav/ul/li[1]/a/p') # кнопка "Конструктор"
    LOGO_BURGERS = ('//*[@id="root"]/div/header/nav/div/a') # лого Бургерс
    EXIT_LK_BUTN = ('//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    BREAD_BUTN = ("//div[contains(@class, 'noselect') and contains(., 'Булки')]")  # кнопка Булки
    SAUCE_BUTN = ("//div[contains(@class, 'noselect') and contains(., 'Соусы')]")  # кнопка Соусы
    ACTIVE_CLASS = ("tab_tab_type_current") # класс активного раздела "Кнструктор"
    FILLING_BUTN = ("//div[contains(@class, 'noselect') and contains(., 'Начинки')]")  # кнопка Начинки
