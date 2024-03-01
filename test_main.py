import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_water_jug_solution():
    # Test case with a solution
    response = client.get("/water_jug_solution/?x=3&y=5&z=4")
    assert response.status_code == 200
    assert response.json() == {"solution": [(0, 0), (3, 0), (0, 3), (3, 3), (1, 5), (1, 0), (0, 1), (3, 1), (0, 4)]}

    # Test case with no solution
    response = client.get("/water_jug_solution/?x=2&y=3&z=4")
    assert response.status_code == 200
    assert response.json() == {"message": "No solution possible"}

    # Test case with invalid input (negative values)
    response = client.get("/water_jug_solution/?x=-2&y=3&z=4")
    assert response.status_code == 422

    # Test case with invalid input (non-integer values)
    response = client.get("/water_jug_solution/?x=2.5&y=3&z=4")
    assert response.status_code == 422

    # Test case with valid input (larger numbers)
    response = client.get("/water_jug_solution/?x=10&y=15&z=7")
    assert response.status_code == 200
    assert response.json() == {"solution": [(0, 0), (10, 0), (0, 10), (10, 10), (10, 5), (5, 10), (5, 0), (0, 5), (10, 5), (7, 8)]}

if __name__ == "__main__":
    pytest.main()