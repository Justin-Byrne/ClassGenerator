# ClassGenerator

![issues](https://img.shields.io/github/issues/Justin-Byrne/ClassGenerator)
![forks](https://img.shields.io/github/forks/Justin-Byrne/ClassGenerator)
![stars](https://img.shields.io/github/stars/Justin-Byrne/ClassGenerator)
![license](https://img.shields.io/github/license/Justin-Byrne/ClassGenerator)
<img src="https://img.shields.io/badge/Python-3.11.2-blue" />
 
PlantUML class generator for JavaScript

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
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
> python3 BuildClass.py <source> [<destination>] [<flag>] [<flag_value>]
```

## Configuration

Configurations settings for each generated file can be set within `../app/config/config.txt`.

> These settings are commented out by default

```bash
#### 	FILE OMISSIONS
one
two
three

#### 	SKIN PARAM
left to right direction
skinparam DefaultFontSize 16
skinparam DefaultFontName Courier 10 Pitch
skinparam ClassAttributeIconSize 0

```

## Examples

> `python3 BuildClass.py ~/Programs/JavaScript/Classes/class.js`

<table>
<tr>
<th> JavaScript </th>
<th> PlantUml ( Text ) </th>
<th> PlantUml ( PNG ) </th>
</tr>
<tr>
<td>

```js
class ClassName
{
    _prop0 = 0;
    _prop1 = 'string';
    _prop2 = new Two;
    _prop3 = new Three;

    constructor ( ) { }

    set prop0 ( value ) { }
    get prop0 ( ) { }

    set prop1 ( value ) { }
    get prop1 ( ) { }

    set prop2 ( value ) { }
    get prop2 ( ) { }

    set prop3 ( value ) { }
    get prop3 ( ) { }
}

```
</td>
<td>

```bash
@startuml

class ClassName {
_prop0   <color:gray>{number}</color>
_prop1   <color:gray>{string}</color>
_prop2   <color:gray>{Object}</color>
_prop3   <color:gray>{Object}</color>
__ Setter __
prop0
prop1
prop2
prop3
__ Getter __
prop0
prop1
prop2
prop3
}
@enduml
```
</td>
</tr>
<img src="https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/class.png">
</td>
</tr>
</table>

## Support

Please [open an issue](https://github.com/Justin-Byrne/ClassGenerator/issues/new) for support.


## Structure

```
.
├── LICENSE
├── README.md
├── docs
│   └── CHANGELOG.md
└── source
    └── app
        ├── BuildClass.py
        ├── config
        │   └── config.txt
        ├── core
        │   ├── generator.py
        │   └── linker.py
        ├── test-generator.py
        └── utilities
            ├── custom
            │   ├── cleanup
            │   │   └── clean_properties.py
            │   └── validation
            │       ├── is_extension.py
            │       └── is_js_class.py
            ├── system
            │   ├── file
            │   │   ├── get_eof.py
            │   │   └── get_files.py
            │   ├── get_command_type.py
            │   ├── get_commands.py
            │   ├── list
            │   │   ├── create_2d_list.py
            │   │   ├── entry_padding.py
            │   │   └── list_to_string.py
            │   ├── parse_commands.py
            │   ├── string
            │   │   └── repeat_character.py
            │   └── validation
            │       ├── is_directory.py
            │       ├── is_file.py
            │       └── is_flag.py
            └── util.py
```

## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/cube_sm.png)

== Byrne-Systems © 2023 - All rights reserved. ==
