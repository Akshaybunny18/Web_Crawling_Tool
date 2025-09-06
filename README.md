# 🐇 Bunny Web Surfer

A powerful recursive web crawler built in Python that intelligently fetches links from websites. Originally developed as a club task to extract files from IIITH intranet, now generalized to work on any website with advanced crawling capabilities.

## 🎯 Project Overview

Developed a recursive web scraping tool using Python, Requests and BeautifulSoup for extracting specific file types from websites. The tool features depth-limited crawling with exception handling to prevent infinite recursion and timeouts, plus URL validation and duplicate detection mechanisms for efficient data collection.

---

## ✨ Key Features

- **🌐 Universal Website Crawling** - Works on any website by providing a starting URL
- **🎯 Targeted File Collection** - Specify file extensions (`.pdf`, `.jpg`, `.mp4`, etc.) to collect only those files
- **🔄 Comprehensive Link Extraction** - Use `"all"` option to grab every discovered link
- **🔗 Smart URL Handling** - Automatically handles both absolute and relative URLs
- **⚡ Depth-Limited Crawling** - Configurable recursion depth (default: 8 levels) to prevent infinite loops
- **🛡️ Robust Exception Handling** - Built-in timeout protection and SSL certificate handling
- **🔍 Duplicate Detection** - Efficient URL validation and duplicate prevention
- **📊 Real-time Progress** - Live progress updates during crawling process
- **💾 Automated Results Export** - Saves all collected URLs to `urls.txt` file
- **🏫 IIITH Intranet Support** - Specialized version for institutional intranet crawling

---

## 📂 Project Structure

### 1. `web-scraper.py` (Universal Version)
The main general-purpose web crawler that works on any website.

**Features:**
- Universal website compatibility
- Configurable file type filtering
- Smart relative/absolute URL resolution
- Progress tracking with detailed output

### 2. `Webfile_Req_intranet.py` (IIITH Specialized)
Optimized version specifically designed for intranet.iiit.ac.in crawling.

**Features:**
- Pre-configured for `intranet.iiit.ac.in` domain
- Specialized link handling for institutional websites
- Optimized for internal network structures

---

## 🚀 Quick Start

### Prerequisites
```bash
pip install requests beautifulsoup4 lxml
```

### Installation
```bash
git clone https://github.com/<your-username>/bunny-web-surfer.git
cd bunny-web-surfer
```

### Usage

#### General Web Crawling
```bash
python web-scraper.py
```

#### IIITH Intranet Crawling
```bash
python Webfile_Req_intranet.py
```

---

## 💡 Usage Examples

### Example 1: PDF Collection
```
=== Bunny Web Surfer ===
Enter a file extension (like pdf, jpg, mp4) or 'all': pdf
Enter the starting URL: https://example.com

(Bunny) Fetching SUB(URLS): https://example.com
(Bunny) Fetching SUB(URLS): https://example.com/documents
(Bunny) Fetching SUB(URLS): https://example.com/research

Surfing complete. Found 24 links. Saved to urls.txt
```

### Example 2: All Links Collection
```
Enter a file extension (like pdf, jpg, mp4) or 'all': all
Enter the starting URL: https://university.edu

Surfing complete. Found 156 links. Saved to urls.txt
```

### Example 3: Image Collection
```
Enter a file extension (like pdf, jpg, mp4) or 'all': jpg
Enter the starting URL: https://gallery.com

Surfing complete. Found 89 links. Saved to urls.txt
```

---

## ⚙️ Configuration Options

### Recursion Depth
Default maximum depth is **8 levels**. Modify in the code:
```python
def sif(x, url, visited, data, deep=0, maxdeep=8):  # Change maxdeep value
```

### Timeout Settings
Default request timeout is **10 seconds**:
```python
code = requests.get(url, timeout=10, verify=False).text  # Modify timeout value
```

### SSL Verification
SSL verification is disabled by default for flexibility:
```python
requests.get(url, timeout=10, verify=False)  # Set verify=True for strict SSL
```

---

## 🔧 Technical Implementation

### Core Algorithm & 🎓 Educational Value
- **Recursive Depth-First Search** traversal
- **BeautifulSoup HTML parsing** for link extraction
- **Set-based duplicate prevention** for efficiency
- **Exception handling** for network failures
- **URL normalization** for consistent link processing
This project demonstrates:
- **Web scraping fundamentals** and best practices
- **Recursive algorithms** and depth management
- **Exception handling** in network programming  
- **Data structures** usage (sets for deduplication)
- **File I/O operations** and data persistence
- **URL manipulation** and validation techniques

### Supported HTML Elements
The crawler extracts URLs from:
- `<a>` tags (href attribute)
- `<link>` tags (href attribute)  
- `<img>` tags (src attribute)
- `<iframe>`, `<frame>` tags (src attribute)
- `<audio>`, `<video>` tags (src attribute)
- `<script>` tags (src attribute)
- `<base>`, `<area>` tags (href attribute)

---

## ⚠️ Important Notes

- **Rate Limiting**: Be respectful of target websites and consider adding delays between requests for heavy crawling
- **SSL Warnings**: When `verify=False` is used, SSL warnings may appear but are suppressed
- **Network Timeouts**: 10-second timeout prevents hanging on unresponsive pages
- **Memory Usage**: Large websites may consume significant memory due to URL storage
- **Legal Compliance**: Always ensure you have permission to crawl target websites

---

## 🛠️ Built With

- **[Python](https://python.org)** - Core programming language
- **[Requests](https://docs.python-requests.org/)** - HTTP library for web requests
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** - HTML/XML parsing library
- **[lxml](https://lxml.de/)** - Fast XML and HTML parser

---

## 🚀 Future Enhancements

- [ ] **Multi-threading support** for faster crawling
- [ ] **Database integration** for large-scale data storage  
- [ ] **GUI interface** for non-technical users
- [ ] **Advanced filtering options** (regex patterns, file size limits)
- [ ] **Export formats** (CSV, JSON, XML)
- [ ] **Crawl scheduling** and automation features
- [ ] **Statistics dashboard** with crawling analytics


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


**Happy Crawling! 🐇🌐**