
from pyscript import document

club_members = [
    "Ryle Benipauo",
    "Leeroy Torres",
    "Lucas Jared",
    "Mark Herrington",
    "Carlos Aguas",
    "Jared Silvestre"
]

def verify_candidate(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()

    full_name = f"{first_name} {last_name}".strip()

    is_member = full_name in club_members

    messages = {
        True: f"Congratulations {full_name}! You are now part of the ICT club.",
        False: f"Sorry {full_name}, your name is not on the list."
    }

    document.getElementById("result").innerHTML = messages[is_member]














