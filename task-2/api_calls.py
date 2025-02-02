import requests
from dataclasses import asdict

base_url = "https://petstore.swagger.io/v2/pet"

def add_a_pet(pet):
    dpet = asdict(pet)
    headers = { 'Content-Type': 'application/json' }
    response = requests.post(base_url, json = dpet, headers = headers)
    return response

def update_pet(pet):
    dpet = asdict(pet)
    headers = {'Content-Type': 'application/json' }
    response = requests.put(base_url, json = dpet, headers = headers)
    return response


def get_pet_with_id(petid):
    response = requests.get(f"{base_url}/{petid}")
    return response

def delete_pet(petid):
    headers = { "api_key": "special-key" }
    response = requests.delete(f"{base_url}/{petid}", headers = headers)
    return response

def get_pets_with_status(*statuses):
    status = "status=" + ",".join(statuses)
    url = f"{base_url}/findByStatus?{status}"
    response = requests.get(url)
    return response

def upload_image(petid, metadata, filepath):
    requrl = f"{base_url}/{petid}/uploadImage"
    addmetadata = {"additionalMetadata": metadata}
    with open(filepath, "rb") as file:
        files = {"file": (filepath, file)}
        response = requests.post(requrl, data = addmetadata, files = files)
    return response 

def update_pet_with_form(petid, newname, status):
    requrl = f"{base_url}/{petid}"
    update_form = {"name": newname, "status": status}
    response = requests.post(requrl, data = update_form)
    return response 



