import requests
from config import HEADERS

BASE_URL = "https://api.clickup.com/api/v2"


# ==========================================================
# WORKSPACES
# ==========================================================

def get_teams():

    url = f"{BASE_URL}/team"

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
        return []

    return r.json()["teams"]


# ==========================================================
# SPACES
# ==========================================================

def get_spaces(team_id):

    url = f"{BASE_URL}/team/{team_id}/space"

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
        return []

    return r.json()["spaces"]


# ==========================================================
# FOLDERS
# ==========================================================

def get_folders(space_id):

    url = f"{BASE_URL}/space/{space_id}/folder"

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
        return []

    return r.json()["folders"]


# ==========================================================
# LISTAS
# ==========================================================

def create_list(folder_id, name):

    url = f"{BASE_URL}/folder/{folder_id}/list"

    data = {
        "name": name,
        "content": ""
    }

    r = requests.post(url, json=data, headers=HEADERS)

    if r.status_code not in [200, 201]:
        print("--------------------------------")
        print("ERROR CREANDO LISTA")
        print(r.status_code)
        print(r.text)
        print("--------------------------------")
        return None

    return r.json()


# ==========================================================
# TAREAS
# ==========================================================

def create_task(
    list_id,
    name,
    parent=None,
    description="",
    priority=None,
    status="pendiente"
):

    url = f"{BASE_URL}/list/{list_id}/task"

    data = {
        "name": name,
        "description": description,
        "status": status
    }

    if priority is not None:
        data["priority"] = priority

    if parent is not None:
        data["parent"] = parent

    r = requests.post(url, json=data, headers=HEADERS)

    if r.status_code not in [200, 201]:
        print()
        print("==========================================")
        print("ERROR CREANDO TAREA")
        print("==========================================")
        print("Nombre :", name)
        print("HTTP   :", r.status_code)
        print("Respuesta:")
        print(r.text)
        print("==========================================")
        print()
        return None

    return r.json()


# ==========================================================
# OBTENER TAREA
# ==========================================================

def get_task(task_id):

    url = f"{BASE_URL}/task/{task_id}"

    r = requests.get(url, headers=HEADERS)

    if r.status_code != 200:
        print(r.status_code)
        print(r.text)
        return None

    return r.json()


# ==========================================================
# ACTUALIZAR TAREA
# ==========================================================

def update_task(task_id, data):

    url = f"{BASE_URL}/task/{task_id}"

    r = requests.put(url, json=data, headers=HEADERS)

    if r.status_code != 200:
        print()
        print("ERROR ACTUALIZANDO TAREA")
        print(r.status_code)
        print(r.text)
        return None

    return r.json()


# ==========================================================
# ELIMINAR TAREA
# ==========================================================

def delete_task(task_id):

    url = f"{BASE_URL}/task/{task_id}"

    r = requests.delete(url, headers=HEADERS)

    return r.status_code == 200