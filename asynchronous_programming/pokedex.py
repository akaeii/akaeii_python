import asyncio
import time
import httpx


def read_list(list_dir):
    with open(list_dir, "r") as file:
        lines = file.readlines()
        pokemon_list = [line.strip() for line in lines]
    return pokemon_list


async def fetch_pokemon(name, client):
    print(f"Fetching {name}...")
    response = await client.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")

    if response.status_code != 200:
        poke_type = "n/a"

    else:
        data = response.json()
        poke_type = data["types"][0]["type"]["name"]

    print(f"Done with {name}")
    return poke_type


async def main(list_dir):
    async with httpx.AsyncClient() as client:
        coroutines = [fetch_pokemon(name, client) for name in pokemon_list]
        results = await asyncio.gather(*coroutines, return_exceptions=True)

    return results


if __name__ == "__main__":
    start = time.perf_counter()

    pokemon_list = read_list("./pokemon_list.txt")
    results = asyncio.run(main(pokemon_list))

    end = time.perf_counter()

    print(f"Execution of main took {end-start} seconds")

    for n, t in zip(pokemon_list, results):
        print(n, t)
