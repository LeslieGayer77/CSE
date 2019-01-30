states = {
    "CA": "California",
    "FL": "florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
    }
}

print(nested_dictionary["GA"]["POPULATION"])

Georgia = nested_dictionary["GA"]
print(Georgia)

Complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }}

print(Complex_dictionary["AK"]["CITIES"][0])
print(Complex_dictionary["CA"]["CITIES"][1])
print(Complex_dictionary.keys())
print(Complex_dictionary.items())
print(nested_dictionary.items())

print()

for key, value in Complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

print()

for state, info in Complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("-" * 20)
