"""Demonstration of oneenv integration with refinire-tool-tavily."""

import subprocess
import sys
from pathlib import Path


def main():
    """Demonstrate oneenv template generation."""
    
    print("OneEnv Template Generation Demo")
    print("=" * 35)
    print()
    
    # Show oneenv help
    print("1. OneEnv template functionality:")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "oneenv", "--help"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print("✅ OneEnv is available")
        else:
            print("❌ OneEnv command failed")
    except Exception as e:
        print(f"❌ OneEnv not available: {e}")
    
    print()
    print("2. Generate environment template:")
    print("   Run: oneenv template")
    print("   This will create .env.example with grouped variables")
    print()
    
    print("3. Template includes:")
    print("   🔑 Tavily API Configuration (critical)")
    print("   ⚙️  Application Settings (optional)")
    print("   🔍 Search Defaults (optional)")
    print()
    
    print("4. Manual template generation:")
    from refinire_tool_tavily import setup_env
    setup_env()
    
    print()
    print("5. Environment variable help:")
    from refinire_tool_tavily import ConfigManager
    config = ConfigManager()
    config.show_env_help()


if __name__ == "__main__":
    main()