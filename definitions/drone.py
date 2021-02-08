class Drone:
    def __init__(self,id,max_payload,pos):
        self.id = id
        self.payload = []
        self.capacity = max_payload
        self.current_position = pos
        self.busy = False

    def is_busy(self):
        return self.busy

    def get_payload(self):
        return self.payload

    def update_payload(self,id,quantity,keyword):
        if keyword == 'add':
            self.payload[id] += quantity

        else:
            if self.payload[id] >= quantity:
                self.payload[id] -= quantity
