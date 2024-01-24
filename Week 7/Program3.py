country_capitals = {}

def manage_countries():
    while True:
        country = input("Enter the name of a country (or 'exit' to terminate): ").lower()
        if country == 'exit':
            break
        elif country in country_capitals:
            print(f"The capital of {country.capitalize()} is {country_capitals[country]}")
        else:
            capital = input(f"Enter the capital of {country.capitalize()}: ")
            country_capitals[country] = capital
            print(f"{country.capitalize()} and its capital {capital.capitalize()} added to the list.")


manage_countries()
