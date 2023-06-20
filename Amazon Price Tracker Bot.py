import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.amazon.ca/Cuckoo-Electric-Heating-Pressure-CRP-P1009SB/dp/B00XQEM2E4/'
header = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-language': 'en-US,en;q=0.9,fr-CA;q=0.8,fr;q=0.7'
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'lxml')

price = soup.find(class_="a-offscreen").get_text()
price = price.split('$')[1]
price = float(price)
print(price)

#From here We will set up the code to send an email to myself when the price is below target_price
import smtplib
email = "mtlplants@gmail.com"
title = soup.find(id="productTitle").get_text().strip()
print(title)
target_price = 430

if price <= target_price:
    message = f'the product:{title}. Is now below the set target price of $430!'

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(email, 'password')
        connection.sendmail(
            from_addr= email,
            to_addrs= email,
            msg= f'Subject: Amazon Price Alert!\n\n{message}\n{url}'.encode("utf-8")
        )
        #connection.close(),
        #this command usually goes after using the code to close the connection, but it's
        #not necessary in this occasion because I used the "with ... as connection" trick. Which will close
        #the connection automatically.


#Here obviously is not going to work because that is not my actual password, but also because gmail has increased their
#security since May 20th 2022, and stopped access of weak third-party apps. So now apparently the solution is to make an
#app-password and I believe they're only a one-use. For my gmail I cannot use an app-password, because I have enabled
#advanced protection program, and it's quite a hassle to deactivate it. So I will leave this project here.

#Short reminder of the With-Statement:
#The with statement is a replacement for commonly used try/finally error-handling statements. EXAMPLE:
with open("example.txt", "w") as file:
    file.write("Hello World!")
#This replaced the outdated try/finally statements:
f = open("example.txt", "w")

try:
    f.write("hello world")
finally:
    f.close()
