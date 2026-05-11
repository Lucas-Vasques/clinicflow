import requests


class AddressAPIError(Exception):
    """Erro ao consultar a API de endereço."""


def clean_cep(cep):
    return "".join(character for character in cep if character.isdigit())


def get_address_by_cep(cep):
    cleaned_cep = clean_cep(cep)

    if len(cleaned_cep) != 8:
        raise ValueError("O CEP deve conter 8 dígitos.")

    url = f"https://viacep.com.br/ws/{cleaned_cep}/json/"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as error:
        raise AddressAPIError("Não foi possível consultar o CEP.") from error

    data = response.json()

    if data.get("erro"):
        raise AddressAPIError("CEP não encontrado.")

    return {
        "cep": data.get("cep", ""),
        "street": data.get("logradouro", ""),
        "neighborhood": data.get("bairro", ""),
        "city": data.get("localidade", ""),
        "state": data.get("uf", ""),
    }