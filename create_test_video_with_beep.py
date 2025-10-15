#!/usr/bin/env python3

"""
Create a simple test video with audio for testing video/audio sync issues.
This creates a 5-second video with:
- Visual frame counter
- Audio beep every second
- 30 FPS for smooth playback
"""

import subprocess
import os
import sys

def create_test_video():
    """Create a test video with visual frame counter and audio beeps."""
    
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("FFmpeg found - creating test video...")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERROR: FFmpeg not found. Please install FFmpeg to create test videos.")
        return False
    
    output_file = "sync_test_video.mp4"
    
    # Remove existing file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Removed existing {output_file}")
    
    # Create video with frame counter and continuous audio tone
    cmd = [
        'ffmpeg',
        '-f', 'lavfi',
        '-i', 'testsrc2=duration=5:size=640x480:rate=30',  # Test pattern with frame counter
        '-f', 'lavfi', 
        '-i', 'sine=frequency=440:duration=5',  # 440Hz sine wave (A note)
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-shortest',  # Use shortest input
        '-y',  # Overwrite output
        output_file
    ]
    
    try:
        print("Creating test video with frame counter and continuous tone...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Successfully created {output_file}")
        print(f"📹 Video: 5 seconds, 30fps, 640x480")
        print(f"🔊 Audio: Continuous 440Hz tone")
        print(f"📁 File size: {os.path.getsize(output_file)} bytes")
        
        # Test if the file can be read
        test_cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_streams', output_file]
        probe_result = subprocess.run(test_cmd, capture_output=True, text=True)
        if probe_result.returncode == 0:
            print("✅ Video file is valid and readable")
        else:
            print("⚠️  Warning: Video file may have issues")
            
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error creating video: {e}")
        print(f"FFmpeg output: {e.stderr}")
        return False

if __name__ == "__main__":
    print("🎬 Creating test video for sync testing...")
    print("=" * 50)
    
    success = create_test_video()
    
    if success:
        print("\n🎯 Test video ready!")
        print("This video can be used to test:")
        print("- First loop: Should be smooth with audio")
        print("- Subsequent loops: Should remain smooth with audio")
        print("- Speed changes: Audio should stay synced")
        print("- Frame rate changes: Should affect smoothness not sync")
        print("\n📝 Load this video in the 3D app to test sync issues.")
    else:
        print("\n❌ Failed to create test video")
        sys.exit(1)
