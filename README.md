# ClinicFlow

## Descrição

O ClinicFlow é uma aplicação simples em linha de comando (CLI) desenvolvida para auxiliar clínicas pequenas e consultórios no cadastro de pacientes e no agendamento de consultas.

Nesta entrega intermediária, o projeto foi evoluído com integração à API pública ViaCEP, permitindo consultar dados de endereço a partir do CEP informado no cadastro do paciente.

## Problema real

Pequenas clínicas e profissionais da saúde frequentemente organizam pacientes e consultas de forma manual, com anotações em papel, mensagens dispersas ou planilhas desorganizadas. Isso pode causar retrabalho, dificuldade de consulta das informações e falhas no acompanhamento dos atendimentos.

Além disso, o preenchimento manual de dados de endereço pode gerar erros e tornar o cadastro mais demorado.

## Proposta da solução

O ClinicFlow foi criado para oferecer uma solução simples e funcional para o fluxo básico de atendimento de uma clínica.

A aplicação permite cadastrar pacientes, buscar registros, criar agendamentos, listar consultas, atualizar o status dos atendimentos e consultar automaticamente dados de endereço a partir de um CEP.

## Público-alvo

- clínicas pequenas
- consultórios
- profissionais autônomos da saúde
- recepcionistas e atendentes

## Funcionalidades

- cadastro de pacientes
- listagem de pacientes
- busca de paciente por ID
- busca de paciente por nome
- consulta de endereço por CEP usando a API ViaCEP
- armazenamento de dados de endereço no cadastro do paciente
- agendamento de consultas
- listagem de agendamentos
- atualização de status do agendamento
- cancelamento de agendamentos

## Integração com API pública

O projeto utiliza a API pública ViaCEP para consultar dados de endereço a partir do CEP informado pelo usuário.

Ao cadastrar um paciente, o sistema permite informar um CEP. Caso o CEP seja válido, a aplicação busca automaticamente informações como:

- CEP
- logradouro
- bairro
- cidade
- estado

Essa integração melhora o fluxo de cadastro e reduz erros de digitação manual.

## Tecnologias utilizadas

- Python
- JSON para persistência de dados
- Requests para consumo da API ViaCEP
- Pytest para testes automatizados
- Ruff para linting e análise estática
- GitHub Actions para integração contínua
- Git e GitHub para versionamento, branch, issue e pull request

## Estrutura do projeto

```text
clinicflow/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   ├── patients.json
│   └── appointments.json
├── src/
│   ├── __init__.py
│   ├── address_api.py
│   ├── appointment.py
│   ├── main.py
│   ├── patient.py
│   ├── storage.py
│   └── utils.py
├── tests/
│   ├── test_address_api.py
│   ├── test_appointment.py
│   └── test_patient.py
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
└── VERSION