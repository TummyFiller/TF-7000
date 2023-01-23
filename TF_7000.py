# Lunch selection program for Hudson, WI - Created by: Nick Sullivan - Last Update: 22JAN2023

# import modules
import datetime
import shutil
import random
import time
import os

# Begin main loop
while True:

    # Define the "create_directory_and_file" function, which will create the "TF 7000" directory and the "All_Data.txt" file
    def create_directory_and_file():
        os.makedirs("C:\\TF 7000")
        with open("C:\\TF 7000\\All_Data.txt", "w") as all_data_file:
            all_data_file.write("-------------------------\nRestaurant List:\n-------------------------\n\n")
            all_data_file.write("Agave\nAgave to Go\nAzul\nBBC\nBBQ\nBarker's\nBennett's\nBricks\nKeys\nLocal\nLolos\n"
                                "Pier 500\nPost Mark Grill\nSan Pedro\nSapporo\nSmiling Moose\nSubhouse\nThai\nUrban Olive and Vine\n\n")
            all_data_file.write("-------------------------\nPrevious Restaurants:\n-------------------------\n\n")
            all_data_file.write("Thai\nSapporo\nLolos\nKeys\n\n")
            all_data_file.write("-------------------------\nRestaurant Ranks:\n-------------------------\n\n")
            all_data_file.write("5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n5\n\n")
            all_data_file.write("-------------------------\nRestaurant Counter:\n-------------------------\n\n")
            all_data_file.write(str(datetime.date.today()) + "\n")
            all_data_file.write("0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n\n")

    # Check if the "TF 7000" directory and the "All_Data.txt" file exist. If not, create them.
    if not os.path.exists("C:\\TF 7000"):
        create_directory_and_file()
    if not os.path.exists("C:\\TF 7000\\All_Data.txt"):
        shutil.rmtree("C:\\TF 7000")
        create_directory_and_file()

    # Retrieve all data from "All_Data.txt" file and create all_data_list
    with open("C:\\TF 7000\\All_Data.txt", "r") as all_data_file:
        initial_data_list = all_data_file.readlines()
    all_data_list = []
    for item in initial_data_list:
        all_data_list.append(item.replace("\n", ""))

    # Retrieve restaurants visited this week and create previous_restaurant_list
    for i in range(4):
        exec(f"previous_restaurant_{i + 1} = all_data_list[i + 28]")
    previous_restaurant_list = [previous_restaurant_1, previous_restaurant_2, previous_restaurant_3, previous_restaurant_4]

    # Retrieve current restaurant ranks and create rank_list
    for i in range(19):
        exec(f"r{i + 1}_rank = int(all_data_list[i + 37])")
    rank_list = [r1_rank, r2_rank, r3_rank, r4_rank, r5_rank, r6_rank, r7_rank, r8_rank, r9_rank, r10_rank, r11_rank,
                 r12_rank, r13_rank, r14_rank, r15_rank, r16_rank, r17_rank, r18_rank, r19_rank]

    # Retrieve current restaurant counts and create restaurant_count_list
    for i in range(19):
        exec(f"r{i + 1}_count = int(all_data_list[i + 62])")
    restaurant_count_list = [r1_count, r2_count, r3_count, r4_count, r5_count, r6_count, r7_count, r8_count, r9_count, r10_count,
                             r11_count, r12_count, r13_count, r14_count, r15_count, r16_count, r17_count, r18_count, r19_count]

    # Define restaurant class
    class Restaurant:
        def __init__(self, name, is_lunch_long, outside_avail, open_m, open_t, open_w, rank):
            self.name = name
            self.is_lunch_long = is_lunch_long
            self.outside_avail = outside_avail
            self.open_m = open_m
            self.open_t = open_t
            self.open_w = open_w
            self.rank = rank

    # Define all restaurants
    R1 = Restaurant("Agave", "y", "n", "y", "y", "y", r1_rank)
    R2 = Restaurant("Agave to Go", "n", "n", "y", "y", "y", r2_rank)
    R3 = Restaurant("Azul", "n", "y", "y", "y", "y", r3_rank)
    R4 = Restaurant("BBC", "y", "n", "n", "n", "y", r4_rank)
    R5 = Restaurant("BBQ", "n", "n", "y", "y", "y", r5_rank)
    R6 = Restaurant("Barker's", "y", "n", "y", "y", "Y", r6_rank)
    R7 = Restaurant("Bennett's", "y", "n", "y", "y", "y", r7_rank)
    R8 = Restaurant("Bricks", "n", "n", "n", "n", "n", r8_rank)
    R9 = Restaurant("Keys", "n", "y", "y", "y", "y", r9_rank)
    R10 = Restaurant("Local", "n", "n", "y", "y", "y", r10_rank)
    R11 = Restaurant("Lolos", "y", "n", "y", "y", "y", r11_rank)
    R12 = Restaurant("Pier 500", "y", "y", "y", "y", "y", r12_rank)
    R13 = Restaurant("Post Mark Grill", "y", "y", "y", "y", "y", r13_rank)
    R14 = Restaurant("San Pedro", "y", "y", "y", "y", "y", r14_rank)
    R15 = Restaurant("Sapporo", "n", "n", "y", "y", "y", r15_rank)
    R16 = Restaurant("Smiling Moose", "Y", "y", "y", "y", "y", r16_rank)
    R17 = Restaurant("Subhouse", "n", "y", "y", "y", "y", r17_rank)
    R18 = Restaurant("Thai", "n", "y", "y", "y", "y", r18_rank)
    R19 = Restaurant("Urban Olive and Vine", "y", "y", "y", "y", "y", r19_rank)

    # Define complete list of restaurant objects
    restaurant_list_full = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19]

    # Define a list of all restaurant names
    restaurant_name_list = ["Agave", "Agave to Go", "Azul", "BBC", "BBQ", "Barker's", "Bennett's", "Bricks", "Keys", "Local", "Lolos",
                            "Pier 500", "Post Mark Grill", "San Pedro", "Sapporo", "Smiling Moose", "Subhouse", "Thai",
                            "Urban Olive and Vine"]

    # Define the try_again function, to be called when the user enters an invalid string / value
    def try_again():
        input("\n*******   Press enter to try again   *******\n\n")
        os.system("CLS")

    # Print entry prompt
    print("\n*******   Welcome to TF 7000   *******              Last Updated: 22JAN2023\n")
    input("Press enter to begin\n\n")
    os.system("CLS")

    # Ask if user wants to choose a restaurant, review a restaurant, modify a restaurant rank, or view the restaurant counter
    users_choice = ""
    while users_choice not in ("1", "2", "3", "4", "5"):
        print()
        users_choice = input("Select one of the following options:\n------------------------------------\n\n"
                             "1:  Choose a restaurant\n\n2:  Review a restaurant\n\n3:  Modify a restaurant rank\n\n4:"
                             "  View restaurant counter\n\n5:  Reset all restaurant statistics\n\n")
        if users_choice not in ("1", "2", "3", "4", "5"):
            os.system("CLS")
            print("\n*** Entry Error ***      Must enter one of the following responses - (1 / 2 / 3 / 4 / 5)")
            try_again()
        print()
        os.system("CLS")

    # Define choice 1: choose a restaurant
    if users_choice == "1":

        # Question 1 - Ask what day it is and create restaurant_list_1 based on the response
        day = ""
        while day not in ("m", "M", "tu", "Tu", "w", "W", "th", "Th", "f", "F"):
            print()
            day = input("What day is it today? (M / Tu / W / Th / F)\n\n")
            if day not in ("m", "M", "tu", "Tu", "w", "W", "th", "Th", "f", "F"):
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter one of the following responses - (M / Tu / W / Th / F)")
                try_again()
            print()
            os.system("CLS")
        if day in ("m", "M"):
            restaurant_list_1 = [x for x in restaurant_list_full if x.open_m == "y"]
        elif day in ("tu", "Tu"):
            restaurant_list_1 = [x for x in restaurant_list_full if x.open_t == "y" and x.name not in previous_restaurant_list]
        elif day in ("w", "W"):
            restaurant_list_1 = [x for x in restaurant_list_full if x.open_w == "y" and x.name not in previous_restaurant_list]
        else:
            restaurant_list_1 = [x for x in restaurant_list_full if x.name not in previous_restaurant_list]

        # Question 2 - Ask if the user would prefer to eat outside and create restaurant_list_2 based on the response
        eat_outside = ""
        while eat_outside not in ("y", "Y", "n", "N"):
            print()
            eat_outside = input("Would you prefer to eat outside today? (y / n)\n\n")
            if eat_outside not in ("y", "Y", "n", "N"):
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter one of the following responses - (y / n)")
                try_again()
            print()
            os.system("CLS")
        if eat_outside in ("y", "Y"):
            restaurant_list_2 = [x for x in restaurant_list_1 if x.outside_avail in ("y", "Y")]
        else:
            restaurant_list_2 = [x for x in restaurant_list_1]

        # Question 3 - Ask the user if they have time for a long lunch and create restaurant_list_3 based on the response
        eat_long_lunch = ""
        while eat_long_lunch not in ("y", "Y", "n", "N"):
            print()
            eat_long_lunch = input("Do you have time for a long lunch today? (y / n)\n\n")
            if eat_long_lunch not in ("y", "Y", "n", "N"):
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter one of the following responses - (y / n)")
                try_again()
            os.system("CLS")
        if eat_long_lunch in ("y", "Y"):
            restaurant_list_3 = [x for x in restaurant_list_2]
        else:
            restaurant_list_3 = [x for x in restaurant_list_2 if x.is_lunch_long in ("n", "N")]

        # Create restaurant_list_4 and choose_rank_list using the names and ranks of restaurant_list_3
        restaurant_list_4 = [x.name for x in restaurant_list_3]
        choose_rank_list = [x.rank for x in restaurant_list_3]

        # Show a list of restaurants we've already eaten at this week
        if day in ("tu", "Tu", "w", "W", "th", "Th", "f", "F"):
            print("\nHere's where we've eaten this week:\n")
            if day in ("tu", "Tu"):
                print(previous_restaurant_list[0])
            elif day in ("w", "W"):
                for i in range(2):
                    print(previous_restaurant_list[i])
            elif day in ("th", "Th"):
                for i in range(3):
                    print(previous_restaurant_list[i])
            elif day in ("f", "F"):
                for i in range(4):
                    print(previous_restaurant_list[i])
            print()
            input("press enter to continue\n\n")
            os.system("CLS")

        # Ask for the user for restaurants to exclude and remove them from restaurant_list_4
        exclude_a_restaurant = ""
        while exclude_a_restaurant != "done":
            print("\nHere is a list of suitable restaurants for today:\n")
            for item in restaurant_list_4:
                print(item)
            print()
            if len(restaurant_list_4) == 2:
                print("There are only 2 restaurants remaining. You cannot exclude any more.\n")
                input("press enter to continue\n\n")
                break
            exclude_a_restaurant = input("Enter the name of a restaurant you want to exclude. If none, enter 'done'\n\n")
            if exclude_a_restaurant == "done":
                break
            elif exclude_a_restaurant not in restaurant_list_4:
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter restaurant name correctly\n")
                try_again()
            else:
                os.system("CLS")
                choose_rank_list.pop(restaurant_list_4.index(exclude_a_restaurant))
                restaurant_list_4.remove(exclude_a_restaurant)
        os.system("CLS")

        # Randomly select today's restaurant and print
        todays_Restaurant_1 = ''.join(random.choices(restaurant_list_4, weights=choose_rank_list))
        choose_rank_list.pop(restaurant_list_4.index(todays_Restaurant_1))
        restaurant_list_4.remove(todays_Restaurant_1)
        todays_Restaurant_2 = ''.join(random.choices(restaurant_list_4, weights=choose_rank_list))
        alternate_restaurant = ""
        while alternate_restaurant not in ("y", "Y", "n", "N"):
            print("\n*******   Today's restaurant is   *******\n")
            time.sleep(2)
            print(todays_Restaurant_1 + "\n")
            if len(restaurant_list_4) < 1:
                alternate_restaurant = "y"
            elif len(restaurant_list_4) > 0:
                alternate_restaurant = input("Would you like to see an alternate restaurant? - (y / n)\n\n")
                if alternate_restaurant not in ("y", "Y", "n", "N"):
                    os.system("CLS")
                    print("\n*** Entry Error ***      Must enter one of the following responses - (y / n)")
                    try_again()
            if alternate_restaurant in ("y", "Y"):
                print("\n*******   Today's alternate restaurant is   *******")
                time.sleep(2)
                print()
                print(todays_Restaurant_2)

    # Define choice 2: review a restaurant
    elif users_choice == "2":

        # Question 1 - What is the day of the week?
        day = ""
        while day not in ("m", "M", "tu", "Tu", "w", "W", "th", "Th", "f", "F"):
            print()
            day = input("What day is it today? (M / Tu / W / Th / F)\n\n")
            if day not in ("m", "M", "tu", "Tu", "w", "W", "th", "Th", "f", "F"):
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter one of the following responses - (M / Tu / W / Th / F)")
                try_again()
            print()
            os.system("CLS")

        # Question 2 - Where did you eat today?
        todays_restaurant = ""
        while todays_restaurant not in restaurant_name_list:
            print()
            for item in restaurant_name_list:
                print(item)
            print()
            todays_restaurant = input("Where did you eat today?\n\n")
            if todays_restaurant not in restaurant_name_list:
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter restaurant name correctly")
                try_again()
            os.system("CLS")

        # Question 3 - Do you want to update the restaurant's score?
        update = ""
        while update not in ("y", "Y", "n", "N"):
            print()
            update = input("Based on today's meal, do you want to update " + todays_restaurant + "'s score? (y / n)\n\n")
            if update not in ("y", "Y", "n", "N"):
                os.system("CLS")
                print("\n****** Entry Error ***      Must enter one of the following responses - (y / n)")
                try_again()
            os.system("CLS")

        # Update the "Previous Restaurants" section of "all_data_list"
        if day in ("m", "M"):
            all_data_list[28] = todays_restaurant
        elif day in ("tu", "Tu"):
            all_data_list[29] = todays_restaurant
        elif day in ("w", "W"):
            all_data_list[30] = todays_restaurant
        elif day in ("th", "Th"):
            all_data_list[31] = todays_restaurant

        # Update the "Restaurant Ranks" section of "all_data_list"
        index = restaurant_name_list.index(todays_restaurant)
        if update in ("y", "Y"):
            update_yes = ""
            while update_yes not in ("+", "-"):
                print()
                update_yes = input("Would you like to increase or decrease the rank? (+ / -)\n\n")
                if update_yes not in ("+", "-"):
                    os.system("CLS")
                    print("\n****** Entry Error ***      Must enter one of the following responses - (+ / -)")
                    try_again()
                os.system("CLS")
            if update_yes == "+":
                if int(all_data_list[index + 37]) < 10:
                    print(f"\n{todays_restaurant}'s ran has been increased from {all_data_list[index + 37]} to {rank_list[index] + 1}")
                    all_data_list[index + 37] = str(rank_list[index] + 1)
                else:
                    print(f"\n{todays_restaurant}'s rank is already at the maximum value of 10, and cannot be increased")
                    all_data_list[index + 37] = "10"
            else:
                if int(all_data_list[index + 37]) > 1:
                    print(f"\n{todays_restaurant}'s ran has been decreased from {all_data_list[index + 37]} to {rank_list[index] - 1}")
                    all_data_list[index + 37] = str(rank_list[index] - 1)
                else:
                    print(f"\n{todays_restaurant}'s rank is already at the minimum value of 1, and cannot be decreased")
                    all_data_list[index + 37] = "1"

        # Update the "Restaurant Counter" section of the "all_data_list"
        all_data_list[index + 62] = str(restaurant_count_list[index] + 1)

        # Write all updates made in choice 2 to the "All_Data.txt" file
        with open("C:\\TF 7000\\All_Data.txt", "w") as all_data_file:
            for item in all_data_list:
                all_data_file.writelines(item + "\n")

    # Define choice 3: modify a restaurant rank
    elif users_choice == "3":
        reset = ""
        while reset not in ("y", "Y", "n", "N"):
            print("\nHere is a list of all available restaurants and each rank (1 - 10):\n")
            for i in range(19):
                print(restaurant_name_list[i] + " : " + str(rank_list[i]))
            print()

            # Ask the user if they would like to modify the rank of a restaurant
            reset = input("Would you like to modify the rank of a restaurant? (y / n)    ")
            if reset not in ("y", "Y", "n", "N"):
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter one of the following responses - (y / n)")
                try_again()
                os.system("CLS")
            os.system("CLS")

        # Ask the user for the name of the restaurant for which the rank will be changed
        if reset in ("y", "Y"):
            restaurant_name = ""
            while restaurant_name not in restaurant_name_list:
                print()
                for i in range(19):
                    print(restaurant_name_list[i] + " : " + str(rank_list[i]))
                print()
                restaurant_name = input("Which restaurant rank would you like to modify?\n\n")
                if restaurant_name not in restaurant_name_list:
                    os.system("CLS")
                    print("\n*** Entry Error ***      Must enter restaurant name correctly")
                    try_again()
                os.system("CLS")

            # Ask the user for the new restaurant rank
            index = restaurant_name_list.index(restaurant_name)
            new_rank = ""
            while new_rank not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                print()
                new_rank = input("What would you like the new rank of " + restaurant_name + " to be? (1 - 10)\n\n")
                if new_rank not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                    os.system("CLS")
                    print("\n*** Entry Error ***      Must enter one of the following responses - (1 - 10)")
                    try_again()
                    os.system("CLS")
                    continue
                else:
                    if new_rank == f"{all_data_list[index + 37]}":
                        os.system("CLS")
                        print(f"\n*** Entry Error ***      {restaurant_name}'s rank is already {new_rank}")
                        try_again()
                        new_rank = ""
                        continue
                    else:
                        break
            os.system("CLS")

            # Let the user know that the rank has been modified and write the new rank to the "All_Data.txt" file.
            print(f"\n{restaurant_name}'s rank has been modified from {all_data_list[index + 37]} to {new_rank}")
            all_data_list[index + 37] = str(new_rank)
            with open("C:\\TF 7000\\All_Data.txt", "w") as all_data_file:
                for item in all_data_list:
                    all_data_file.writelines(item + "\n")

    # Define choice 4: view the restaurant counter
    elif users_choice == "4":
        print(f"\nRestaurant Counter as of: {all_data_list[61]}\n")
        for i in range(19):
            print(restaurant_name_list[i] + " : " + all_data_list[i + 62])

    # Define choice 5: reset all restaurant statistics
    else:
        reset = ""
        while reset not in ("y", "Y", "n", "N"):
            reset = input("\nAre you sure you want to reset all restaurant statistics? (y / n)\n\n")
            if reset not in ("y", "Y", "n", "N"):
                os.system("CLS")
                print("\n*** Entry Error ***      Must enter one of the following responses - (y / n)")
                try_again()
                os.system("CLS")
            os.system("CLS")
        if reset in ("y", "Y"):
            shutil.rmtree("C:\\TF 7000")
            create_directory_and_file()

    # Ask the user if he wants to run TF 7000 again
    final_question = ""
    while final_question not in ("y", "Y", "n", "N"):
        print()
        final_question = input("Would you like to run TF 7000 again (y / n)\n\n")
        if final_question not in ("y", "Y", "n", "N"):
            os.system("ClS")
            print("\n*** Entry Error ***      Must enter one of the following responses - (y / n)")
            try_again()
        elif final_question in ("y", "Y"):
            break_out_flag_1 = True
            break
        elif final_question in ("n", "N"):
            break_out_flag_1 = False
            break
    if break_out_flag_1:
        os.system("CLS")
        continue
    else:
        os.system("CLS")
        break

# Print exit prompt
input("\nPress enter to exit")
