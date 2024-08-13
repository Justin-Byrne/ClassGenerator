# Changelog
All notable changes to this project will be documented in this file.

## [0.10.15] - 2024-08-13
### Added
- :blossom: `Generator` class, `get_validators ( )`: to get validators in submitted class(es)
- :sunny: `replace_value ( )` utility: to replace a value within a list

### Refactored
- :last_quarter_moon: `Generator` class
  - `prepare_file ( )` - modified to save files to a 'text' sub-directory
  - `compose_image ( )` - modified to save images to a 'image' sub-directory
- :last_quarter_moon: `Linker` class,
  - `get_classes ( )` - modified to search for files in newly set 'text' sub-directory
  - `set_regexes ( )` - modified to identify arrow types, sub-types, or encapsulated types
  - `link_objects ( )` - modified to save linked texts in newly set 'text' sub-directory
  - `compose_image ( )` - modified to save linked images to newly set 'text' sub-directory
- :last_quarter_moon: `filter_type` utility - modified type list to include 'Object' as a type
- :last_quarter_moon: `get_commands` utility - modified destination argument to include 'text' as a sub-directory, when a destination isn't provided

### Fixed
- :dragon: `Linker` class, `get_classes ( )` - fixed '|||' aberration

## [0.9.9] - 2023-10-17
### Added
- `Linker` class, `set_regexes ( )` function to set regexes for each identified class

### Changed
- `Linker` class
  - `self.classes` global variable to `self.classSources` for specificity
  - renamed `read_files ( )` to `get_objects ( )`
  - refactored:
    - `get_objects   ( )`
    - `match_files   ( )`
    - `find_files    ( )`
    - `link_objects  ( )`
    - `compose_image ( )`
- `get_commands.py` to parse output to `_output` directory, instead of `output`

### Fixed
- `Generator` class, fixed issue where tag title parses regardless of no tag elements

## [0.8.9] - 2023-10-11
### Changed
- Refactored and cleaned `linker` class

## [0.8.8] - 2023-10-11
### Changed
- Refactored and cleaned entire `generator` class

### Added
- Added the following utilities
  - `filter_properties ( )`
  - `filter_type ( )`
  - `get_column_max ( )`
  - `get_file_bounds ( )`
  - `set_file ( )`

### Removed
- Removed the following utilities
  - `get_eof ( )`
  - `entry_padding ( )`
  - `create_2d_list ( )`
  - `repeat_character ( )`
  - `list_to_string ( )`
  - `clean_properties ( )`

## [0.7.8] - 2023-05-03
### Added
- Help menu to `get_commands ( )`

### Changed
- Minor error refinement:
  - `view_arguments ( )`
  - `create_2d_list ( )`
  - `entry_padding ( )`
  - `parse_commands ( )`
  - `repeat_character ( )`
  - `is_file ( )`

### Fixed
- Path validation for PlantUml program executable under `parse_commands ( )`

## [0.7.7] - 2023-05-03
### Fixed
- PlantUml program executable location management under `parse_commands ( )`

## [0.7.6] - 2023-05-02
### Added
- Fully implemented class linker; to link referenced classes
  - `linker ( )`

### Fixed
- Discrepancies with README.md

### Changed
- Refactored and refined:
  - `generator ( )`
  - `parse_commands ( )`

## [0.6.5] - 2023-04-29
### Added
- Validation
  - `is_program ( )`
- Debug
  - `view_arguments ( )`

### Changed
- Refactored and refined:
  - `generator ( )`
  - `parse_commands ( )`
- Expanded configuration file and parsing methods

## [0.5.5] - 2023-04-27
### Added
- Unit tests for main app `BuildClass.py`

### Fixed
- `skin_param` properly populates when available
- `prepare_file ( )` to create proper file and directory path(s)

## [0.5.2] - 2023-04-26
- Implemented configuration file and parsing methods

### Changed
- Refactored and refined:
  - `clean_properties ( )`
  - `get_files ( )`
  - `get_commands ( )`
  - `parse_commands ( )`

## [0.4.2] - 2023-04-23
### Added
- Implemented various functions to parse JavaScript document data:
  - `get_header ( )`
  - `get_class ( )`
  - `get_properties ( )`
  - `get_setters ( )`
  - `get_getters ( )`

### Changed
- Refactored and refined:
  - `clean_properties ( )`
  - `get_files ( )`
  - `generator ( )`

## [0.3.2] - 2023-04-21
### Added
- Custom utilities, `is_js_class ( )`

### Changed
- Refactored and refined:
  - `get_files ( )`
  - `generator ( )`

## [0.3.1] - 2023-04-20
### Changed
- Refactored and refined:
  - `get_files ( )`
  - `generator ( )`
- Updated `README.md`

## [0.3.0] - 2023-04-20
### Added
- System utilities:
  - `get_files ( )`
  - `list_to_string ( )`
  - `parse_commands ( )`
- Expanded test cases

### Changed
- Refactored:
  - `clean_properties ( )`
  - `get_commands ( )`
  - `repeat_character ( )`

## [0.2.0] - 2023-04-17
### Added
- Custom utilities:
  - `clean_properties ( )`
  - `is_extension ( )`
- System utilities:
  - `get_eof ( )`
  - `create_2d_list ( )`
  - `entry_padding ( )`
  - `repeat_character ( )`
- Expanded test suite

### Changed
- Refactored:
  - `parse_commands ( )`
  - `get_commands ( )`
- Refactored validation scripts, and:
  - `is_directory ( )`
  - `is_file ( )`

## [0.1.0] - 2023-04-11
### Added
- Core source files for application
- Core unit tests for application
- License

### Changed
- Updated `README.md`

## [0.0.0] - 2023-04-02
### Added
- Directory structure
- `CHANGELOG.md`
- `README.md`

---

| Version | Date       | Commit                                                                   | Comments                                                          |
| :-----: | :--------: | :----------------------------------------------------------------------: | :---------------------------------------------------------------- |
| 0.10.15 | 2024-08-13 | Current                                                                  | Added identification of validators
| 0.9.9   | 2023-10-17 | [17c1b1a](https://github.com/Justin-Byrne/ClassGenerator/commit/17c1b1a) | Fixed linker class issues
| 0.8.9   | 2023-10-11 | [cd79df5](https://github.com/Justin-Byrne/ClassGenerator/commit/cd79df5) | Refactored linker class
| 0.8.8   | 2023-10-11 | [6154c3e](https://github.com/Justin-Byrne/ClassGenerator/commit/6154c3e) | Major refactoring of project
| 0.7.7   | 2023-05-03 | [bb4ef56](https://github.com/Justin-Byrne/ClassGenerator/commit/bb4ef56) | PlantUml program executable location management
| 0.7.6   | 2023-05-02 | [63dab81](https://github.com/Justin-Byrne/ClassGenerator/commit/63dab81) | Fully implemented class linker
| 0.6.5   | 2023-04-29 | [ed8937b](https://github.com/Justin-Byrne/ClassGenerator/commit/ed8937b) | Expanded config, validation, and debugging
| 0.5.5   | 2023-04-27 | [ae2d7e9](https://github.com/Justin-Byrne/ClassGenerator/commit/ae2d7e9) | Finalized generator processes and unit-tests
| 0.5.2   | 2023-04-26 | [2256899](https://github.com/Justin-Byrne/ClassGenerator/commit/2256899) | Implemented configuration file and parsing methods
| 0.4.2   | 2023-04-23 | [4a78b19](https://github.com/Justin-Byrne/ClassGenerator/commit/4a78b19) | Implemented various functions to parse JavaScript document data
| 0.3.2   | 2023-04-21 | [28b0d8e](https://github.com/Justin-Byrne/ClassGenerator/commit/28b0d8e) | Implemented further source validation
| 0.3.1   | 2023-04-20 | [3251d7a](https://github.com/Justin-Byrne/ClassGenerator/commit/3251d7a) | Minor refactoring
| 0.3.0   | 2023-04-20 | [4dbb4d9](https://github.com/Justin-Byrne/ClassGenerator/commit/4dbb4d9) | System utility additions, and general revisions
| 0.2.0   | 2023-04-17 | [7968397](https://github.com/Justin-Byrne/ClassGenerator/commit/7968397) | Further utility implementation, and general revision(s)
| 0.1.0   | 2023-04-11 | [f9b479d](https://github.com/Justin-Byrne/ClassGenerator/commit/f9b479d) | Core application files added
| 0.0.0   | 2023-04-02 | [5d504a3](https://github.com/Justin-Byrne/ClassGenerator/commit/5d504a3) | initial upload

---

## Types of changes
- `Added` added features.
- `Changed` changes to function calls, names, or placement.
- `Deprecated` soon-to-be removed features.
- `Fixed` bug fixes.
- `Refactored` refactoring functionality.
- `Removed` removed features.
- `Security` securing vulnerabilities.

## Copyright

![Byrne-Systems](https://github.com/Justin-Byrne/ClassGenerator/blob/main/images/byrne-systems.logo.png)

==Byrne-Systems © 2023 - All rights reserved.==
