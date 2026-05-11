import pytest

from src.address_api import AddressAPIError, clean_cep, get_address_by_cep


class FakeResponse:
    def __init__(self, data):
        self.data = data

    def raise_for_status(self):
        return None

    def json(self):
        return self.data


def test_clean_cep_removes_non_digits():
    assert clean_cep("01001-000") == "01001000"


def test_get_address_by_cep_success(monkeypatch):
    def fake_get(url, timeout):
        return FakeResponse(
            {
                "cep": "01001-000",
                "logradouro": "Praça da Sé",
                "bairro": "Sé",
                "localidade": "São Paulo",
                "uf": "SP",
            }
        )

    monkeypatch.setattr("src.address_api.requests.get", fake_get)

    address = get_address_by_cep("01001-000")

    assert address["cep"] == "01001-000"
    assert address["street"] == "Praça da Sé"
    assert address["neighborhood"] == "Sé"
    assert address["city"] == "São Paulo"
    assert address["state"] == "SP"


def test_get_address_by_cep_invalid_format():
    with pytest.raises(ValueError):
        get_address_by_cep("123")


def test_get_address_by_cep_not_found(monkeypatch):
    def fake_get(url, timeout):
        return FakeResponse({"erro": True})

    monkeypatch.setattr("src.address_api.requests.get", fake_get)

    with pytest.raises(AddressAPIError):
        get_address_by_cep("00000000")