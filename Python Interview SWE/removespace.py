#Python program to remove blank space from a string.

def rem_blank_space(string):
    removed_space = string.replace(" ","")
  
    return removed_space

if __name__ == "__main__":
    string = "abc def ghi jkl mno pqr stu vwxyz"
    print(rem_blank_space(string))