import json
import os

# Helper function to extract usernames from JSON file
def extract_usernames(file_path, key=None):
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return []
    
    with open(file_path) as f:
        data = json.load(f)
    
    usernames = []

    if key:
        if key in data:
            data = data[key]  # Move deeper into the JSON using the key
        else:
            print(f"Error: Key '{key}' not found in the data.")
            return []
    
    # Extract usernames from "string_list_data"
    for entry in data:
        if "string_list_data" in entry:
            for user in entry["string_list_data"]:
                usernames.append(user["value"].lower().strip())  # Extract username and clean it
        else:
            print(f"Warning: 'string_list_data' not found in entry: {entry}")
    
    return usernames

# File paths
followers_file = r'path/to/your/followers.json'
following_file = r'path/to/your/following.json'

# Extract followers and following usernames
follower = extract_usernames(followers_file)  # No additional key needed
following = extract_usernames(following_file, "relationships_following")  # add key parameter if needed

# Print first 10 entries for review / debug if the data can't be read
print("Followers (first 10):", follower[:10])
print("Following (first 10):", following[:10])

# Conditional to find users who have unfollowed you
unfollowers = [user for user in follower if user not in following]

# Show unfollowers
print("Unfollowers (users who no longer follow you):", unfollowers)
if unfollowers:
    for person in unfollowers:
        print(f"https://www.instagram.com/{person}")
else:
    print("No unfollowers found.")
