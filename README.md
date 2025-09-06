# 🤖 AI Web Scraper

## What is this? 🤔

Imagine you want to get specific information from a website, but instead of reading through all the text yourself, you have a smart robot friend that can do it for you! This AI Web Scraper is like that robot friend.

**In simple words:** This app visits any website you want, reads all the text on that website, and then finds exactly what you're looking for using AI.

## How does it work? ⚙️

Think of it like this:
1. 📱 You tell the app which website to visit (like telling your friend to go to a library)
2. 🔍 The app goes to that website and copies all the text (like your friend reading all the books)
3. 🧠 You ask the AI to find something specific (like asking "find all the phone numbers")
4. ✨ The AI gives you exactly what you asked for!

## What can you do with it? 🎯

- **Extract emails** from a company's website
- **Find all phone numbers** on a contact page
- **Get product prices** from a shopping website
- **Collect news headlines** from a news site
- **Extract any specific information** you need!

## What do you need to run this? 📋

Before you can use this cool app, you need to install some things on your computer:

### Required Software:
1. **Python** (the programming language this app is written in)
2. **Google Chrome browser** (the app uses this to visit websites)
3. **ChromeDriver** (a special tool that lets the app control Chrome)
4. **Ollama with Llama3.1** (the AI brain that understands and extracts information)

### Required Python Packages:
The app needs these special tools (called packages):
- `streamlit` - Creates the web app interface
- `langchain` - Helps talk to the AI
- `langchain_ollama` - Connects to the Ollama AI
- `selenium` - Controls the web browser
- `beautifulsoup4` - Reads website content
- `lxml` - Helps parse website data
- `html5lib` - Another website reading tool
- `python-dotenv` - Manages settings

## How to set it up? 🛠️

### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org/)

### Step 2: Install the required packages
Open your computer's terminal/command prompt and type:
```bash
pip install -r requirements.txt
```

### Step 3: Install Ollama and Llama3.1
1. Download Ollama from [ollama.ai](https://ollama.ai/)
2. Install it on your computer
3. Open terminal and run: `ollama pull llama3.1`

### Step 4: Download ChromeDriver
1. Go to [ChromeDriver downloads](https://chromedriver.chromium.org/)
2. Download the version that matches your Chrome browser
3. Put the `chromedriver` file in the same folder as your app

## How to use it? 🚀

### Step 1: Start the app
Open terminal in your app folder and type:
```bash
streamlit run main.py
```

### Step 2: Open your web browser
The app will automatically open in your browser at `http://localhost:8501`

### Step 3: Enter a website URL
Type the website address you want to scrape (like `https://example.com`)

### Step 4: Click "Scrape Site"
The app will visit the website and get all the text content

### Step 5: Tell the AI what to find
In the text box, write what you want to extract, like:
- "Find all email addresses"
- "Extract all phone numbers"
- "Get all product names and prices"
- "Find all links to other pages"

### Step 6: Click "Parse"
The AI will read through all the website content and give you exactly what you asked for!

## Example Usage 💡

Let's say you want to find all email addresses from a company's contact page:

1. Enter: `https://company-website.com/contact`
2. Click "Scrape Site"
3. In the prompt box, write: "Extract all email addresses"
4. Click "Parse"
5. The AI will return something like:
   ```
   info@company.com
   support@company.com
   sales@company.com
   ```

## Important Files 📁

- **main.py** - The main app that creates the user interface
- **scrape.py** - The code that visits websites and gets the content
- **parse.py** - The code that talks to the AI to extract information
- **requirements.txt** - List of all the tools the app needs

## Tips for better results 🌟

1. **Be specific** in your requests: Instead of "find contact info", try "find email addresses and phone numbers"
2. **Use simple language**: The AI understands normal English better than technical terms
3. **Try different websites**: Some websites work better than others
4. **Be patient**: Large websites might take a few seconds to process

## Troubleshooting 🔧

**Problem**: "ChromeDriver not found"
**Solution**: Make sure you downloaded ChromeDriver and put it in the right folder

**Problem**: "Ollama model not found"
**Solution**: Run `ollama pull llama3.1` in your terminal

**Problem**: "Website won't load"
**Solution**: Make sure you included `http://` or `https://` in the URL

## Is it safe? 🔒

- The app only reads public information from websites
- It doesn't store any personal data
- It's like having a person visit the website and take notes
- Always respect website terms of service and robots.txt files

## Have fun exploring! 🎉

This app is like having a super-powered research assistant. You can use it to quickly gather information from websites without spending hours reading through everything yourself. The more you use it, the better you'll get at asking the right questions to get the information you need!

Remember: With great power comes great responsibility - always use this tool ethically and respect website owners' wishes!
