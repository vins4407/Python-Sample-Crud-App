def noteEntity(note) -> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "category": note["category"],
        "note": note["note"],
        "published": note["published"],
        "description": note["description"],
        "createdAt": note["createdAt"],
        "updatedAt": note["updatedAt"]
    }


def noteListEntity(notes) -> list:
    return [noteEntity(note) for note in notes]
