# ComfyUI Workflows Collection

A collection of ready-to-use [ComfyUI](https://github.com/comfyanonymous/ComfyUI) projects covering image, video, music, and face/clothing editing. Each folder holds a self-contained workflow (the `.json` file, plus notes or sample inputs) that you can load into ComfyUI and run.

---

## Projects Included

| Folder | What it does |
|---|---|
| `Comfy_facial_expression` | Change or edit facial expressions on a portrait |
| `Comfyui_Ace_step_music_generation` | Generate music from text prompts with ACE-Step |
| `Comfyui_Changing_cloth` | Swap or change clothing on a person in an image |
| `Comfyui_Face_swap` | Swap a face from one image onto another |
| `Comfyui_image_to_video_generation` | Turn a still image into a short video |
| `Comfyui_Image_to_video_Wan` | Image-to-video generation using the Wan model |
| `Comfyui_qwen_image_generation` | Text-to-image generation with Qwen-Image |
| `ComfyUI_Upscaler` | Upscale and enhance images |
| `Comfyui_Video_generation` | Text-to-video generation |
| `Comfyui_video_upscaling` | Upscale and enhance existing videos |
| `ComfyUI_virtual_tryon` | Virtual clothing try-on |
| `Creating_long_video_with_holo...` | Build long videos by chaining generated clips |

> **Note:** Some folder names in your file manager are truncated. Rename the folders to their full names before uploading, and update the table above to match. Avoid spaces and brackets in folder names (use `_` instead); this prevents problems on GitHub and in the terminal.

---

## 1. Prerequisites

- [Git](https://git-scm.com/downloads) installed
- A [GitHub](https://github.com) account
- [Git LFS](https://git-lfs.com) installed (needed for large model/media files)
- ComfyUI installed locally (to run the workflows)

Check your setup:

```bash
git --version
git lfs version
```

---

## 2. Prepare the Folders Before Uploading

### Clean up folder names

Rename each folder to a simple name with no spaces or special characters, for example:

```
Comfyui (Changing cloth wit...)  ->  Comfyui_Changing_cloth
CpmfyUi(virtual tryon)           ->  ComfyUI_virtual_tryon
```

### What to upload, and what NOT to upload

**Upload:**
- Workflow `.json` files
- Small example inputs and outputs (screenshots, short clips)
- A short `README.md` or notes file per project

**Do NOT upload to regular Git:**
- Model weights (`.safetensors`, `.ckpt`, `.pth`, `.gguf`, `.bin`), which are often several GB
- Large generated videos and audio

GitHub rejects any file over **100 MB**, and repositories become unwieldy past a few GB. Keep models out of the repo and document where to download them instead (see section 5).

### Create a `.gitignore`

In the root of your repository, create `.gitignore`:

```gitignore
# Model weights (download separately)
*.safetensors
*.ckpt
*.pth
*.pt
*.gguf
*.bin

# ComfyUI generated output
output/
temp/
__pycache__/

# System files
.DS_Store
Thumbs.db
```

If you do want to keep a few small models or large sample videos in the repo, use Git LFS instead (section 4).

---

## 3. Upload to GitHub

### Step 1: Create the repository

1. Go to [github.com/new](https://github.com/new).
2. Name it (for example `comfyui-workflows`), add a description, and choose Public or Private.
3. Leave "Add a README" unchecked, since you already have one.
4. Click **Create repository**.

### Step 2: Initialize and push from your computer

Open a terminal in the folder that contains all the project folders:

```bash
git init
git add .
git commit -m "Add ComfyUI workflow collection"
git branch -M main
git remote add origin https://github.com/<your-username>/comfyui-workflows.git
git push -u origin main
```

Replace `<your-username>` with your GitHub username. If prompted for a password, use a [Personal Access Token](https://github.com/settings/tokens) rather than your account password.

### Step 3: Verify

Refresh the repository page on GitHub. All folders and workflow files should be listed.

---

## 4. Handling Large Files with Git LFS

If you need to store large files (sample videos, small models), track them with Git LFS **before** committing them:

```bash
git lfs install
git lfs track "*.mp4"
git lfs track "*.wav"
git lfs track "*.mp3"
git add .gitattributes
git add .
git commit -m "Track large media with Git LFS"
git push
```

Note that GitHub's free LFS quota is limited (1 GB storage and 1 GB bandwidth per month). For multi-GB model files, host them on [Hugging Face](https://huggingface.co) or [Civitai](https://civitai.com) and link to them instead.

---

## 5. Working With the Workflows

### Step 1: Clone the repository

```bash
git clone https://github.com/<your-username>/comfyui-workflows.git
cd comfyui-workflows
```

### Step 2: Load a workflow in ComfyUI

1. Start ComfyUI.
2. Open the browser interface (usually `http://127.0.0.1:8188`).
3. Drag and drop the project's `.json` file onto the canvas, or use **Workflow > Open**.

### Step 3: Install missing custom nodes

If nodes appear in red, they are missing:

1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you don't have it.
2. Click **Manager > Install Missing Custom Nodes**.
3. Restart ComfyUI.

### Step 4: Download the required models

Place each model in the matching ComfyUI folder:

| Model type | Folder inside `ComfyUI/models/` |
|---|---|
| Checkpoints | `checkpoints/` |
| Diffusion models (Wan, Qwen-Image, etc.) | `diffusion_models/` |
| VAE | `vae/` |
| Text encoders / CLIP | `text_encoders/` or `clip/` |
| LoRA | `loras/` |
| Upscalers | `upscale_models/` |
| Face swap models (e.g. inswapper) | `insightface/` |
| ControlNet | `controlnet/` |

Each project's notes should list the exact model names and download links. If a loader node shows a model name that you don't have, select your downloaded file from its dropdown.

### Step 5: Run it

Load your input image, video, or prompt, then press **Queue Prompt** (or `Ctrl+Enter`). Results are saved to `ComfyUI/output/`.

---

## 6. Updating and Collaborating

Save your changes after tweaking a workflow:

```bash
git add .
git commit -m "Update face swap workflow settings"
git push
```

Pull the latest version on another machine:

```bash
git pull
```

Tips:
- Use **Workflow > Save** in ComfyUI to export the updated `.json` back into the project folder.
- Commit with clear messages such as `Add Wan image-to-video workflow` rather than `update`.
- Use branches to experiment without breaking a working version:
  ```bash
  git checkout -b experiment-new-sampler
  ```

---

## 7. Suggested Repository Structure

```
comfyui-workflows/
├── README.md
├── .gitignore
├── Comfy_facial_expression/
│   ├── workflow.json
│   └── README.md
├── Comfyui_Face_swap/
│   ├── workflow.json
│   └── README.md
├── ComfyUI_Upscaler/
│   ├── workflow.json
│   └── README.md
└── ...
```

Each project README should list: what the workflow does, required custom nodes, required models with download links, recommended settings, and an example result.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `file exceeds GitHub's 100 MB limit` | Remove the file from the commit (`git rm --cached <file>`), add it to `.gitignore` or track it with Git LFS |
| Red nodes after loading a workflow | Install missing custom nodes via ComfyUI-Manager |
| `Value not in list` on a loader node | Select your locally installed model file from the dropdown |
| Out-of-memory errors on video workflows | Lower the resolution or frame count, or use a smaller/quantized (GGUF/fp8) model |
| `git push` authentication fails | Use a Personal Access Token instead of a password |

---

## License

Add a license of your choice (for example MIT) in a `LICENSE` file. Check the licenses of any models you reference, as many have non-commercial or usage restrictions.
