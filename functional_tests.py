from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # convite a inserir novo item na lista
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # digita "Estudar testes funcionais" em uma caixa de texto
        inputbox.send_keys('Estudar testes funcionais')

        # ao apertar ennter, página atualiza, mostrando a lista
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Estudar testes funcionais')

        # ainda existe caixa de texto convidando a adicionar outro item
        # digita "Estudar testes de unidade"
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Estudar testes de unidade')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # a página atualiza novamente, mostrando ambos os itens na lista
        self.check_for_row_in_list_table('1: Estudar testes funcionais')
        self.check_for_row_in_list_table('2: Estudar testes de unidade')

        # verifica se o site gerou uma URL única para a lista

        # visita a URL: a lista TODO ainda está armazenada


if __name__ == "__main__":
    unittest.main()
