# Project Info - InterFace_Inv_Status
This is a python script that will allow a customers to pull the status of all managed devices in Cisco DNA Center with interface information per interface
This allows a customer to pull this info and sort based on state... ie example "sort on all admin down", "sort on up down" etc...

This a tool to help new user to the Cisco DNA Center to better understand the usefulness of Cisco DNA API's.

## Requirements:
* Python 3
* Requests package

## How to run:

'''
python3 dnac_interfaces.py  
$ python3 ./dnac_interfaces.py  
Hostname  : Port Name                     : Admin State : Interface State : Interface Description  
cat_9k_1  : FortyGigabitEthernet1/1/1     : UP          : down            :  
cat_9k_1  : FortyGigabitEthernet1/1/2     : UP          : down            :  
cat_9k_1  : GigabitEthernet0/0            : DOWN        : down            :  
cat_9k_1  : GigabitEthernet1/1/1          : UP          : down            :  
cat_9k_1  : GigabitEthernet1/1/2          : UP          : down            :  
cat_9k_1  : GigabitEthernet1/1/3          : UP          : down            :  
cat_9k_1  : GigabitEthernet1/1/4          : UP          : down            :  
cat_9k_1  : Loopback0                     : UP          : up              :  
cat_9k_1  : TenGigabitEthernet1/0/1       : UP          : up              :  link to host hostA  
cat_9k_1  : TenGigabitEthernet1/0/2       : UP          : down            :  -->added-by-template-edjacks-template<--  
cat_9k_1  : TenGigabitEthernet1/0/3       : UP          : down            :  -->edjacks-template-02<--  
cat_9k_1  : TenGigabitEthernet1/0/4       : UP          : down            :  
'''

Co-Created by Ed Jackson & Bryan Byers
