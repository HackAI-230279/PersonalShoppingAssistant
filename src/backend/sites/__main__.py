import requests
from bs4 import BeautifulSoup
from typing import List

def flipkart(query: str) -> List:
    source = requests.get(f"https://www.flipkart.com/search?q={query}")
    soup = BeautifulSoup(source.content, "html.parser")

    product_json = []
    products = soup.findAll("div", class_="_4rR01T")
    prices = soup.findAll("div", class_="_30jeq3 _1_WHN1")
    ratings = soup.findAll("div", class_="_3LWZlK")
    links = soup.find_all("a", class_="_1fQZEK")

    for i, product in enumerate(products):
        name = product.get_text().strip()
        price = prices[i].get_text().strip()
        price_str = price.replace("₹", "").replace(",", "")
        price_int = int(price_str)

        rating = ratings[i].get_text().strip()
        product_link = "https://www.flipkart.com" + links[i]["href"]
        
        skip = 0
        for i in query.split("+"):
            if i not in name.lower():
                skip = 1
                break
        if skip:
            continue

        product_info = {
            "name": name,
            "price": price_int,
            "rating": rating,
            "link": product_link.split("?")[0],
            "site": "Flipkart",
        }

        product_json.append(product_info)
    
    return product_json


def sorted_results(query: str) -> List:
    res = []
    res += flipkart(query.replace(" ", "+"))[:5]
    
    res = sorted(res, key=lambda x: x["price"])
    return "Here you go!\n"+"\n".join([f"{idx+1}: {val['name'][:70]}... ({val['site']}, Rs. {val['price']})" for idx, val in enumerate(res)]), res