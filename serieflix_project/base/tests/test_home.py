import pytest
from django.test import Client
from django.urls import reverse

from serieflix_project.django_assertions import assert_contains


@pytest.fixture
def resp(client: Client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>SeriesFlix</title>')


def test_title_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">')


def test_footer_link(resp):
    assert_contains(resp, "https://github.com/ravellys")
