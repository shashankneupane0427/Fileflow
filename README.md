# FileFlow

FileFlow is a simple Python CLI tool that automatically organizes files into folders based on their file extensions.

## What It Does

FileFlow takes a folder such as `Downloads` and organizes the files inside it into categories:

```text
Downloads/
├── Images/
│   ├── photo.jpg
│   └── screenshot.png
│
├── Documents/
│   ├── resume.pdf
│   └── notes.docx
│
├── Videos/
│   └── movie.mp4
│
└── Others/
    └── random.xyz
```

## Usage

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd fileflow
```

Run FileFlow with:

```bash
python main.py organize ~/Downloads
```

Replace `~/Downloads` with the folder you want to organize.

## Supported File Types

### Images

```text
.jpg
.jpeg
.png
.gif
```

### Documents

```text
.pdf
.docx
.doc
.txt
```

### Videos

```text
.mp4
.mkv
.avi
.mov
```

### Others

Files with extensions that are not listed above are moved into the `Others` folder.

## Project Structure

```text
fileflow/
│
├── main.py            # Command-line entry point
├── file_manager.py    # Handles file organization
├── utils.py           # Helper functions
└── config.py          # File category configuration
```

## Technologies

* Python
* pathlib
* shutil
* sys

No external Python packages are required.

## Note

FileFlow moves files from the selected folder into category folders. Make sure you are running it on the folder you actually want to organize.

## License

This project is for learning and personal use.
