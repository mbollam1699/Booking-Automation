

from booking.booking import Booking
#
# inst=Booking()
# inst.land_first_page()
try:
    with Booking(teardown=False) as bot:
        bot.land_first_page()
        #bot.change_currency(currency="HUF")
        bot.select_place_to_go(input("Where do you want to go ?: "))
        bot.select_dates(checkin_date=input("What's your check-in date(YYYY-MM-DD) : "),
        checkout_date=input("What's your check-out date(YYYY-MM-DD) : "))
        bot.select_adults(count=int(input("How many people ?: ")))
        bot.click_search()
        bot.apply_filterations()
        bot.refresh()
        bot.handle_reporting()

except Exception as e:
    if 'in PATH' in str(e):
        print("Please add to PATH your Selenium Drivers ",
              "Windows :"
              "set PATH=%PATH%;C:path_to_your_folder"
              "Linux:"
              "PATH = $PATH:/path/toYour/folder/"
              )
    else:
        raise



