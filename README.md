# U-2-Net Background Remover (Enhanced with Docker Compose and Gradio)

This repository is a fork of the original [U-2-Net](https://github.com/xuebinqin/U-2-Net) project, enhanced to provide a seamless web interface for background removal using **Gradio** and simplified deployment via **Docker Compose**.

---

## Features

1. **Background Removal**: High-quality background removal, even for complex details like hair.
2. **Web Interface**: A user-friendly Gradio-based interface for uploading and processing images directly from a browser.
3. **Docker Compose Support**: Easily run the project with a single command.
4. **JPG Output Option**: Processed images are saved in JPG format for improved compatibility.
5. **Transparent Deployment**: Consistent runtime environment using Docker Compose.

---

## Getting Started

### Prerequisites

- Docker
- Docker Compose

---

### Running the Application

To start the application, follow these steps:

1. Clone the repository:

   ```bash
   git clone <your-forked-repo-url>
   cd <repository-folder>
   ```

2. Start the application with Docker Compose:

   ```bash
   docker-compose up -d
   ```
   (if not works download models manually by google [u2net model](https://drive.google.com/uc?id=1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy) and save under save_models/u2net/u2net.pth)

3. Open your browser and navigate to:

   ```
   http://localhost:7860
   ```

4. Upload your image, and the processed image with the background removed will be available for download in JPG format.

---

### Stopping the Application

To stop the application, run:

```bash
docker-compose down
```

---

## Development

If you want to extend or debug the application without Docker, you can run it locally:

1. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the Gradio application:

   ```bash
   python app.py
   ```

---

## Changes from the Original Project

1. Integrated **Gradio** for an easy-to-use web interface.
2. Added support for **Docker Compose** for simplified deployment.
3. Enhanced output to save processed images in JPG format.

---

## License

This project is based on the original [U-2-Net](https://github.com/xuebinqin/U-2-Net) repository and follows its **MIT License**. 

The original license details are as follows:

```
MIT License

Copyright (c) 2020 xuebinqin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

This repository retains the same license and acknowledges the contributions of the original authors.

---

## Acknowledgements

This project is a fork of the original [U-2-Net](https://github.com/xuebinqin/U-2-Net). Special thanks to the original authors for their exceptional work in building the foundation for this tool.
