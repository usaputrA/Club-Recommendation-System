# Club-Recommendation-System
Clubs that a person may be interested in joining will be recommended by the program, based on the scoring system described below, which is a club recommendation system for a social network. 

For further program, kindly check out `club_functions.py`.

## Recommendation score
Imagine that a person wants to get recommendations for potential clubs — clubs they are not a member of but may wish to join. The social network calculates a recommendation score for each potential club.

For a particular person, each potential club starts out with a score of 0 and is scored using the following point system:

* Add 1 point to the potential club’s score for each of the person's friends who is a member of the potential club.
* Add 1 point for every member of the potential club, who is in at least one different club with the person.
Examples: refer to the diagram below, which represents the data in P2F (i.e., a constant value for a "person to friend" dictionary) and P2C (i.e., a constant value for a "person to club" dictionary) in the starter code:
![image](https://user-images.githubusercontent.com/120763767/234979620-d30c31b0-7118-4af2-9fcf-f7e802132f46.png)

When making recommendations for Jesse Katsopolis, the result is: [('Comics R Us', 2), ('Smash Club', 1)]

Comics R Us gets one point because Jesse Katsopolis's friend Joey Gladstone is a member of Comics R Us.
Comics R Us gets a second point because Joey is a member of Comics R Us and both Jesse and Joey are members of Parent Council.
Smash Club gets one point because Kimmy is a member of Smash Club and Kimmy is in a different club (Rock N Rollers) with Jesse.
When making recommendations for Stephanie J Tanner, the result is: [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]

* Comet Club gets one point because Stephanie's friend Michelle Tanner is a member of Comet Club.
* Smash Club gets one point because Stephanie's friend Kimmy Gibbler is a member of Smash Club.
* Rock N Rollers gets one point because Stephanie's friend Kimmy Gibbler is a member of Rock N Rollers.
