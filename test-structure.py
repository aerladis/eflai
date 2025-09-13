#!/usr/bin/env python3
"""
Test script to verify the restructured project works.
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all modules can be imported."""
    try:
        print("Testing imports...")
        
        # Test core modules
        from efl_cafe.core.config import APP_NAME, APP_VERSION
        print(f"✅ Core config: {APP_NAME} v{APP_VERSION}")
        
        from efl_cafe.core.prompts import load_prompts, fmt
        print("✅ Core prompts imported")
        
        # Test utils
        from efl_cafe.utils.debug import debug_print, DEBUG_MODE
        print(f"✅ Utils debug: DEBUG_MODE={DEBUG_MODE}")
        
        from efl_cafe.utils.dpi import setup_dpi_environment
        print("✅ Utils DPI imported")
        
        from efl_cafe.utils.paths import _resource_path, _get_prompts_path
        print("✅ Utils paths imported")
        
        # Test GUI
        from efl_cafe.gui.main_window import MainWindow
        print("✅ GUI main window imported")
        
        print("\n🎉 All imports successful! Project structure is working.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality."""
    try:
        from efl_cafe.core.prompts import fmt, get_tier_instructions
        
        # Test prompt formatting
        template = "Hello {name}, you are {level} level."
        result = fmt(template, name="John", level="B2")
        print(f"✅ Prompt formatting: {result}")
        
        # Test tier instructions
        instructions = get_tier_instructions("B2", "Upper")
        print(f"✅ Tier instructions generated: {len(instructions)} characters")
        
        return True
        
    except Exception as e:
        print(f"❌ Functionality test error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("EFL Cafe - Project Structure Test")
    print("=" * 50)
    
    success = True
    success &= test_imports()
    success &= test_basic_functionality()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests passed! Project is ready for GitHub.")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("=" * 50)
