def revnum(num):
    str_num = str(num)
    rev_num = str_num[::-1]
    return rev_num


if __name__ == "__main__" :
    rev = revnum(9876543210)
    print(rev)