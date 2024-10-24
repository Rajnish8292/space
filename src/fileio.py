# """

# code         error
# -1            error while opening the file
# -2            error while reading the file

# """

# class opener():
#     __output = None
#     __mode = "r"
#     def __init__(self) -> None:
#         pass

#     def get(self, path, mode = __mode):
#         try:
#             file_ = open(path, mode)
#             try:
#                 __output = file_.read()
#             except:
#                 pass
#                ## __output = -2
#         except:
#             pass
           
#            ##__output = -1

#         return __output

# fileio = opener()

# output = fileio.get("something.txt")

# print(output)


