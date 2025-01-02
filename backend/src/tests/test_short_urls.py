import pytest
from starlette import status


async def test_create_short_url(client):
    url = {
        "url": "www.google.com"
    }
    resp = await client.post("shorten/", json=url)
    assert resp.status_code == status.HTTP_200_OK
    response_data = resp.json()
    assert response_data["url"] == "https://www.google.com/"
    assert response_data["short_code"]


async def test_get_short_url(client, create_short_url):
    resp = await client.get(f"shorten/{create_short_url.short_code}")
    assert resp.status_code == status.HTTP_200_OK
    response_data = resp.json()
    assert response_data["url"] == "https://www.test.com/"


@pytest.mark.parametrize(
    "update_field, update_value",
    [
        ("url", "https://www.test.com/update/"),
    ],
)
async def test_update_short_url(client, create_short_url, update_field, update_value):
    resp = await client.put(
        f"shorten/{create_short_url.short_code}", json={update_field: update_value}
    )
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json()[update_field] == update_value


async def test_delete_job(client, create_short_url):
    resp = await client.delete(f"shorten/{create_short_url.short_code}")
    assert resp.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.parametrize(
    "url_data, expected_status_code, expected_detail",
    [
        (
                {
                    "url": "wrong_url"
                },
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {
                    "detail": [
                        {
                            "type": "url_parsing",
                            "loc": [
                                "body",
                                "url"
                            ],
                            "msg": "Input should be a valid URL, relative URL without a base",
                            "input": "wrong_url",
                            "ctx": {
                                "error": "relative URL without a base"
                            }
                        }
                    ]
                },
        ),
        (
                {
                    "url": ""
                },
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {
                    "detail": [
                        {
                            "type": "url_parsing",
                            "loc": [
                                "body",
                                "url"
                            ],
                            "msg": "Input should be a valid URL, input is empty",
                            "input": "",
                            "ctx": {
                                "error": "input is empty"
                            }
                        }
                    ]
                },
        ),
        (
                {},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
                {
                    "detail": [
                        {
                            "type": "missing",
                            "loc": [
                                "body",
                                "url"
                            ],
                            "msg": "Field required",
                            "input": {}
                        }
                    ]
                },
        )
    ],
)
async def test_create_url_fail(
        client, url_data, expected_status_code, expected_detail
):
    resp = await client.post("shorten/", json=url_data)
    assert resp.status_code == expected_status_code
    assert resp.json() == expected_detail
