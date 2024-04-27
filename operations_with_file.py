import csv


def create_file():
    with open('data_base_file.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "item's link",
                "item's name",
                "Hero name",
                "Type of the item",
                "item's price",
                "min price",
                "max price",
                "avg price",
                "buys call"
            )
        )


def write_in_file(link, item_name, hero_name, item_type, curr_price, min_price, max_price, avg_price, buys_call):
    with open('data_base_file.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                link,
                item_name.replace('\n', ''),
                hero_name.replace('\n', ''),
                item_type.replace('\n', ''),
                curr_price.replace('\n', ''),
                min_price.replace('\n', ''),
                max_price.replace('\n', ''),
                avg_price.replace('\n', ''),
                buys_call.replace('\n', ''),
            )
        )