import requests
import csv
import logging as log
import inspect

from APIGetCSVWrite.constants import LOGS_DIR
log.basicConfig(filename=LOGS_DIR + 'API.log', level=log.INFO, datefmt='%Y-%m-%d %H:%M:%S')


# def log_args(func):
#
#     """This decorator dumps out the arguments passed to a function before calling it"""
#     argnames = func.fund_code.co_varnames[:func.func_code.co_argcount]
#     fname = func.func_name
#
#     def echo_func(*args, **kwargs):
#         print(
#             fname, "(", ', '.join(
#                 '%s=%r' % entry
#                 for entry in zip(argnames, args[:len(argnames)]) + [("args", list(args[len(argnames):]))] + [
#                     ("kwargs", kwargs)]) + ")")
#     return echo_func


class APIHelper:

    def __init__(self, url):
        self.url = url
        self.columns = ["name", "height", "gender"]

    def star_wars_characters(self):
        api_response = requests.get(self.url)
        if api_response.status_code == 200:
            output = []
            for column_val in api_response.json()['results']:
                output.append([x for x in map(lambda x: column_val[x], self.columns)])
            return output

        else:
            return api_response.reason

    # @log_args
    def append_to_file(self, file_path):
        # file_path = os.path.join('outputs/' + file_path)
        with open(file_path, "w") as file_w:
            csv_file = csv.writer(file_w, delimiter=',')
            csv_file.writerow([x.title() for x in self.columns])
            for row in self.star_wars_characters():
                csv_file.writerow(row)
        log.info("Finished writing to file : {}".format(file_path))
        file_w.close()

# url = "https://swapi.dev/api/people/"
# o_file_name = 'output_001.csv'
#
# obj = APIHelper(url)
#
# api_o = obj.star_wars_characters()
# obj.append_to_file(o_file_name)
