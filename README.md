# ClassGenerator

![issues](https://img.shields.io/github/issues/Justin-Byrne/ClassGenerator)
![license](https://img.shields.io/github/license/Justin-Byrne/ClassGenerator)
<img src=https://img.shields.io/badge/Python-3.11.2-blue />
<img src=https://img.shields.io/badge/PlantUML-1.2.023.4-purple />
<img src=https://img.shields.io/badge/Graphviz-8.0.5-gray />
<img src=https://img.shields.io/badge/Version-0.9.9-green />
<img src=https://img.shields.io/github/languages/code-size/Justin-Byrne/ClassGenerator />

PlantUML class generator for JavaScript

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Support](#support)
- [Structure](#structure)

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

source                       File or directory location of javascript file(s) to convert

                             usage:
                                 (single)    "/javascript/classes/one.js"
                                 (multiple)  "/javascript/classes"

destination                  File or directory location to save class diagrams

                                 usage:
                                     (single)    "/javascript/classes/output/one.txt"
                                     (multiple)  "/javascript/classes/output"

FLAGS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

-o, --omit "<filename>"      Omit the following filenames from the source directory

                             usage:
                                 (single)    --omit "file1"
                                 (multiple)  --omit "file1|file2|file3"

-s, --skin "<skinparam>"     Embed skin parameters within the class uml generated

                             usage:
                                 (single)    --skin "skinparam+one+1"
                                 (multiple)  --skin "skinparam+one+1|skinparam+two+2"

-m, --make "<image_type>"    Make the class generated diagram into an image

                             usage:
                                 (single)    --make "png"
                                 (multiple)  --make "png|svg|eps"

-l, --link                   Link available classes to generated class diagrams

                             usage: --link

-h, --help                   Display this help menu

                             usage: --help
```

## Configuration

Configurations settings for each generated file can be set within `../app/config/config.txt`.

> These settings are commented out by default

```bash
####    FILE OMISSIONS
filename_one
filename_two
filename_three

####    SKIN PARAM
left to right direction
skinparam DefaultFontSize 16
skinparam DefaultFontName Courier New
skinparam ClassAttributeIconSize 0

####    IMAGE OUTPUT
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

####    PLANTUML PATH
path=~/Programs/PlantUML

```

<b>Note:</b> for best results use the following skin-params:
```bash
skinparam DefaultFontSize 16
skinparam DefaultFontName Courier New
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
_prop0   {number}
_prop1   {string}
_prop2   {Object}
_prop3   {Object}
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
prop0   {number}
prop1   {string}
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
prop0   {number}
prop1   {string}
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
prop0   {number}
prop1   {string}
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
├── docs
│   ├── CHANGELOG.md
│   └── FUNDING.yml
├── source
│   └── app
│       ├── config
│       │   └── config.txt
│       ├── core
│       │   ├── generator.py
│       │   └── linker.py
│       ├── utilities
│       │   ├── custom
│       │   │   ├── debug
│       │   │   │   └── view_arguments.py
│       │   │   ├── filter
│       │   │   │   ├── filter_properties.py
│       │   │   │   └── filter_type.py
│       │   │   ├── list
│       │   │   │   └── get_column_max.py
│       │   │   └── validation
│       │   │       ├── is_extension.py
│       │   │       └── is_js_class.py
│       │   ├── system
│       │   │   ├── file
│       │   │   │   ├── get_file_bounds.py
│       │   │   │   ├── get_file_omissions.py
│       │   │   │   ├── get_files.py
│       │   │   │   └── set_file.py
│       │   │   ├── validation
│       │   │   │   ├── is_directory.py
│       │   │   │   ├── is_file.py
│       │   │   │   ├── is_flag.py
│       │   │   │   └── is_program.py
│       │   │   ├── get_command_type.py
│       │   │   ├── get_commands.py
│       │   │   └── parse_commands.py
│       │   └── util.py
│       └── BuildClass.py
├── LICENSE
└── README.md
```
 
## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/cube_sm.png)

== Byrne-Systems © 2023 - All rights reserved. ==
