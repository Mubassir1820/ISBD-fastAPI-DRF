#  sort ja list (descending order)
ls = [10, 1, 25, 75, 30, 15]

#  way-1

ite = reversed(sorted(ls))
rev_ls = list(ite)
print(rev_ls)


# way - 2

new_ls = sorted(ls, reverse=True)
print(new_ls)
