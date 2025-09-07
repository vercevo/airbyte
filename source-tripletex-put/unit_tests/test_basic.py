from source_tripletex_put.source import SourceMyApi


def test_streams():
    src = SourceMyApi()
    streams = src.streams({
        "base_url": "https://api-test.tripletex.tech",
        "consumer_token": "dummy",
        "employee_token": "dummy",
        "expiration_date": "2025-12-31"
    })
    assert len(streams) == 1
