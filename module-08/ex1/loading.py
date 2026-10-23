import sys
import importlib

def check_and_load_modules() -> bool:
    """
    Checks if all required external libraries are installed in the current
    Python environment before attempting to run the main program.
    """
    required_modules = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }
    all_good = True
    print("Checking dependencies:")

    for mod_name, description in required_modules.items():
        try:
            # Dynamically attempt to import the module by its string name
            imported_mod = importlib.import_module(mod_name)
            # Retrieve the installed version of the module
            version = imported_mod.__version__
            print(f"[OK] {mod_name} ({version}) - {description}")
        except ImportError:
            # If the import fails, the dependency is missing
            print(f"[ERROR] Missing {mod_name}! Run: pip install {mod_name}")
            all_good = False

    return all_good


def analyze_matrix_data() -> None:
    """
    Simulates data processing by generating random matrix anomaly scores,
    structuring them, and rendering a stylized 2D visualization.
    """
    try:
        # Local imports ensure these are only loaded if the check passes
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")

        # 1. NUMPY: Generate 1000 random "anomaly scores" between 0 and 100
        anomaly_scores = np.random.rand(1000) * 100

        # 2. PANDAS: Organize the raw numbers into a structured DataFrame
        df = pd.DataFrame({
            "Data_Index": range(1000),
            "Anomaly_score": anomaly_scores
        })

        print("Generating visualization...\n")

        # 3. MATPLOTLIB: Create a figure (10x6 inches)
        bg_color = "#0d1117"
        grid_color = "#30363d"
        text_color = "#c9d1d9"
        data_color = "#00f0ff"

        plt.figure(figsize=(10, 6))

        # Create the scatter plot using Electric Cyan.
        # Slightly increased 's' and 'alpha' to make the neon glow stand out
        plt.scatter(
            df["Data_Index"], df["Anomaly_score"],
            c=data_color, alpha=0.7, s=20
        )

        # Add labels with the softer white, and make the title bold
        plt.title(
            "Matrix Sector Anomaly Detection",
            color=text_color,
            fontweight="bold"
        )
        plt.xlabel("Data Point Index", color=text_color)
        plt.ylabel("Signal Anomaly Score", color=text_color)

        # Apply the modern dark slate background
        plt.gca().set_facecolor(bg_color)
        plt.gcf().patch.set_facecolor(bg_color)

        # A sleek, dashed grid that doesn't overpower the data
        plt.grid(True, color=grid_color, linestyle="--", alpha=0.7)

        # PRO-TIP: Change axis borders (spines) and tick marks to match theme
        for spine in plt.gca().spines.values():
            spine.set_color(grid_color)
        plt.tick_params(colors=text_color)

        # 4. Save the figure to the exact filename required by the subject
        file_name = "matrix_analysis.png"
        plt.savefig(file_name)

        # Close the plot to free up your computer's memory
        plt.close()
        print("Analysis complete!")
        print(f"Results saved to: {file_name}")

    except Exception as e:
        print(f"[ERROR] The Matrix analysis failed: {e}")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    if check_and_load_modules():
        analyze_matrix_data()
    else:
        sys.exit(1)
