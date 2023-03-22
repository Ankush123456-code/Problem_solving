import luigi
import pandas as pd
from pymongo import MongoClient

from Luigi_tutorial.Model import Model


class LoadMetadata(luigi.Task):
    """Task to load metadata from a CSV file"""
    file_path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.file_path)

    def run(self):
        metadata = pd.read_csv(self.file_path)
        with self.output().open('w') as f:
            metadata.to_csv(f, index=False)


class IngestMetadata(luigi.Task):
    """Task to ingest metadata into MongoDB"""
    file_path = luigi.Parameter()

    def requires(self):
        return LoadMetadata(file_path=self.file_path)

    def run(self):
        try:
            db = Model()
            i = 0
            with self.input().open('r') as f:
                metadata = pd.read_csv(f)
                for index, row in metadata.iterrows():
                    metadata_dict = row.to_dict()
                    db.put_one({"_id": f"row{i}", "data": metadata_dict})
                    i += 1
        except:
            print("Failed")
            return


if __name__ == '__main__':
    # host = "mongodb+srv://Ankush:Ankush@cluster0.tpvyynu.mongodb.net/?retryWrites=true&w=majority"
    luigi.build([IngestMetadata(file_path='train.csv')], local_scheduler=True)
