from utils import generate_id

VALID_STATUS = {"agendado", "concluído", "cancelado"}


def create_appointment(appointments, patients, patient_id, date, time, specialty):
    patient_exists = any(patient["id"] == patient_id for patient in patients)

    if not patient_exists:
        raise ValueError("Paciente não encontrado.")

    if not date.strip():
        raise ValueError("A data não pode ser vazia.")

    if not time.strip():
        raise ValueError("O horário não pode ser vazio.")

    if not specialty.strip():
        raise ValueError("A especialidade ou motivo não pode ser vazio.")

    appointment = {
        "id": generate_id(appointments),
        "patient_id": patient_id,
        "date": date.strip(),
        "time": time.strip(),
        "specialty": specialty.strip(),
        "status": "agendado",
    }

    appointments.append(appointment)
    return appointment


def list_appointments(appointments):
    return appointments


def find_appointment_by_id(appointments, appointment_id):
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            return appointment
    return None


def update_appointment_status(appointments, appointment_id, new_status):
    if new_status not in VALID_STATUS:
        raise ValueError("Status inválido.")

    appointment = find_appointment_by_id(appointments, appointment_id)

    if appointment is None:
        raise ValueError("Agendamento não encontrado.")

    appointment["status"] = new_status
    return appointment


def cancel_appointment(appointments, appointment_id):
    appointment = find_appointment_by_id(appointments, appointment_id)

    if appointment is None:
        raise ValueError("Agendamento não encontrado.")

    appointment["status"] = "cancelado"
    return appointment
