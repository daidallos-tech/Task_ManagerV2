class Task:
    def __init__(self, title, description, status="In", id=None) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.status = status
