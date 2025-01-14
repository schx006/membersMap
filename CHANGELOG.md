# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* Fichier “.vscode/settings.json”, configuration de l'extention “markdownlint”
  (vérification de style dy langage de balisage _Markdown_).
* Répertoire “src”.

### Changed

* …
* Corrections de style des fichiers `*.md`
* Déplacement des fichiers de code dans le répertoire “src”.
* Mise à jour du fichier “README.md”.

### Removed

* …

## [0.7.0-beta] - 2025-01-11

1st release.

### Added

* This CHANGELOG file to hopefully serve as an evolving example of a
  standardized open source project CHANGELOG.
* The “testing.py” debugging script, which uses the test set data files.
* Data files in the “./data/testing/” directory for testing special cases
  and major errors in the data to be processed.
* The main script (“main.py”) uses the “DistributeMembers” class to count
  members commune by commune.
* The “distributemembers.py” file in the “membersmap” library.
  It contains the “DistributeMembers” class, which reads the members file
  of a département and counts them commune by commune (arrondissement by
  arrondissement in the cities of Lyon, Marseille and Paris).
  Each commune (or arrondissement) is identified by its number in the INSEE
  nomenclature of French municipalities.
* The “adh26-2024-10-28.csv” file, which contains the anonymized extraction
  of Drôme members.
* INSEE nomenclature of French municipalities (mainland France and overseas
  territories)

[Unreleased]: https://github.com/schx006/membersMap/compare/v0.7.0-beta...HEAD  
[0.7.0-beta]: https://github.com/schx006/membersMap/releases/tag/v0.7.0-beta
