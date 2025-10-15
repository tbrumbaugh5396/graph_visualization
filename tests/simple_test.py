#!/usr/bin/env python3
print("🎯 SIMPLE TEST: This should show debug is working!")
print("🎯 If you see this, Python3 is working and debug prints work.")

# Test if wx is available
try:
    import wx
    print("✅ wxPython is available")
except ImportError as e:
    print(f"❌ wxPython not available: {e}")

# Test if our main file can be imported
try:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import main
    print("✅ main.py can be imported")
except Exception as e:
    print(f"❌ Cannot import main.py: {e}")
    import traceback
    traceback.print_exc()



