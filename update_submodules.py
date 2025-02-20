import subprocess

subprocess.run("git submodule update --remote --merge", shell=True, check=True)

status_result = subprocess.run("git status ./routes --porcelain", shell=True, check=True, stdout=subprocess.PIPE)

if status_result.stdout:
    subprocess.run("git add ./routes .gitmodules", shell=True, check=True)
    subprocess.run("git commit -m \"Updated submodules\"", shell=True, check=True)
    #subprocess.run("git push", shell=True, check=True)
    print("Submodules update commited! ✅")
else:
    print("Submodules up-to-date. 👍")
