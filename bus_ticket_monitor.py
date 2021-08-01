# -*- coding: utf-8 -*-

# libraries
from bs4 import BeautifulSoup 
from datetime import datetime
import re
import json
import pandas as pd
import requests
import warnings
warnings.filterwarnings("ignore")

# generate range of date to consult - 32 days starting from today
date_range = pd.date_range(pd.datetime.now(), periods=2).strftime( '%Y-%m-%d' ).tolist()

# website path format: https://www.clickbus.com.br/onibus/porto-alegre-rs-todos/ijui-rs?departureDate=2021-08-01
# parameters
root = 'https://www.clickbus.com.br/'
vehicle = 'onibus'
origin = 'porto-alegre-rs-todos'
destinations = ['ijui-rs']

df_final = pd.DataFrame()
for destination in destinations:

    for date in date_range:
        # website address
        web_address = root+vehicle+'/'+origin +'/'+destination+'?departureDate='+date 

        print( web_address )

        # access the link
        response = requests.get(web_address, headers=headers)
        conteudo = response.json()
        print(conteudo)
        page = response.text
        print(response.text)
        soup = BeautifulSoup(page, "html.parser")
        print(soup)

        # get bus lines information & seats available
        date_now = datetime.now().strftime( '%Y-%m-%dT%H:%M:%S' )
        seats = soup.find_all(class_='available-seats' ) 
        print(seats)
        buslines = soup.find_all(class_="search-item search-item-direct " )

        # iterate over bus lines information and seats available
        data_list = list()
        for busline, seat in zip( buslines, seats ):
            data = json.loads( busline['data-content'] )['trips'][0]
            data_dict = { 'departureTime': data['departureTime'], 
                          'company': data['companySlug'], 
                          'arrivalDate': data['arrivalDate'], 
                          'arrivalStation': data['arrivalStation'], 
                          'departureStation': data['departureStation'],
                          'arrivalTime': data['arrivalTime'],
                          'departureDate': data['departureDate'], 
                          'durationTime': data['durationTime'], 
                          'seats_available': int( re.findall( r'\d+', seat.get_text() )[0] ), 
                          'price': data['price'],
                          'timestampScrape': date_now }
            data_list.append( data_dict )

        df = pd.DataFrame( data_list, columns=['departureDate', 'arrivalDate', 'departureStation', 'arrivalStation', 'departureTime', 'arrivalTime', 
                                               'durationTime', 'company', 'price', 'seats_available', 'timestampScrape'] )

    df_final = pd.concat( [df_final, df] )
    
    
# save the dataset as a csv file
#df_final.to_csv( 'buslines-at-{}.csv'.format( re.sub( r':', '-', date_now ) ) )

#https://forum.jornalismodedados.org/t/como-raspar-dados-de-uma-consulta-ajax-usando-python/296/2
