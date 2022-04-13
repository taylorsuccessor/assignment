from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_validation_empty_json():
    response = client.post("/api/opening-hours/", json={})
    assert response.status_code == 422

    response = client.post("/api/opening-hours/second-solution", json={})
    assert response.status_code == 422


def test_validate_payload_is_json():
    response = client.post("/api/opening-hours/", json="")
    assert response.status_code == 422

    response = client.post("/api/opening-hours/second-solution", json="")
    assert response.status_code == 422


def test_only_week_names_allow():

    json = {
        "not_aday": [
            {
                "type" : "open",
                "value" : 3600
            }
        ]
    }

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 422

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 422


def test_just_only_open_and_close_allow():

    json = {
        "sunday": [
            {
                "type" : "not_correct_option",
                "value" : 3600
            }
        ]
    }

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 422

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 422


def test_time_range_allow():

    json = {
        "sunday": [
            {
                "type" : "open",
                "value" : 99999
            }
        ]
    }

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 422

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 422


def test_success_one_day_open_and_close():

    json = {
        "saturday": [
            {
                "type" : "open",
                "value" : 3600
            },
            {
                "type" : "close",
                "value" : 39600
            }
        ]
    }

    expected_response = """Saturday: 1 AM - 11 AM"""

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_open_in_one_day_and_close_next_day():

    json = {
        "friday" : [
            {
                "type" : "open",
                "value" : 64800
            }
        ],
        "saturday": [
            {
                "type" : "close",
                "value" : 3600
            },
            {
                "type" : "open",
                "value" : 32400
            },
            {
                "type" : "close",
                "value" : 39600
            },
            {
                "type" : "open",
                "value" : 57600
            },
            {
                "type" : "close",
                "value" : 82800
            }
        ]
    }

    expected_response = """Friday: 6 PM - 1 AM\nSaturday: 9 AM - 11 AM, 4 PM - 11 PM"""

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_if_open_in_last_day_and_closed_in_first():
    json = {
        "monday": [
            {
                "type": "close",
                "value": 1
            },
            {
                "type": "open",
                "value": 5
            },
            {
                "type": "close",
                "value": 900
            },
            {
                "type": "close",
                "value": 599
            },
            {
                "type": "open",
                "value": 700
            }
        ],
        "sunday": [
            {
                "type": "open",
                "value": 599
            }
        ]
    }

    expected_response = "Monday: 12 AM - 12:09 AM, 12:11 AM - 12:15 AM\nSunday: 12:09 AM - 12 AM"

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_it_order_days_of_the_week():

    json = {
        "friday": [
            {
                "type": "close",
                "value": 1
            }
        ],
        "thursday": [
            {
                "type": "open",
                "value": 1200
            }
        ]
    }

    expected_response = "Thursday: 12:20 AM - 12 AM\nFriday: Closed"

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_it_order_hours_of_the_day():

    json = {
        "thursday": [
            {
                "type": "close",
                "value": 30000
            },
            {
                "type": "open",
                "value": 20000
            },
            {
                "type": "open",
                "value": 500
            },
            {
                "type": "close",
                "value": 9000
            }
        ]
    }

    expected_response = "Thursday: 12:08 AM - 2:30 AM, 5:33 AM - 8:20 AM"

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response


def test_validation_for_each_open_one_close():

    json = {
        "saturday": [
            {
                "type" : "open",
                "value" : 3000
            },
            {
                "type" : "open",
                "value" : 3600
            },
            {
                "type" : "close",
                "value" : 39600
            }
        ]
    }


    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 422

    json = {
        "saturday": [
            {
                "type" : "close",
                "value" : 3000
            },
            {
                "type" : "close",
                "value" : 3600
            }
        ]
    }


    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 422


def test_full_test():
    json = {
        "monday" : [],
        "tuesday" : [
            {
                "type" : "open",
                "value" : 36000
            },
            {
                "type" : "close",
                "value" : 64800
            }
        ],
        "wednesday" : [],
        "thursday" : [
            {
                "type" : "open",
                "value" : 37800
            },
            {
                "type" : "close",
                "value" : 64800
            }
        ],
        "friday" : [
            {
                "type" : "open",
                "value" : 36000
            }
        ],
        "saturday" : [
            {
                "type" : "close",
                "value" : 3600
            },
            {
                "type" : "open",
                "value" : 36000
            }
        ],
        "sunday" : [
            {
                "type" : "close",
                "value" : 3600
            },
            {

                "type" : "open",
                "value" : 43200
            },
            {
                "type" : "close",
                "value" : 75600
            }
        ]
    }

    expected_response = "Monday: Closed\nTuesday: 10 AM - 6 PM\n" + \
                        "Wednesday: Closed\n" + \
                        "Thursday: 10:30 AM - 6 PM\n" + \
                        "Friday: 10 AM - 1 AM\n" + \
                        "Saturday: 10 AM - 1 AM\n" + \
                        "Sunday: 12 PM - 9 PM"

    response = client.post("/api/opening-hours/", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response

    response = client.post("/api/opening-hours/second-solution", json=json)
    assert response.status_code == 200
    assert response.json() == expected_response
