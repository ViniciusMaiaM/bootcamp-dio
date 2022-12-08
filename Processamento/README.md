### Exemplos de estruturas:

Pacote simples:


    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            file1_name.py
            file2_name.py


Exemplo de importação: 'import package_name.file1_name'

Pacote com vários módulos:

    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            module1_name/
                __init__.py
                file1_name.py
                file2_name.py
            module2_name/
                __init__.py
                file1_name.py
                file2_name.py    

Exemplo de importação: 'import package_name.module1_name.file1_name'