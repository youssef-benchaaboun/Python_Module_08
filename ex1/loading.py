import importlib
import sys
from types import ModuleType


DEPENDENCIES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def load_dependencies() -> dict[str, ModuleType] | None:
    loaded: dict[str, ModuleType] = {}
    missing: list[str] = []

    print("Checking dependencies:")
    for package, purpose in DEPENDENCIES.items():
        try:
            module = importlib.import_module(package)
            loaded[package] = module
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {purpose}")
        except ImportError:
            missing.append(package)
            print(f"[MISSING] {package} - {purpose}")

    if missing:
        print("\nMissing dependencies: " + ", ".join(missing))
        print("Install with pip: pip install -r requirements.txt")
        print("Or install with Poetry: poetry install")
        return None
    return loaded


def analyze_matrix_data(modules: dict[str, ModuleType]) -> None:
    np = modules["numpy"]
    pd = modules["pandas"]
    pyplot = importlib.import_module("matplotlib.pyplot")

    generator = np.random.default_rng(42)
    signals = generator.normal(50, 15, 1000)
    frame = pd.DataFrame({"signal_strength": signals})
    rolling_average = frame["signal_strength"].rolling(30).mean()

    print("\nAnalyzing Matrix data...")
    print(f"Processing {len(frame)} data points...")
    print("Generating visualization...")

    figure, axes = pyplot.subplots(figsize=(10, 5))
    axes.plot(frame.index, frame["signal_strength"], alpha=0.35,
              label="Matrix signal")
    axes.plot(frame.index, rolling_average, linewidth=2,
              label="30-point average")
    axes.set(title="Matrix Signal Analysis", xlabel="Data point",
             ylabel="Signal strength")
    axes.legend()
    figure.tight_layout()
    figure.savefig("matrix_analysis.png")
    pyplot.close(figure)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    modules = load_dependencies()
    if modules is None:
        sys.exit(1)
    analyze_matrix_data(modules)


if __name__ == "__main__":
    main()
