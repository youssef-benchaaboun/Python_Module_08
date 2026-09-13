import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    print("Missing dependency: python-dotenv")
    print("Install it with: pip install -r requirements.txt")
    sys.exit(1)


REQUIRED_VARIABLES: tuple[str, ...] = (
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT",
)


def masked_status(value: str | None, success: str) -> str:
    return success if value else "Not configured"


def main() -> None:
    env_loaded = load_dotenv(override=False)
    mode = os.getenv("MATRIX_MODE", "development").lower()
    log_level = os.getenv("LOG_LEVEL", "DEBUG" if mode == "development"
                          else "WARNING")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")
    if mode not in ("development", "production"):
        print("ERROR: MATRIX_MODE must be development or production.")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {masked_status(database_url, 'Configured')}")
    print(f"API Access: {masked_status(api_key, 'Authenticated')}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {masked_status(zion_endpoint, 'Online')}")

    missing = [name for name in REQUIRED_VARIABLES if not os.getenv(name)]
    print("\nEnvironment security check:")
    print("[OK] Secrets are read from environment variables")
    print(f"[{'OK' if env_loaded else 'WARNING'}] "
          f".env file {'loaded' if env_loaded else 'not found'}")
    print("[OK] Environment variables override .env values")

    if missing:
        print("\nWARNING: Missing configuration: " + ", ".join(missing))
        print("Copy .env.example to .env and configure its values.")
        sys.exit(1)

    if mode == "production":
        print("Production configuration active.")
    else:
        print("Development configuration active.")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
