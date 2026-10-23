import random
import os

# -----------------------------
# TREASURE HUNTER
# -----------------------------

WIDTH = 12
HEIGHT = 8

player = {
    "x": 0,
    "y": 0,
    "health": 100,
    "gold": 0,
    "potions": 2,
    "score": 0
}

monsters = {}
treasures = set()
traps = set()

# Create random objects
for _ in range(5):
    pos = (random.randint(1, WIDTH - 1), random.randint(0, HEIGHT - 1))
    if pos != (0, 0):
        treasures.add(pos)

for _ in range(4):
    pos = (random.randint(1, WIDTH - 1), random.randint(0, HEIGHT - 1))
    if pos != (0, 0) and pos not in treasures:
        traps.add(pos)

monster_names = ["Goblin", "Skeleton", "Wolf", "Orc"]

for _ in range(4):
    pos = (random.randint(1, WIDTH - 1), random.randint(0, HEIGHT - 1))

    if (
        pos != (0, 0)
        and pos not in treasures
        and pos not in traps
        and pos not in monsters
    ):
        monsters[pos] = random.choice(monster_names)

exit_pos = (WIDTH - 1, HEIGHT - 1)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw():
    clear()

    print("=" * 45)
    print("       🏴 TREASURE HUNTER 🏴")
    print("=" * 45)

    print(
        f"❤️ Health: {player['health']}   "
        f"💰 Gold: {player['gold']}   "
        f"🧪 Potions: {player['potions']}   "
        f"⭐ Score: {player['score']}"
    )

    print()

    for y in range(HEIGHT):
        for x in range(WIDTH):

            pos = (x, y)

            if pos == (player["x"], player["y"]):
                print("🧙", end=" ")

            elif pos == exit_pos:
                print("🚪", end=" ")

            else:
                # Hide objects until discovered
                print("⬜", end=" ")

        print()

    print()
    print("W/A/S/D = Move   P = Potion   Q = Quit")


def battle(monster):
    monster_hp = random.randint(25, 45)

    print(f"\n⚔️ A {monster} attacks you!")
    print(f"{monster} HP: {monster_hp}")

    while monster_hp > 0 and player["health"] > 0:

        print("\n1. Attack")
        print("2. Run")
        choice = input("> ")

        if choice == "1":
            damage = random.randint(10, 25)
            monster_hp -= damage

            print(f"You hit the {monster} for {damage} damage!")

            if monster_hp <= 0:
                reward = random.randint(15, 40)
                player["gold"] += reward
                player["score"] += 50

                print(f"🎉 You defeated the {monster}!")
                print(f"💰 You found {reward} gold!")
                return True

            enemy_damage = random.randint(5, 18)
            player["health"] -= enemy_damage

            print(
                f"The {monster} hits you for "
                f"{enemy_damage} damage!"
            )

        elif choice == "2":
            if random.random() < 0.5:
                print("🏃 You escaped!")
                return False
            else:
                print("❌ You couldn't escape!")

                enemy_damage = random.randint(5, 15)
                player["health"] -= enemy_damage
                print(f"The {monster} hits you for {enemy_damage} damage!")

        else:
            print("Invalid choice.")

    return False


def check_location():

    pos = (player["x"], player["y"])

    # Treasure
    if pos in treasures:
        treasures.remove(pos)

        gold = random.randint(20, 60)
        player["gold"] += gold
        player["score"] += 25

        print(f"\n💎 TREASURE FOUND!")
        print(f"You found {gold} gold!")

    # Trap
    if pos in traps:
        traps.remove(pos)

        damage = random.randint(10, 30)
        player["health"] -= damage
        player["score"] -= 10

        print(f"\n💥 TRAP!")
        print(f"You lost {damage} health!")

    # Monster
    if pos in monsters:
        monster = monsters.pop(pos)
        battle(monster)


def use_potion():
    if player["potions"] <= 0:
        print("\n❌ You have no potions!")
        return

    if player["health"] >= 100:
        print("\n❤️ Your health is already full!")
        return

    player["potions"] -= 1

    healing = random.randint(20, 40)
    player["health"] = min(100, player["health"] + healing)

    print(f"\n🧪 You recovered {healing} health!")


def game_over():
    clear()

    print("=" * 45)
    print("             GAME OVER")
    print("=" * 45)

    print(f"\n⭐ Final Score: {player['score']}")
    print(f"💰 Gold Collected: {player['gold']}")

    if player["health"] <= 0:
        print("\n💀 You were defeated!")

    input("\nPress ENTER to exit...")


def victory():
    clear()

    print("=" * 45)
    print("          🏆 YOU ESCAPED! 🏆")
    print("=" * 45)

    print("\nYou found the exit and escaped the dungeon!")
    print(f"\n💰 Gold: {player['gold']}")
    print(f"⭐ Score: {player['score']}")

    # Bonus for remaining health
    bonus = player["health"] * 2
    player["score"] += bonus

    print(f"❤️ Health Bonus: +{bonus}")
    print(f"\n🏆 FINAL SCORE: {player['score']}")

    input("\nPress ENTER to exit...")


# -----------------------------
# MAIN GAME LOOP
# -----------------------------

while True:

    draw()

    if player["health"] <= 0:
        game_over()
        break

    if (player["x"], player["y"]) == exit_pos:
        victory()
        break

    move = input("\nYour move: ").lower()

    if move == "q":
        print("\nThanks for playing!")
        break

    if move == "p":
        use_potion()
        input("\nPress ENTER...")
        continue

    new_x = player["x"]
    new_y = player["y"]

    if move == "w":
        new_y -= 1
    elif move == "s":
        new_y += 1
    elif move == "a":
        new_x -= 1
    elif move == "d":
        new_x += 1
    else:
        print("\n❌ Invalid command!")
        input("Press ENTER...")
        continue

    # Keep player inside map
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        player["x"] = new_x
        player["y"] = new_y

        check_location()

        input("\nPress ENTER to continue...")

    else:
        print("\n🧱 You can't walk through the wall!")
        input("Press ENTER...")