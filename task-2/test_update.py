from pet import Pet
import random
from api_calls import get_pet_with_id, update_pet, delete_pet, update_pet_with_payload
import sys

def test_put_a_pet_with_success():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetUpdate"
        #act
        response = update_pet(pet_temp)
        #assert
        assert response.status_code == 200
        getpet = get_pet_with_id(pet_temp.id)
        result = getpet.json()
        assert result['name'] == "PetUpdate"

def test_put_a_pet_404():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        delete_pet(pet_temp.id)
        #act
        response = update_pet(pet_temp)
        #assert
        assert response == 404

def test_put_pet_no_data_405():
     #arrange
     payloads = [None, ""]
     responses = []
     #act
     for payload in payloads:
           responses.append(update_pet_with_payload(payload))
     #assert
     for response in responses:
           assert response.status_code == 405

def test_put_pet_string_400():
      #arrange
      payload = "Not a pet"
      #act
      response = update_pet_with_payload(payload)
      #assert
      response.status_code == 400


