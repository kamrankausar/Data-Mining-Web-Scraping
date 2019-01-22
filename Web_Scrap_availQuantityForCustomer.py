#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:16:08 2019

@author: kamran
"""

### Final Script

"""
Created on Mon Jan 21 18:26:29 2019

@author: kamran
Get the URL from ALIExpress and return the number of the Quantity left
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup 
import re
#my_url1 = 'https://www.aliexpress.com/store/product/100-Original-16-Shimano-Casitas-150-151-150hg-151hg-Right-Left-Hand-Baitcasting-Fishing-Reel-4/1053031_32657797704.html?spm=2114.12010608.0.0.22e12d66I7a3Dp'
#my_url = "https://www.aliexpress.com/item/Pioneer-camp-new-thick-warm-sweatshirt-hoodies-men-brand-clothing-solid-hooded-sweatshirt-male-fleece-winter/32956324421.html?spm=2114.search0203.3.3.3f8c41d4sSpBMJ&s=p&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_319_10059_10884_317_10887_10696_100031_321_322_10084_453_10083_454_10103_433_10618_431_10307_537_536,searchweb201603_50,ppcSwitch_0&algo_expid=66f9726c-2223-499b-8c2e-02c7026dac18-0&algo_pvid=66f9726c-2223-499b-8c2e-02c7026dac18&transAbTest=ae803_4"
#my_url = "https://www.aliexpress.com/item/Mr-1991INC-Space-Galaxy-Hoodies-Hooded-Men-Women-Hat-3d-Sweatshirts-Print-Colorful-Nebula-Thin-Autumn/32850938012.html?spm=2114.search0203.3.16.3f8c41d4sSpBMJ&s=p&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_319_10059_10884_317_10887_10696_100031_321_322_10084_453_10083_454_10103_433_10618_431_10307_537_536,searchweb201603_50,ppcSwitch_0&algo_expid=66f9726c-2223-499b-8c2e-02c7026dac18-2&algo_pvid=66f9726c-2223-499b-8c2e-02c7026dac18&transAbTest=ae803_4"
my_url = input('Enter the URL for which you need AvailQuantityForCustomer of the Product: ')
print("\n")
uClient = uReq(my_url)  # bs4 part
page_html = uClient.read()  # bs4 part
uClient.close()  # bs4 part

soup = BeautifulSoup(page_html, "html.parser")  # bs4 part
a_text  = str(soup)
a_list = list(re.findall('[a-zA-Z,0-9]\w+', a_text))  # [] Matches any character inside
avail_quality_pos = [i for i,x in enumerate(a_list) if x == 'availQuantityForCustomer']
avail_quality_pos = int(avail_quality_pos[0])
AvailQuantityForCustomer_pos = avail_quality_pos + 1
#type(AvailQuantityForCustomer_pos)
AvailQuantityForCustomer = a_list[AvailQuantityForCustomer_pos]
print("Getting Quantity...")
print("The number of Quantity left for the product is :", AvailQuantityForCustomer)
print("\n")
