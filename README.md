# 🐶 City Dog Show Classifier

This project uses convolutional neural networks (CNNs) to automatically classify whether an uploaded image is a dog or not, and if it is, identify the **dog breed**. It supports popular CNN architectures like **AlexNet**, **VGG**, and **ResNet**.

The project was built as part of an image classification challenge to analyze, test, and compare model performance across pet and uploaded images.

---
## 🚀 Project Structure
project/ │ ├── data/ # Contains all image files and classification scripts │ ├── pet_images/ # Dog images provided for training and testing │ ├── uploaded_images/ # Custom test images uploaded by the user │ ├── adjust_results4_isadog.py │ ├── calculates_results_stats.py │ ├── classify_images.py │ ├── check_images.py │ ├── classifier.py │ └── dognames.txt # List of all valid dog breeds │ ├── project-workspace-* # Multiple folders with step-wise breakdown (adjusting, classifying, final results, etc.) └── .vscode/ # Editor-specific settings


---

## 🔍 How it Works

1. The system accepts image files from two folders:
   - `pet_images/` (known labeled dog images)
   - `uploaded_images/` (new user-provided test images)

2. A pre-trained CNN model classifies each image.

3. The script compares classifier labels with actual labels.

4. Final metrics are calculated, including:
   - Accuracy
   - % correctly identified dogs
   - % correctly classified breeds
   - Overall classifier performance

---

## 🧠 Supported CNN Architectures

- **AlexNet**
- **VGG**
- **ResNet**

These models are accessed via PyTorch’s `torchvision.models`.

---

## 💻 How to Run

1. Clone this repo:
```bash
git clone https://github.com/5agvvebj/city-dog-show-classifier.git
cd city-dog-show-classifier

(Optional) Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

Install required libraries:
pip install -r requirements.txt

Run the classifier:
python check_images.py --dir data/pet_images/ --arch resnet --dogfile data/dognames.txt
You can also test on custom images inside uploaded_images/.

📊 Sample Output
Model used: resnet
Number of Images: 40
Number of Dog Images: 30
Correctly Classified Dogs: 27
Correctly Classified Breed: 24

🙌 Credits
Pre-trained models from PyTorch

Image classification challenge, adapted for City Dog Show









