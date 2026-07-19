#!/usr/bin/env python3
"""
ALADDIN Starlink Bypass - Launcher
.so file ကို load ပြီး run ပေးသော script

Usage: python3 run.py
"""
import importlib.util
import sys
import os
import glob

def find_so_file():
    """aladdin_main .so file ကို ရှာခြင်း"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Try exact name first
    exact = os.path.join(base_dir, "aladdin_main.so")
    if os.path.exists(exact):
        return exact
    
    # Try cpython naming pattern
    pattern = os.path.join(base_dir, "aladdin_main.cpython-*.so")
    matches = glob.glob(pattern)
    if matches:
        return matches[0]
    
    # Try any aladdin_main*.so
    pattern = os.path.join(base_dir, "aladdin_main*.so")
    matches = glob.glob(pattern)
    if matches:
        return matches[0]
    
    return None

def main():
    so_file = find_so_file()
    
    if not so_file:
        print("\033[1;31m[ERROR] aladdin_main.so file not found!\033[0m")
        print("\033[1;33m[INFO] Make sure aladdin_main.so is in the same folder as run.py\033[0m")
        sys.exit(1)
    
    try:
        spec = importlib.util.spec_from_file_location("aladdin_main", so_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if hasattr(module, 'main'):
            module.main()
        else:
            print("\033[1;31m[ERROR] main() function not found in module\033[0m")
            sys.exit(1)
    except Exception as e:
        print(f"\033[1;31m[ERROR] Failed to load module: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
