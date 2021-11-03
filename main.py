import pathlib
import os
from datetime import datetime, timedelta


# get all files in target directory
def create_file_list(target_dir: str, search_term: str) -> list:
    results = list(pathlib.Path(target_dir).glob(f"**/{search_term}"))
    return results


# filter function
# Takes ctime and target days
def is_older(item: str, days: int) -> str:
    target_days = days if days > 0 else 0
    if os.path.getctime(item) < (datetime.utcnow() - timedelta(days=target_days)).timestamp():
        return item
    else:
        return ""


# filter all items older than X time
def filter_by_datetime(coll: list, target_days: int) -> filter:
    results = filter(lambda x: is_older(x, target_days), coll)
    return results


# delete each item
def remove_items(coll: filter) -> str:
    for item in coll:
        print(f"Would os.remove() : {item}")

    return "Files deleted"


def main(target_dir: str):
    results = remove_items(filter_by_datetime(create_file_list(target_dir, "*"), 0))
    print(results)


if __name__ == "__main__":
    main(".")
