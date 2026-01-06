# 🦁 Animal Information Website Generator

This project generates a simple HTML website that displays information about animals.
The user enters an animal name, data is fetched from an external API, and the results
are dynamically inserted into an HTML template.

## 📌 Overview
- Prompts the user for an animal name
- Fetches animal data via an API
- Injects the data into an HTML template
- Generates a final `index.html` file
- Displays an error message if the animal does not exist

## 📂 Project Structure
animals_web_generator.py  
data_fetcher.py  
animals_template.html  
index.html  
README.md  

## ▶️ How to Run
1. Make sure Python 3.8+ is installed
2. Run the script:
   `python animals_web_generator.py`
3. Enter an animal name (e.g. `lion`)
4. Open `index.html` in your browser

## 🛠 Technologies
- Python 3
- HTML
- External Animal API
- File handling and string manipulation

## ✅ Output
The generated website displays:
- Animal name
- Diet
- Location
- Type (if available)

If the animal does not exist, an error message is shown on the page.

## 🚀 Notes
This project was created as part of a Python backend learning exercise and can be
extended with styling, testing, or additional features.
