import luigi
import pandas as pd


class ReadDataTask(luigi.Task):
    """Task to read data from a source"""
    file_path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.file_path)

    def run(self):
        data = pd.read_csv(self.file_path)
        with self.output().open('w') as f:
            f.write(data.to_csv(index=False))


class TransformDataTask(luigi.Task):
    """Task to transform data"""
    file_path = luigi.Parameter()

    def requires(self):
        return ReadDataTask(file_path=self.file_path)

    def output(self):
        return luigi.LocalTarget(self.file_path.replace('.csv', '_transformed.csv'))

    def run(self):
        with self.input().open('r') as f:
            data = pd.read_csv(f)
            # perform transformations here
            transformed_data = data
        with self.output().open('w') as f:
            f.write(transformed_data.to_csv(index=False))


if __name__ == '__main__':
    luigi.build([TransformDataTask(file_path='data.csv')])
