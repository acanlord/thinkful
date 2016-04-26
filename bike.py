#! /usr/bin/python

class Bicycle(object):
    def __init__(self, model_name, bike_weight, bike_cost):
        self.model_name = model_name
        self.bike_weight = bike_weight
        self.bike_cost = bike_cost

class BikeShop(Bicycle):
    def __init__(self, shop_name, inventory):
        self.shop_name = shop_name
        self.inventory = inventory
        self.profit = 0

    def get_shop_name(self):
        return self.shop_name

    def get_inventory(self):
        return self.inventory

class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.own_bike = None


if __name__ == '__main__':

    # Bicycle inventory
    bmx = Bicycle("bmx", 10, 300)
    road = Bicycle("road", 30, 900)
    mountain = Bicycle("mountain", 40, 600)

    current_inventory = [bmx, road, mountain]

    shop = BikeShop("Bobs Bikes", current_inventory)

    # Customers

    veronica = Customer("Shannon", 1000)
    julie = Customer("julie", 900)
    rick = Customer("rick", 600)

    customersList = [veronica, julie, rick]



    #print "Welcome to {}!".format(shop.get_shop_name())
    print ("Current Inventory")
    print ("Model - Weight - Cost")
    for bike in shop.get_inventory():
        print ("{0} {1} ${2}".format(bike.model_name, bike.bike_weight, bike.bike_cost))

