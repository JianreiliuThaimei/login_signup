# 1. os.path.basename(path) : It is used to return the basename of the file . 
# This function basically return the file name from the path given. 
# import os
# out = os.path.basename("/baz/foo")
# print(out)

# 2. os.path.dirname(path):It is used to return the directory name from the path given.
# This function returns the name from the path except the path name. 
# import os
# out = os.path.dirname("/baz/foo")
# print(out)

# 3. os.path.isabs(path) : It specifies whether the path is absolute or not. 
# In Unix system absolute path means path begins with the slash(‘/’) and 
# in Windows that it begins with a (back)slash after chopping off a potential drive letter
# import os 
# out=os.path.isabs("/bazz/foo")
# print(out)


# 4. os.path.isdir(path) : This function specifies whether the path is existing directory or not. 
# import os
# out = os.path.isdir("C:\\Users")
# print(out)

# 5. os.path.isfile(path) : This function specifies whether the path is existing file or not. 
# import os
# out = os.path.isfile("C:\\Users\foo.csv")
# print(out)

# 6. os.path.normcase(path) : This function normalizes the case of the pathname specified.
# In Unix and Mac OS X system it returns the pathname as it is .
# But in Windows it converts the path to lowercase and forward slashes to backslashes. 
# import os
# out = os.path.normcase("/BAz")
# print(out)

# 7. os.path.normpath(path) : This function normalizes the path names by collapsing redundant
# separators and up-level references so that A//B, A/B/, A/./B and A/foo/../B 
# all become A/B. On Windows, it converts forward slashes to backward slashes . 

# normpath function in Unix
# import os
# out = os.path.normpath("foo/./bar")
# print(out)