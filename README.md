# Paris Metro Station Game: Navigating the Cityscape Challenge

## Introduction

Exploring the vibrant city of Paris just became an engaging challenge with the Paris Metro Station Game. Drawing inspiration from popular memory games like [Memory Pour Paris](https://memory.pour.paris/) and [Name SF Streets](https://carvin.github.io/sf-street-names/), this web app transforms the exploration of Parisian metro stations into an exciting gaming experience.

## Demo
[![Demo](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fyoutu.be%2FZF4eB_3864Q)](https://youtu.be/ZF4eB_3864Q)

## Game Overview

### How it Works

The game's premise is straightforward. Players input the names of Paris metro stations, earning points for each correct entry. The twist? The game doesn't store cookies, ensuring a fresh start with each session. The goal is to explore the vast network of Paris metro stations and test your knowledge of the city's transit system.

### User Interface

The user interface is divided into two main sections. On the left side, a dynamic map centered around Paris provides an interactive view of the metro stations and lines. On the right side, players can track their score and view a list of correctly guessed station names.

## Installation Guide

Getting started with the Paris Metro Station Game is simple. Follow these steps to install and launch the game on your local machine:

1. **Download Dependencies:** Ensure you have the necessary dependencies installed. The list of requirements is available in the `requirements.txt` file.

2. **Run the Game:** Execute the following command in the game's directory to launch the web app:
   ```bash
   flask --app app.py --debug run
   ```

3. **Explore the Parisian Metro:** Once the game is running, start exploring Paris and guessing metro station names to accumulate points.

## Project Directory Structure

Understanding the project's directory structure is crucial for developers interested in exploring or contributing to the Paris Metro Station Game. Here's a breakdown of the key directories and files:

```bash
.
├── README.md
├── app.py
├── data
│   ├── metro_lines.geojson
│   └── metro_station.geojson
├── requirements.txt
├── static
│   ├── favicon.ico
│   └── style.css
└── templates
    ├── index.html
    └── layout.html
```

- **`app.py`:** The main application file that orchestrates the game's functionality.

- **`data/`:** Contains GeoJSON files with information about metro stations and lines. The data is sourced from the official Paris transportation website.

- **`static/`:** Holds static visual elements such as the game's favicon and CSS styles.

- **`templates/`:** Includes HTML templates for the game interface, with `index.html` being the primary file containing the game logic.

## Data Sources

The game relies on data obtained from the official Paris transportation website. Two GeoJSON files are used:

1. **Métro Stations Per Line:** Provides details about station names, coordinates, and their corresponding metro lines.

2. **Métro Line Information:** Contains coordinates of line segments along with their associated colors.

## Static Elements

Visual appeal is crucial for an engaging gaming experience. The `static` directory hosts the game's favicon and CSS styles. Developers can enhance the CSS file to introduce more vibrant and visually appealing elements.

## Templates Structure

The `templates` directory consists of two HTML files:

1. **`layout.html`:** Defines the base layout of the web app, dividing it into two sides - the left side for the map and the right side for the score and correctly guessed station names.

2. **`index.html`:** Contains the primary logic for the game. It creates a map centered around Paris, generates metro lines, places circle markers for stations, and handles user input.

## Game Logic and Features

### Interactive Map

The heart of the game lies in the interactive map. Utilizing Leaflet JS, the map provides a dynamic and visually appealing representation of Paris and its metro stations. 

Only the last correctly guessed station name would been shown on the map. This choice was made so that the map can still be readable. 

### Scoring System

Players earn points for correctly guessing metro station names. The scoring system calculates the score as a percentage of correctly guessed stations out of the total number of stations.

```bash
score = (station_found / total_station) * 100
```

### Typos and Levenshtein Distance

For an added challenge, the game handles typos using [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance). This feature allows players to have a more forgiving experience, especially when dealing with variations or minor errors in station names.

## Conclusion

The Paris Metro Station Game is a delightful blend of exploration and knowledge-testing within the city of Paris. Whether you're a local resident or a virtual traveler, this game offers a unique way to engage with the iconic Parisian metro system. Install the game, start exploring, and see how well you know the metro stations of the City of Lights. Happy gaming!