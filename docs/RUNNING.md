# Running notes

These modules are independent exercise collections. Keep their working directories separate: several modules use names such as `ex0`, so adding every module to one global import path can select the wrong package.

## Module 00

The exercise files define functions. Invoke a function explicitly, for example from `module-00`:

```sh
python -c 'from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()'
```

The preserved `main.py` helper expects exercise modules on the import path even though the original repository stores them in subdirectories. On macOS/Linux, run it from `module-00` with:

```sh
PYTHONPATH=ex0:ex1:ex2:ex3:ex4:ex5:ex6:ex7 python main.py
```

## Module 01

Run individual scripts, such as `python ex2/ft_plant_growth.py`, from `module-01`. The original README describes an `ex6` analytics exercise, but the source snapshot only contains `ex0` through `ex5`. The original assignment is preserved as `module01.pdf`.

## Module 04

Run scripts from their exercise directory, for example `cd module-04/ex0` then `python ft_ancient_text.py`. Several exercises look for files in `../data-generator-tools/`, meaning `module-04/data-generator-tools/` with this working directory.

The original repository does not include the data generator or its fixtures. Supply your own sample text files before running the read examples:

- `ancient_fragment.txt` for `ex0`.
- `classified_data.txt` for `ex3`; this exercise writes `security_protocols.txt` alongside it.
- `ex4` tries `lost_archive.txt`, `classified_vault.txt`, and `standard_archive.txt`, handling missing files and permission errors.

`ex1` writes `new_discovery.txt` in its current directory. `ex2` prompts for an archivist ID and status report. Use disposable sample data when exploring the file-writing exercises.

## Module 08

Activate your virtual environment first. Exercise 00 reports whether it is active:

```sh
cd module-08/ex0
python construct.py
```

Exercise 01 has its own requirements and Poetry metadata. From `module-08/ex1`:

```sh
python -m pip install -r requirements.txt
python loading.py
```

It generates random sample data and saves `matrix_analysis.png` in the current directory.

Exercise 02 needs `python-dotenv`. From `module-08/ex2`:

```sh
python -m pip install python-dotenv
cp .env.example .env
python oracle.py
```

The environment example contains sample values. The script reports configuration presence; its database/API status text does not verify an actual connection or credential. Keep real credentials out of Git.

## Module 09

These exercises use Pydantic v2 APIs. From `module-09`, with the virtual environment active:

```sh
python -m pip install 'pydantic>=2,<3'
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py
```

## Checking syntax

From the repository root:

```sh
python -m compileall -q module-*
```

Compilation checks syntax only. Running the demonstration entry points is a smoke check, not comprehensive correctness or assignment-compliance testing.
