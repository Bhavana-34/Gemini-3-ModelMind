import json
import numpy as np
from pathlib import Path


class TrainingAnalyzer:
    """Analyze training logs"""
    
    @staticmethod
    def analyze_logs(logs_text):
        """Analyze training logs"""
        try:
            if logs_text.startswith('{'):
                logs = json.loads(logs_text)
            else:
                logs = TrainingAnalyzer.parse_text_logs(logs_text)
            
            return {
                "status": "success",
                "metrics": logs,
                "analysis": TrainingAnalyzer.get_insights(logs)
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    @staticmethod
    def parse_text_logs(text):
        """Parse text-based logs"""
        lines = text.split('\n')
        metrics = {
            "loss": [],
            "accuracy": [],
            "val_loss": [],
            "val_accuracy": []
        }
        
        for line in lines:
            line_lower = line.lower()
            if 'loss' in line_lower:
                try:
                    val = float(line.split(':')[-1].strip())
                    metrics["loss"].append(val)
                except:
                    pass
        
        return metrics
    
    @staticmethod
    def get_insights(metrics):
        """Get insights from metrics"""
        insights = []
        
        if "loss" in metrics and metrics["loss"]:
            loss_list = metrics["loss"] if isinstance(metrics["loss"], list) else [metrics["loss"]]
            if len(loss_list) > 1:
                improvement = (loss_list[0] - loss_list[-1]) / loss_list[0] * 100
                insights.append(f"Loss improved by {improvement:.1f}%")
        
        if "accuracy" in metrics and metrics["accuracy"]:
            acc_list = metrics["accuracy"] if isinstance(metrics["accuracy"], list) else [metrics["accuracy"]]
            if len(acc_list) > 0:
                insights.append(f"Final accuracy: {max(acc_list):.2%}")
        
        return insights
