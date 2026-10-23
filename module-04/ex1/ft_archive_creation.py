print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
f = open("new_discovery.txt", 'w')
print("Initializing new storage unit: new_discovery.txt")
line_1 = "[ENTRY 001] New quantum algorithm discovered"
print(line_1)
f.write(line_1 + '\n')
line_2 = "[ENTRY 002] Efficiency increased by 347%"
print(line_2)
f.write(line_2 + '\n')
line_3 = "[ENTRY 003] Archived by Data Archivist trainee"
print(line_3)
f.write(line_3 + '\n')

f.close()
print("\nData inscription complete. Storage unit sealed.\nArchive 'new_discovery.txt' ready for long-term preservation.")
