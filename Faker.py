from faker import Faker
import csv

faker = Faker()
keys = ['ID', 'NAME', 'JOB', 'PHONE NUMBER', 'COUNTRY', 'ADDRESS', 'EMAIL', 'SALARY']

def generate_fake_data(rows):
    data = []
    for _ in range(rows):
        list_data = {
            'ID': faker.random_int(min=1, max=10000),
            'NAME': faker.name(),
            'JOB': faker.job(),
            'PHONE NUMBER': faker.phone_number(),
            'COUNTRY': faker.country(),
            'ADDRESS': faker.address(),
            'EMAIL': faker.email(),
            'SALARY': str(faker.random_int(min=10000, max=100000)) + '$'
        }
        data.append(list_data)
    return data

def write_to_csv(file, data):
    with open(file, mode='w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(data)

def main():
    file = input("Enter The File Name: ")
    rows = int(input("Enter The Number Of Rows: "))
    data = generate_fake_data(rows)
    write_to_csv(file, data)

if __name__ == "__main__":
    main()