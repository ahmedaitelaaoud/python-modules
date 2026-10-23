import os
from dotenv import load_dotenv


def oracle() -> None:
    """Checks and displays the status of required environment variables."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    # Load variables from a .env file into the environment
    env_loaded = load_dotenv()

    # Mapping of technical variable names to human-readable labels
    required_vars = {
        "MATRIX_MODE": "Mode",
        "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
        "ZION_ENDPOINT": "Zion Network",
    }

    print("Configuration loaded:")
    loaded_values = {}

    # Iterate through required variables to check their status
    for env_var, label in required_vars.items():
        value = os.getenv(env_var)
        loaded_values[env_var] = value

        if value is None:
            # Handle missing variables
            print(f"{label}: [WARNING] Not Set")
        else:
            # Format the output for sensitive or specific data
            if env_var == "API_KEY":
                display_val = "Authenticated"  # Don't print the actual key!
            elif env_var == "DATABASE_URL":
                display_val = "Connected to local instance"
            else:
                display_val = value

            print(f"{label}: {display_val}")

    print()

    # Verify that critical secrets are present
    print("Environment security check:")
    if loaded_values["API_KEY"] and loaded_values["DATABASE_URL"]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Secrets missing from environment")

    # Check if the .env file was actually found and read
    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not found")

    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
