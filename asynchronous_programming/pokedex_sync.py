import httpx
import time


def read_list(list_dir):
    with open(list_dir, "r") as file:
        lines = file.readlines()
        pokemon_list = [line.strip() for line in lines]
    return pokemon_list


def fetch_pokemon(name):
    print(f"Fetching {name}...")
    with httpx.Client() as client:
        response = client.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        print(response.status_code)


def main(list_dir):
    pokemon_list = read_list(list_dir)

    for name in pokemon_list:
        fetch_pokemon(name)


if __name__ == "__main__":
    start = time.perf_counter()
    (main("./pokemon_list.txt"))
    end = time.perf_counter()

    print(f"Execution of main took {end-start} seconds")
