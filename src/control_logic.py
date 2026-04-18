class ControlLogic:

    def __init__(self, hydraulic, pumps, jockey, settings):

        self.hydraulic = hydraulic
        self.pumps = pumps
        self.jockey = jockey
        self.settings = settings

        self.mode_auto = True
        self.state = "ОЖИДАНИЕ"
        self.timer = 0

    def update(self, dt):

        pressure = self.hydraulic.pressure

        if not self.mode_auto:
            return

        if self.state == "ОЖИДАНИЕ":

            if pressure < self.settings.jockey_on:
                self.jockey.start()
                self.timer = 0
                self.state = "ЖН"

        elif self.state == "ЖН":

            self.timer += dt

            if pressure >= self.settings.jockey_off:
                self.jockey.stop()
                self.state = "ОЖИДАНИЕ"

            elif (self.timer >= self.settings.jockey_fire_time
                  and pressure <= self.settings.jockey_on):
                self.jockey.stop()
                self.pumps[0].start()
                self.timer = 0
                self.state = "ПН1"

            elif (self.timer >= self.settings.jockey_normal_time
                  and pressure < self.settings.jockey_off):
                self.jockey.stop()
                self.pumps[0].start()
                self.timer = 0
                self.state = "ПН1"

        elif self.state.startswith("ПН"):

            self.timer += dt

            if pressure >= self.settings.pn_target:
                self.state = "ПОДДЕРЖАНИЕ"

            elif self.timer >= self.settings.pn_stage_time:

                index = int(self.state[-1]) - 1

                if index + 1 < len(self.pumps):
                    self.pumps[index + 1].start()
                    self.timer = 0
                    self.state = f"ПН{index + 2}"

        elif self.state == "ПОДДЕРЖАНИЕ":

            if pressure < self.settings.hold_pressure:
                self.timer = 0
                self.state = "ПН1"
