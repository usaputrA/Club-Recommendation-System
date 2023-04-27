""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import TextIO
import io

# Sample Data (Used by Docstring examples)
# What a Profile File might look like.
EXAMPLE_PROFILE_DATA = '''Katsopolis, Jesse
Parent Council
Rock N Rollers
Tanner, Danny R
Donaldson-Katsopolis, Rebecca
Gladstone, Joey

Donaldson-Katsopolis, Rebecca
Gibbler, Kimmy

Tanner, Stephanie J
Tanner, Michelle
Gibbler, Kimmy

Tanner, Danny R
Parent Council
Tanner-Fuller, DJ
Gladstone, Joey
Katsopolis, Jesse

Gibbler, Kimmy
Smash Club
Rock N Rollers

Gladstone, Joey
Comics R Us
Parent Council

Tanner, Michelle
Comet Club
'''

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
       'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

P2FRIENDS = {
    'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'],
    'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'],
    'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],
    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'],
    'Alex Dunphy': ['Luke Dunphy'],
    'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'],
    'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'],
    'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],
    'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],
    'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'],
    'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 
                    'Phil Dunphy']}

P2CLUBS = {
    'Claire Dunphy': ['Parent Teacher Association'],
    'Manny Delgado': ['Chess Club'],
    'Mitchell Pritchett': ['Law Association'],
    'Alex Dunphy': ['Chess Club', 'Orchestra'],
    'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'],
    'Phil Dunphy': ['Real Estate Association'],
    'Gloria Pritchett': ['Parent Teacher Association']}


# Helper functions


def update_dict(key: str, value: str,
                key_to_values: dict[str, list[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """
    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)

# Required functions


def load_profiles(profiles_file: TextIO) -> tuple[dict[str, list[str]],
                                                  dict[str, list[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.

    >>> data = io.StringIO(EXAMPLE_PROFILE_DATA) # this treats a str as a file
    >>> result = load_profiles(data)
    >>> result == (P2F, P2C)
    True
    
    >>> file = open("profiles.txt")
    >>> result = load_profiles(file)
    >>> result == (P2FRIENDS, P2CLUBS)
    True
    >>> file.close()
    """
    d = {}
    e = {}
    line = profiles_file.readline().strip()
    while line != '':
        name = line
        last_name = name.split(',')[-1].strip()
        first_name = name.split(',')[0].strip()
        name_person = last_name + ' ' + first_name
        clubs = []
        friends = []
        line = profiles_file.readline().strip()
        while line != '' and ',' not in line:
            clubs.append(line)
            line = profiles_file.readline().strip()
        clubs.sort()
        if clubs and name_person not in d:
            d[name_person] = clubs
        elif clubs and name_person in d:
            d[name_person].extend(clubs)  
            
        while line != '' and ',' in line:
            friend = line
            last_name2 = friend.split(',')[-1].strip()
            first_name2 = friend.split(',')[0].strip()
            friend_name = last_name2 + ' ' + first_name2
            friends.append(friend_name)
            line = profiles_file.readline().strip()
        friends.sort()
        if friends and name_person not in e:
            e[name_person] = friends
        elif friends and name_person in e:
            e[name_person].extend(friends)  
        line = profiles_file.readline().strip()
    return (e, d)


def get_average_club_count(person_to_clubs: dict[str, list[str]]) -> int:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to, rounded down to the nearest integer (i.e. use // instead of /).

    >>> get_average_club_count(P2C)
    1
    
    >>> file = open("profiles.txt")
    >>> P2CLUBS = load_profiles(file)[1]
    >>> get_average_club_count(P2CLUBS)
    1
    >>> file.close()
    """
    count = 0
    persons = 0
    for key in person_to_clubs:
        count += len(person_to_clubs[key])
        persons += 1
    if persons != 0:    
        return count // persons
    else:
        return 0


def get_last_to_first(
        person_to_friends: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    >>> file = open("profiles.txt")
    >>> P2FRIENDS = load_profiles(file)[0]
    >>> get_last_to_first(P2FRIENDS) == {
    ...    'Pritchett': ['Gloria', 'Jay', 'Mitchell'],
    ...    'Dunphy': ['Alex', 'Claire', 'Haley Gwendolyn','Luke', 'Phil'],
    ...    'Delgado': ['Manny'],
    ...    'Tucker': ['Cameron'],
    ...    'D-Money': ['Dylan'],
    ...    'D-Cat': ['Chairman', 'Gilbert']}
    True
    >>> file.close()
    """
    last_to_first = {}
    for name in person_to_friends:
        last = name.split()[-1]
        first_name = name[:-len(last) - 1]
        if last not in last_to_first:
            last_to_first[last] = [first_name]
        elif last in last_to_first and first_name not in last_to_first[last]:
            last_to_first[last].append(first_name)

        for friend in person_to_friends[name]:
            last2 = friend.split()[-1]
            first_name2 = friend[:-len(last2) - 1]
            if last2 not in last_to_first:
                last_to_first[last2] = [first_name2]
            elif first_name2 not in last_to_first[last2]:
                last_to_first[last2].append(first_name2)
                
    for key in last_to_first:
        last_to_first[key].sort()
    
    return last_to_first    


def invert_and_sort(key_to_value: dict[object, object]) -> dict[object, list]:
    """Return key_to_value inverted so that each key in the returned dict
    is a value from the original dict (for non-list values) or each item from a
    value (for list values), and each value in the returned dict
    is a list of the corresponding keys from the original key_to_value.
    The value lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    >>> club_to_score = {'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}
    >>> invert_and_sort(club_to_score) == {
    ...  3: ['Parent Council'], 2: ['Orchestra', 'Smash Club']}
    True
    
    >>> file = open("profiles.txt")
    >>> P2CLUBS = load_profiles(file)[1]
    >>> invert_and_sort(P2CLUBS) == {
    ...  'Parent Teacher Association': ['Claire Dunphy', 'Gloria Pritchett'],
    ...  'Chess Club': ['Alex Dunphy', 'Manny Delgado'],
    ...  'Law Association': ['Mitchell Pritchett'],
    ...  'Orchestra': ['Alex Dunphy'],
    ...  'Clown School': ['Cameron Tucker'],
    ...  'Wizard of Oz Fan Club': ['Cameron Tucker'],
    ...  'Real Estate Association': ['Phil Dunphy']}
    True
    >>> file.close()
    """
    value_to_key = {}
    for key in key_to_value.keys():
        value = key_to_value[key]
        if type(value) != int:
            for val in value:
                if val not in value_to_key:
                    value_to_key[val] = [key]
                else:
                    value_to_key[val].append(key)     
        else:
            if value not in value_to_key:
                value_to_key[value] = [key]
            else:
                value_to_key[value].append(key)
    for val in value_to_key.values():
        val.sort()

    return value_to_key    


def helper_get_clubs_of_friends(person: str, club: str,
                                person_to_clubs: dict[str, list[str]],
                                clubs: list) -> None:
    """
    Update the list of clubs with the club.
    If the person is in the person_to_clubs, if the given club is not already 
    in the list associated with the given person and if the given club is not 
    in the list, appends it to the list of clubs.

    If the given person is not in the person_to_clubs, appends 
    the given club to the list of clubs if it is not already in the list.
    
    >>> clubs = []
    >>> helper_get_clubs_of_friends('Danny R Tanner', 
    ...  'Rock N Rollers', P2C, clubs)
    >>> clubs == ['Rock N Rollers']
    True
    """
    if person in person_to_clubs:
        if club not in clubs and club not in person_to_clubs[person]:
            clubs.append(club)
    else:
        if club not in clubs:
            clubs.append(club)


def get_clubs_of_friends(person_to_friends: dict[str, list[str]],
                         person_to_clubs: dict[str, list[str]],
                         person: str) -> list[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    
    >>> file = open("profiles.txt")
    >>> profile = load_profiles(file)
    >>> P2FRIENDS = profile[0]
    >>> P2CLUBS = profile[1]
    >>> get_clubs_of_friends(P2FRIENDS, P2CLUBS, 'Claire Dunphy')
    ['Law Association', 'Real Estate Association']
    >>> file.close()
    """
    clubs = []
    friends = person_to_friends[person]
    if person in person_to_friends:
        for friend in friends:
            if friend in person_to_clubs:
                for club in person_to_clubs[friend]:
                    helper_get_clubs_of_friends(person, club, 
                                                person_to_clubs, clubs)
    clubs.sort()
    return clubs   
  
    
def helper_recommend_clubs1(score: int, friend: str, club: str, person: str,
                            person_to_clubs: dict[str, list[str]]) -> tuple:
    """
    Return a tuple containing `club` and `score`. Add 1 to the `score` 
    if the friend is a member of the `club` and 
    if the `person` has the same club as `friend`.
    
    >>> helper_recommend_clubs1(1, 'Kimmy Gibbler',
    ...  'Rock N Rollers', 'Stephanie J Tanner', P2C)
    ('Rock N Rollers', 2)
    """
    if friend in person_to_clubs and club in person_to_clubs[friend]:
        score += 1
        if person in person_to_clubs:
            for person_club in person_to_clubs[person]:
                if person_club in person_to_clubs[friend]:
                    score += 1 
    return (club, score)
    
    
def helper_recommend_clubs2(person: str, person_club1: str, 
                            new_club: None, score2: int,
                            person_to_clubs: dict[str, list[str]]) -> tuple:
    """
    Return a tuple containing `new_club` and `score2`. Add 1 to the `score2` 
    if person's friend and person has the same club but person's friend has
    other different club with the person.
    
    >>> helper_recommend_clubs2('Jesse Katsopolis', 'Rock N Rollers', 
    ...  'Smash Club', 0, P2C)
    ('Smash Club', 1)
    """
    for people_names in person_to_clubs:
        if person_club1 in person_to_clubs[people_names]: 
            for friends_club in person_to_clubs[people_names]:
                if friends_club not in person_to_clubs[person]:
                    new_club = friends_club
                    score2 += 1 
    return (new_club, score2)
    
    
def recommend_clubs(
        person_to_friends: dict[str, list[str]],
        person_to_clubs: dict[str, list[str]],
        person: str) -> list[tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    
    >>> recommend_clubs(P2F, P2C, 'Jesse Katsopolis')
    [('Comics R Us', 2), ('Smash Club', 1)]
    
    >>> file = open("profiles.txt")
    >>> profile = load_profiles(file)
    >>> P2FRIENDS = profile[0]
    >>> P2CLUBS = profile[1]
    >>> recommend_clubs(P2FRIENDS, P2CLUBS, 'Manny Delgado')
    [('Orchestra', 1), ('Parent Teacher Association', 1)]
    >>> file.close()
    """
    lst = []
    clubs = get_clubs_of_friends(person_to_friends, person_to_clubs, person) 
    friends = person_to_friends[person]
    for club in clubs:
        score = 0
        for friend in friends:
            tup = helper_recommend_clubs1(score, friend, club, person,
                                          person_to_clubs) 
            club = tup[0]
            score = tup[1]
        lst.append((club, score))
        
    new_club = None
    score2 = 0
    if person in person_to_clubs:    
        for person_club1 in person_to_clubs[person]:
            score2 = 0
            tup2 = helper_recommend_clubs2(person, person_club1, new_club, 
                                           score2, person_to_clubs)
            new_club = tup2[0]
            score2 = tup2[1]
            
        if new_club is not None:
            lst.append((new_club, score2))
    lst.sort()
    return lst


if __name__ == '__main__':

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    import doctest
    doctest.testmod()
