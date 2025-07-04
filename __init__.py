"""
Super Simple AO Connect - Child-friendly interface
"""

from .simple import SimpleAO, quick_start

# Export the main class for easy import
__all__ = ['SimpleAO', 'quick_start']

# Super simple usage - just import and go!
"""
# Example usage - as easy as it gets!

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

# That's it! Super simple! 🎉
""" 