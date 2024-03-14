# This File is a reference FOR USING API CALLS TO Assert All The COMPONENTS
#
# import logging
# import requests
# import json
#
# def get_response_from_endpoint(url, headers):
#     response = requests.get(url=url, headers=headers)
#     return response.json()
#
# # Filter store names and add into an empty list
# def filter_store_names(stores_api_response):
#     stores_name_list = []
#     stores_list = stores_api_response['shopping_list']
#     for store in stores_list:
#         stores_name_list.append(store['store_name'])
#     return stores_name_list
#
# # Get the hotel object by search its hotel name from api
# def get_hotel_by_name(hotels_api_response, name):
#     hotels_list = hotels_api_response['hotels_list']
#     return filter(lambda hotel: hotel["hotel_name"] == name, hotels_list)
#
# # Check if benefits section is empty for a venue/hotel/event
# def check_benefits_exists(object):
#     if len(object['benefits']) > 0:
#         return True
#     else:
#         return False
