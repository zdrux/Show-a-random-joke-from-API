# Joke endpoint:
# https://sv443.net/jokeapi/v2/joke
#
# Categories list endpoints:
# https://sv443.net/jokeapi/v2/categories
#
# Joke types:
# single, twopart

from requests import get

# Define API url
apiUrl = "https://sv443.net/jokeapi/v2"

# Get list of categories from API
get_categories = get(apiUrl + "/categories")

# Convert categories from json to dictionary
categories_dict = get_categories.json()["categories"]

# Show user enumerated category list
def show_categories():
  for count, choice in (enumerate(categories_dict, 1)):
    print(count, choice)

# Main function to retrieve the joke based on category and joke "type"
def get_joke(category, type):
  if type == 1:
    result = get(apiUrl + "/joke/" + category + joke_type)
    joke = result.json()
    return "\n" + joke["joke"] + "\n\n"

  elif type == 2:
    result = get(apiUrl + "/joke/" + category + joke_type)
    joke = result.json()
    return "\n" + joke["setup"] + "\n" + joke["delivery"] + "\n\n"


# Main function
def main():
  show_categories()
  category_num = int(input("Enter selection: "))
  if category_num > len(categories_dict):
    print("\n\n" + "Wrong entry, try again!")
    main()

  print("\nJoke types:")
  print("1. Single")
  print("2. Two part")

  # Below section will alter the API url based on anser of joke "type"
  my_type = int(input("Enter joke type (ENTER for ""any"":) "))
  if my_type != 1 or 2:
    print("\n\n" + "Wrong entry, try again!")
    main()
  global joke_type
  if my_type == 1:
    joke_type = "?type=single"
  elif my_type == 2:
    joke_type = "?type=twopart"  
  else:
    joke_type = ""
  
  # Print result
  print(get_joke(categories_dict[category_num -1], my_type))

# Run main() on loop
while True:
  main()
