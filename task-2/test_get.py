from pet import Pet
import random
from api_calls import get_pet_with_id, add_a_pet, delete_pet
import sys

def test_get_pet_with_id():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetGet"
        add_a_pet(pet_temp)
        #act
        getpet = get_pet_with_id(pet_temp.id)
        #assert
        assert getpet.status_code == 200, f"Expected status code 200, but received {getpet.status_code}"
        result = getpet.json()
        assert result['name'] == "PetGet", f"Expected name PetGet, but received {result['name']}"

def test_get_pet_with_non_existent_id():
        #arrange
        pet_id = random.randrange(0, sys.maxsize)
        delete_pet(pet_id)
        #act
        response = get_pet_with_id(pet_id)
        #assert
        assert response.status_code == 404, f"Expected status code 404, but received {response.status_code}"

        
        



       
