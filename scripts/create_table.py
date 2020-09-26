"""
    Creates the markdown tables for the urls

    @F1r3f0x - 2020
"""

INSTANCE_URL = 'https://na1.salesforce.com/'

def create_table():
    urls = []
    with open('urls.txt', 'r') as f_obj:
        for line in f_obj:
            stripped = line.strip()
            urls.append(f'| {stripped} | ![icon]({INSTANCE_URL}{stripped})\n')

    header = '| URL | Icon|\n'
    separator = '|-|-|\n'
    with open('table.md', 'w') as f_obj:
        f_obj.write(header)
        f_obj.write(separator)
        f_obj.writelines(urls)

if __name__ == '__main__':
    create_table()
