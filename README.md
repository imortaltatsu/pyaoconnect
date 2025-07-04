# PyAOConnect - Super Simple AO Connect 🚀

The easiest way to use AO Connect from Python! As simple as it gets.

## Installation

### Prerequisites
- Python 3.7+
- Node.js (download from https://nodejs.org/)
- Git

### Method 1: Direct Installation (Recommended)
```bash
# Clone the repository
git clone https://github.com/imortaltatsu/pyaoconnect.git
cd pyaoconnect

# Install using setup.py (this will handle all dependencies automatically)
python setup.py install

# Or for development
python setup.py develop
```

### Method 2: pip install git+https
```bash
# Install directly from GitHub
pip install git+https://github.com/imortaltatsu/pyaoconnect.git

# After installation, run the post-install script to set up dependencies
python -c "import post_install; post_install.main()"
```

The setup script will automatically:
- ✅ Install Node.js dependencies (@permaweb/aoconnect)
- ✅ Clone and install aopy-connect dependency
- ✅ Set up everything you need

## Super Simple Usage

```python
from pyaoconnect import SimpleAO

# Create your AO instance
ao = SimpleAO()

# Generate a wallet (if you don't have one)
ao.generate_wallet()

# Spawn a process
process_id = ao.spawn_process("your_process_hash", "My Cool App")

# Send a message
ao.send_message(process_id, "Hello AO!")

# Send some code to run
ao.send_eval(process_id, "print('Hello from Python!')")

# Read the results
results = ao.read_results(process_id)

# Test something safely
ao.dry_run(process_id, "print('Just testing!')")
```

## That's it! 🎉

No complex setup, no confusing APIs. Just simple commands that do exactly what you expect:

- `generate_wallet()` - Create a new wallet
- `spawn_process()` - Start a new process
- `send_message()` - Send a message
- `send_eval()` - Send code to evaluate
- `read_results()` - Get the results
- `dry_run()` - Test safely

## Quick Start

```python
# Run the super simple example
from pyaoconnect import quick_start
quick_start()
```

## Requirements

- Python 3.7+
- Node.js (for the underlying AO Connect)
- npm package `@permaweb/aoconnect`

## Features

✅ **Super Simple** - No complex setup required  
✅ **Auto Wallet Management** - Creates and loads wallets automatically  
✅ **Friendly Messages** - Clear success/error messages with emojis  
✅ **Safe Testing** - Dry run functionality for testing  
✅ **Child-Friendly** - Easy enough for anyone to use  

## Examples

### Basic Usage
```python
from pyaoconnect import SimpleAO

ao = SimpleAO()
ao.generate_wallet()
process_id = ao.spawn_process("process_hash", "My App")
ao.send_message(process_id, "Hello!")
```

### Advanced Usage
```python
# Send code to evaluate
ao.send_eval(process_id, "print('Hello from AO!')")

# Read results
results = ao.read_results(process_id, limit=10)

# Test safely
ao.dry_run(process_id, "print('Test message')")
```

## License

MIT License - Use it however you want! 