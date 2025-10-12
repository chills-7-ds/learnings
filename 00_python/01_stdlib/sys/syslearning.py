import sys

print(sys.version)    
print(sys.platform)    

# These tell you which Python version and which system you’re on.

print(sys.argv)

print("Before exit")
# sys.exit()
# if the above exit is actually in code then - print("This line will never run")

#Used when you detect an error or want to stop execution intentionally.

sys.stdout.write("Hello world!\n")
data = sys.stdin.readline()  # waits for user input
sys.stderr.write("Oops, something went wrong!\n")

print(sys.path)
# Control import locations

"""
These are the core 6 modules in the sys library. There are many more functions and variables available in the sys module, which you can explore in the official Python documentation.

https://dramatic-psychology-0d8.notion.site/Sys-28903656c6c380028480fbe27aa07c10?source=copy_link

the above link is my notion page which contains all the important functions regarding sys module in python. 
(90% of them are covered other 10% commands are used for engineers who write tools that control Python itself or shell environments)
"""
