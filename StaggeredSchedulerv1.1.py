#-------------------------------------------------------------------------------
# Name:        Staggered Schedule.py
# Purpose:     Generate an SBS .ser file to generate a schedule
#              that will allow for each member of a starting rotation
#              to pitch at HOME & AWAY an equal number of times
#              against each opposing team's starting rotation...
#              Starting rotaton from 3-6 pitchers
#              Number of opposing teams = 19 (total of 20 teams supported)
#              Unlimited number of HOME and AWAY games selected...
#
# Author:      7thInning (Wiki-Baseball-Pedia)
#
# Created:     05/10/2023
# Copyright:   (c) 7th Productions, Inc. 2023
# Licence:     <LTK-3202-01-50>
#
# Modified:    07/10/2023
# Versioning:  v1.1
#    Fixed glitch in program using lagre values for teams and Games played...
#    Increased number of opposing teams from 14 to 19 (total of 20 Total teams)
#
# Author makes no guarantees as to the validity, workability, or accuracy of
# this program. User assumes/accepts all risk using this program.
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
            num_pitchers = int(input("Number of pitchers in starting rotation (3-6): "))
            if num_pitchers < 3 or num_pitchers > 6:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number between 3 and 6.")

    while True:
        try:
            num_opposing_teams = int(input("Number of teams to play against (1-19): "))
            if num_opposing_teams < 1 or num_opposing_teams > 19:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number between 1 and 19.")

    while True:
        try:
            games_home = int(input("Number of games your starter will pitch at HOME against each opposing team's starter (Schedule generated will be an equal number of HOME & AWAY games): "))
            if games_home <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive number.")

    # Generate Schedule
    all_teams = ["T" + str(i) for i in range(1, num_opposing_teams + 2)]
    all_pitchers = [str(i) for i in range(1, num_pitchers + 1)]

    schedule = []

    for index, team1 in enumerate(all_teams):
        for team2 in all_teams[index+1:]:  # This ensures we don't double count
            for pitcher1 in all_pitchers:
                for pitcher2 in all_pitchers:
                    for _ in range(games_home):  # for each home game
                        # home game for team1
                        schedule.append(f"/v:{team2}.dat /h:{team1}.dat /vp:{pitcher2} /hp:{pitcher1}")
                        # away game for team1
                        schedule.append(f"/v:{team1}.dat /h:{team2}.dat /vp:{pitcher1} /hp:{pitcher2}")

    random.shuffle(schedule)

    # Prompt the user for the file path
    file_path = input("Enter the full path and filename where you want to save the schedule (e.g., c:\\sched.txt): ")

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
