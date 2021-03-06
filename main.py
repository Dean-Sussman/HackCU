import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open("https://www.foodpantries.org/st/new_jersey")
# print(response.read())      # the text of the page
print(br.title())
br.form = list(br.forms())[0]
br["address"] = "1 Fake Street"
br["city"] = "New Brunswick"
controlState = br.form.find_control("state")
br[controlState.name] = ["nj"]
response = br.submit()
# print(response.read())
with open("temp.txt", "wb") as code:
    code.write(response.read())

    #TO-DO: Extract food pantry websites (3 max.)
    #Navigate to those websites
    #Get food items
        # Or statement for what to look for when web-scraping (Items in need, donate food, etc.)
        # Take items in list and add them to our website!