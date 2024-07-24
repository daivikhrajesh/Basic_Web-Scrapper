# Web Scraper with BeautifulSoup

This project is a basic web scraper built using Python's `requests` and `BeautifulSoup` libraries. It fetches a webpage, parses the HTML content, and extracts specific elements such as headings, images, and special divs.

## Features

- Extracts and prints all `<h1>` headings from the webpage.
- Extracts and prints all image sources (`src` attributes) from the webpage.
- Extracts and prints the text of the first `<div>` element with the class "special".

## Prerequisites

Make sure you have Python installed on your system. You also need to install the `requests` and `BeautifulSoup` libraries. You can install them using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the script.

2. Replace `"example url"` with the actual URL you want to scrape in the `url` variable in the script.

3. Run the script:

```bash
python main.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

---

Feel free to customize this README file as per your project's requirements.
