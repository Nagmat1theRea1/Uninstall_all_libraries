import subprocess

command = ["pip list", "pip uninstall"]

help_result = subprocess.run(
    ["powershell", "-Command", command[0]],
    capture_output=True,
    text=True
)


delete = ""
pwsAllinAll = str(help_result)
pwsSeparte = pwsAllinAll.split("\\n")
for i in range(len(pwsSeparte)-1):
    if i < 2:
        i += 1
    else:
        for j in range(len(pwsSeparte[i])):
            if pwsSeparte[i][j] != " ":
                delete = delete + pwsSeparte[i][j]
            elif delete == "pip":
                break
            else:
                subprocess.run(
                    ["powershell", "-Command", command[1]+" "+ delete + " --y"],
                    text=True
                    )
                break
        delete = ""