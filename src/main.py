from src.appointment import cancel_appointment, create_appointment, list_appointments, update_appointment_status
from storage import load_data, save_data
from address_api import AddressAPIError, get_address_by_cep
from patient import (
    create_patient,
    list_patients,
    find_patient_by_id,
    find_patients_by_name,
)

PATIENTS_FILE = "data/patients.json"
APPOINTMENTS_FILE = "data/appointments.json"


def show_menu():
    print("\n=== ClinicFlow ===")
    print("1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente")
    print("4. Agendar consulta")
    print("5. Listar agendamentos")
    print("6. Atualizar status do agendamento")
    print("7. Cancelar agendamento")
    print("8. Sair")


def handle_list_patients(patients):
    items = list_patients(patients)

    if not items:
        print("Nenhum paciente cadastrado.")
        return

    for patient in items:
        print(
            f"ID: {patient['id']} | Nome: {patient['name']} | "
            f"Idade: {patient['age']} | Telefone: {patient['phone']} | "
            f"Cidade: {patient.get('city', '')} | Estado: {patient.get('state', '')}"
        )


def handle_search_patient(patients):
    try:
        search_type = input("Buscar por ID ou nome? (id/nome): ").strip().lower()

        if search_type == "id":
            patient_id = int(input("ID do paciente: "))
            patient = find_patient_by_id(patients, patient_id)

            if not patient:
                print("Paciente não encontrado.")
                return

            print(
                f"ID: {patient['id']} | Nome: {patient['name']} | "
                f"Idade: {patient['age']} | Telefone: {patient['phone']} | "
                f"Cidade: {patient.get('city', '')} | Estado: {patient.get('state', '')}"
            )

        elif search_type == "nome":
            name = input("Nome: ")
            found = find_patients_by_name(patients, name)

            if not found:
                print("Nenhum paciente encontrado com esse nome.")
                return

            for patient in found:
                print(
                    f"ID: {patient['id']} | Nome: {patient['name']} | "
                    f"Idade: {patient['age']} | Telefone: {patient['phone']} | "
                    f"Cidade: {patient.get('city', '')} | Estado: {patient.get('state', '')}"
                )

        else:
            print("Opção de busca inválida.")
    except ValueError as error:
        print(f"Erro: {error}")


def handle_create_patient(patients):
    try:
        name = input("Nome: ")
        age = int(input("Idade: "))
        phone = input("Telefone: ")
        notes = input("Observações: ")
        cep = input("CEP: ")

        address = {
            "cep": cep,
            "street": "",
            "neighborhood": "",
            "city": "",
            "state": "",
        }

        if cep.strip():
            try:
                address = get_address_by_cep(cep)
                print("Endereço encontrado:")
                print(
                    f"{address['street']} - {address['neighborhood']} | "
                    f"{address['city']} - {address['state']}"
                )
            except (ValueError, AddressAPIError) as error:
                print(f"Aviso: não foi possível buscar o endereço. {error}")

        patient = create_patient(
            patients,
            name,
            age,
            phone,
            notes,
            address["cep"],
            address["street"],
            address["neighborhood"],
            address["city"],
            address["state"],
        )

        print(f"Paciente cadastrado com sucesso. ID: {patient['id']}")
    except ValueError as error:
        print(f"Erro: {error}")


def handle_create_appointment(appointments, patients):
    try:
        patient_id = int(input("ID do paciente: "))
        date = input("Data (AAAA-MM-DD): ")
        time = input("Horário (HH:MM): ")
        specialty = input("Especialidade ou motivo: ")

        appointment = create_appointment(
            appointments, patients, patient_id, date, time, specialty
        )
        print(f"Agendamento criado com sucesso. ID: {appointment['id']}")
    except ValueError as error:
        print(f"Erro: {error}")


def handle_list_appointments(appointments):
    items = list_appointments(appointments)

    if not items:
        print("Nenhum agendamento encontrado.")
        return

    for appointment in items:
        print(
            f"ID: {appointment['id']} | Paciente ID: {appointment['patient_id']} | "
            f"Data: {appointment['date']} | Horário: {appointment['time']} | "
            f"Motivo: {appointment['specialty']} | Status: {appointment['status']}"
        )


def handle_update_status(appointments):
    try:
        appointment_id = int(input("ID do agendamento: "))
        new_status = input("Novo status (agendado, concluído, cancelado): ")
        appointment = update_appointment_status(
            appointments, appointment_id, new_status
        )
        print(f"Status atualizado para: {appointment['status']}")
    except ValueError as error:
        print(f"Erro: {error}")


def handle_cancel_appointment(appointments):
    try:
        appointment_id = int(input("ID do agendamento: "))
        appointment = cancel_appointment(appointments, appointment_id)
        print(f"Agendamento {appointment['id']} cancelado com sucesso.")
    except ValueError as error:
        print(f"Erro: {error}")


def main():
    patients = load_data(PATIENTS_FILE)
    appointments = load_data(APPOINTMENTS_FILE)

    while True:
        show_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            handle_create_patient(patients)
            save_data(PATIENTS_FILE, patients)

        elif choice == "2":
            handle_list_patients(patients)

        elif choice == "3":
            handle_search_patient(patients)

        elif choice == "4":
            handle_create_appointment(appointments, patients)
            save_data(APPOINTMENTS_FILE, appointments)

        elif choice == "5":
            handle_list_appointments(appointments)

        elif choice == "6":
            handle_update_status(appointments)
            save_data(APPOINTMENTS_FILE, appointments)

        elif choice == "7":
            handle_cancel_appointment(appointments)
            save_data(APPOINTMENTS_FILE, appointments)

        elif choice == "8":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
