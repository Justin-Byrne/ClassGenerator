# ClassGenerator

![issues](https://img.shields.io/github/issues/Justin-Byrne/ClassGenerator)
![forks](https://img.shields.io/github/forks/Justin-Byrne/ClassGenerator)
![stars](https://img.shields.io/github/stars/Justin-Byrne/ClassGenerator)
![license](https://img.shields.io/github/license/Justin-Byrne/ClassGenerator)
<img src="https://img.shields.io/badge/Python-3.11.2-blue" />
<img src="https://img.shields.io/badge/PlantUML-1.2.023.4-purple" />
<img src="https://img.shields.io/badge/Graphviz-8.0.5-green" />
 
PlantUML class generator for JavaScript

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Support](#support)
- [Structure](#structure)
- [Copyright](#copyright)

## Requirements

| Program | Function | Optional | Download |
| :---: | :--- | :---: | :---: |
| PlantUML | Render UML images; PNG, SVG, etc... | :white_check_mark: | [:floppy_disk:](https://plantuml.com/download) |
| Graphviz | Render linked UML images. | :white_check_mark: | [:floppy_disk:](https://graphviz.org/download/) |

## Installation

Download a copy of this repository to your system.

> Git clone

```sh
git clone https://github.com/Justin-Byrne/ClassGenerator.git
```

## Usage

> Help menu

```
python3 BuildClass.py {<source>} [<destination>] [flags] [args[|args...]]

PATHS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

source				File or directory location of javascript file(s) to convert

				usage:
					(single)    "/javascript/classes/one.js"
					(multiple)  "/javascript/classes"

destination			File or directory location to save class diagrams

				usage:
					(single)    "/javascript/classes/output/one.txt"
					(multiple)  "/javascript/classes/output"

FLAGS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

-o, --omit "<filename>"		Omit the following filenames from the source directory

				usage:
					(single)   	--omit "file1"
					(multiple) 	--omit "file1|file2|file3"

-s, --skin "<skinparam>"	Embed skin parameters within the class uml generated

				usage:
					(single)     --skin "skinparam+one+1"
					(multiple)   --skin "skinparam+one+1|skinparam+two+2"

-m, --make "<image_type>"	Make the class generated diagram into an image

				usage:
					(single) 	--make "png"
					(multiple)	--make "png|svg|eps"

-l, --link			Link available classes to generated class diagrams

				usage: --link

-h, --help			Display this help menu

				usage: --help
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

#### 	IMAGE OUTPUT
png
svg
eps
eps:text
pdf
vdx
xmi
scxml
html
txt
utxt
latex
latex:nopreamble
braille

####	PLANTUML PATH
path=~/Programs/PlantUML

```

## Examples

> `python3 BuildClass.py ~/Programs/JavaScript/Classes/class.js -m "png"`

<table>
<tr>
<th> JavaScript </th>
<th> PlantUml ( Text ) </th>
<th> PlantUml ( PNG ) </th>
</tr>
<tr valign="top">
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
<td>
<img src="https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/class.png">
</td>
</tr>
</td>
</tr>
</table>

> `python3 BuildClass.py ~/Programs/JavaScript/Classes/class.js -l -m "png"`

<table>
<tr>
<th> JavaScript </th>
<th> PlantUml ( Text ) </th>
<th> PlantUml ( PNG ) </th>
</tr>
<tr valign="top">
<td>

```js
/**
 * @class     {Object}  One
 * @property  {number}  prop0
 * @property  {string}  prop1
 * @property  {Two}     prop2
 * @property  {Three}   prop3
 *
 */
class One
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

class One {
prop0   <co..ay>{number}</co.or>
prop1   <co..ay>{string}</co.or>
prop2   {Two}
prop3   {Three}
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
One *-- Three
One *-- Two

class Two {
prop0   <co..ay>{number}</co.or>
prop1   <co..ay>{string}</co.or>
prop2   {One}
prop3   {Three}
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

class Three {
prop0   <co..ay>{number}</co.or>
prop1   <co..ay>{string}</co.or>
prop2   {One}
prop3   {Two}
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
<td>
<img src="https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/linked.png">
</td>
</tr>
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
            │   ├── debug
            │   │   └── view_arguments.py
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
            │       ├── is_flag.py
            │       └── is_program.py
            └── util.py
```

## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/cube_sm.png)

== Byrne-Systems © 2023 - All rights reserved. ==

:lotus_position:
