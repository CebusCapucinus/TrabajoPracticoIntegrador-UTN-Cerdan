import os

def load_countries(filename):
    countries = []
    if not os.path.exists(filename):
        return countries
    
    file = open(filename, 'r', encoding='utf-8')
    for line in file:
        data = line.strip().split(',')
        if len(data) == 4:
            country = {
                'name': data[0],
                'population': int(data[1]),
                'area': int(data[2]),
                'continent': data[3]
            }
            countries.append(country)
    file.close()
    return countries

def save_countries(filename, countries):
    file = open(filename, 'w', encoding='utf-8')
    for country in countries:
        line = f"{country['name']},{country['population']},{country['area']},{country['continent']}\n"
        file.write(line)
    file.close()

def validate_positive_integer(message):
    while True:
        value = input(message)
        if value.isdigit() and int(value) >= 0:
            return int(value)
        print("Please enter a valid positive number")

def validate_non_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty")

def display_menu():
    print("\n=== COUNTRY MANAGEMENT SYSTEM ===")
    print("1. Add country")
    print("2. Update country")
    print("3. Search country")
    print("4. Filter countries")
    print("5. Sort countries")
    print("6. Show statistics")
    print("7. Exit")
    return validate_positive_integer("Select option: ")

def add_country(countries, filename):
    print("\n--- ADD NEW COUNTRY ---")
    name = validate_non_empty("Country name: ")
    
    for country in countries:
        if country['name'].lower() == name.lower():
            print("Country already exists")
            return
    
    population = validate_positive_integer("Population: ")
    area = validate_positive_integer("Area (km²): ")
    continent = validate_non_empty("Continent: ")
    
    new_country = {
        'name': name,
        'population': population,
        'area': area,
        'continent': continent
    }
    
    countries.append(new_country)
    save_countries(filename, countries)
    print("Country added successfully")

def update_country(countries, filename):
    print("\n--- UPDATE COUNTRY ---")
    name = validate_non_empty("Country name to update: ")
    
    found = False
    for country in countries:
        if country['name'].lower() == name.lower():
            found = True
            print(f"Current population: {country['population']}")
            country['population'] = validate_positive_integer("New population: ")
            
            print(f"Current area: {country['area']}")
            country['area'] = validate_positive_integer("New area: ")
            
            save_countries(filename, countries)
            print("Country updated successfully")
            break
    
    if not found:
        print("Country not found")

def search_country(countries):
    print("\n--- SEARCH COUNTRY ---")
    name = validate_non_empty("Enter country name: ").lower()
    
    found = []
    for country in countries:
        if name in country['name'].lower():
            found.append(country)
    
    if found:
        print("\nFound countries:")
        for country in found:
            print(f"Name: {country['name']}, Population: {country['population']}, Area: {country['area']} km², Continent: {country['continent']}")
    else:
        print("No countries found")

def filter_menu():
    print("\n--- FILTER OPTIONS ---")
    print("1. By continent")
    print("2. By population range")
    print("3. By area range")
    return validate_positive_integer("Select filter option: ")

def filter_by_continent(countries):
    continent = validate_non_empty("Enter continent: ").lower()
    
    filtered = []
    for country in countries:
        if country['continent'].lower() == continent:
            filtered.append(country)
    
    if filtered:
        print(f"\nCountries in {continent}:")
        for country in filtered:
            print(f"Name: {country['name']}, Population: {country['population']}, Area: {country['area']} km²")
    else:
        print("No countries found in this continent")

def filter_by_population(countries):
    print("Enter population range:")
    min_pop = validate_positive_integer("Minimum population: ")
    max_pop = validate_positive_integer("Maximum population: ")
    
    filtered = []
    for country in countries:
        if min_pop <= country['population'] <= max_pop:
            filtered.append(country)
    
    if filtered:
        print(f"\nCountries with population between {min_pop} and {max_pop}:")
        for country in filtered:
            print(f"Name: {country['name']}, Population: {country['population']}, Area: {country['area']} km², Continent: {country['continent']}")
    else:
        print("No countries found in this range")

def filter_by_area(countries):
    print("Enter area range:")
    min_area = validate_positive_integer("Minimum area (km²): ")
    max_area = validate_positive_integer("Maximum area (km²): ")
    
    filtered = []
    for country in countries:
        if min_area <= country['area'] <= max_area:
            filtered.append(country)
    
    if filtered:
        print(f"\nCountries with area between {min_area} and {max_area} km²:")
        for country in filtered:
            print(f"Name: {country['name']}, Population: {country['population']}, Area: {country['area']} km², Continent: {country['continent']}")
    else:
        print("No countries found in this range")

def filter_countries(countries):
    option = filter_menu()
    
    if option == 1:
        filter_by_continent(countries)
    elif option == 2:
        filter_by_population(countries)
    elif option == 3:
        filter_by_area(countries)
    else:
        print("Invalid option")

def sort_menu():
    print("\n--- SORT OPTIONS ---")
    print("1. By name")
    print("2. By population")
    print("3. By area")
    return validate_positive_integer("Select sort option: ")

def sort_countries(countries):
    option = sort_menu()
    
    if option == 1:
        sorted_countries = sorted(countries, key=lambda x: x['name'])
        order = "name"
    elif option == 2:
        sorted_countries = sorted(countries, key=lambda x: x['population'])
        order = "population"
    elif option == 3:
        sorted_countries = sorted(countries, key=lambda x: x['area'])
        order = "area"
    else:
        print("Invalid option")
        return
    
    print(f"\nCountries sorted by {order}:")
    for country in sorted_countries:
        print(f"Name: {country['name']}, Population: {country['population']}, Area: {country['area']} km², Continent: {country['continent']}")

def show_statistics(countries):
    if not countries:
        print("No data available")
        return
    
    print("\n--- STATISTICS ---")
    
    max_pop_country = countries[0]
    min_pop_country = countries[0]
    total_population = 0
    total_area = 0
    continent_count = {}
    
    for country in countries:
        if country['population'] > max_pop_country['population']:
            max_pop_country = country
        if country['population'] < min_pop_country['population']:
            min_pop_country = country
        
        total_population += country['population']
        total_area += country['area']
        
        continent = country['continent']
        if continent in continent_count:
            continent_count[continent] += 1
        else:
            continent_count[continent] = 1
    
    avg_population = total_population / len(countries)
    avg_area = total_area / len(countries)
    
    print(f"Country with highest population: {max_pop_country['name']} ({max_pop_country['population']})")
    print(f"Country with lowest population: {min_pop_country['name']} ({min_pop_country['population']})")
    print(f"Average population: {avg_population:.2f}")
    print(f"Average area: {avg_area:.2f} km²")
    
    print("\nCountries by continent:")
    for continent, count in continent_count.items():
        print(f"{continent}: {count} countries")

def main():
    filename = "countries.csv"
    countries = load_countries(filename)
    
    while True:
        option = display_menu()
        
        if option == 1:
            add_country(countries, filename)
        elif option == 2:
            update_country(countries, filename)
        elif option == 3:
            search_country(countries)
        elif option == 4:
            filter_countries(countries)
        elif option == 5:
            sort_countries(countries)
        elif option == 6:
            show_statistics(countries)
        elif option == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()