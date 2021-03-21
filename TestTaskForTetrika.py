import requests

WIKIPEDIA_API_URL = "https://ru.wikipedia.org/w/api.php"


def get_first_null_index(num):
    low = 0
    high = len(num) - 1
    mid = len(num) // 2
    while low < high:
        if num[mid] == '0':
            high = mid
        else:
            low = mid + 1
        mid = (low + high) // 2
    return low if num[low] == '0' else "no null value"


def print_first_letters_number_in_category(category):
    # create russian alphabet dict
    a = ord('А')
    titles_count = {chr(i): 0 for i in range(a, a+6)}
    titles_count.update({"Ё": 0})
    titles_count.update({chr(i): 0 for i in range(a+6, a+32)})

    s = requests.Session()

    params = {
        "action": "query",
        "format": "json",
        "list": "categorymembers",
        "cmtitle": category,
        "cmprop": "title",
        "cmlimit": "max",
    }

    while True:
        r = s.get(url=WIKIPEDIA_API_URL, params=params)
        data = r.json()
        pages = data["query"]["categorymembers"]
        for page in pages:
            first_letter = page["title"][0]
            if first_letter in titles_count:
                titles_count[first_letter] += 1
        if "continue" not in data:
            break
        params["cmcontinue"] = data["continue"]["cmcontinue"]

    for letter, count in titles_count.items():
        print(f"{letter}: {count}")


if __name__ == '__main__':
    print(get_first_null_index("111111111100000000"))
    print_first_letters_number_in_category('Категория:Животные по алфавиту')
