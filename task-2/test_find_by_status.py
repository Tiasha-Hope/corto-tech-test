from api_calls import get_pets_with_status


def test_get_pets_with_statuses():
        #arrange
        statuses = ["available", "pending", "sold"]
        #act
        for status in statuses:
             response = get_pets_with_status(status)
        #assert
             assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
             result = response.json()
             assert len(result) > 0, f"Expected at least 1 result, but received none"
             for pet in result:
                  assert pet['status'] == status, f"Expected status to match for each pet."

def test_get_pets_with_multiple_statuses():
        #arrange
        #act
        response = get_pets_with_status("pending", "sold")
        #assert
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        result = response.json()
        assert len(result) > 0
        for pet in result:
                assert pet['status'] == "pending" or "sold", f"Expected no statuses besdies pending or sold"

# I expect this to pass but it doesn't, bug?
def test_get_pets_with_invalid_status():
       #arrange
        #act
        response = get_pets_with_status("Guava")
        #assert
        assert response.status_code == 400, f"Expected status code 400, but received {response.status_code}"
       