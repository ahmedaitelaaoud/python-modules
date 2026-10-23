print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")
print("SECURE EXTRACTION:")
with open("../data-generator-tools/classified_data.txt", 'r') as file:
    data = file.read()
    print(data)
    print()
print("SECURE PRESERVATION:")
with open("../data-generator-tools/security_protocols.txt", 'w') as file:
    line1 = "[CLASSIFIED] New security protocols archived"
    file.write(line1 + '\n')
    print(line1)
    print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")
