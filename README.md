# OpenAI Schemas Repository

## Overview

This repository provides modularized JSON schemas for custom GPTs to integrate with several APIs. These schemas define expected data structures and endpoints, facilitating seamless interaction between GPTs and external APIs. Each API schema is organized into directories by API name, with modular endpoint schemas referenced by a main schema file.

## Contents

### ![GitHub Logo](assets/github.svg) GitHub API Schema

- **Directory**: `schemas/github/`
- **Description**: Schemas for GitHub API endpoints to retrieve repository details.
- **Main Schema**: `schemas/github/main.json` links to endpoint schemas.
- **Endpoints**:
  - `repos/owner/repo.json`: Details for a specified repository by owner and repo name.
  - `repos/owner/repo/contents/path.json`: Retrieves contents of a repository path.

### ![Spotify Logo](assets/spotify.svg) Spotify API Schema

- **Directory**: `schemas/spotify/`
- **Description**: Modularized schemas for Spotify API endpoints, covering audio features, playlists, and track information.
- **Main Schema**: `schemas/spotify/main.json`
- **Endpoints**:
  - `audio-features.json` and `audio-features/track_id.json`: Information on audio features for a track or multiple tracks.
  - `me/playlists.json`: Retrieves playlists for the current user.
  - `playlists/playlist_id.json`: Information about a specific playlist.
  - `playlists/playlist_id/images.json`: Playlist image information.
  - `playlists/playlist_id/tracks.json`: Tracks within a specified playlist.
  - `recommendations.json`: Recommendations based on various parameters.
  - `search.json`: Search for items on Spotify.
  - `tracks/track_id.json`: Specific track details.
  - `users/user_id/playlists.json`: User's playlists.

### Magic: The Gathering API Schema

- **Directory**: `schemas/mtg/`
- **Description**: Schemas for Magic: The Gathering API, covering cards, sets, and various classification types.
- **Main Schema**: `schemas/mtg/main.json` provides a high-level structure for MTG API interactions.
- **Endpoints**:
  - `cards.json`: Retrieves a list of cards.
  - `card_details.json`: Details for a specific card.
  - `sets.json`: Retrieves a list of sets.
  - `set_details.json`: Details for a specific set.
  - `sets_id.json`: Retrieve a set by ID.
  - `sets_id_booster.json`: Generate a booster pack for a specified set.
  - `types.json`: List all card types.
  - `subtypes.json`: List all card subtypes.
  - `supertypes.json`: List all card supertypes.
  - `formats.json`: Lists all game formats.

## Building the Schema from Modules

The `build.py` script consolidates endpoint schemas for each API into a single output JSON file per API.

### Building Instructions

1. **Install Dependencies**:
   ```bash
   npm install

2. **Run the Build Script**:
   ```bash
   npm run build
   ```

3. The output files will be located in the `build/` directory. (e.g., `build/github.json`, `build/spotify.json`, `build/mtg.json`)