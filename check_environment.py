#!/usr/bin/env python3
"""
Space Raid - Python Version and Environment Check
This script validates that the game is compatible with the current Python version.
"""

import sys
import pygame

def main():
    print("=" * 60)
    print("🚀 Space Raid - Python Environment Check")
    print("=" * 60)
    
    # Python version check
    print(f"✅ Python Version: {sys.version}")
    print(f"✅ Python Version Info: {sys.version_info}")
    
    # Dependencies check
    print(f"✅ Pygame Version: {pygame.version.ver}")
    print(f"✅ SDL Version: {pygame.version.SDL}")
    
    # Compatibility check
    if sys.version_info >= (3, 8):
        print("✅ Python version is compatible (3.8+)")
    else:
        print("❌ Python version is too old. Please upgrade to Python 3.8+")
        return 1
        
    # Try importing core game modules
    try:
        import objects.player
        import objects.leaderboards.leaderboard_service
        import objects.resources.ResourcesContext
        print("✅ All core game modules import successfully")
    except ImportError as e:
        print(f"❌ Failed to import core modules: {e}")
        return 1
    
    print("=" * 60)
    print("🎮 Space Raid is ready to run!")
    print("To start the game: python __init__.py")
    print("=" * 60)
    return 0

if __name__ == '__main__':
    sys.exit(main())