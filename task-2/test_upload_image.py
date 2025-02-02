import random
import sys
from api_calls import add_a_pet, upload_image
from pet import Pet


def test_post_image_with_success():
        #arrange
        pet_temp = Pet()
        pet_temp.id = random.randrange(0, sys.maxsize)
        pet_temp.name = "PetPic"
        add_a_pet(pet_temp)
        #act
        response = upload_image(pet_temp.id, "rabbit", "BunesPic.jpg")
        #assert
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"