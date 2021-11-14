"""Import Libraries in first place"""
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import timeit



start = 421
end = 451


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def verification_get(soupy_object):
    """
    return whether property has verified or not
    :param soupy_object: sopu_object
    :return: string (Verified / None)
    """
    try:
        a = (soupy_object.find('div', attrs={
            'class': "component__label component__Verified component__pdFixWidth component__verifiedInfoTag"}).text)
    except:
        a = (None)
    return a

def bedroom_count(soupy_object):
    """
    return number of bedrooms inside room
    :param soupy_object: Soup object
    :return: number if bedrooms (int)
    """

    try:
        bedroom = (soupy_object.find('span', attrs={"id": "bedRoomNum"}).text.split(' ')[0])
    except:
        bedroom = None
    return bedroom

def bathroom_count(soupy_object):
    """
    return bathrooms count
    :param soupy_object: Soup Object
    :return: int
    """
    try:
        bathroom =  soupy_object.find('span', attrs= {'id':'bathroomNum'}).text.split(' ')[0]
    except:
        bathroom = None
    return bathroom

def balcany_count(soupy_object):
    """
    return balcany count
    :param soupy_object: Soup Object
    :return: int
    """
    try:
        balcany =  soupy_object.find('span', attrs= {'id':'balconyNum'}).text.split(' ')[0]
    except:
        balcany = 0
    return balcany

def additional_rooms(soupy_object):
    """
    return balcany count
    :param soupy_object: Soup Object
    :return: int
    """
    try:
        otr_rooms =  soupy_object.find('span', attrs= {'id':'additionalRooms'}).text
    except:
        otr_rooms = 'Not given'
    return otr_rooms

def rent_amt(soupy_object):
    try:
        rent = soupy_object.find('span', attrs = {'id':"pdPrice2"}).text
    except:
        rent = None
    return rent

def brokarge_amt(soupy_object):
    """
    return brokarage acmout
    :param soupy_object: soup object
    :return: int
    """
    try:
        brokarage = soupy_object.find('div', attrs = {'class':'component__tableTooltip'}).text
    except :
        brokarage =  None
    return brokarage

def built_area(soupy_object):
    """
    return area parameters
    :param soupy_object: soup object
    :return: int
    """
    try:
        built_area = soupy_object.find('div', attrs = {'id':'factArea'}).text
    except:
        built_area = "None"

    return (built_area )

def furnishing(soupy_object):
    """
    return furnishing style
    :param soupy_object:  soup object
    :return: str
    """
    try:
        furnishing_type = soupy_object.find('span', attrs=  {'id':'furnishingLabel'}).text
    except:
        furnishing_type = None
    return  furnishing_type

def availability_label(soupy_object):
    """
    return flat availbality for family, couple, students,Bachelors, all.
    :param soupy_object: soup object
    :return: values
    """
    try:
        availability = soupy_object.find('span', attrs = {'id':'availableForLabel'}).text
    except:
        availability = 'None'
    return availability

def facility_major(soupy_object):
    """
    return major facility why ou want to stay at room
    :param soupy_object: soup object
    :return: list
    """
    try:
        facility = soupy_object.find('div', attrs = {"class":"reasonToBuy__pd_hghlgtProp"})
    except:
        facility = None
    return  facility

def address(soupy_object):
    """
    return address of house
    :param soupy_object: soup object
    :return: string
    """
    try:
        address_list = soupy_object.find('span', attrs = {'class':'component__pdPropAddress'}).text

    except:
        address_list =None
    return address_list

def floor_num(soupy_object):
    """
    return number of floor
    :param soupy_object: soup object
    :return: dirction string
    """
    try:
        floornum = soupy_object.find('span', attrs = {'id':'Floor_Num_Label'}).text
    except:
        floornum = None
    return floornum

def facing(soupy_object):
    """
    return dir of face of door
    :param soupy_object: soup object
    :return: floor number string
    """
    try:
        direction = soupy_object.find('span', attrs = {'id':'Facing_Label'}).text
    except:
        direction = None
    return direction

def flooring(soupy_object):
    """
    return the type of flooring
    :param soupy_object: soup objecct
    :return: direction string
    """
    try:
        flooring_type = soupy_object.find('span', attrs ={'id':'Flooring_Label'}).text
    except:
        flooring_type =None
    return flooring_type

def gated_community(soupy_object):
    """
    gate facility
    :param soupy_object: soup
    :return: string
    """
    try:
        gate = soupy_object.find('span', attrs ={'id':'Gated_community'}).text
    except:
        gate = None
    return gate

def corner_property(soupy_object):
    """
    return yes or no
    :param soupy_object: soup
    :return: string/boolen
    """
    try:
        corner = soupy_object.find('span', attrs = {'id':'Corner_Property'}).text
    except:
        corner =None
    return corner

def parking_status(soup_object):
    """
    return parking status
    :param soup_object: soup object
    :return: string
    """

    try:
        parking = soup_object.find('span', attrs = {'id':'Reserved_Parking_Label'}).text
    except:
        parking = None
    return parking

def wheelchair(soup_object):
    """
    return is wheel chair friend or not
    :param soup_object: soup
    :return: string
    """
    try:
        wheel = soup_object.find('span', attrs={'id': 'WheelChairFriendly'}).text
    except:
        wheel = None
    return wheel

def PetFriendly(soup_object):
    """
    return is pet friendly or not
    :param soup_object: soup
    :return: string
    """
    try:
        pet = soup_object.find('span', attrs={'id': 'PetFriendly'}).text
    except:
        pet = None
    return pet

def rentAgreementDuration(soup_object):
    """
    return agreement duration
    :param soup_object: soup
    :return: string
    """
    try:
        agreement = soup_object.find('span', attrs={'id': 'rentAgreementDuration'}).text
    except:
        agreement = None
    return agreement

def noticeDuration(soup_object):
    """
    return notice  duration
    :param soup_object: soup
    :return: string
    """
    try:
        notice = soup_object.find('span', attrs={'id': 'noticeDuration'}).text
    except:
        notice = None
    return notice

def electricityWaterCharges(soup_object):
    """
    return notice  duration
    :param soup_object: soup
    :return: string
    """
    try:
        lightbill = soup_object.find('span', attrs={'id': 'electricityWaterCharges'}).text
    except:
        lightbill = None
    return lightbill

def Powerbackup_Label(soup_object):
    """
    return power backup condition
    :param soup_object: soup
    :return: string
    """
    try:
        lightbill = soup_object.find('span', attrs={'id': 'Powerbackup_Label'}).text
    except:
        lightbill = None
    return lightbill

def age_label(soup_object):
    """
    return power backup condition
    :param soup_object: soup
    :return: string
    """
    try:
        age = soup_object.find('span', attrs={'id': 'Age_Label'}).text
    except:
        age = None
    return age

# url_list =[]
# def all_urls(start, end):
#     for pagenumber in range(start, end):
#         url = f'https://www.99acres.com/property-for-rent-in-pune-ffid-page-{pagenumber}'
#         data = get(url, headers = hdr)
#         soup = BeautifulSoup(data.content, 'html.parser')
#         links = soup.find_all('a', attrs= {"class":"body_med srpTuple__propertyName"})
#         for item in links:
#             main_url = 'https://www.99acres.com'
#             sub_url = item.get('href')
#             data_url = main_url + sub_url
#             url_list.append(data_url)
#     return (url_list)
# #



data_list = []
def get_all(start, end):
    """
    return a complete datframe into csv file

    :param url: string - html
    :param start: int
    :param end: int
    :return:  csv & dataframe
    """
    for pagenubmer in range(start, end):
        url = f'https://www.99acres.com/property-for-rent-in-pune-ffid-page-{pagenubmer}'
        data = get(url, headers = hdr)
        soup = BeautifulSoup(data.content, 'html.parser')
        links = soup.find_all('a', attrs= {"class":"body_med srpTuple__propertyName"})
        timestart = timeit.default_timer()
        for j, item in enumerate(links):
            main_url = 'https://www.99acres.com'
            sub_url = item.get('href')
            data_url = main_url + sub_url
            print(f'page started   {j}')
            data = get(data_url, headers=hdr)
            soup_get = BeautifulSoup(data.content, 'html.parser')
            bedrooms = bedroom_count(soup_get)
            bathrooms = bathroom_count(soup_get)
            balcanys = balcany_count(soup_get)
            add_room = additional_rooms(soup_get)
            rent = rent_amt(soup_get)
            brokarage = brokarge_amt(soup_get)
            area = built_area(soup_get)
            fursn = furnishing(soup_get)
            type_liv = availability_label(soup_get)
            add = address(soup_get)
            floornum = floor_num(soup_get)
            face = facing(soup_get)
            floor_type = flooring(soup_get)
            gate_comm = gated_community(soup_get)
            corner = corner_property(soup_get)
            parking = parking_status(soup_get)
            handicaped = wheelchair(soup_get)
            pet = PetFriendly(soup_get)
            agreement = rentAgreementDuration(soup_get)
            notice = noticeDuration(soup_get)
            light = electricityWaterCharges(soup_get)
            backup = Powerbackup_Label(soup_get)
            age = age_label(soup_get)
            my_data = {'rent': rent, 'bedroom': bedrooms, 'bathrooms':bathrooms, "additional_rooms":add_room, "balcany":balcanys,
                       "brokarage":brokarage, "area":area,'furnishing':fursn,'avalable_for': type_liv, 'address':add,
                       'floor_number':floornum,'facing':face,"floor_type":floor_type,'gate_community':gate_comm, "corner_pro":corner,
                       'parking': parking, 'wheelchairadption':handicaped, 'petfacility':pet, 'aggDur':agreement, 'noticeDur':notice,
                       'lightbill':light, 'powerbackup':backup, 'propertyage':age}
            data_list.append(my_data)
        print(f'page {pagenubmer}')
        stop = timeit.default_timer()
        print('Time: ', stop - timestart)
    return data_list


a = pd.DataFrame(get_all(start, end))
a.to_csv('my_data421_450.csv', index_label= False)
