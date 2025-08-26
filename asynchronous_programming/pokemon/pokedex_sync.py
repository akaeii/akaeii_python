import httpx
import time


def read_list(list_dir):
    with open(list_dir, "r") as file:
        lines = file.readlines()
        pokemon_list = [line.strip().replace(" ", "") for line in lines]
    return pokemon_list


def fetch_pokemon(name, client):
    print(f"Fetching {name}...")
    response = client.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")

    if response.status_code != 200:
        poke_type = "n/a"

    else:
        data = response.json()
        poke_type = data["types"][0]["type"]["name"]

    print(f"Done with {name}")
    return poke_type


def main(pokemon_list):
    pokemon_list = read_list("./pokemon_list.txt")

    with httpx.Client() as client:
        requests = [fetch_pokemon(name, client) for name in pokemon_list]

    return requests


if __name__ == "__main__":
    start = time.perf_counter()
    pokemon_list = read_list("./pokemon_list.txt")
    results = main(pokemon_list)
    end = time.perf_counter()

    print(f"Execution of main took {end-start} seconds")

    with open("pokedex_sync_results.txt", "w") as file:
        file.write("pokemon name - type\n")
        for n, t in zip(pokemon_list, results):
            file.write(f"{n} - {t}\n")
        file.write(f"Execution of main took {end-start} seconds")
