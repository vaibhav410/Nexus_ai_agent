# Nexus_ai_agent
Mental Wellness Companion


Today, millions of people experience anxiety, stress, and emotional burnout, but most do not have immediate access to emotional support or guided self-care tools.
The challenge is creating an accessible, always-available system that can help users regulate emotions, journal their thoughts, meditate, and feel supported — without pretending to be a medical professional.

Why Agents?

Mental wellness is dynamic. Different situations require different types of responses.
Agents are the perfect solution because they allow the system to break the problem into multiple expert behaviours:

Assessment Agent → understands the emotional tone

Support Agent → provides grounding, breathing, journaling prompts

Follow-up Agent → tracks mood patterns and provides long-term suggestions

Each agent works independently but collaborates to provide personalized support.
This modular structure makes the system more intelligent, safe, and flexible.

What I Created (Architecture)

MindMate AI is built using a multi-agent architecture:

 1. User Interface (Frontend)

A clean chat-based interface built with HTML, CSS, and JS inspired by Google’s ADK design.

 2. Core Reasoning Agent

Powered by Gemini 2.5 Flash, fine-tuned with a short empathetic persona that ensures:

Short 3–6 line responses

No therapy or medical advice

Safe tone following Google safety guidelines

 3. Mode-specific Agents

Therapy Mode → comforting small emotional support

Meditation Mode → guided breathing + mindfulness

Journal Mode → reflection prompts

Crisis Mode → grounding + safety-first messaging

 4. Rule-Based Layer

Before calling Gemini, the system uses rule-based triggers for:

Anxiety

Stress

Panic

Sleep issues

This reduces API cost and increases reliability.

 5. Tools (MCP-style local tools)

Breathing Tool → step-by-step breathing routine

Grounding Tool → 5-4-3-2-1 grounding

Sleep Routine Tool → sleep hygiene suggestions

 6. Lightweight Memory (JSON)

Stores recent messages, emotional states, and modes to improve future responses.


Used for structuring multi-agent workflows

Helpful for reasoning, tool-use, and agent orchestration

(Even if backend runs on Flask, ADK tools/ideas are used in logic design)

🔹 Gemini 2.5 Flash

Fast, lightweight model

Powers:

empathetic conversation

mode-aware responses (Therapy / Meditation / Journal / Crisis)

grounding, breathing guidance

short supportive replies

Safety-filtering + custom rule-based fallback

🔹 Custom Rule-Based Agent Layer

Anxiety/stress quick responses

Short HINGLISH fallback answers

Ensures no long medical essays

Prevents blocked outputs

Fast, offline-safe response layer before LLM

 Backend (Server Layer)
🔹 Flask

Main backend framework

Routes:

/ → Serve index.html

/analyze → Process AI messages

Lightweight & perfect for Kaggle notebooks + fast prototyping

🔹 Python

Core logic, agent orchestration, utilities

🔹 Flask-CORS

To connect frontend ↔ backend smoothly

Handles cross-origin requests

🔹 python-dotenv

Secure handling of:

GEMINI_KEY

Environment configs

🔹 Google Generative AI SDK

Official Gemini library

Used for:

content generation

controlled output

safe responses

 3. Frontend (UI Layer)
🔹 HTML

Chat layout

Agent dashboard

Mode selector (Therapy, Meditation, Journal, Crisis)

🔹 CSS (Custom + Dark UI)

Fully custom design, inspired by:

Google ADK UI

Modern assistants

Animated background

Smooth transitions

Mobile responsive

🔹 JavaScript

Handles:

sending/receiving messages

typing animation

mood cards

quick replies

local session management

UI mode switching

scroll handling

 4. Tools Layer
🔹 Custom Tools (Python Modules)

Inside /tools/ folder:

breathing.py → guided breathing exercises

grounding.py → grounding techniques

sleep_routine.py → sleep hygiene micro-tips

These are AI-callable functions (mini-tools) similar to ADK tools.

 5. Data Layer
🔹 JSON-based Mood Storage

Path: logs.json
Stores:

mood

reason

date/time

Example: 

logs

🔹 Simple DB Manager

Found in database folder:
Stores + retrieves user mood patterns for personalized suggestions.


