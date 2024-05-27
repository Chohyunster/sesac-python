import uuid

class IDGenerator:
    def generate_id(self):
        return str(uuid.uuid4())