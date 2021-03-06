import mechanize


class foodPantry:
    def __init__(self, name, url, foodItems):
        self.name = name
        self.url = url
        self.foodItems = str(foodItems)


def writeFoodBanks(br):
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                                    'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("https://www.foodpantries.org/st/new_jersey")
    br.form = list(br.forms())[0]
    br["address"] = "1 Fake Street"
    br["city"] = "New Brunswick"
    controlState = br.form.find_control("state")
    br[controlState.name] = ["nj"]
    response = br.submit()
    with open("foodBanks.txt", "wb") as code:
        code.write(response.read())


def getFoodBankUrls(br):
    file = open("foodBanks.txt", 'r').read().split(" ")
    prefix = "href=\"https://www.foodpantries.org/li/"
    suffix = ">Website</a></span>"
    foodBankUrls = []
    for line in file:
        if line.startswith(prefix) and line.endswith(suffix):
            foodBankUrls.append(line[6:-len(suffix) - 1])
    return getUrls(br, foodBankUrls)


def getUrls(br, foodBankUrls):
    urls = []
    for url in foodBankUrls:
        br.open(url)
        browserData = (str(br.response().read()).split(" "))
        index = browserData.index("target=\"_blank\">Website</a></li>\\r\\n")-1;
        urls.append(browserData[index][6:-1])
    return urls


def writeFoodItems(br, url):
    try:
        br.open(url)
    except:
        return -1
    browserData = (''.join(str(br.response().read()).upper()))
    return foodPantry(br.title(), url, getFoodItems(browserData))


def getFoodItems(browserData):
    commonFoodItems = ['TUNA', 'CEREAL', 'MEAT', 'MACARONI', 'MAC AND CHEESE',
                       'NOODLES', 'PASTA', 'SOUP', 'PEANUT BUTTER', 'JELLY',
                       'FRUIT', 'MILK', 'CANNED', 'CHICKEN', 'JUICE', 'VEGETABLES',
                       'OATMEAL', 'TOMATO SAUCE', 'RICE', 'PUDDING', 'SNACKS',
                       'GRANOLA BARS', 'DRIED FRUIT', 'CRACKERS', 'JELLO',
                       'CONDIMENTS', 'POTATO', 'BEANS']
    foodItems = []
    for item in commonFoodItems:
        if item in browserData:
            foodItems.append(item)
    return foodItems


def main():
    br = mechanize.Browser()
    br.set_handle_robots(False)  # ignore robots
    writeFoodBanks(br)
    foodBankUrls = getFoodBankUrls(br)
    foodPantries = []
    for url in foodBankUrls:
        var = writeFoodItems(br, url)
        if (var != -1):
            foodPantries.append(var)

    # foodPantry items are done
    for var in foodPantries:
        print("Name: " + var.name)
        print("Url: " + var.url)
        print("Food Items: " + var.foodItems, "\n")


main()
