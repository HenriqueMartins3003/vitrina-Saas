from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Vitrina AI Worker",
    version="0.1.0",
    description="AI service responsible for content generation tasks.",
)


class HealthResponse(BaseModel):
    status: str
    service: str


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="ai-worker",
    )


class GenerateContentRequest(BaseModel):
    brand_name: str
    target_audience: str
    tone_of_voice: str
    topic: str
    channel: str


class GenerateContentResponse(BaseModel):
    title: str
    content: str
    channel: str


@app.post("/generate-content", response_model=GenerateContentResponse)
def generate_content(payload: GenerateContentRequest) -> GenerateContentResponse:
    return GenerateContentResponse(
        title=f"Conteúdo sobre {payload.topic}",
        content=(
            f"Este é um rascunho inicial para {payload.channel}, "
            f"no tom {payload.tone_of_voice}, direcionado para {payload.target_audience}."
        ),
        channel=payload.channel,
    )