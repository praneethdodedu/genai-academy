# -*- coding: utf-8 -*-
"""
Instructor profile and "field notes" — real-world context drawn from
Praneeth Dodedu's actual career, woven into the curriculum defined in
data.py. This is what turns a generic AI/GenAI course into a personal,
credibility-backed one.

FIELD_NOTES maps a lesson id (see data.py) to a short callout connecting
that lesson's concept to something Praneeth actually built. Not every
lesson has one — they're placed only where the connection is genuine.
"""

INSTRUCTOR = {
    "name": "Praneeth Dodedu",
    "title": "AI Engineering Lead · Principal Engineer",
    "location": "Bantwal, Karnataka, India",
    "tagline": "12+ years turning complex business problems into scalable AI systems.",
    "summary": (
        "I'm an AI Engineering Lead with 12+ years of experience building enterprise-grade "
        "Generative AI applications — using Azure OpenAI, LangChain, LangGraph, and RAG "
        "architectures. My work spans conversational AI platforms, multi-agent systems, and "
        "agentic workflows that serve real users in production, across healthcare education, "
        "e-commerce, robotics, and even quantum computing."
    ),
    "email": "praneeth.dodedu@gmail.com",
    "linkedin": "https://www.linkedin.com/in/praneethdodedu",
    "stats": [
        {"value": "12+", "label": "years in engineering"},
        {"value": "5+", "label": "enterprise AI chatbots shipped"},
        {"value": "6", "label": "domains: healthcare, e-commerce, robotics & more"},
    ],
    "what_i_do": [
        "Design & build conversational AI platforms with real-time WebSocket streaming",
        "Architect multi-agent systems with tool calling, MCP, and agentic workflows",
        "Implement RAG solutions using Azure AI Search, vector embeddings, and hybrid search",
        "Develop microservices with Python, FastAPI, Kafka, and Kubernetes",
        "Lead teams in delivering production-ready AI applications",
    ],
    "achievements": [
        {
            "title": "Claire AI — Conversational Assessment Platform",
            "detail": (
                "Architected a plugin-based conversational platform (Item Generator, Educator "
                "Assistant, Student Mentor) letting nursing faculty generate assessments through "
                "natural conversation — multi-turn dialogue with intent classification on Azure "
                "OpenAI GPT-4.1 and RAG, integrated with legacy systems via Kafka."
            ),
        },
        {
            "title": "5+ Enterprise AI Chatbots",
            "detail": (
                "Delivered production chatbots (Virtual Mentor, AloraAI, a legal assistant) using "
                "Azure OpenAI, Azure AI Search, and Microsoft Teams integration — with automated "
                "ticketing, document Q&A with citations, and compliance guardrails."
            ),
        },
        {
            "title": "Autonomous Surveillance Robot",
            "detail": (
                "Led a 26-month robotics project: autonomous patrolling and object counting with "
                "ROS nodes, YOLO-based object detection, and real-time WebRTC video streaming."
            ),
        },
        {
            "title": "Quantum Computing Optimization",
            "detail": (
                "Pioneered D-Wave quantum computing optimization for an advertising platform — "
                "applying quantum annealing to a real allocation problem."
            ),
        },
    ],
    "skills": {
        "GenAI": ["Azure OpenAI", "LangChain", "LangGraph", "LangSmith", "Semantic Kernel", "Prompt Engineering"],
        "AI / ML": ["RAG", "Agentic Workflows", "Tool Calling", "MCP", "YOLO", "RetinaNet", "OpenCV"],
        "Cloud": ["Azure OpenAI", "Azure AI Search", "Azure Functions", "AKS", "Cosmos DB", "Document Intelligence"],
        "Backend": ["Python", "FastAPI", "Flask", "Java", "Spring Boot", "C++"],
        "Frontend": ["React", "Angular"],
        "DevOps": ["Kubernetes", "Docker", "Kafka", "GitLab CI/CD", "Datadog"],
    },
    "domains": [
        "Healthcare Education",
        "E-Commerce",
        "Robotics",
        "Video Analytics",
        "Quantum Computing",
        "Travel",
    ],
    "experience": [
        {
            "company": "Ascendion",
            "role": "Principal Engineer",
            "period": "June 2026 — Present",
            "location": "Bengaluru, India",
        },
        {
            "company": "Happiest Minds Technologies",
            "role": "AI Engineering Lead",
            "period": "Jan 2025 — May 2026",
            "location": "Bangalore Urban",
            "detail": (
                "Led AI engineering initiatives, architecting enterprise-scale GenAI solutions on "
                "Azure OpenAI, LangChain, and microservices — including Claire AI and 5+ enterprise chatbots."
            ),
        },
        {
            "company": "Happiest Minds Technologies",
            "role": "Module Lead",
            "period": "May 2017 — Nov 2025",
            "location": "Bengaluru Area, India",
            "detail": "8+ years spanning the autonomous surveillance robot and drone-based 3D object tracking projects.",
        },
        {
            "company": "Mindtree",
            "role": "Senior Software Engineer",
            "period": "Feb 2015 — May 2017",
            "location": "Bengaluru Area, India",
            "detail": "Enterprise Java/Spring microservices for Global Business Travel (American Express).",
        },
        {
            "company": "Ontash Systems",
            "role": "Software Developer",
            "period": "Nov 2012 — Feb 2015",
            "location": "Calicut Area, India",
            "detail": "E-commerce integration platform for 1800 Flowers (USA).",
        },
    ],
    "education": {"school": "Visvesvaraya Technological University", "degree": "Bachelor of Engineering (B.E.)", "years": "2007 — 2011"},
}


def _note(project: str, text: str) -> dict:
    return {"project": project, "text": text}


FIELD_NOTES = {
    # --- AI Foundations ---
    "ai-p-1": _note(
        "Claire AI",
        "In production, this is exactly what powers multi-turn intent classification in Claire AI: "
        "Azure OpenAI's GPT-4.1, a decoder-only Transformer, reasoning over the running conversation "
        "on every turn to decide what the user actually wants before any retrieval or generation happens.",
    ),
    # --- Generative AI ---
    "genai-b-2": _note(
        "Claire AI",
        "Claire AI — a conversational assessment platform for nursing faculty — runs on exactly this "
        "loop: Azure OpenAI GPT-4.1 processes each conversational turn token by token to classify intent "
        "and drive the next step in the dialogue.",
    ),
    "genai-i-2": _note(
        "Enterprise chatbots",
        "This is a decision made for real on every enterprise chatbot project: prompting alone couldn't "
        "keep answers current with fast-changing internal documentation, and fine-tuning was overkill for "
        "data that changes weekly — so RAG over Azure AI Search became the default architecture.",
    ),
    "genai-p-2": _note(
        "Production stack",
        "This is close to the actual stack behind Claire AI and the enterprise chatbot fleet: a Python "
        "FastAPI backend orchestrating Azure OpenAI calls, Kafka for integrating with legacy systems, and "
        "AKS (Kubernetes) for running it all in production at scale.",
    ),
    # --- RAG ---
    "rag-b-1": _note(
        "Enterprise chatbots",
        "The Virtual Mentor and legal-assistant chatbots both lean on this exact pattern — Azure AI Search "
        "retrieves relevant internal documents, and Azure OpenAI generates an answer grounded in them, with "
        "citations back to the source documents so users (and compliance reviewers) can verify the answer.",
    ),
    "rag-i-2": _note(
        "Azure AI Search",
        "Azure AI Search's hybrid search — combining vector similarity with traditional keyword search — is "
        "what makes enterprise document Q&A reliable in practice: policy documents are full of exact terms, "
        "codes, and product names that pure semantic search alone tends to miss.",
    ),
    "rag-p-1": _note(
        "LangGraph & MCP",
        "This is the shape of the multi-agent, tool-calling systems built with LangGraph and MCP (Model "
        "Context Protocol) in current production work — agentic workflows where the model decides which "
        "tool or retrieval step to invoke next, rather than following one fixed pipeline.",
    ),
    "rag-p-2": _note(
        "Compliance guardrails",
        "For the legal chatbot, this evaluation discipline wasn't optional — every answer had to be checked "
        "for faithfulness to the retrieved policy text before shipping, since an ungrounded but confident "
        "answer in a compliance context is a real liability, not just a quality issue.",
    ),
    # --- Prompt Engineering ---
    "pe-i-2": _note(
        "Claire AI plugins",
        "Claire AI's plugin architecture — Item Generator, Educator Assistant, Student Mentor — is role "
        "prompting at the product level: each plugin carries its own system message defining its persona, "
        "scope, and tone, sharing the same underlying model.",
    ),
    "pe-p-3": _note(
        "Claire AI architecture",
        "Claire AI's Conversational Core is a real example of this: intent classification, retrieval, and "
        "item generation run as distinct, focused stages rather than one giant prompt trying to do "
        "everything at once — each stage independently testable and improvable.",
    ),
    "pe-p-4": _note(
        "Compliance guardrails",
        "The legal and enterprise chatbots ship with explicit guardrails against exactly this: untrusted "
        "content retrieved from documents or user input is treated as data, never as instructions, and "
        "high-stakes actions (like ticket creation) go through validation before they execute.",
    ),
}
