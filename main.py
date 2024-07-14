import csv


class Record:
    def __init__(self, headers: list):
        self.headers = headers
        self.data = {header: [] for header in headers}

    def add_record(self, record: list):
        for header, value in zip(self.headers, record):
            self.data[header].append(value if value != '' else None)
        for i in range(len(record), len(self.headers)):
            self.data[self.headers[i]].append(None)

    def __setattr__(self, name, value):
        if name in ('headers', 'data'):
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Cannot add new attribute '{name}'")


def read_file(file_path: str) -> Record:
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            record_obj = Record(headers)
            for row in reader:
                record_obj.add_record(row)
        return record_obj
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def print_records(record_obj: Record):
    if not record_obj:
        print("No records to display.")
        return
    try:
        headers = record_obj.headers
        print(', '.join(headers))
        rows = zip(*[record_obj.data[header] for header in headers])
        for row in rows:
            print(', '.join(map(str, row)))
    except Exception as e:
        print(f"Error printing records: {e}")


def add_record(file_path: str, new_record: list):
    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(new_record)
    except Exception as e:
        print(f"Error adding record: {e}")



if __name__ == "__main__":
    file_path = 'C:\\Users\\ahmed\\PycharmProjects\\csvKullanımı\\worker.txt'

    record_obj = read_file(file_path)
    print_records(record_obj)

    new_record = ['new_value1', 'new_value2', 'new_value3']
    add_record(file_path, new_record)
