# crawl4ai-tutorials


## Project Setup

### Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager

### Initial Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd crawl4ai-tutorials
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Install Playwright browsers (required for crawl4ai):
   ```bash
   uv run playwright install
   ```

   This downloads the Chromium browser binary that crawl4ai uses for web scraping.

## Configuration

### Running Scripts

The project uses Click for command-line interfaces. Each tutorial script can accept an optional URL parameter.

**Basic usage:**
```bash
uv run python <script_name>.py
```

**With custom URL:**
```bash
# Using positional argument
uv run python basic_config.py https://example.com

# Or using the option flag (if configured)
uv run python basic_config.py --url https://example.com
```

**If no URL is provided**, scripts use their hardcoded default URLs.

### Script Options

Most scripts support:
- `url` - Target URL to crawl (optional, defaults to script-specific URL)

Run any script with `--help` to see available options:
```bash
uv run python basic_config.py --help
```

## Tutorials

Each Python file in this repository represents a different crawl4ai tutorial or example.