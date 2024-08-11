# Background Remover Web App

This is a simple web application built with Python and Flask that removes the background from an image using the `rembg` library. The user can upload an image, view the processed image with the background removed, and optionally download the result.

## Features

- Upload an image in any common format (JPEG, PNG, etc.).
- View the image with the background removed directly on the web page.
- Download the processed image as a PNG file.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/redianmarku/image-background-remover-website
   cd image-background-remover-website
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

5. **Access the app**:
   - Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Upload an Image**:
   - On the homepage, click the "Choose File" button to select an image from your device.
2. **Remove Background**:
   - Click the "Remove Background" button to process the image.
3. **View and Download**:
   - The processed image will be displayed on the page. You can download it by clicking the "Download Image" button.

## Project Structure

```plaintext
background-remover-web-app/
│
├── app.py                # The main Flask application
├── templates/
│   └── index.html        # HTML template for the web interface
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Dependencies

- Flask: A lightweight WSGI web application framework in Python.
- rembg: A tool to remove the background from images.
- Pillow: Python Imaging Library, which adds image processing capabilities to your Python interpreter.

To install the dependencies, use:

```bash
pip install Flask rembg Pillow
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

If you want to contribute to this project, feel free to submit a pull request or open an issue with your ideas or suggestions.

## Contact

For any inquiries or feedback, feel free to contact me at [redian@topnotch-programmer.com].
