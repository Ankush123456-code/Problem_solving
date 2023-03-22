import csv
import json
from typing import List


class NestedDataIngestion:
    def __init__(self, data: List[dict]):
        self.data = data

    def flatten_dict(self, d, parent_key='', sep='_'):
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, dict):
                yield from self.flatten_dict(v, new_key, sep=sep)
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    yield from self.flatten_dict(item, new_key + sep + str(i), sep=sep)
            else:
                yield new_key, v

    def write_csv(self, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.get_fieldnames())
            for d in self.data:
                flat_dict = dict(self.flatten_dict(d))
                writer.writerow(flat_dict.values())

    def get_fieldnames(self):
        fieldnames = set()
        for d in self.data:
            for k, v in self.flatten_dict(d):
                fieldnames.add(k)
        return sorted(fieldnames)


# Example usage
nested_data = [
    {
        "id": 1,
        "name": {
            "first": "John",
            "last": "Doe"
        },
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        },
        "phone_numbers": [
            {
                "type": "home",
                "number": "555-555-1234"
            },
            {
                "type": "work",
                "number": "555-555-5678"
            }
        ]
    },
    {
        "id": 2,
        "name": {
            "first": "Jane",
            "last": "Smith"
        },
        "age": 25,
        "address": {
            "street": "456 Elm St",
            "city": "Othertown",
            "state": "NY",
            "zip": "67890"
        },
        "phone_numbers": [
            {
                "type": "home",
                "number": "555-555-4321"
            },
            {
                "type": "work",
                "number": "555-555-8765"
            }
        ]
    }
]

nested_data_ingestion = NestedDataIngestion(nested_data)
nested_data_ingestion.write_csv('nested_data.csv')
