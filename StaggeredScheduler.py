#-------------------------------------------------------------------------------
# Name:        Staggered Schedule.py
# Purpose:     Generate an SBS .ser file to generate a schedule
#              that will allow for each member of a starting rotation
#              to pitch at HOME & AWAY an equal number of times
#              against each opposing team's starting rotation...
#
# Author:      7thInning (Wiki-Baseball-Pedia)
#
# Created:     05/10/2023
# Copyright:   (c) 7th Productions, Inc. 2023
# Licence:     <LTK-3202-01-50>
#
# Author makes no guarantees as to the validity or workability of this program.
# User assumes all risk using this program.
#-------------------------------------------------------------------------------

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    # Get user input
    while True:
        try:
            num_pitchers = int(input("Number of starters in the starting rotation (3-6): "))
            if num_pitchers < 3 or num_pitchers > 6:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number between 3 and 6.")

    while True:
        try:
            num_teams = int(input("Number of teams to play against (1-14): "))
            if num_teams < 1 or num_teams > 14:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number between 1 and 14.")

    while True:
        try:
            games_home = int(input("# of games to play at HOME against each team (will be an equal number of AWAY games): "))
            if games_home <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number.")

    # Generate Schedule
    all_teams = ["T" + str(i) for i in range(2, num_teams + 2)]  # +1 to account for the main team being T1
    all_pitchers = [str(i) for i in range(1, num_pitchers + 1)]

    schedule = []

    for team in ["T1"]:  # Main team is T1
        for opponent in all_teams:  # All other teams
            for home_pitcher in all_pitchers:
                for away_pitcher in all_pitchers:
                    for _ in range(games_home):  # Iterating for number of home games
                        # home game for 'team'
                        schedule_line_home = f"/v:{opponent}.dat /h:{team}.dat /vp:{away_pitcher} /hp:{home_pitcher}"
                        schedule.append(schedule_line_home)

                        # away game for 'team'
                        schedule_line_away = f"/v:{team}.dat /h:{opponent}.dat /vp:{home_pitcher} /hp:{away_pitcher}"
                        schedule.append(schedule_line_away)

    random.shuffle(schedule)

    # Prompt the user for the file path
    file_path = input("Enter the full path and filename where you want to save the schedule (e.g., e:\\Stagger.ser): ")

    # Write Schedule to File
    try:
        with open(file_path, 'w') as file:
            for line in schedule:
                file.write(line + '\n')
        print(f"Schedule written to {file_path} with {len(schedule)} lines.")
    except Exception as e:
        print(f"Error writing to the file: {e}")

if __name__ == "__main__":
    main()
