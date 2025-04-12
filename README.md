
# WiFi Network Simulator

A Python-based simulator for WiFi networks that models the interaction between clients, access points, and an access controller. This simulation handles client connections, roaming behavior, channel allocation, and signal strength calculations.

## Project Overview

This simulator models a WiFi network environment where:

-   Access points operate on specific channels and frequencies
-   Clients connect to access points based on signal strength (RSSI)
-   Clients can roam between access points
-   Access controller manages channel allocation to minimize interference

The simulation reads network configurations from a file and provides detailed logs of all network activities.

## Features

-   Dynamic channel allocation with interference avoidance
-   Client roaming based on signal strength
-   Distance and RSSI calculations
-   Comprehensive logging of network events
-   Binary storage of logs using pickle serialization
-   Multiple frequency band support (2.4GHz, 5GHz)
-   Intelligent client-AP matching algorithm with load balancing

## Project Structure

### Core Components

-   **log.py**: Custom binary logging system using pickle
-   **network.py**: Base network class with shared attributes
-   **client.py**: Client implementation with connection handling
-   **ap.py**: Access Point implementation with signal calculations
-   **ac.py**: Access Controller for managing AP channel allocation
-   **main.py**: Main simulation coordinator

### Class Hierarchy

```
Network (Base Class)
├── Client
└── AccessPoint

AccessController (Independent)
Bin (Logging System)

```

## How It Works

1.  The simulation reads network configuration from an input file
2.  Access points are initialized and assigned channels by the Access Controller
3.  Clients are introduced to the network and connected to optimal access points
4.  As clients move, signal strengths are recalculated
5.  Clients roam to better access points when necessary
6.  All events are logged for analysis

## Usage

bash

`# Run the simulator with a configuration file`
`python main.py path/to/config_file.txt`

### Configuration File Format

The configuration file should contain lines defining:

-   Access Points (AP)
-   Clients (CLIENT)
-   Movement instructions (MOVE)

Example:

```
AP 1 2.4 0 0
AP 2 5 10 10
CLIENT 1 2.4 5 5
MOVE 1 7 7

```

## Algorithm Details

The simulator uses a sophisticated algorithm to determine the best access point for each client:

1.  Check which frequencies are supported by both client and access point
2.  Filter access points by minimum required RSSI
3.  Apply roaming logic following the "When to Roam" priorities
4.  If multiple access points remain available, connect to the one with the lowest connection count

## Dependencies

-   Python 3.6+
-   Standard library modules only (no external dependencies)

## Development

This project follows object-oriented design principles with clear class responsibilities:

-   Separation of concerns between network entities
-   Inheritance for shared functionality
-   Encapsulation of logging within each component
-   Custom magic methods for enhanced usability

----------

_This simulator was developed as an educational/research project to demonstrate WiFi networking principles._
