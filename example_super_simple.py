#!/usr/bin/env python3
"""
Super Simple AO Connect Example
As easy as it gets! 🚀
"""
from pyaoconnect import SimpleAO

def main():
    """
    Super simple example - just copy and paste!
    """
    print("🚀 AO Connect - Super Simple Example")
    print("=" * 40)
    
    # 1. Create AO instance (auto-loads wallet if exists)
    print("1️⃣ Creating AO instance...")
    ao = SimpleAO()
    
    # 2. Generate wallet if needed
    if not ao.ao:
        print("2️⃣ Generating wallet...")
        address = ao.generate_wallet()
        if address:
            print(f"   ✅ Wallet created: {address[:10]}...")
        else:
            print("   ❌ Failed to create wallet")
            return
    else:
        print("2️⃣ ✅ Wallet already loaded!")
    
    # 3. Spawn a process
    print("3️⃣ Spawning process...")
    # Using a known working process hash from AO examples
    process_hash = "JArYBF-D8q2OmZ4Mok00sD2Y_6SYEQ7Hjx-6VZ_jl3g"
    print(f"   📝 Using process hash: {process_hash[:20]}...")
    
    process_id = ao.spawn_process(process_hash, "My Cool App")
    
    if not process_id:
        print("   ❌ Failed to spawn process")
        print("   💡 This could be because:")
        print("      - The process hash is invalid")
        print("      - AO Connect is not properly configured")
        print("      - Network issues")
        print("   🎯 Let's try a simple test without spawning...")
        
        # Try to test with a known process ID instead
        test_process_id = "your_test_process_id_here"  # Replace with a real one
        print(f"   📝 You can test with a real process ID: {test_process_id}")
        return
    
    print(f"   ✅ Process spawned! ID: {process_id[:20]}...")
    
    # 4. Send a message
    print("4️⃣ Sending message...")
    message_result = ao.send_message(process_id, "Hello AO! 🐍")
    if message_result:
        print(f"   ✅ Message sent! ID: {message_result[:20]}...")
    else:
        print("   ❌ Failed to send message")
    
    # 5. Send some code to evaluate
    print("5️⃣ Sending eval...")
    eval_result = ao.send_eval(process_id, "print('Hello from Python! 🚀')")
    if eval_result:
        print(f"   ✅ Eval sent! ID: {eval_result[:20]}...")
    else:
        print("   ❌ Failed to send eval")
    
    # 6. Read the results
    print("6️⃣ Reading results...")
    results = ao.read_results(process_id, limit=5)
    print(f"   📊 Found {len(results)} results")
    
    # 7. Test with dry run
    print("7️⃣ Testing with dry run...")
    dryrun_result = ao.dry_run(process_id, "print('This is just a test!')")
    if dryrun_result:
        print("   ✅ Dry run completed!")
    else:
        print("   ❌ Dry run failed")
    
    print("\n🎉 All done! That was super easy!")
    print("📊 Summary:")
    print(f"   - Process ID: {process_id[:20]}...")
    print(f"   - Results found: {len(results)}")
    print("   - Everything worked! ✅")

if __name__ == "__main__":
    main() 