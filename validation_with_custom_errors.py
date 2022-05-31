import json
from validation.model import ChannelMenu
from validation.validator import MenuValidator
from validation.channels.Dvroo.models import DVRoMenu


import pathlib
from os.path import dirname, realpath


path = pathlib.PurePath(dirname(realpath(__file__)))

with open(path.joinpath("validation", "channels", "Dvroo", "example.json")) as file:
    data = json.load(file)

r = MenuValidator.validate(model=DVRoMenu, menuData=data)
print(r)
