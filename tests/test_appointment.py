from appointment import (
    create_appointment,
    update_appointment_status,
    cancel_appointment,
)


def test_create_appointment_success():
    patients = [
        {"id": 1, "name": "Maria", "age": 30, "phone": "999", "notes": ""}
    ]
    appointments = []

    appointment = create_appointment(
        appointments,
        patients,
        patient_id=1,
        date="2026-04-10",
        time="14:00",
        specialty="Clínico Geral",
    )

    assert appointment["id"] == 1
    assert appointment["status"] == "agendado"
    assert len(appointments) == 1


def test_create_appointment_with_invalid_patient():
    patients = []
    appointments = []

    try:
        create_appointment(
            appointments,
            patients,
            patient_id=99,
            date="2026-04-10",
            time="14:00",
            specialty="Clínico Geral",
        )
        assert False
    except ValueError as error:
        assert str(error) == "Paciente não encontrado."


def test_update_appointment_status():
    appointments = [
        {
            "id": 1,
            "patient_id": 1,
            "date": "2026-04-10",
            "time": "14:00",
            "specialty": "Clínico Geral",
            "status": "agendado",
        }
    ]

    updated = update_appointment_status(appointments, 1, "concluído")

    assert updated["status"] == "concluído"


def test_cancel_appointment():
    appointments = [
        {
            "id": 1,
            "patient_id": 1,
            "date": "2026-04-10",
            "time": "14:00",
            "specialty": "Clínico Geral",
            "status": "agendado",
        }
    ]

    cancelled = cancel_appointment(appointments, 1)

    assert cancelled["status"] == "cancelado"
