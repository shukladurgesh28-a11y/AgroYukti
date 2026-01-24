#!/usr/bin/env python3
"""
Startup script for AgriYuti backend on Render
"""
import uvicorn
import os
import sys

if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 10000))
        
        print(f"[INFO] Starting AgriYuti API on 0.0.0.0:{port}")
        print("[INFO] Working directory:", os.getcwd())
        print("[INFO] Python version:", sys.version)
        
        uvicorn.run(
            "main:app",  # Changed from scripts.main:app to main:app
            host="0.0.0.0",
            port=port,
            reload=False,
            log_level="info"
        )
        
    except Exception as e:
        print(f"[ERROR] Failed to start server: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
