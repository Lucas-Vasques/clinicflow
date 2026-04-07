from storage import load_data, save_data
from patient import (
    create_patient,
    list_patients,
    find_patient_by_id,
    find_patients_by_name,
)
from appointment import (
    create_appointment,
    list_appointments,
    update_appointment_status,
    cancel_appointment,
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


def handle_create_patient(patients):
    try:
        name = input("Nome: ")
        age = int(input("Idade: "))
        phone = input("Telefone: ")
        notes = input("Observações: ")

        patient = create_patient(patients, name, age, phone, notes)
        print(f"Paciente cadastrado com sucesso. ID: {patient['id']}")
    except ValueError as error:
        print(f"Erro: {error}")


def handle_list_patients(patients):
    items = list_patients(patients)

    if not items:
        print("Nenhum paciente cadastrado.")
        return

    for patient in items:
        print(
            f"ID: {patient['id']} | Nome: {patient['name']} | "
            f"Idade: {patient['age']} | Telefone: {patient['phone']}"
        )


def handle_search_patient(patients):
    try:
        option = input("Buscar por (1) ID ou (2) Nome? ")

        if option == "1":
            patient_id = int(input("Digite o ID: "))
            patient = find_patient_by_id(patients, patient_id)

            if patient:
                print(patient)
            else:
                print("Paciente não encontrado.")

        elif option == "2":
            name = input("Digite o nome: ")
            results = find_patients_by_name(patients, name)

            if results:
                for patient in results:
                    print(patient)
            else:
                print("Nenhum paciente encontrado.")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Entrada inválida.")


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
