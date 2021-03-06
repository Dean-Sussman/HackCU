import requests
# import ast
# import time
# from bs4 import BeautifulSoup

link = "https://www.feedingamerica.org/find-your-local-foodbank"
f = requests.get(link)
print(f.text)

# response = requests.get("https://www.feedingamerica.org/find-your-local-foodbank")
# if ((response.status_code == 200) or (response.status_code == 304)):
#     print('Successful response from server')
# else:
# 	print("Bad response from server")
# print("")
# print(response.text);
