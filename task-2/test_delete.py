import random
import sys
from api_calls import add_a_pet, delete_pet, get_pet_with_id
from pet import Pet


def test_delete_pet_with_success():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetDel"
        add_a_pet(pet_temp)
        #act
        response = delete_pet(pet_temp.id)
        #assert
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        getpet = get_pet_with_id(pet_temp.id)
        assert getpet.status_code == 404, f"Expected status code 404, but received {getpet.status_code}"

def test_delete_pet_with_non_existent_id():
        #arrange
        pet_id = random.randrange(0, sys.maxsize)
        #Deleting twice in case ID exists already
        delete_pet(pet_id)
        #act
        response = delete_pet(pet_id)
        #assert
        assert response.status_code == 404, f"Expected status code 404, but received {response.status_code}"