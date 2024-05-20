## Instruction for runing the code
- For CIFAR-100
  - iCaRL
    ```python
        python main.py --config ./exps/icarl_dm.json

  - FOSTER
    ```python
        python main.py --config ./exps/foster_dm.json
    
  - BEEF
    ```python
        python main.py --config ./exps/beefl_dm.json

- For TinyImageNet
  - Download the dataset, and unzip into train, and val folders.
  - Modify the code at 'utils/data.py', Line 116-119, and Line 146-147.
  - iCaRL
    ```python
        python main.py --config ./exps/icarl_dm_tiny.json

  - FOSTER
    ```python
        python main.py --config ./exps/foster_dm_tiny.json
    
  - BEEF
    ```python
        python main.py --config ./exps/beefl_dm_tiny.json
