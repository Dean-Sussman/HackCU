import mechanize


def writeFoodBanks(br):
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("https://www.foodpantries.org/st/new_jersey")
    print(br.title())
    br.form = list(br.forms())[0]
    br["address"] = "1 Fake Street"
    br["city"] = "New Brunswick"
    controlState = br.form.find_control("state")
    br[controlState.name] = ["nj"]
    response = br.submit()
    with open("foodBanks.txt", "wb") as code:
        code.write(response.read())


def writeFoodItems(br, url, i):
    br.open("url")
    print(br.title())
    response = br.response()
    with open("foodItems" + i + ".txt", "wb") as code:
        code.write(response.read())


def getFoodBanks():
    file = open("foodBanks.txt", 'r').read().split(" ")
    prefix = "href=\"https://www.foodpantries.org/li/"
    suffix = ">Website</a></span>"
    for line in file:
        if line.startswith(prefix) and line.endswith(suffix):
            print(line[len(prefix):-len(suffix)])


def main():
    br = mechanize.Browser()
    br.set_handle_robots(False)  # ignore robots
    writeFoodBanks(br)
    getFoodBanks()

    # writeFoodItems(br, "https://www.foodpantries.org/li/elijahs_promise_08901", '0')
main()
