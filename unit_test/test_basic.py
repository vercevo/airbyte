import pytest
from source_myapi.source import SourceMyApi


def test_streams():
    source = SourceMyApi()
    streams = source.streams({
        "base_url": "https://api-test.tripletex.tech",  
        "consumer_token": "dummy",
        "employee_token": "dummy",
        "expiration_date": "2025-12-31"
    })
    assert len(streams) == 1
