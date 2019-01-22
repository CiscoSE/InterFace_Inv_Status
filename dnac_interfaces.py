#!/usr/bin/env python3

import requests

def get_token(host, username, password):
    res = requests.post(f'https://{host}/api/system/v1/auth/token', auth=(username, password))
    res.raise_for_status()
    return(res.json()['Token'])


def get_devices(host, token):
    res = requests.get(f'https://{host}/api/v1/network-device', headers={'x-auth-token': token})
    res.raise_for_status()
    return(res.json()['response'])
    

def get_interface_status(host, token, deviceId):
    res = requests.get(f'https://{host}/api/v1/interface/network-device/{deviceId}', \
            headers = {'x-auth-token': token})
    res.raise_for_status()
    return(res.json()['response'])


def print_interface_status(host, username, password):
    token = get_token(host, username, password)
    #
    # get devices
    devices = get_devices(host, token)
    #
    for device in devices:
        hostname = device['hostname']
        family = device['family']
        id = device['id']
        #
        # get interfaces
        interfaces = get_interface_status(host, token, id)
        #
        for interface in interfaces:
            description = interface['description']
            status = interface['status']
            adminStatus = interface['adminStatus']
            portName = interface['portName']
            #
            print(f'{hostname}: {portName}: {adminStatus}/{status} : {description}')
            #
        print()


def main():
    host = 'sandboxdnac.cisco.com'
    username = 'devnetuser'
    password = 'Cisco123!'
    print_interface_status(host, username, password)



if __name__ == '__main__':
    main()
