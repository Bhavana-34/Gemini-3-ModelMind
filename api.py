from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
from pathlib import Path

from ml_engine.model_parser import ModelParser
from ml_engine.training_analyzer import TrainingAnalyzer
from ml_engine.error_miner import ErrorMiner
from gemini_engine.reasoner import Reasoner
from gemini_engine.planner import Planner
from report.generate_report import ReportGenerator

app = FastAPI(title="ModelMind API")

# Create storage directories
Path("storage/uploads").mkdir(parents=True, exist_ok=True)
Path("storage/outputs").mkdir(parents=True, exist_ok=True)
Path("storage/reports").mkdir(parents=True, exist_ok=True)


@app.post("/analyze")
async def analyze_model(model_file: UploadFile = File(...), logs_file: UploadFile = None):
    """Upload and analyze model"""
    try:
        # Save model file
        model_path = f"storage/uploads/{model_file.filename}"
        with open(model_path, "wb") as f:
            f.write(await model_file.read())
        
        # Parse model
        model_info = ModelParser.parse(model_path)
        
        # Analyze logs if provided
        logs_info = {}
        if logs_file:
            logs_content = (await logs_file.read()).decode()
            logs_info = TrainingAnalyzer.analyze_logs(logs_content)
        
        # Find issues
        issues = ErrorMiner.find_issues(model_info, logs_info.get("metrics", {}))
        
        # Get Gemini analysis
        analysis_result = Reasoner.analyze(model_info, issues)
        
        # Get improvements
        improvements = Reasoner.get_improvements(model_info)
        
        # Generate report
        report_text = ReportGenerator.generate(
            model_info,
            analysis_result.get("analysis", "No analysis"),
            improvements.get("improvements", "No improvements"),
            issues
        )
        
        report_path = ReportGenerator.save_report(report_text)
        
        return JSONResponse({
            "status": "success",
            "model_info": model_info,
            "issues": issues,
            "analysis": analysis_result.get("analysis", ""),
            "improvements": improvements.get("improvements", ""),
            "report_path": report_path
        })
    
    except Exception as e:
        return JSONResponse({
            "status": "error",
            "error": str(e)
        }, status_code=400)


@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
