class InstallPackage:
    def PipDefaut(Package):
        import os
        pip =  str(os.system(f'pip install {Package}'))
        if pip != '0':
            print(f'Pipe: Package dont has been installed, output: {pip}')
    def PipAlternative(Package):
        import os
        pip =  str(os.system(f'pip install --break-system-packages {Package}'))
        if pip != '0':
            print(f'Pipe: Package dont has been installed, output: {pip}')
def ShowPackages():
    import os
    os.system('pip list')
def DeletePackage(Package):
    import os
    os.system(f'pip uninstall {Package}')