"""Example demonstrating environment setup functionality."""

from refinire_tool_tavily import setup_env, check_config, ConfigManager


def main():
    """Demonstrate setup and configuration management."""
    
    print("Refinire Tool Tavily - Setup Example")
    print("=" * 40)
    
    # Setup environment from template
    print("1. Setting up environment from template...")
    setup_env()
    
    print("\n" + "=" * 40)
    
    # Check current configuration
    print("2. Checking configuration...")
    config_manager = ConfigManager()
    config_manager.print_config_status()
    
    print("\n" + "=" * 40)
    
    # Validate configuration
    print("3. Validating configuration...")
    if check_config():
        print("✅ Configuration is valid and ready to use!")
    else:
        print("❌ Configuration needs attention. Please edit .env file.")
    
    print("\n" + "=" * 40)
    
    print("Next steps:")
    print("1. Edit the .env file and set your actual Tavily API key")
    print("2. Run: python examples/basic_usage.py")


if __name__ == "__main__":
    main()