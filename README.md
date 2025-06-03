# Activity Tracker CLI

The Activity Tracker CLI is a Python-based command-line application designed to help users log and manage their daily activities. Unlike traditional fitness trackers, this tool supports a wide range of activities—from learning and creative work to physical exercise and mindfulness.

Built with SQLAlchemy for database management and Alembic for migrations, it provides a structured way to track time spent on different tasks, categorize them, and review progress.


![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0%2B-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A command-line activity tracker with SQLite database storage, supporting multiple users and activity categories.

## Features

- 🧑 User management (create, list users)
- 📊 Activity logging with categories
- ⏱️ Duration tracking
- 📅 Date-based organization
- 🔍 View all user activities
- 🗃️ SQLite database storage
- 🔄 Alembic database migrations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/activity-tracker-cli.git
cd activity-tracker-cli