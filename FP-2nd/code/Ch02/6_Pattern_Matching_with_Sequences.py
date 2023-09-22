"""
@Description: Pattern Matching with Sequences
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-21 13:31:14
"""


# def handle_command(self, message):
#     match message:
#         case ['BEEPER', frequency, times]:
#             self.beep(times, frequency)
#         case ['NECK', angle]:
#             self.rotate_neck(angle)
#         case ['LED', ident, intensity]:
#             self.leds[ident].set_brightness(ident, intensity)
#         case ['LED', ident, red, green, blue]:
#             self.leds[ident].set_color(ident, red, green, blue)
#         case _:
#             raise InvalidCommand(message)

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.69722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    # for name, _, _, (lat, lon) in metro_areas:
    #     if lon <= 0:
    #         print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
    for record in metro_areas:
        match record:
            # case [str(name), _, _, (float(lat), float(lon))] if lon <= 0:
            # typing hint, the first of item must be string and the 4th must be a pair of float
            # case [str(name), *_, (float(lat), float(lon))] if lon <= 0:
            # *_ match any item, without binding value
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    main()
