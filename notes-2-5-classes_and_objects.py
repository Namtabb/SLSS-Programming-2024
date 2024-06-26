# Classes and Objects

# Big Ideas:
#   - Classes allow us to couple data and functions together


# Create a class that represents a Pokemon
class Pokemon:  # always name classes with capital
    def __init__(self):
        """Constructor: contains all properties
        of a Pokemon. It also contains the default
        state of the properties.
        """
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "Normal"
        self.actual_cry = "Rooooooooooooooar"

        # Announce that Pokemon is born
        print("A Pokémon is born!")

    def cry(self) -> str:
        """Represents the sound a Pokemon makes

        Returns:
            - As a string the sound a pokemon makes
            - e.g. "{name} says, "{actual_cry}"""

        return f'{self.name} says, "{self.actual_cry}!"'

    def consume(self, item: str) -> str:
        """Pokemon consumes the item

        Params:
            - the item the pokemon consumes

        Returns:
            - the response of the pokemon
        """
        if item.lower() == "berry":
            return f'{self.name} eats the berry and says, "YUM!"'
        elif item.lower() == "potion":
            return f"{self.name} feels much better after the potion!"
        else:
            return f"{self.name} batted away the {item}!"


class Pikachu(Pokemon):
    """Child class of Pokemon"""

    def __init__(self, name="Pikachu"):
        # Call the super-class constructor
        super().__init__()

        # Setting the default values for
        # a Pikachu
        self.name = name
        self.id = 25
        self.type = "Electric"
        self.actual_cry = "Pikachu"

    def thunder(self, defender: Pokemon) -> str:
        """Represents the thunder attack.

        Params:
            - defender: defending pokemon"""
        response = f"{self.name} used thunder on {defender.name}."

        if defender.type.lower() == "water":
            response = response + " It was super effective."

        return response


def main():
    # Create two Pokemon

    # Create something 'Pikachu'-like
    pokemon_one = Pokemon()

    # Access the properties inside pokemon_one
    # Print the name of pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.type)

    # Change the values of the propeties
    pokemon_one.name = "Pikachu"
    pokemon_one.type = "Electric"
    pokemon_one.id = 25

    # Print the values from pokemon_one
    print(pokemon_one.name)
    print(pokemon_one.type)

    # TODO: Create something 'Squirtle'-like
    #  - Create a new Pokemon object
    #      - Store this in variable pokemon_two
    #  - Squirtle's Pokedex id is 4
    #  - Squirtle's type is Water

    pokemon_two = Pokemon()
    pokemon_two.name = "Squirtle"
    pokemon_two.type = "Water"
    pokemon_two.id = 4

    # To test, print out all of squirtle's properties
    print(pokemon_two.name)
    print(pokemon_two.id)
    print(pokemon_two.type)

    # Test Pokemon cry
    pokemon_one.actual_cry = "Pikachu"
    print(pokemon_one.cry())
    pokemon_two.actual_cry = "Grraaaaaoooorrr"
    print(pokemon_two.cry())

    # Test Pokemon consume
    print(pokemon_one.consume("berry"))
    print(pokemon_one.consume("potion"))
    print(pokemon_one.consume("poison"))  # mr. ubial doesn't condone
    print(pokemon_two.consume("berry"))

    # Create a new Pikachu object
    pikachu_one = Pikachu()
    # Print name, type, and id of pikachu_one
    print(pikachu_one.name, pikachu_one.type, pikachu_one.id)
    # Use the Pokemon methods on Pikachu object
    print(pikachu_one.cry())
    print(pikachu_one.consume("berry"))

    # Use the thunder method on pokemon_two
    print(pikachu_one.thunder(pokemon_one))
    print(pikachu_one.thunder(pokemon_two))


if __name__ == "__main__":
    main()

class Ditto(Pokemon):
    def __init__(self, name = "Ditto"):
        super().__init__
        self.name = "ditto"
        self.id = 132
        self.type = "normal"
        self.actual_cry = "hasfafjh"

    def transform(self, defender: Pokemon) -> str:
        response = f"{self.name} used transform\n {self.name} transformed into {defender.name}"

        return response                                                         

