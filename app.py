import streamlit as st

from src.address_api import AddressAPIError, get_address_by_cep

st.set_page_config(page_title="ClinicFlow", page_icon="🏥")

st.title("🏥 ClinicFlow")
st.write("Aplicação para apoio ao cadastro de pacientes em clínicas pequenas.")

st.header("Consulta de endereço por CEP")

cep = st.text_input("Digite o CEP")

if st.button("Buscar endereço"):
    try:
        address = get_address_by_cep(cep)

        st.success("Endereço encontrado")
        st.write(f"**CEP:** {address['cep']}")
        st.write(f"**Logradouro:** {address['street']}")
        st.write(f"**Bairro:** {address['neighborhood']}")
        st.write(f"**Cidade:** {address['city']}")
        st.write(f"**Estado:** {address['state']}")

    except (ValueError, AddressAPIError) as error:
        st.error(str(error))