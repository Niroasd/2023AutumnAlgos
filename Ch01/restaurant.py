class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.name}')
        print(f'{self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.name} serves wonderful {self.cuisine_type}.')
        print(f'{self.name} is open. Come on in!')

	
restaurant = Restaurant('Kotipizza', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()