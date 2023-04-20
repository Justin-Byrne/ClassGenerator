# ClassGenerator

![issues](https://img.shields.io/github/issues/Justin-Byrne/ClassGenerator)
![forks](https://img.shields.io/github/forks/Justin-Byrne/ClassGenerator)
![stars](https://img.shields.io/github/stars/Justin-Byrne/ClassGenerator)
![license](https://img.shields.io/github/license/Justin-Byrne/ClassGenerator)
<img src="https://img.shields.io/badge/Python-3.11.2-blue" />
 
PlantUML class generator for JavaScript

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Structure](#structure)
- [Copyright](#copyright)

## Installation

Download a copy of this repository to your system.

> Git clone

```sh
git clone https://github.com/Justin-Byrne/ClassGenerator.git
```

## Usage

> Python

```sh
> python3 BuildClass.py [<flag>] <source> [<destination>]
```

## Support

Please [open an issue](https://github.com/Justin-Byrne/ClassGenerator/issues/new) for support.


## Structure

```
.
├── LICENSE
├── README.md
├── docs
│   ├── CHANGELOG.md
│   └── commands.txt
└── source
    ├── app
    │   ├── BuildClass.py
    │   ├── core
    │   │   ├── generator.py
    │   │   └── linker.py
    │   └── utilities
    │       ├── custom
    │       │   ├── cleanup
    │       │   │   └── clean_properties.py
    │       │   └── validation
    │       │       └── is_extension.py
    │       ├── system
    │       │   ├── file
    │       │   │   ├── get_eof.py
    │       │   │   └── get_files.py
    │       │   ├── get_command_type.py
    │       │   ├── get_commands.py
    │       │   ├── list
    │       │   │   ├── create_2d_list.py
    │       │   │   ├── entry_padding.py
    │       │   │   └── list_to_string.py
    │       │   ├── parse_commands.py
    │       │   ├── string
    │       │   │   └── repeat_character.py
    │       │   └── validation
    │       │       ├── is_directory.py
    │       │       ├── is_file.py
    │       │       └── is_flag.py
    │       └── util.py
    └── tests
        ├── cases
        │   ├── source
        │   │   ├── class-ext-docstring.js
        │   │   ├── class-ext.js
        │   │   ├── class.js
        │   │   └── sub
        │   │       ├── one.js
        │   │       ├── three.js
        │   │       └── two.js
        │   └── test-file.txt
        └── tests.py
```

## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/cube_sm.png)

== Byrne-Systems © 2023 - All rights reserved. ==
