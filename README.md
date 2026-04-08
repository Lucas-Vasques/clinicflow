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
