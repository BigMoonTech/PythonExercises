
from cellphone import CellPhone

def main():

    manufacturer = input("Manufactor: ")
    model = input("Model: ")
    retail_price = input("Retail_price: ")

    phone = CellPhone(manufacturer, model, retail_price)

    print(phone.get_manufact())
    print(phone.get_model())
    print(phone.get_retail_price())

if __name__ == '__main__':
    main()