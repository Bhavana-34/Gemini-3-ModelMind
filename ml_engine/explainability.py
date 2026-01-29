class Explainability:
    """Explain model decisions"""
    
    @staticmethod
    def explain_model(model_info):
        """Explain what the model does"""
        explanation = f"""
**Model Summary:**
- Type: {model_info.get('type', 'Unknown')}
- Layers: {model_info.get('layers', 'Unknown')}
- Parameters: {model_info.get('parameters', 'Unknown')}

**Architecture:** 
This model uses a {model_info.get('type', 'neural network')} architecture.

**Purpose:**
Based on the architecture, this model is likely designed for:
- Pattern recognition in sequential or image data
- Feature extraction and classification
        """
        return explanation.strip()
    
    @staticmethod
    def explain_issue(issue):
        """Explain an issue in simple terms"""
        explanations = {
            "architecture": "The model structure may not be optimal for the task",
            "training": "The model is having trouble learning from the data",
            "data": "There may be issues with the training data quality",
            "gradient": "The learning process is unstable"
        }
        
        issue_type = issue.get("type", "unknown")
        return explanations.get(issue_type, "Unknown issue detected")
