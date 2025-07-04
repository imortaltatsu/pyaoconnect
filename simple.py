"""
Super Simple AO Connect - Child-friendly interface
"""

import json
import os
from typing import Dict, List, Optional, Any
from .core import AOConnect

class SimpleAO:
    """
    Super simple AO Connect - as easy as possible!
    """
    
    def __init__(self, wallet_file: str = "my_wallet.json"):
        self.wallet_file = wallet_file
        self.ao = None
        self._load_wallet()
    
    def _load_wallet(self):
        """Load wallet if it exists"""
        if os.path.exists(self.wallet_file):
            self.ao = AOConnect(self.wallet_file)
            print(f"✅ Loaded wallet from {self.wallet_file}")
        else:
            print(f"📝 No wallet found. Use 'generate_wallet()' to create one!")
    
    def generate_wallet(self) -> str:
        """
        Generate a new wallet - super simple!
        Returns: wallet address
        """
        print("🔐 Generating new wallet...")
        result = AOConnect().create_wallet()
        
        if result.get('success') and 'wallet' in result:
            wallet_data = result['wallet']
            address = wallet_data['address']
            
            # Save wallet
            with open(self.wallet_file, 'w') as f:
                json.dump(wallet_data['jwk'], f)
            
            self.ao = AOConnect(self.wallet_file)
            print(f"✅ Wallet created! Address: {address[:10]}...")
            return address
        else:
            print("❌ Failed to create wallet")
            return None
    
    def spawn_process(self, process_hash: str, name: str = "My Process") -> str:
        """
        Spawn a new process - give it a name!
        Returns: process ID
        """
        if not self.ao:
            print("❌ No wallet loaded. Use 'generate_wallet()' first!")
            return None
        
        print(f"🚀 Spawning process: {name}")
        tags = [
            {"name": "Name", "value": name},
            {"name": "Authority", "value": "fcoN_xJeisVsPXA-trzVAuIiqO3ydLQxM-L4XbrQKzY"}
        ]
        
        # Add scheduler and data like the working test
        scheduler = "_GQ33BkPtZrqxA84vM8Zk-N2aO0toNNu_C-l-rawrBA"
        data = "optional initial data"
        
        result = self.ao.spawn(process_hash, tags=tags, scheduler=scheduler, data=data)
        print("DEBUG SPAWN RESULT:", result)
        
        if result.get('success'):
            process_id = result.get('processId') or result.get('result', {}).get('processId')
            print(f"✅ Process spawned! ID: {process_id[:10]}...")
            return process_id
        else:
            print("❌ Failed to spawn process")
            return None
    
    def send_message(self, process_id: str, message: str, action: str = "Message") -> str:
        """
        Send a simple message to a process
        Returns: message ID
        """
        if not self.ao:
            print("❌ No wallet loaded. Use 'generate_wallet()' first!")
            return None
        
        print(f"📤 Sending message: {message}")
        tags = [{"name": "Action", "value": action}]
        
        result = self.ao.send(process_id, message, tags=tags)
        
        if result.get('success'):
            message_id = result.get('messageId') or result.get('result', {}).get('messageId')
            print(f"✅ Message sent! ID: {message_id[:10]}...")
            return message_id
        else:
            print("❌ Failed to send message")
            return None
    
    def send_eval(self, process_id: str, code: str) -> str:
        """
        Send code to be evaluated - super simple!
        Returns: message ID
        """
        return self.send_message(process_id, code, action="Eval")
    
    def read_results(self, process_id: str, limit: int = 10) -> List[Dict]:
        """
        Read results from a process - get the latest messages!
        Returns: list of results
        """
        print(f"📖 Reading results from process...")
        result = self.ao.results(process_id, options={"limit": limit})
        
        if result.get('success'):
            edges = result.get('results', {}).get('edges', [])
        else:
            edges = result.get('edges', [])
        
        print(f"✅ Found {len(edges)} results!")
        return edges
    
    def dry_run(self, process_id: str, message: str, action: str = "Test") -> Dict:
        """
        Test a message without sending it - safe testing!
        Returns: dry run result
        """
        if not self.ao:
            print("❌ No wallet loaded. Use 'generate_wallet()' first!")
            return None
        
        print(f"🧪 Testing message: {message}")
        tags = [{"name": "Action", "value": action}]
        
        result = self.ao.dryrun(process_id, message, tags=tags)
        
        if result.get('success'):
            dryrun_data = result.get('result', {})
            print("✅ Dry run completed successfully!")
            return dryrun_data
        else:
            print("❌ Dry run failed")
            return result

# Super simple usage examples
def quick_start():
    """
    Super simple example - just copy and paste!
    """
    print("🚀 AO Connect Quick Start")
    print("=" * 30)
    
    # Create simple AO instance
    ao = SimpleAO()
    
    # Generate wallet (if needed)
    if not ao.ao:
        ao.generate_wallet()
    
    # Example process hash (replace with real one)
    process_hash = "JArYBF-D8q2OmZ4Mok00sD2Y_6SYEQ7Hjx-6VZ_jl3g"
    
    # Spawn a process
    process_id = ao.spawn_process(process_hash, "My Cool Process")
    
    if process_id:
        # Send a message
        ao.send_message(process_id, "Hello AO!")
        
        # Send some code to evaluate
        ao.send_eval(process_id, "print('Hello from Python!')")
        
        # Read the results
        results = ao.read_results(process_id)
        print(f"📊 Got {len(results)} results!")
        
        # Test something safely
        ao.dry_run(process_id, "print('This is just a test')")
    
    print("🎉 Done! That was easy!")

if __name__ == "__main__":
    quick_start() 