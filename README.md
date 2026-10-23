# Python Modules

Python learning exercises by Ahmed AIT ELAAOUD, collected in one repository. The modules progress from functions and classes to packages, abstract interfaces, data validation, and decorators.

Each module keeps its original exercise layout. These are educational implementations, not a single application or a production framework.

## Modules

| Module | Focus |
| --- | --- |
| [00](module-00/) | Functions, input, conditionals, loops, and recursion |
| [01](module-01/) | Classes, encapsulation, and inheritance |
| [02](module-02/) | Exceptions, custom errors, and cleanup |
| [03](module-03/) | Collections, command-line arguments, and generators |
| [04](module-04/) | Files, standard streams, and resource handling |
| [05](module-05/) | Abstract classes and polymorphic data processors |
| [06](module-06/) | Packages, imports, and circular dependencies |
| [07](module-07/) | Card-game exercises using interfaces, factories, and strategies |
| [08](module-08/) | Virtual environments, dependencies, and environment variables |
| [09](module-09/) | Pydantic models and validation |
| [10](module-10/) | Lambdas, closures, higher-order functions, and decorators |

## Running exercises

Use Python 3.10 or later; consolidation checks were run with Python 3.12. Create a virtual environment from the repository root:

```sh
python3 -m venv .venv
. .venv/bin/activate
```

Run exercises from their module directory. For example:

```sh
cd module-02
python ex0/ft_first_exception.py
```

Module 06 imports its local `alchemy` package:

```sh
cd module-06
python ft_sacred_scroll.py
```

Module 07 exercises import one another. Run them as modules from `module-07`:

```sh
cd module-07
python -m ex0.main
python -m ex3.main
```

Start each example above from the repository root. See [running notes](docs/RUNNING.md) for module 00's helper, module 04's external fixtures, and dependency setup for modules 08 and 09.

## Scope and provenance

The source files are consolidated snapshots of 11 original repositories. Their contents, author comments, existing READMEs, and module 01's assignment PDF are preserved. Original Git histories remain in the source repositories; they are not imported into this repository's history.

[Source revisions](docs/SOURCES.md) record the exact commits used. Existing module READMEs describe the original exercises and may contain outdated setup details; the running notes explain verified caveats. No new license is assigned by this consolidation.
