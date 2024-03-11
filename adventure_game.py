# Define locations and their descriptions
locations = {
  "Start": "You stand at the entrance of a dark forest. A path leads north and a faint light flickers in the east.",
  "North": "You venture deeper into the forest. The trees grow denser and the air chills you. To the west, you see a small clearing.",
  "East": "Following the light, you arrive at a crumbling stone bridge. The bridge spans a wide river, but its condition is uncertain. To the south, you see the path you came from.",
  "West": "Emerging from the trees, you find yourself in a clearing. A small hut sits nestled amongst the trees. To the east, the path leads back into the forest.",
  "Bridge": "You stand on the crumbling bridge. The river roars below. To the west, you see the clearing. To the east, the bridge leads across the river.",
  "End": "Congratulations! You've crossed the bridge and reached the other side. You see a village nestled in the distance."
}

# Define valid exits for each location
exits = {
  "Start": {"north": "North", "east": "East"},
  "North": {"west": "West", "east": "Start"},
  "East": {"south": "Start", "east": "Bridge"},
  "West": {"east": "North"},
  "Bridge": {"west": "West", "east": "End"}
}

# Current location
current_location = "Start"

# Game loop
while True:
  # Print current location description
  print(locations[current_location])

  # Display available exits
  available_exits = ", ".join(exits[current_location].keys())
  print(f"Available exits: {available_exits}")

  # Get user input for next move
  next_move = input("Enter your next move (north, east, south, west): ").lower()

  # Check if chosen exit is valid
  if next_move in exits[current_location]:
    current_location = exits[current_location][next_move]
  else:
    print("Invalid exit. Please choose from the available options.")

  # Check if the game ends
  if current_location == "End":
    print("You have won the game!")
    break
