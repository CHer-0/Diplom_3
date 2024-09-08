import allure


# класс с автотестом
class TestResetPass:

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_eye_button(self, reset_pass_page):
        reset_pass_page.prepare_reset_pass()
        type_start = reset_pass_page.type_pass()
        reset_pass_page.set_new_pass()
        reset_pass_page.click_eye()
        type_end = reset_pass_page.type_pass()

        assert type_start == 'password' and type_end == 'text', f'type_start = {type_start}, type_end = {type_end}'
