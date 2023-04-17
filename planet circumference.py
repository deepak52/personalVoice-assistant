def planet_circumference(planet_name):
    # Define the radii of the three planets in kilometers
    earth_radius = 6371
    saturn_radius = 58232
    jupiter_radius = 69911

    # Calculate the circumference of the selected planet
    if planet_name == "Earth":
        planet_circumference = 2 * 3.1416 * earth_radius
    elif planet_name == "Saturn":
        planet_circumference = 2 * 3.1416 * saturn_radius
    elif planet_name == "Jupiter":
        planet_circumference = 2 * 3.1416 * jupiter_radius
    else:
        planet_circumference = None
        print("Invalid planet name. Please enter Earth, Saturn, or Jupiter.")

    return planet_circumference

while(True):
    print("Planet Circumference Calculator")
    print("____MENU____")
    print("  1.Earth")
    print("  2.Saturn")
    print("  3.Jupiter")
    choice_str = input("Enter your choice\n")
    choice = int(choice_str)
    if choice == 1:
        print(planet_circumference("Earth"))
    elif choice == 2:
        print(planet_circumference("Saturn"))
    elif choice == 3:
        print(planet_circumference("Jupiter"))
    else:
        print("Invalid choice please try again")
