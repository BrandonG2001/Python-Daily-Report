from subprocess import Popen
from shutil import rmtree, copyfile
from os import path, environ, remove

from warnings import filterwarnings
filterwarnings("ignore", category=UserWarning)

# Create function #
def create_exe(script_name, exe_name, log_level='FATAL'):
    command_list = [
                  "pyinstaller" ,
                  '-F',
                  f'{script_name}',
                  f'--paths="{environ["VIRTUAL_ENV"]}\\Lib\\site_packages"',
                  f'--log-level {log_level}',
                  '--clean',
                  f'--name="{exe_name}"',
                  ]
    command = ''
    for command_part in command_list:
        command = command + command_part + ' '
    
    print(f'\nCreating {exe_name} executable\n')
    result = Popen(command)
    result.wait()
    print()
    print(f'Finished Creating {exe_name} EXE')
    print()
    
    
    # cleanup
    spec_file = exe_name + '.spec'
    if path.isfile(spec_file):
        remove(spec_file)
    
    # delete temporary build files
    if path.isdir('build'):
        rmtree('build')
        
    desktop_path = path.join(environ['UserProfile'], 'Desktop')
    copyfile(src=exe_name+'.exe', dst=path.join(desktop_path, exe_name+'.exe'))

if __name__ == '__main__':
    # check to make sure personal_information.py exists
    if not path.exists('personal_information.py'):
        copyfile(src='personal_information template.py', dst='personal_information.py')


    create_exe(script_name='gui_ui_frontend_v2.py', exe_name='Daily Report GUI')
    

    