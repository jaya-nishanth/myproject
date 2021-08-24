from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import *

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        #Again comments! Again!!
        self.browser.get('http://localhost:8000')

        #Notice whether the browser hear and title says "To-do Lists"
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        """
        #She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            input.get_attribute('placeholder'),
            "Enter a to-do item"
        )

        #She types "Buy Peacock feathers" into a text box
        inputbox.send_keys("Buy Peacock feathers")

        #When she hits enter, the page updates and now the page lists in the todo list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows),
            "New to-do item did not appear in table"
        )
        

        #blah blah
        self.fail("Finish the test!!!")
        """
        #[..rest of comments as before]

if __name__ == "__main__":
    unittest.main(warnings="ignore")
