class Pump:

    def __init__(self, name, flow_m3h):
        self.name = name
        self.flow_m3h = flow_m3h
        self.running = False
        self.hours = 0.0

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def update_hours(self, dt):
        if self.running:
            self.hours += dt / 3600.0
