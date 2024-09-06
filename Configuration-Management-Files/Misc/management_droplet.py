# Baseline Script From ChatGPT. Made a few edits to manage different droplet IDs.

import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/grant/projects/tde101/Configuration-Management-Files/Misc/variables.env")

# Replace these values with your own
DO_TOKEN = os.getenv("DO_TOKEN")
HONEYPY_DROPLET_ID = os.getenv("DROPLET_ID")

T_POT_DROPLET_ID = os.getenv("T_POT_DROPLET_ID")

# Create parser.

parser = argparse.ArgumentParser()

headers = {
    "Authorization": f"Bearer {DO_TOKEN}",
    "Content-Type": "application/json"
}

def get_droplet_status(id):
    url = f"https://api.digitalocean.com/v2/droplets/{id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        droplet = response.json()["droplet"]
        return droplet["status"]
    else:
        print(f"Error: {response.status_code}")
        return None

def power_on_droplet(id):
    url = f"https://api.digitalocean.com/v2/droplets/{id}/actions"
    data = {"type": "power_on"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Droplet is powering on.")
    else:
        print(f"Error: {response.status_code}")

def power_off_droplet(id):
    url = f"https://api.digitalocean.com/v2/droplets/{id}/actions"
    data = {"type": "power_off"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Droplet is powering off.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    #current_status = get_droplet_status()
    parser.add_argument('-o', '--on', action="store_true")
    parser.add_argument('-f', '--off', action="store_true")
    parser.add_argument('-t','--type', type=str, required=True)

    args = parser.parse_args()

    if args.type == 'tpot' or 'honeypy':
        if args.type == 'tpot':
            id = T_POT_DROPLET_ID
        elif args.type == 'honeypy':
            id = HONEYPY_DROPLET_ID

        current_status = get_droplet_status(id)
        
        if args.on:
            print("Turn droplet on...")
            if current_status == "active":
                print("Droplet is already running.")
            else:
                power_on_droplet(id)
        elif args.off:
            print("Turning off droplet...")
            if current_status == 'off':
                print("Droplet is already off.")
            else:
                power_off_droplet(id)
            # else:
            #     print(f"Droplet status: {current_status}")
    else:
        print("Specify a honeypot type.")
