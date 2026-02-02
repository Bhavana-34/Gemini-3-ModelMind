import os
import json
import pickle
from pathlib import Path

try:
    import tensorflow as tf
    HAS_TF = True
except ImportError:
    HAS_TF = False

try:
    import torch
    HAS_TORCH = True
except ImportError:
    HAS_TORCH = False


class ModelParser:
    """Parse model files"""
    
    @staticmethod
    def parse(filepath):
        """Parse any model file"""
        ext = Path(filepath).suffix.lower()
        
        if ext == ".h5":
            return ModelParser.parse_tensorflow(filepath)
        elif ext in [".pt", ".pth"]:
            return ModelParser.parse_pytorch(filepath)
        elif ext == ".pkl":
            return ModelParser.parse_pickle(filepath)
        else:
            return {"error": f"Unsupported format: {ext}"}
    
    @staticmethod
    def parse_tensorflow(filepath):
        """Parse TensorFlow model"""
        if not HAS_TF:
            return {"error": "TensorFlow not installed. Install with: pip install tensorflow"}
        try:
            model = tf.keras.models.load_model(filepath, compile=False)
            return {
                "type": "tensorflow",
                "layers": len(model.layers),
                "parameters": model.count_params(),
                "input_shape": str(model.input_shape),
                "output_shape": str(model.output_shape)
            }
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def parse_pytorch(filepath):
        """Parse PyTorch model"""
        if not HAS_TORCH:
            return {"error": "PyTorch not installed. Install with: pip install torch"}
        try:
            checkpoint = torch.load(filepath, map_location='cpu')
            return {
                "type": "pytorch",
                "loaded": True,
                "checkpoint_keys": list(checkpoint.keys()) if isinstance(checkpoint, dict) else ["model"]
            }
        except Exception as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": str(e)}
    
    @staticmethod
    def parse_pickle(filepath):
        """Parse pickle model"""
        try:
            with open(filepath, 'rb') as f:
                obj = pickle.load(f)
            return {
                "type": "pickle",
                "object": type(obj).__name__
            }
        except Exception as e:
            return {"error": str(e)}
