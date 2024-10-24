class Creature:
    def power(self):
        pass

class Dragon(Creature):
    def power(self):
        return "breathes fire"

class Phoenix(Creature):
    def power(self):
        return "rises from ashes"

def display_power(creatures, index=0):
    if index < len(creatures):
        print(f"The {creatures[index].__class__.__name__} {creatures[index].power()}.")
        display_power(creatures, index + 1)


dragon = Dragon()
phoenix = Phoenix()

creatures = [dragon, phoenix]

display_power(creatures)
#2
class Tree:
    def growth(self, depth):
        pass

class Pine(Tree):
    def growth(self, depth):
        if depth == 0:
            return "Pine Seedling"
        else:
            return f"Pine Branch -> {self.growth(depth - 1)}"

class Oak(Tree):
    def growth(self, depth):
        if depth == 0:
            return "Oak Seedling"
        else:
            return f"Oak Branch -> {self.growth(depth - 1)}"

def visualize_growth(tree, depth):
    print(tree.growth(depth))


pine = Pine()
oak = Oak()


depth = int(input('Enter depth value: '))


print("Pine Tree Growth Pattern:")
visualize_growth(pine, depth)

print("\nOak Tree Growth Pattern:")
visualize_growth(oak, depth)
#3
class Book:
    def content(self, depth):
        pass

class FantasyBook(Book):
    def content(self, depth):
        if depth == 0:
            return "Fantasy Book: Once upon a time..."
        else:
            return f"Fantasy Chapter {depth}: Mystical adventure... " + self.content(depth - 1)

class SciFiBook(Book):
    def content(self, depth):
        if depth == 0:
            return "Sci-Fi Book: In a galaxy far, far away..."
        else:
            return f"Sci-Fi Chapter {depth}: Futuristic discovery... " + self.content(depth - 1)

def display_content(book, depth):
    print(book.content(depth))

fantasy_book = FantasyBook()
scifi_book = SciFiBook()

depth = 3

print("Fantasy Book Content:")
display_content(fantasy_book, depth)

print("\nSci-Fi Book Content:")
display_content(scifi_book, depth)
