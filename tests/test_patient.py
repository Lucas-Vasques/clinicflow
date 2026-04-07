from patient import create_patient, find_patient_by_id, find_patients_by_name


def test_create_patient_success():
    patients = []

    patient = create_patient(
        patients,
        name="Maria Silva",
        age=30,
        phone="88999999999",
        notes="Primeira consulta",
    )

    assert patient["id"] == 1
    assert patient["name"] == "Maria Silva"
    assert len(patients) == 1


def test_create_patient_with_negative_age():
    patients = []

    try:
        create_patient(
            patients,
            name="João",
            age=-1,
            phone="88999999999",
        )
        assert False
    except ValueError as error:
        assert str(error) == "A idade não pode ser negativa."


def test_find_patient_by_id():
    patients = [
        {"id": 1, "name": "Ana", "age": 22, "phone": "111", "notes": ""},
        {"id": 2, "name": "Carlos", "age": 40, "phone": "222", "notes": ""},
    ]

    patient = find_patient_by_id(patients, 2)

    assert patient is not None
    assert patient["name"] == "Carlos"


def test_find_patients_by_name():
    patients = [
        {"id": 1, "name": "Ana Souza", "age": 22, "phone": "111", "notes": ""},
        {"id": 2, "name": "Carlos Lima", "age": 40, "phone": "222", "notes": ""},
    ]

    results = find_patients_by_name(patients, "Ana")

    assert len(results) == 1
    assert results[0]["name"] == "Ana Souza"
