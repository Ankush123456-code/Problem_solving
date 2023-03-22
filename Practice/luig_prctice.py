# import luigi
#
#
# class PrintNumbers(luigi.Task):
#     n = luigi.IntParameter()
#
#     def run(self):
#         for i in range(self.n):
#             print(i)
#
#     def complete(self):
#         return False
#
#
# class SquaredNumbers(luigi.Task):
#     n = luigi.IntParameter()
#
#     def requires(self):
#         return PrintNumbers(n=self.n)
#
#     def run(self):
#         for i in range(self.n):
#             print(i ** 2)
#
#     def complete(self):
#         return False
#
#
# if __name__ == '__main__':
#     luigi.run()
def improt_module():
    pass


repo = getattr(improt_module, "hello")(
    1, 3

)
print(repo)