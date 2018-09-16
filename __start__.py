
# encrypting
"""
1. Check if en


"""
# 1 check if encrypted exits ()


import os
import crypto




bib_name = 'Tools_e'


# def file_walker(path):
#     for entry in os.scandir(path):
#         if entry.is_dir(follow_symlinks=False):
#             yield from file_walker(entry.path)
#         else:
#             yield entry.path


def dir_encrypt(key):
    base_dir = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-1])
    bib_dir = base_dir + os.sep + bib_name

    if os.path.exists(base_dir + os.sep + bib_name):
        # clear current dataset
        def walker(path):
            for entry in os.scandir(path):
                if entry.is_dir():
                    walker(entry.path)
                    os.rmdir(entry.path)
                else:
                    os.remove(entry.path)
        walker(bib_dir)
    else:
        os.mkdir(bib_dir)

    def walker(path):
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                if entry.name != bib_name and not entry.name.startswith('.'):
                    # genuine dir
                    enc_dir = entry.path.replace(base_dir, bib_dir)
                    if not os.path.exists(enc_dir):
                        os.mkdir(entry.path.replace(base_dir, bib_dir))
                    walker(entry.path)
            else:
                print("should encrypt file %s" % entry.path)
    walker(base_dir)

    def file_encrypt(path):
        pass


if __name__ == "__main__":
    dir_encrypt("halloDu")


