
#city_functions.py
def city_country(city, country,population=None,language=None): #Added new parameters for population and language
    """Return a string like' City, Country - Population xxx, language '."""
    output = f"{city.title()}, {country.title()}"
    if population is not None:
        output += f" - Population: {population}"
    if language is not None:
        output += f", {language.title()}"
    return output



if __name__ == "__main__":
    #call the function at least three times

    print(city_country("Santiago", "Chile"))
    print(city_country("Paris", "France",population=2148000))
    print(city_country("Tokyo", "Japan",population=14000000,language="Japanese"))