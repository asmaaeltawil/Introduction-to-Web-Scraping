import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.sultan-center.com/fresh-food.html/fruit-veg.html')

soup = BeautifulSoup(response.text,'html.parser')

products = soup.findAll(class_='item product product-item')

with open('products.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title','image Link','measurement']
    csv_writer.writerow(headers)

    for product in products:
        title = product.find(class_='product-item-link').get_text().replace('\n','')
        image_link = product.find(class_='product-image-wrapper').find('img')['src']
        measurement = product.find(class_='product_measurement').find('span').get_text().replace('\n','')
        csv_writer.writerow([title,image_link,measurement])