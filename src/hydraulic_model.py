class HydraulicModel:

    def __init__(self):
        self.pressure = 4.0
        self.level_1 = 12.0
        self.level_2 = 12.0
        self.fire_mode = False
        self.fire_demand = 0.0

    def toggle_fire(self):
        self.fire_mode = not self.fire_mode
        if not self.fire_mode:
            self.fire_demand = 0.0

    def update(self, pumps, jockey, dt):

        if self.fire_mode:
            self.fire_demand += 50 * dt
            self.fire_demand = min(1500, self.fire_demand)

        total_flow = 0

        if jockey.running:
            total_flow += jockey.flow_m3h

        for pump in pumps:
            if pump.running:
                total_flow += pump.flow_m3h

        delta = (total_flow - self.fire_demand) * 0.002
        self.pressure += delta
        self.pressure -= 0.03

        self.pressure = max(0, min(10, self.pressure))

        if total_flow > 0:
            drop = total_flow * dt / 3000
            self.level_1 = max(0, self.level_1 - drop)
            self.level_2 = max(0, self.level_2 - drop)
