# Script From ChatGPT

import requests
import os
import argparse
from dotenv import load_dotenv

load_dotenv(dotenv_path="/home/grant/projects/tde101/Configuration Management Files/Misc/variables.env")

# Replace these values with your own
DO_TOKEN = os.getenv("DO_TOKEN")
DROPLET_ID = os.getenv("DROPLET_ID")

# Create parser.

parser = argparse.ArgumentParser()

headers = {
    "Authorization": f"Bearer {DO_TOKEN}",
    "Content-Type": "application/json"
}

def get_droplet_status():
    url = f"https://api.digitalocean.com/v2/droplets/{DROPLET_ID}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        droplet = response.json()["droplet"]
        return droplet["status"]
    else:
        print(f"Error: {response.status_code}")
        return None

def power_on_droplet():
    url = f"https://api.digitalocean.com/v2/droplets/{DROPLET_ID}/actions"
    data = {"type": "power_on"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Droplet is powering on.")
    else:
        print(f"Error: {response.status_code}")

def power_off_droplet():
    url = f"https://api.digitalocean.com/v2/droplets/{DROPLET_ID}/actions"
    data = {"type": "power_off"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Droplet is powering off.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    current_status = get_droplet_status()
    parser.add_argument('-o', '--on', action="store_true")
    parser.add_argument('-f', '--off', action="store_true")

    args = parser.parse_args()

    if args.on:
        print("Turn droplet on...")
        if current_status == "active":
            print("Droplet is already running.")
        else:
            power_on_droplet()
    elif args.off:
       print("Turning off droplet...")
       if current_status == 'off':
            print("Droplet is already off.")
       else:
            power_off_droplet()
    else:
        print(f"Droplet status: {current_status}")
