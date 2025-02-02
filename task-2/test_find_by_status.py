from api_calls import get_pets_with_status


def test_get_pets_with_statuses():
        #arrange
        statuses = ["available", "pending", "sold"]
        #act
        for status in statuses:
             response = get_pets_with_status(status)
        #assert
             assert response.status_code == 200
             result = response.json()
             assert len(result) > 0
             for pet in result:
                  assert pet['status'] == status

def test_get_pets_with_multiple_statuses():
        #arrange
        #act
        response = get_pets_with_status("pending", "sold")
        #assert
        assert response.status_code == 200
        result = response.json()
        assert len(result) > 0
        for pet in result:
                assert pet['status'] == "pending" or "sold"

# I expect this to pass but it doesn't, bug?
def test_get_pets_with_invalid_status():
       #arrange
        #act
        response = get_pets_with_status("Guava")
        #assert
        assert response.status_code == 400
       