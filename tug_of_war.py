#!/usr/bin/python
"""This python scripts is designed for grouping team for "tug of war" game

        Team's strength is based on
        1. weights
        2. balance of gender
"""

import time
import datetime
import sys
import itertools

class Match:
    
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def get_weight_diff(self):
        return abs(self.team1.get_weight() - self.team2.get_weight())

    def get_class_diff(self):
        return self.get_weight_diff() + abs(self.team1.get_sex_number_diff() + self.team2.get_sex_number_diff())

    def get_info(self):
        return self.team1.get_info() + " VS " + self.team2.get_info() + "----(w_diff: " + str(self.get_weight_diff()) + ")"


class Team:

    def __init__(self):
        self.persons = []

    def get_weight(self):
            total_weight = 0
            for person in self.persons:
                total_weight += person.weight
            return total_weight

    def get_average_age(self):
        total_age = 0
        for person in self.persons:
            total_age += person.age
        return total_age/len(self.persons)

    def add_person(self, person):
        self.persons.append(person)

    def get_male_number(self):
        male_number = 0
        for person in self.persons:
            if person.sex == 1:
                male_number += 1
        return male_number

    def get_female_number(self):
        return len(self.persons) - self.get_male_number()

    def get_sex_number_diff(self):
        return abs(self.get_male_number() - self.get_female_number())

    @staticmethod
    def combine_names(person1, person2):
        return person1.get_name() + "," + person2.get_name()

    def get_info(self):
        all_names = reduce(lambda x,y: x + "," +  y, map(lambda p: p.name, self.persons))
        # return "[(" + all_names + ") weight: " + str(self.get_weight()) + ", avg_age: " + str(self.get_average_age()) + " sex_diff: " + str(self.get_sex_number_diff()) + "]"
        return "[(" + all_names + ") w" + str(self.get_weight()) + ", s(" + str(self.get_male_number()) + "/" + str(self.get_female_number()) + ")]"

    def print_info(self):
        print self.get_info()

class Person:
    name = ""
    sex = 1
    age = 0
    weight = 0
    strength = 0
    pid = 0

    def __init__(self, name, weight, sex, age, strength):
        self.name = name
        self.weight = weight
        self.sex = sex
        self.age = age
        self.strength = strength

    def get_name(self):
        print self.name

    def get_sex_name(self):
        if self.sex == 1:
            return "M"
        return "F"

    def print_info(self):
        print self.name + ", " + self.get_sex_name() + ", age " + str(self.age) + ", weight " + str(self.weight) + "kg" + ", hp " + str(self.strength)

if __name__ == '__main__':
    hoang_viet = Person("HV", 60, 1, 28, 10)
    doan = Person("Doan", 59, 1, 25, 9)
    bang = Person("Bang", 58, 1, 27, 8)
    tien = Person("Tien", 70, 1, 28, 10)
    trung = Person("Trung", 59, 1, 31, 7)
    truong = Person("Truong", 51, 1, 23, 7)
    tanaka = Person("Na", 70, 1, 40, 10)
    takano = Person("No", 70, 1, 40, 10)

    nhung = Person("Nhung", 44, 0, 32, 6)
    le_phuong = Person("LP", 49, 0, 26, 6)
    thuy = Person("Thuy", 47, 0, 26, 6)
    chi = Person("Chi", 52, 0, 23, 7)
    hoan = Person("Hoan", 45, 0, 24, 6)
    hue = Person("Hue", 48, 0, 28, 6)
    tphuong = Person("T.Phuong", 46, 0, 31, 6)
    lien = Person("Lien", 49, 0, 31, 6)

    staff=[]

    staff.append(hoang_viet)
    staff.append(doan)
    staff.append(bang)
    staff.append(tien)
    staff.append(trung)
    staff.append(truong)
    #staff.append(tanaka)
    staff.append(takano)
    staff.append(nhung)
    staff.append(le_phuong)
    staff.append(thuy)
    staff.append(chi)
    staff.append(hoan)
    staff.append(hue)
    #staff.append(tphuong)
    #staff.append(lien)

    print "\nStaff information:\n"
    for person in staff:
        person.print_info()

    #Team size as large as possible
    team_size = len(staff)/2

    possible_teams = []
    for combination in itertools.combinations(staff, team_size):
        new_team = Team()
        for person in combination:
            new_team.add_person(person)
        possible_teams.append(new_team)

    possible_matchs = []
    for team in possible_teams:
        remaining_staff = set(staff) - set(team.persons)
        for combination in itertools.combinations(remaining_staff, team_size):
            opponent_team = Team()
            for person in combination:
                opponent_team.add_person(person)
            new_match = Match(team, opponent_team)
            possible_matchs.append(new_match)

    possible_matchs.sort(key=lambda match: match.get_class_diff())


    print "\nGrouping results:\n"
    for i in range(1, 6):
        print i, possible_matchs[i - 1].get_info()
        