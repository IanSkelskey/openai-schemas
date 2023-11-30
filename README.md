# OpenAI Schemas Repository

## Overview

This repository is dedicated to storing and sharing JSON schemas for custom GPTs (Generative Pre-trained Transformers). These schemas are designed to define the structure and expected data for various APIs, making it easier to integrate and work with different services using custom GPTs.

## Contents

### ![Github Logo](assets/github.svg) GitHub API Schema

- `github.json`: This schema defines the structure for fetching details of a specified GitHub repository. It outlines the necessary parameters, such as repository owner and name, and the expected response format, including repository details like name, description, creation date, and more.

### ![Spotify Logo](assets/spotify.svg) Spotify API Schema

- `spotify/`: Contains the modularized schema files for the Spotify API, with individual endpoint descriptions.
  - `main.json`: Acts as the master file linking to all modular endpoint schemas.
  - `audio-features.json`, `me/playlists.json`, etc.: Define specific endpoints.

## Modular Endpoint Schemas

The individual endpoint schemas for each API are stored in the parent directory for each API (e.g. `spotify/` for Spotify API). These schemas are modularized to allow for easier maintenance and updating of the schemas. The modular endpoint schemas are linked together by the main schema file (e.g. `spotify/main.json`).

### Building the Schema from Modules

- `npm run build`: Builds the master schema file `spotify/main.json` from the modular endpoint schemas in `spotify/`. Outputs to `build/spotify.json`.

## Usage

These schemas can be used to create custom GPTs tailored for specific APIs. By defining the expected data structure, these schemas help in ensuring that the custom GPTs can interact effectively with the APIs, providing accurate and relevant responses.
