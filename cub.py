class Cub:
    add_number = int(input())

    def cub_function(self):
        result = Cub.add_number * Cub.add_number * Cub.add_number
        return result

my_class = Cub()
print(my_class.cub_function())