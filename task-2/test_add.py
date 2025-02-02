from pet import Category, Pet, Tag
import random
from api_calls import get_pet_with_id, add_a_pet, add_a_pet_with_payload
import sys

def test_post_a_pet_with_success():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetTemp"
        pet_temp.category = Category()
        pet_temp.category.name = "cat"
        pet_temp.category.id = random.randrange(0, 10)
        pet_temp.photoUrls = ["photourls"]
        pet_temp.status = "available"
        tag = Tag()
        tag.id = random.randrange(0,10)
        tag.name = "pettag"
        pet_temp.tags = [tag]

        #act
        response = add_a_pet(pet_temp)

        #assert
        data_error = "data not saved correctly"
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        getpet = get_pet_with_id(pet_temp.id)
        result = getpet.json()
        assert result['name'] == pet_temp.name, f"pet_temp name {data_error}"
        assert result['id'] == pet_temp.id, f"pet_temp id {data_error}"
        assert result['category']['id'] == pet_temp.category.id, f"pet_temp category id {data_error}"
        assert result['category']['name'] == pet_temp.category.name, f"pet_temp category name {data_error}"
        assert result['photoUrls'][0] == pet_temp.photoUrls[0], f"pet_temp photoUrls {data_error}"
        assert result['status'] == pet_temp.status, f"pet_temp status {data_error}"
        assert result['tags'][0]['id'] == pet_temp.tags[0].id, f"pet_temp tage id {data_error}"
        assert result['tags'][0]['name'] == pet_temp.tags[0].name, f"pet_temp tag name {data_error}"

def test_post_pet_no_data_405():
     #arrange
     payloads = [None, ""]
     responses = []
     #act
     for payload in payloads:
           responses.append(add_a_pet_with_payload(payload))
     #assert
     for response in responses:
           assert response.status_code == 405, f"Expected status code 405, but received {response.status_code}"

def test_post_pet_string_400():
      #arrange
      payload = "Not a pet"
      #act
      response = add_a_pet_with_payload(payload)
      #assert
      response.status_code == 400, f"Expected status code 400, but received {response.status_code}"


            








      


    






















