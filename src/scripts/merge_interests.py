from populate import read_json


if __name__ == "__main__":

    researchers = read_json('./assets/researchers_en.json')
    interests = set()
    for person in researchers:
        for interest in person["interests"]:
            interests.add(interest)

    interests = sorted(interests)

    interests_map = read_json("./assets/interests_map.json")
    print(f"Before: {len(interests)} | After: {len(interests_map)}")
