from pet import Pet
import random
from api_calls import get_pet_with_id, add_a_pet, update_pet_with_form
import sys


def test_post_pet_with_form_data():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetForm"
        add_a_pet(pet_temp)
        #act
        response = update_pet_with_form(pet_temp.id, "NewName", "sold")
        #assert
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        getupdate = get_pet_with_id(pet_temp.id)
        result = getupdate.json()
        assert result['name'] == "NewName", f"Expected name NewName, but received {result['name']}"
        assert result['status'] == "sold", f"Expected status sold, but received {result['status']}"

