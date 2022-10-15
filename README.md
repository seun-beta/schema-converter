## Solution

### Prerequisites 

- Python 3.10

### Repo structure 

```sh
├── PROBLEM.md
├── README.md
├── data
│   ├── data_1.json
│   └── data_2.json
├── main.py
├── schema
│   ├── example.json
│   ├── schema_1.json
│   └── schema_2.json
├── test_data
│   ├── invalid.json
│   └── output.json
├── test_main.py
└── utility
    └── utils.py 
```

### Run processor file

```sh
python main.py <INPUT FILE PATH> <OUT FILE PATH>
```

```sh
python main.py data/data_1.json schema/schema_1.json
```

### Run unit tests 

```sh
python test_main.py
```

- Test dataset can be located in test_data folder
