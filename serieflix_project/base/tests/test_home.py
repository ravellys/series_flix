import pytest
from django.test import Client
from django.urls import reverse

# from serieflix_project.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200
