import tensorflow as tf

print("TensorFlow:", tf.__version__)
print("TensorFlow file:", tf.__file__)
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPUs:", tf.config.list_physical_devices("GPU"))
print("All devices:", tf.config.list_physical_devices())