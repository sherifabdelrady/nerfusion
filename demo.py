"""
NeRFusion Demo — render orbit video from a trained 3DGS checkpoint.
Usage: python demo.py --model ./output/my_scene --mode orbit [--output orbit.mp4]
"""
import argparse, math, os
import numpy as np
import torch

def render_orbit(model_path: str, n_frames: int = 120, output: str = "orbit.mp4"):
    print(f"Loading checkpoint: {model_path}")
    # In full implementation: load Gaussian parameters from .ply
    # and run CUDA tile rasterizer
    print("Checkpoint structure (example):")
    print("  xyz:       (N, 3)  — Gaussian centres")
    print("  features:  (N, 48) — SH coefficients (degree 3)")
    print("  opacity:   (N, 1)  — per-Gaussian opacity")
    print("  scaling:   (N, 3)  — log-scale")
    print("  rotation:  (N, 4)  — quaternion")
    print(f"\nRendering {n_frames}-frame orbit...")
    for i in range(n_frames):
        angle = 2 * math.pi * i / n_frames
        # Camera pose would be computed here
        if i % 20 == 0:
            print(f"  Frame {i:3d}/{n_frames} | angle {math.degrees(angle):.1f}°")
    print(f"\nOutput would be saved to: {output}")
    print("Run: python train.py --source ./data/my_scene to train first.")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="NeRFusion Demo")
    p.add_argument("--model",  required=True, help="Path to trained checkpoint directory")
    p.add_argument("--mode",   default="orbit", choices=["orbit","freeview"], help="Render mode")
    p.add_argument("--output", default="output.mp4", help="Output video path")
    p.add_argument("--frames", type=int, default=120)
    a = p.parse_args()
    render_orbit(a.model, a.frames, a.output)
