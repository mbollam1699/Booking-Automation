# This file is going to include method that will parse
# The specific datda that we need from each one of the deal noxes
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BookingReporting:
    def __init__(self,boxes_section_element:WebElement):
        self.boxes_section_element=boxes_section_element
        self.deal_boxes=self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_css_selector(
            '.c82435a4b8.a178069f51.a6ae3c2b40.a18aeea94d.d794b7a0f7.f53e278e95.c6710787a4')

    def pull_data(self):
        collections = []
        for deal_box in self.deal_boxes:
            try:
                hotel_name = deal_box.find_element(By.CSS_SELECTOR, 'div.f6431b446c.a15b38c233').get_attribute(
                    'innerHTML').strip()
            except NoSuchElementException:
                hotel_name = None

            try:
                hotel_price = deal_box.find_element(By.CSS_SELECTOR,
                                                    'span.f6431b446c.fbfd7c1165.e84eb96b1f').get_attribute(
                    'innerHTML').strip()
            except NoSuchElementException:
                hotel_price = None

            try:
                hotel_rating = deal_box.find_element(By.CSS_SELECTOR, 'div.a3b8729ab1.d86cee9b25').get_attribute(
                    'innerHTML').strip()
            except NoSuchElementException:
                hotel_rating = None

            # print(hotel_name, hotel_price, hotel_rating)
            collections.append([hotel_name, hotel_price, hotel_rating])

        return collections



