class SystemSettings:

    def __init__(self):

        self.jockey_on = 3.6
        self.jockey_off = 4.5
        self.pn_target = 6.0
        self.hold_pressure = 5.5

        self.jockey_normal_time = 30
        self.jockey_fire_time = 15
        self.pn_stage_time = 15

    def validate(self):

        if self.jockey_on >= self.jockey_off:
            return False, "ЖН ВКЛ должно быть ниже ЖН ВЫКЛ"

        if self.jockey_off >= self.pn_target:
            return False, "ЖН ВЫКЛ должно быть ниже целевого ПН"

        if self.hold_pressure >= self.pn_target:
            return False, "Давление поддержания ниже целевого ПН"

        return True, ""
