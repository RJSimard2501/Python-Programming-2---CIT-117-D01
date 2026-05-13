# Name: Remi Simard
# Assignment: Planetary Weights Dictionaries
# Reflection:
# Share what you liked about this assignment?
# I liked upgrading my old code from using named constants to using dectionary's. There is more moving parts in this assignmnet than before but its good to use them in a more realistic example.
# 
# Share what you struggled with?
# I struggled with the show history step the most with the For statements and getting them to output in the right order.
#
# How did you like working with dictionaries and pickling concepts? Share exactly 2 things you learned on this assignment:
# 1. Nesting a Dictionary inside a dictionary is super usefull because you can store data in a specific order and then can be reformatted later
# 2. You can Pickle a Dictionary nested inside another dictionary and then save it. Then after you can do ^ and then re pickle it for later again. Pretty cool.

#Imports
import pickle

#Main
def main():
    #File to store pickled history
    db_filename = "RSPlanetary Weights.db"

    #Dictionary of surface gravity factors (Key: planet name, Value: factor)
    surface_gravity = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066
    }

    #Open the pickling file that stored data
    try:
        with open(db_filename, "rb") as f:
            dictPlanetHistory = pickle.load(f)
            #Make sure it's a dictionary
            if not isinstance(dictPlanetHistory, dict):
                dictPlanetHistory = {}
                
    #Start new if no file is found or if there is any issue
    except FileNotFoundError:
        dictPlanetHistory = {}
    except Exception:
        dictPlanetHistory = {}

    #Prompt if they want to see the history
    show_hist = input("Would you like to see the history? y/n: ").strip()
    if show_hist.lower() == 'y':
        if dictPlanetHistory:
            print("Previous entries:")
            #Print each person's stored planetary weights
            for person_name, weights in dictPlanetHistory.items():
                print(f"\n{person_name}'s Solar System's Planetary Weights")
                for planet, w in weights.items():
                    print(f"{planet:10s}{w:10.2f}")
        else:
            print("No history found.")

    #Set everything to lowercase
    existing_names_lower = {name.lower() for name in dictPlanetHistory.keys()}

    #Loop to collect new entries
    while True:
        name = input("\nWhat is your name (enter key to quit): ").strip()
        #Exit Loop check
        if name == "":
            break

        #Deny duplicate names
        if name.lower() in existing_names_lower:
            print("That name already exists in history. Please enter a different unique name.")
            continue

        #Prompt for Earth Weight with validation
        while True:
            earth_weight_str = input("What is your weight: ").strip()
            try:
                earth_weight = float(earth_weight_str)
                break
            except ValueError:
                print("Invalid number. Please enter a valid numeric Earth weight.")

        #Declare dictPersonWeights and compute weights for each planet
        dictPersonWeights = {}
        print(f"\n{name}, here are your weights on our Solar System's planets")
        for planet, factor in surface_gravity.items():
            planet_weight = earth_weight * factor
            dictPersonWeights[planet] = planet_weight
            # Planet name left aligned in 10 chars; weight takes up 10 positions with 2 decimals
            print(f"Weight on {planet:10s}{planet_weight:10.2f}")

        #Add the person's data to history
        dictPlanetHistory[name] = dictPersonWeights
        existing_names_lower.add(name.lower())

    #Pickle the output to the dictPlanetHistory file
    try:
        with open(db_filename, "wb") as f:
            pickle.dump(dictPlanetHistory, f)
        print(f"\nHistory saved to '{db_filename}'.")
    except Exception as e:
        print(f"Error saving history to file: {e}")

#Program Start
main()
