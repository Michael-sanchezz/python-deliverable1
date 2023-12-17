name = input("Welcome to GC mini golf! What is your name? ")
print("Hello " + name)
hole_count = input("would you like to play 3 or 6 holes today? ")
end_score = 0
put_score = 0
hole_count = int(hole_count)
if hole_count == 3:
    end_score = 9
    for x in range(0, hole_count):
        temp_score = input(f"how many puts for hole  {x + 1}? ")
        put_score = put_score + int(temp_score)
    if put_score < end_score:
        end_score = (end_score - put_score) * -1
        print(f"Great job, {name} Your total score was {end_score}")
    elif put_score > end_score:
        end_score = (end_score - put_score) * -1
        print(f"Nice try, {name}! Your total score is +{end_score}")
    else:
        print(f"Good game, {name}. Your total score was: 0.")
elif hole_count == 6:
    end_score = 18
    for x in range(0, hole_count):
        temp_score = input(f"how many puts for hole  {x + 1}? ")
        put_score = put_score + int(temp_score)
    if put_score < end_score:
        end_score = (end_score - put_score) * -1
        print(f"Great job, {name} Your total score was {end_score}")
    elif put_score > end_score:
        end_score = (end_score - put_score) * -1
        print(f"Nice try, {name}! Your total score is {end_score}")
    else:
        print(f"Good game, {name}. Your total score was: 0.")
else:
    print("Not a valid entry")
