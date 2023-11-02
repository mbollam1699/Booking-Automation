from selenium import webdriver
import os
import booking.constants as const
from booking.Booking_Filteration import BookingFilteration
from booking.Booking_reporting import BookingReporting
# from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\mveen\Downloads\chromedriver-win32 (1)\chromedriver-win32\chromedriver.exe",teardown=True):
        self.teardown=teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])

        super(Booking, self).__init__(executable_path=driver_path,options=options)
        self.implicitly_wait(15)
        self.maximize_window()


    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency=None):
        currency_element=self.find_element_by_css_selector(
            'button[aria-label="Prices in U.S. Dollar"]'
        )
        currency_element.click()
        self.implicitly_wait(50)
        # The below code checks for a div that has text=currency & clicks it.Instead of div we can also use span.
        selected_currency_element = self.find_element_by_xpath(f'//div[text()="{currency}"]')
        # selected_currency_element=self.find_element_by_css_selector(
        #     'a[data-modal-header-async-url-param*="selected_currency=USD"]'
        # )
        selected_currency_element.click()

    def select_place_to_go(self,place_to_go):
        search_field= self.find_element_by_id(':re:')
        search_field.clear()
        search_field.send_keys(place_to_go)
        first_result=self.find_element_by_xpath(f'//div[text()="{place_to_go}"]')
        first_result.click()

    def select_dates(self,checkin_date,checkout_date):
        check_in_element=self.find_element_by_css_selector(
            f'span[data-date="{checkin_date}"]'
        )
        check_in_element.click()

        check_out_element=self.find_element_by_css_selector(
            f'span[data-date="{checkout_date}"]'
        )
        check_out_element.click()


    def select_adults(self,count):
        select_adults_element= self.find_element_by_css_selector('button[data-testid="occupancy-config"]')
        select_adults_element.click()

        button = self.find_element_by_css_selector(
            "button.a83ed08757.c21c56c305.f38b6daa18.d691166b09.ab98298258.deab83296e.bb803d8689.e91c91fa93")

        while True:
            button.click()
            span_count=self.find_element_by_css_selector('span[class="d723d73d5f"]')
            adults_value=span_count.text
            #print(adults_value)
            if int(adults_value)==1:
                break
        increase_button_element=self.find_element_by_css_selector('button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a"]')

        for _ in range(count-1):
            increase_button_element.click()

    def click_search(self):
        search_button_element=self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button_element.click()


    def apply_filterations(self):
        filteration= BookingFilteration(driver=self)
        filteration.apply_rating(70,80)
        filteration.price_sort()


    def handle_reporting(self):
        cards_found=self.find_element_by_css_selector('div[class="d4924c9e74"]')
        reporting = BookingReporting(cards_found)
        # table=PrettyTable(
        #     field_names= ["Hotel Name","Hotel Ptice","Hotel Score"]
        # )
        # table.add_rows(reporting.pull_data())
        # print(table)
        print(reporting.pull_data())






    # CONTEXT MANAGERS
    # The below context manager executes once the code in the main.py, with method is completed

    def __exit__(self, exc_type, exc_val, exc_tb):
        if(self.teardown):
            self.quit()

inst = Booking()
