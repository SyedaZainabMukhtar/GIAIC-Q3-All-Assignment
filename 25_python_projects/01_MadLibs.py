# Mad Libs Game
def mad_libs():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    
    story = f"The {adjective} {noun} was {verb} in {place}."
    print("\nYour Mad Libs story:")
    print(story)

if __name__ == "__main__":
    print("Welcome to Mad Libs!")
    mad_libs()