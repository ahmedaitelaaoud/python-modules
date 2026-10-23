print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

def crisis_handler(filename):
    """Handle archive access attempts with crisis response protocols"""
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, failsafe protocols active\n")

# Test different crisis scenarios
crisis_handler("../data-generator-tools/lost_archive.txt")
crisis_handler("../data-generator-tools/classified_vault.txt")
crisis_handler("../data-generator-tools/standard_archive.txt")

print("All crisis scenarios handled successfully. Archives secure.")
