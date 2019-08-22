import pytest

@pytest.mark.django_db
def test_disable_cache_control(client):
    res = client.get("/")
    assert "cache-control" not in res
