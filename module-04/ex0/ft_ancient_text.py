print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
try:
    print("Accessing Storage Vault: ancient\\_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    f = open("../data-generator-tools/ancient_fragment.txt", "r")
    print(f.read())
    f.close()
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
