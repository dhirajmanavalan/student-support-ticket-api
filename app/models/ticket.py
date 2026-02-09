from schemas.ticket import Status, Priority
class Ticket:
    def __init__(self,
                 user_id : str,
                 ticket_id : str,
                 title : str,
                 description : str,
                 priority = Priority.MEDIUM,
                 status = Status.OPEN):

        self.user_id = user_id
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        