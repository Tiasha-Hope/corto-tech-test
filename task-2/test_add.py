from pet import Pet
import random
from api_calls import get_pet_with_id, add_a_pet, add_a_pet_with_payload
import sys

def test_post_a_pet_with_success():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetTemp"
        #act
        response = add_a_pet(pet_temp)
        #assert
        assert response.status_code == 200
        getpet = get_pet_with_id(pet_temp.id)
        result = getpet.json()
        assert result['name'] == "PetTemp"

def test_post_pet_no_data_405():
     #arrange
     payloads = [None, ""]
     responses = []
     #act
     for payload in payloads:
           responses.append(add_a_pet_with_payload(payload))
     #assert
     for response in responses:
           assert response.status_code == 405

def test_post_pet_string_400():
      #arrange
      payload = "Not a pet"
      #act
      response = add_a_pet_with_payload(payload)
      #assert
      response.status_code == 400


            








      


    






















