# Proyecto de Agentes
 
## Instrucciones para crear un ambiente virtual con Conda

1. **Abre una terminal** (Anaconda Prompt o CMD).

2. **Crea un nuevo ambiente** (puedes cambiar `agents` por el nombre que prefieras):

    ```bash
conda create -n agents python=3.10
```


3. **Activa el ambiente** :
    ```bash
    conda activate agents
    ```

4. **Instala las dependencias necesarias** :
```bash
   conda install -c conda-forge poetry
    ```



4. **Replicar las dependencias (enviroments.txt)** :
```bash
   conda env export --from-history > enviroment.txt
    ```

