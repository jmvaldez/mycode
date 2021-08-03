#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "Peter Quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "Raven Darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "Jennifer Walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
 }


char_name = input(" Which character do you want to know about? (Starlord, Mystique, She-Hulk)")

char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy")
        
print(f"{char_name.title()}'s {char_stat} is: {marvelchars[char_name].get(char_stat)} ")


