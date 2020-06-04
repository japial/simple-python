class TicketManager:
    tickets = {}

    def get(self, pk):
        return self.tickets[pk]

    def add(self, ticket: 'Ticket'):
        try:
            new_pk = max(self.tickets.keys()) + 1
        except ValueError:
            new_pk = 1

        self.tickets[new_pk] = ticket
        self.tickets[new_pk].tid = new_pk

    def all(self):
        return self.tickets.values()


class Ticket:
    tid: int = None
    name: str
    email: str
    phone: str

    objects = TicketManager()

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def save(self):
        if not self.tid:
            self.objects.add(self)
        else:
            raise NotImplementedError('UpdateNot')



