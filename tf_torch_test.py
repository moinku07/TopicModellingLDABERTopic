import os
import tensorflow as tf
import torch

# Suppress minor diagnostic logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print("=" * 45)
print("       FRAMEWORK HARDWARE REPORT       ")
print("=" * 45)

# TensorFlow Test
print(f"TensorFlow Version: {tf.__version__}")
tf_gpus = tf.config.list_physical_devices('GPU')
if tf_gpus:
    print(f"✅ TensorFlow GPU Status: AVAILABLE")
    print(f"   Device Information: {tf_gpus[0]}")
else:
    print("❌ TensorFlow GPU Status: NOT FOUND (Check CUDA 11.2 paths)")

print("-" * 45)

# PyTorch Test
print(f"PyTorch Version: {torch.__version__}")
if torch.cuda.is_available():
    print(f"✅ PyTorch GPU Status: AVAILABLE")
    print(f"   Device Name: {torch.cuda.get_device_name(0)}")
else:
    print("❌ PyTorch GPU Status: NOT FOUND")
print("=" * 45)