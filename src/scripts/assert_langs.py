import numpy as np
from populate import read_json

if __name__ == "__main__":

    profiles_en = read_json("../assets/researchers_en.json")
    profiles_ar = read_json("../assets/researchers_ar.json")

    keys = np.array(sorted(list(profiles_en[0].keys()))).astype(str)

    for profile in profiles_ar:
        p_keys = np.array(sorted(list(profile.keys()))).astype(str)
        if len(keys) != len(p_keys) or not all(keys == p_keys):
            print(profile["name"])

    for p_en, p_ar in zip(profiles_en, profiles_ar):
        assert p_en["hindex"] == p_ar["hindex"]
        assert p_en["citedby"] == p_ar["citedby"]

