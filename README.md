# Market research use case generation
## Table of Contents
- [Project Overview](#project-overview)
- [How It Works](#How-It-Works)
- [Features](#Features)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Tasks Performed.](#task-performed)
- [Streamlit Screenshot](#streamlit-screenshot)
- [Results and Findings.](#results-and-findings)

## Project Overview

This project is a web application that helps users explore AI/ML use cases and find relevant datasets to bring those ideas to life. Using GPT-2, the app generates AI/ML use cases based on the user's input about an industry and its trends. It also searches popular platforms like HuggingFace and Kaggle to suggest datasets matching the generated use cases.

---

## How It Works

1. The user inputs the **industry** (e.g., Retail) and **trends** (e.g., Supply chain optimization).
2. The app uses GPT-2 to generate 3 AI/ML use cases tailored to the input.
3. Keywords are extracted from these use cases to perform a search for datasets.
4. The app retrieves relevant datasets from HuggingFace and Kaggle and displays them to the user.

The process is managed by a **Multi-Agent System** that coordinates between the components responsible for generating use cases and fetching datasets.

---

## Features

- **Generate AI/ML Use Cases**:
  - Get three actionable AI/ML ideas based on the given industry and trends.
- **Find Relevant Datasets**:
  - Search and retrieve datasets from HuggingFace and Kaggle automatically.
- **Interactive User Interface**:
  - A clean and easy-to-use interface powered by Streamlit.

---

## Tools and Technologies Used

- **Python**: Main programming language.
- **Streamlit**: Framework for building the web interface.
- **HuggingFace Transformers**: GPT-2 model for text generation.
- **Requests**: For making API calls to HuggingFace and Kaggle.
- **Pandas**: For handling data and results.

---

## Tasks Performed

1. Designed a multi-agent system with two agents:
   - **UseCaseAgent**: For generating AI/ML ideas.
   - **ResourceAgent**: For finding relevant datasets.
2. Integrated GPT-2 from HuggingFace for natural language generation.
3. Developed API integration for HuggingFace and Kaggle dataset searches.
4. Built a Streamlit application for user interaction.
5. Tested the app with various industries and trends to ensure functionality.

---

## Streamlit Screenshot
![Screenshot 2024-12-31 154718](https://github.com/user-attachments/assets/d0d5f9d4-8069-4a53-94b2-ecc16621ff54)
---

## Results

- The application successfully generates tailored AI/ML use cases for any given industry and trends.
- It retrieves relevant datasets from HuggingFace and Kaggle, providing users with resources to start implementing their ideas.
- A user-friendly interface allows seamless interaction and exploration of AI/ML possibilities.

---
