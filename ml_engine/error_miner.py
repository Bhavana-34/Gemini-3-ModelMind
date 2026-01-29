import numpy as np


class ErrorMiner:
    """Detect errors and issues in models"""
    
    @staticmethod
    def find_issues(model_info, training_logs):
        """Find issues in model"""
        issues = []
        
        # Check model architecture
        if model_info.get("layers"):
            if model_info["layers"] > 50:
                issues.append({
                    "type": "architecture",
                    "severity": "high",
                    "message": "Too many layers - may cause vanishing gradients",
                    "fix": "Reduce number of layers or add skip connections"
                })
        
        # Check training
        if training_logs:
            if "loss" in training_logs:
                loss_list = training_logs.get("loss", [])
                if len(loss_list) > 10:
                    # Check if loss is increasing (bad)
                    recent = loss_list[-5:]
                    initial = loss_list[:5]
                    if np.mean(recent) > np.mean(initial) * 1.1:
                        issues.append({
                            "type": "training",
                            "severity": "high",
                            "message": "Loss is increasing - model is diverging",
                            "fix": "Lower learning rate or check data"
                        })
        
        return issues
    
    @staticmethod
    def get_recommendations(issues):
        """Get recommendations based on issues"""
        recommendations = []
        
        for issue in issues:
            recommendations.append({
                "issue": issue["message"],
                "action": issue["fix"],
                "priority": issue["severity"]
            })
        
        return recommendations
