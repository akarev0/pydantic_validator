from validation.model import ChannelMenu
from validation.validator import MenuValidator


data = {
    "categories": [
        {
            "id": 1,
            "name": "",
        }
    ],
    "products": [
        {
            "plu": "sdfsdfsdfsfdsdfsdfsfdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdf",
            "price": -1,
        }
    ],
}


# if __name__ == "__main__":

r = MenuValidator.validate(model=ChannelMenu, menuData=data)
print(r)
