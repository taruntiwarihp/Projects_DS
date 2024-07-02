import requests, re
from bs4 import BeautifulSoup 
from os.path  import basename

# PRODUCT LIST DETAILS
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 
URL = "https://d9creation.com/product-category/affordable-earrings-under-%e2%82%b950/" 
product_pages_link = []

while True:
    try:
        r = requests.get(URL, headers=headers) 
        soup = BeautifulSoup(r.content, 'html5lib') 
        price_cells = soup.findAll('a', {'class': 'next page-number'})
        product_pages_link.append(URL)
        URL = price_cells[0].get('href')

    except:
        break

# print(product_pages_link)
product_lnk = []
for single_page in product_pages_link:

    r = requests.get(single_page, headers=headers) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    for link in soup.find_all('a',  
                            attrs={'href': re.compile("^https://")}): 
        # display the actual urls 
        if '/product/' in link.get('href'):
            product_lnk.append(link.get('href'))  

all_product_links = list(set(product_lnk))


data_list = []
for prod_lnk  in all_product_links:

    r = requests.get(prod_lnk, headers=headers) 
    soup = BeautifulSoup(r.content, 'html5lib')
    data_dick = {}
    # PRODUCT DETAILS
    price_cells = soup.findAll('div', {'class': 'product-info summary col-fit col entry-summary product-summary text-left form-flat'})
    texts = []
    for price_cell in price_cells:
        if price_cell.text:
            item = price_cell.text
            # Split based on \n and \t
            split_items = re.split(r'[\n\t]+', item)
            try:
                data_dick['RAW'] = split_items
                data_dick['Link'] = prod_lnk
                data_dick['Product_Title'] = split_items[1].strip()
                if split_items[2][0] == '₹':
                    data_dick['Price'] = split_items[2].split(' ')[0].split('.')[0].strip()
                    data_dick['Stock'] = split_items[2].split(' ')[0].split('.00')[1].strip()
                    data_dick['Metal'] = split_items[4].split(':')[2].replace('Chain', '').replace('Polish', '').strip()
                    data_dick['Type'] = split_items[4].split(':')[3].replace('Weight', '').strip()
                else:
                    data_dick['Price'] = split_items[3].split(' ')[0].split('.')[0].strip()
                    data_dick['Stock'] = split_items[3].split(' ')[0].split('.00')[1].strip()
                    data_dick['Metal'] = split_items[5].split(':')[2].replace('Chain', '').replace('Polish', '').strip()
                    data_dick['Type'] = split_items[5].split(':')[3].replace('Weight', '').strip()
            except:
                print(prod_lnk)
                # https://d9creation.com/product/silver-look-bangle-openable-kada-oxidized/

    # PRODUCT DISCRIPTION
    price_cells = soup.findAll('div', {'class': 'woocommerce-Tabs-panel woocommerce-Tabs-panel--description panel entry-content active'})
    texts = []
    for price_cell in price_cells:
        if price_cell.text:
            data_dick['Discription'] = price_cell.text

    # PRODUCT IMAGE
    data_dick['img_path'] = []
    c = 0
    for link in soup.find_all('a',  
                            attrs={'href': re.compile("^https://")}): 
        # display the actual urls 
        if link.get('href')[-3:] == 'jpg':
            lnk = link.get('href')  
            c += 1
            file_name = f"images/{data_dick['Product_Title'].replace(' ','')}_{c}.jpg"
            data_dick['img_path'].append(file_name)
            with open(file_name, 'wb') as f:
                f.write(requests.get(lnk).content)

    data_list.append(data_dick)


from pprint import pprint 
print(len(data_list))
import pandas as pd
df = pd.DataFrame.from_records(data_list,) 
print(df.head())
df.to_csv("data.csv", index=False)