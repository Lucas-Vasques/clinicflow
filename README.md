# ClinicFlow

## Descrição
O ClinicFlow é uma aplicação simples em linha de comando (CLI) desenvolvida para auxiliar clínicas pequenas e consultórios no cadastro de pacientes e no agendamento de consultas.

## Problema real
Pequenas clínicas e profissionais da saúde frequentemente organizam pacientes e consultas de forma manual, com anotações em papel, mensagens dispersas ou planilhas desorganizadas. Isso pode causar retrabalho, dificuldade de consulta das informações e falhas no acompanhamento dos atendimentos.

## Proposta da solução
O ClinicFlow foi criado para oferecer uma solução simples e funcional para o fluxo básico de atendimento de uma clínica. A aplicação permite cadastrar pacientes, buscar registros, criar agendamentos, listar consultas e atualizar o status dos atendimentos.

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
- agendamento de consultas
- listagem de agendamentos
- atualização de status do agendamento
- cancelamento de agendamentos

## Tecnologias utilizadas
- Python
- JSON para persistência de dados
- Pytest para testes automatizados
- Ruff para linting e análise estática
- GitHub Actions para integração contínua

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
│   ├── appointment.py
│   ├── main.py
│   ├── patient.py
│   ├── storage.py
│   └── utils.py
├── tests/
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
1. Clonar o repositório
git clone <LINK_DO_SEU_REPOSITORIO>
cd clinicflow
2. Criar o ambiente virtual
python -m venv .venv
3. Ativar o ambiente virtual
Windows PowerShell
.venv\Scripts\Activate.ps1
Windows CMD
.venv\Scripts\activate
4. Instalar as dependências
pip install -r requirements.txt

## Como executar o projeto
python src/main.py

## Como rodar os testes
pytest

## Como rodar o lint
ruff check .

## Exemplo de uso

Ao executar o programa, o usuário verá um menu com as opções principais do sistema:

=== ClinicFlow ===
1. Cadastrar paciente
2. Listar pacientes
3. Buscar paciente
4. Agendar consulta
5. Listar agendamentos
6. Atualizar status do agendamento
7. Cancelar agendamento
8. Sair
   
## Testes automatizados

O projeto possui testes automatizados para validar comportamentos importantes, como:

- cadastro de paciente com sucesso
- bloqueio de idade negativa
- criação de agendamento válido
- erro ao agendar consulta para paciente inexistente
- atualização de status de agendamento
- cancelamento de agendamento

## Integração contínua

O projeto utiliza GitHub Actions para rodar automaticamente:

- instalação das dependências
- lint com Ruff
- testes com Pytest

## Versionamento

Versão atual do projeto:

1.0.0

## Autor

Lucas Vasques

## Repositório

[Repositório](https://github.com/Lucas-Vasques/clinicflow/edit/main/README.md)
