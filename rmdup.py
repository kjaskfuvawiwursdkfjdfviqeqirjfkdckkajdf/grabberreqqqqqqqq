#!/usr/bin/env python

import timeit
import os

overwriteMode = True


def f7(seq):
    """
    The following function f7 is from this file.
    www.peterbe.com/plog/uniqifiers-benchmark/uniqifiers_benchmark.py
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def Convsize(filename):
    """
    Converts file size from bytes to a human-readable format (KB or MB).
    """
    filesize = os.path.getsize(filename) / 1024.0
    if len(str(int(filesize))) >= 3:
        return "%.2f MB" % (filesize / 1024.0)
    else:
        return "%.2f KB" % filesize


def main(filename):
    print("[+] Original File Size : %s" % Convsize(filename))

    start_time = timeit.default_timer()
    with open(filename, encoding="utf-8", errors="ignore") as file:
        content = [line.strip() for line in file]
    org_len = len(content)

    result = f7(content)
    stop_time = timeit.default_timer()
    duration = "%.5f" % (stop_time - start_time)
    result_len = len(result)

    if org_len != result_len:
        print("[+] Processed : [%s] Lines in %s seconds" % (org_len, duration))
        print("[+] <{:,}> duplicates found".format(org_len - result_len))
        newfilename = filename if overwriteMode else filename.replace('.txt', '-no-dup.txt')
        with open(newfilename, 'w') as newfile:
            for line in result:
                newfile.write(line + '\n')
        print("[+] Saved as %s" % newfilename)
        print("[+] New File Size : %s" % Convsize(newfilename))
    else:
        print("[+] Processed : [%s] Lines in %s seconds" % (org_len, duration))
        print("[+] No Duplicates found")


if __name__ == "__main__":
    filename = input("[+] Submit file yang ingin kamu hapus duplikatnya: ")
    if os.path.isfile(filename):
        main(filename)
    else:
        print(f"[!] File '{filename}' tidak ditemukan.")
