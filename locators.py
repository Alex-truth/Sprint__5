from selenium.webdriver.common.by import By

class Locators:
    LOG_IN_MAIN_PAGE_BUTN = ("//button[text()='Войти в аккаунт']")  # войти в акк на главной
    REGISTRATION_BUTN = ("//a[@class='Auth_link__1fOlj']")  # кнопка Регистрации
    INPUT_NAME = ("//label[text()='Имя' and @class='input__placeholder text noselect text_type_main-default']/following-sibling::input")  # страница регистрации ввoд имени
    INPUT_EMAIL = ("//label[text()='Email']/../input")  # страница регистрации ввод email
    INPUT_PASSWORD = ("//label[text()='Пароль']/../input")  # страница регистрации ввод пароль
    INVALID_PWD_ERR = ("//div[@class='input__container']/p[text()='Некорректный пароль']") # ошибка при некорректном пароле
    INPUT_AUTH_LOGIN = ("//input[@class='text input__textfield text_type_main-default' and @type='text']") # логин авторизация
    INPUT_AUTH_PASS = ("//input[@class='text input__textfield text_type_main-default' and @type='password']") # пароль авторизация
    ENTER_BUTN = ("//button[text()='Войти']") # кнопка Войти
    ORDER_BUTN = ("//button[text()='Оформить заказ']") # кнопка Оформить заказ
    LK_BUTN = ("//a[@href='/account']") # кнопка ЛК
    LOGIN_REG_BUTN = ('//a[@class="Auth_link__1fOlj"]') # кнопка войти в форме регистрации
    RECOVERY_BUTN = ("//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']") # кнопка восстановить пароль
    DESIGNER_BUTN = ("//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(@class, 'AppHeader_header__link_active__1IkJo')]") # кнопка "Конструктор"
    LOGO_BURGERS = ("//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']") # лого Бургерс
    EXIT_LK_BUTN = ("//button[text()='Выход']") # кнопка выход из ЛК
    BREAD_BUTN = ("//div[contains(@class, 'noselect') and contains(., 'Булки')]")  # кнопка Булки
    SAUCE_BUTN = ("//div[contains(@class, 'noselect') and contains(., 'Соусы')]")  # кнопка Соусы
    ACTIVE_CLASS = ("tab_tab_type_current") # класс активного раздела "Кнструктор"
    FILLING_BUTN = ("//div[contains(@class, 'noselect') and contains(., 'Начинки')]")  # кнопка Начинки
