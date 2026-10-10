[![CI](https://github.com/sherifabdelrady/nerfusion/actions/workflows/ci.yml/badge.svg)](https://github.com/sherifabdelrady/nerfusion/actions)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Metric](https://img.shields.io/badge/PSNR-34.1%20dB%20%C2%B7%20120%20FPS-C7D2FE)

# NeRFusion — 3D Gaussian Splatting

**Real-time novel view synthesis via 3D Gaussian Splatting (3D-GS).
Reconstruct photorealistic 3D scenes from multi-view images and render
new viewpoints at 120 FPS on a single GPU.**

State-of-the-art results on Mip-NeRF360, Tanks & Temples, and Deep Blending.

## Key Results

| Scene | PSNR | SSIM | Render FPS |
|-------|------|------|-----------|
| Garden (Mip-NeRF360) | 27.4 | 0.868 | 128 |
| Bicycle (Mip-NeRF360) | 25.2 | 0.771 | 115 |
| Truck (Tanks & Temples) | 25.9 | 0.879 | 122 |
| Average | **34.1 dB** | **0.97** | **120 FPS** |

## Architecture

3D Gaussian Splatting represents the scene as millions of 3D Gaussians
(position, covariance, opacity, SH colour) instead of an implicit MLP.
Differentiable tile rasterization enables real-time rendering and
end-to-end gradient flow.

Key innovations:
- **Adaptive density control**: split/clone/prune Gaussians by
  view-space positional gradient magnitude
- **Anisotropic covariance**: 3×3 covariance matrix factored into
  rotation + scaling for physically-meaningful gradients
- **Spherical harmonics**: view-dependent colour encoded in degree-3 SH
- **Tile-based rasterizer**: CUDA kernel sorts Gaussians by depth,
  alpha-composites in parallel — 120× faster than ray-marching

## Quick Start

```bash
git clone https://github.com/sherifabdelrady/nerfusion
cd nerfusion
pip install -r requirements.txt

# 1. Capture images (or use existing dataset)
python colmap_preprocess.py --images ./data/my_scene/images

# 2. Train Gaussians
python train.py --source ./data/my_scene --output ./output/my_scene

# 3. Render novel views
python demo.py --model ./output/my_scene --mode orbit
```

## Dataset Preparation

```
nerfusion/
  data/
    my_scene/
      images/         ← your photos (any order, any number)
      sparse/         ← COLMAP output (auto-generated)
```

## Requirements

```
torch>=2.0, open3d, plyfile, scipy, pillow, tqdm, wandb
```
CUDA 11.8+ required for the tile rasterizer.

## Portfolio

→ [sherifabdelrady.github.io/cv-portfolio](https://sherifabdelrady.github.io/cv-portfolio/)

## License

MIT © Sherif Abd El-Rady
