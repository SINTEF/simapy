# Changelog

All notable changes to this project will be documented in this file.

## [4.6.0] - 2023-06-09

### Added

- Updated data model to relfect SIMA 4.6.0
- New metocean package to enable creation of SIMA metocean data

### Changed

- Breaking changes:
    - sima root package is moved into simapy
    - marmo package is renamed and moved into simapy.sima.signals
    - sima module renamed to sre

### Fixed

- Fixed copy of cross references. Possibility to remove or keep (default) uncontained cross references when copying

