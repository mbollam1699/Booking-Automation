# This file will have logic for filtering bookings
# That wil
from selenium.webdriver.remote.webdriver import WebDriver
class BookingFilteration:

    def __init__(self,driver:WebDriver):
        self.driver=driver


    def apply_rating(self,*star_values):
        rating_element=self.driver.find_element_by_css_selector('div[data-filters-group="review_score"]')
        child_elements=rating_element.find_elements_by_css_selector("*")

        for star_value in star_values:
                for element in child_elements:
                    if (str(element.get_attribute('data-filters-item')) == f'review_score:review_score={star_value}'):
                        # print(" FIltered data-filters-item", str(element.get_attribute('data-filters-item')))
                        element.click()


    def price_sort(self):
        # Clicking on filter button

        filter_click=self.driver.find_element_by_css_selector('button[data-testid="sorters-dropdown-trigger"]')
        filter_click.click()

        price_low_first_element= self.driver.find_element_by_css_selector('button[data-id="price"]')
        price_low_first_element.click()




            # print("data-filters-item",str(element.get_attribute('data-filters-item')))
            # print(f'review_score:review_score={star_value}')



