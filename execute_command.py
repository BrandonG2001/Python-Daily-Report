#import subprocess
from subprocess import run, PIPE
from os import path, environ, walk, remove, getcwd
from winshell import recycle_bin
from shutil import rmtree

# Function to execute a command
def run_command(command):
    try:
        result = run(
            command,
            stdout=PIPE,
            stderr=PIPE,
            shell=True,
            text=True,
        )
        return result.stdout
    except Exception as e:
        return str(e)
    

# Run PowerShell to check for Security updates
power_shell = path.join(environ["SystemRoot"], "System32", 'WindowsPowerShell', 'v1.0', 'powershell.exe')
#power_shell = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
check_updates_command = f'{power_shell} Get-WindowsUpdate -NotCategory "Drivers","FeaturePacks"'
install_command = f'{power_shell} Install-WindowsUpdate -NotCategory "Drivers","FeaturePacks" -AcceptAll -IgnoreReboot'

CREATE_NO_WINDOW = '0x08000000'
DETACHED_PROCESS = "0x00000008"


def install_security_updates():
    run(
        install_command,
        shell=True,
        creationflags=DETACHED_PROCESS # or CREATE_NO_WINDOW
        )


def run_updates():
    run_command("winget.exe upgrade --all --silent --disable-interactivity")
    install_security_updates()


def clean_windows_temp_files():
    # List of common Windows temporary file locations
    temp_folders = [
        path.join(environ["SystemRoot"], "Temp"),
        path.join(environ["SystemRoot"], "Prefetch"),
        path.join(environ["UserProfile"], "AppData", "Local", "Temp"),
    ]

    try:
        for folder in temp_folders:
            if path.exists(folder):
                for root, dirs, files in walk(folder):
                    for file in files:
                        file_path = path.join(root, file)
                        try:
                            remove(file_path)
                        except:
                            pass

        recycle_bin().empty(confirm=False,
            show_progress=False, sound=False)    
        clean_cache()
    except:
        pass
    
def clean_cache():
    cache_folders = [
        path.join(getcwd(), '.cache')
    ]
    
    try:
        for folder in cache_folders:
            if path.exists(folder):
                for root, dirs, files in walk(folder):
                    for file in files:
                        file_path = path.join(root, file)
                        try:
                            remove(file_path)
                        except:
                            pass
                rmtree(folder)
        return True
    except:
        return False
    
if __name__ == "__main__":
    clean_windows_temp_files()