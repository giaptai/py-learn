import random # import new package
import requests
random_num = random.randint(1, 10)

print(random_num)

'''
How to install package, we use Pypi
comment is pip
'''
response = requests.get("https://www.google.com")

print(response)
