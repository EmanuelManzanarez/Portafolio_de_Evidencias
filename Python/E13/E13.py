import subprocess

comando = "Get-Host"
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())

print("fecha: ")
comando = "Get-Date"
lineaPS = "powershell -Executionpolicy ByPass -Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())


