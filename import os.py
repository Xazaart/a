import os
import string


# with open(r"c:\Users\Admin\Desktop\aaaa\as.txt", 'r') as fp:
#     l = len(fp.readlines())
#     print(l)

# with open(r"c:\Users\Admin\Desktop\aaaa\as.txt", 'w') as fp:
#     l = ["aaaa", "bbbb", 1111]
#     fp.writelines(f"{item}" for item in l)

# folder = r"c:\Users\Admin\Desktop\aaaa"
# for letters in string.ascii_uppercase:
#     with open(os.path.join(folder, f"{letters}.txt"), "a") as f:
#         f.write("1")

# a = r"C:\Users\Admin\Desktop\aaaa\as.txt"
# b = r"C:\Users\Admin\Desktop\aaaa\aaaabbbb1111d.txt"
# with open(a, "r") as f, open(b, "w") as s:
#     for line in f:
#         s.write(line)

def l(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            return "Yes"
        else: return "No"
    else: return "No"
a = input()
print(l(a))







