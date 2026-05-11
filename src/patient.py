from utils import generate_id


def create_patient(
    patients,
    name,
    age,
    phone,
    notes="",
    cep="",
    street="",
    neighborhood="",
    city="",
    state="",
):
    if not name.strip():
        raise ValueError("O nome do paciente não pode ser vazio.")

    if age < 0:
        raise ValueError("A idade não pode ser negativa.")

    if not phone.strip():
        raise ValueError("O telefone não pode ser vazio.")

    patient = {
        "id": generate_id(patients),
        "name": name.strip(),
        "age": age,
        "phone": phone.strip(),
        "notes": notes.strip(),
        "cep": cep.strip(),
        "street": street.strip(),
        "neighborhood": neighborhood.strip(),
        "city": city.strip(),
        "state": state.strip(),
    }

    patients.append(patient)
    return patient


def list_patients(patients):
    return patients


def find_patient_by_id(patients, patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def find_patients_by_name(patients, name):
    name = name.strip().lower()
    return [patient for patient in patients if name in patient["name"].lower()]