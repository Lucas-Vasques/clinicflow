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
```

## Instalação

- 1. Clonar o repositório:
git clone https://github.com/Lucas-Vasques/clinicflow.git
cd clinicflow

- 2. Criar o ambiente virtual:
python -m venv .venv

- 3. Ativar o ambiente virtual:
Windows PowerShell: .venv\Scripts\Activate.ps1
Windows CMD: .venv\Scripts\activate

- 4. Instalar dependências: pip install -r requirements.txt

## Como executar o projeto
python src/main.py

## Como rodar os testes
pytest

## Como rodar o lint
ruff check .

## Exemplo de uso
Ao executar o programa, o usuário verá um menu com as opções principais do sistema:
=== ClinicFlow ===
- 1. Cadastrar paciente
- 2. Listar pacientes
- 3. Buscar paciente
- 4. Agendar consulta
- 5. Listar agendamentos
- 6. Atualizar status do agendamento
- 7. Cancelar agendamento
- 8. Sair

Durante o cadastro de paciente, o sistema permite informar um CEP. Se o CEP for válido, o ClinicFlow consulta a API ViaCEP e exibe o endereço encontrado.

Exemplo:
Nome: Lucas
Idade: 20
Telefone: 99999-9999
Observações: paciente novo
CEP: 01001-000

Endereço encontrado:
Praça da Sé - Sé | São Paulo - SP

Paciente cadastrado com sucesso.

## Testes automatizados

O projeto possui testes automatizados para validar comportamentos importantes, como:

- cadastro de paciente com sucesso
- bloqueio de idade negativa
- criação de agendamento válido
- erro ao agendar consulta para paciente inexistente
- atualização de status de agendamento
- cancelamento de agendamento
- limpeza e validação de CEP
- consulta de endereço por CEP com resposta simulada da API
- tratamento de CEP inválido ou não encontrado

## Teste de integração

Foi criado um teste automatizado para validar o fluxo de integração com a API ViaCEP.

O teste utiliza uma resposta simulada da API para garantir que o sistema consiga processar corretamente os dados de endereço sem depender da disponibilidade da internet durante a execução dos testes.

## Integração contínua

O projeto utiliza GitHub Actions para rodar automaticamente:

- instalação das dependências
- lint com Ruff
- testes com Pytest

Isso garante que alterações enviadas ao repositório sejam verificadas automaticamente.

## Fluxo de desenvolvimento de entrega intermediária

Nesta etapa, o desenvolvimento foi realizado seguindo um fluxo profissional com GitHub:

- criação de uma Issue descrevendo a nova funcionalidade
- criação da branch entrega-intermediaria
- implementação da integração com a API ViaCEP
- criação de testes automatizados
- abertura de Pull Request
- validação pelo GitHub Actions
- merge da branch após aprovação dos checks

## Deploy/Publicação

Como o ClinicFlow é uma aplicação em linha de comando, a execução principal é feita localmente pelo terminal.

Para executar a aplicação, siga os passos de instalação e utilize o comando: python src/main.py

## Versionamento

Versão atual do projeto:

1.1.0

## Autor 

Lucas Vasques

## Repositório

[Repositório do ClinicFlow](https://github.com/Lucas-Vasques/clinicflow)
