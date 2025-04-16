print('''Welcome to the Zayan's game of Tresure Island!
               __________
        /\____;;___
       | /         /
       `. ())oo() .
        |\(%()*^^()^
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''');
print("You gotta find a treassure constantly choosing for a ways to go/do");

res1 = input("You arrive at a crossroad after arriving to the area, and eventually it shows two ways, both to the treasure," \
" yet right one seems makeshift, done in hurry. Where do you wanna go?: ").lower()
if res1 == "left":
    # LAKE
    res2 = input("You passing further. There lake appears between the trees, a boat stands, tied to the bridge. " \
    "Otherwise you can go other way around the lake"
    " around or Boat: ");
    if res2 == "around":
        print("You passed around the lake a little, everything seems safe");
        # THE DOORS
        res3 = input("After passing further, you notice three houses with three doors, Red, yellow and Blue, which one do you think smells like gold?"
        " Red, Blue or yellow?").lower()
        if res3 == "yellow":
            print("yellow, smells like gold and money, you find the treasure chest, good job, you won!");
        elif res3 == "red":
            print == "You enter a red door, bloody red, and smells like blood, and well...game over."
        elif res3 == "blue":
            print("The blue one smells like sulfur, and leads to a blue portal to the demon world, where demons eat you. Game over");
    elif res2 == "boat":
        print("You passed to the middle of the lake, but eventually water turned dark, and kraken appeared and ate you");
    else:
        print("You made an absolutely wrong step and stepped into swampy area, although - died");

elif res1 == "right":
    print("You fell into a pit on the way, hidden under leaves, goblins come out to kill you. Game over.");
else:
    print("Game over.")