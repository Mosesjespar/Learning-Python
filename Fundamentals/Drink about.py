# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

def people_with_age_drink(age):
    if age <= 13:
        return "drink toddy"
    elif age <= 17:
        return "drink coke"
    elif age <=20:
        return "drink beer"
    elif age >= 21:
        return "drink whisky"