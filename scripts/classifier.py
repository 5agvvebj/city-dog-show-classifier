import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

# Load models with pretrained weights
resnet18 = models.resnet18(weights=True)
alexnet = models.alexnet(weights=True)
vgg16 = models.vgg16(weights=True)

# Dictionary to map model names to instances
models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# Obtain ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())

def classifier(img_path, model_name):
    # Load the image
    img_pil = Image.open(img_path)
    
    # Convert RGBA to RGB if needed
    if img_pil.mode == 'RGBA':
        img_pil = img_pil.convert('RGB')

    # Define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    # Preprocess the image
    img_tensor = preprocess(img_pil)
    
    # Resize the tensor (add dimension for batch)
    img_tensor.unsqueeze_(0)
    
    # Check PyTorch version to set requires_grad based on version
    pytorch_ver = __version__.split('.')
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)
    else:
        # For PyTorch versions below 0.4, use Variable (deprecated in 0.4 and above)
        data = Variable(img_tensor, volatile=True)

    # Get the specified model and set it to evaluation mode
    model = models[model_name].eval()
    
    # Apply the model to the input tensor
    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        output = model(img_tensor)
    else:
        output = model(data)

    # Return the predicted class label
    pred_idx = output.data.numpy().argmax()
    return imagenet_classes_dict[pred_idx]
