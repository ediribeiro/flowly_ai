## Product Requirements Document (PRD): "flowly" - The Conversational AI English Tutor

**Document Version:** 1.1
**Date:** July 28, 2025
**Status:** Updated Draft
**Author:** Product Management

---

### 1. Executive Summary

This document outlines the updated product requirements for **"flowly"**, a next-generation AI-powered English speaking tutor. Flowly will now integrate **Gemini Live API** to deliver real-time, natural conversational capabilities and voice interaction. This updates enhances reliability, scalability, and development speed while preserving ultra-low latency interaction and seamless user experience.

Flowly continues to use **Microsoft Azure’s Pronunciation Assessment** for detailed linguistic analysis. This hybrid system aims to provide learners with engaging, real-time speaking practice alongside expert-level feedback for improving pronunciation and fluency.

---

### 2. The Problem
English language learners, particularly those without access to native speakers, struggle to find opportunities for authentic, low-stakes speaking practice. Existing digital tools often suffer from:
*   **High Latency:** Awkward delays in conversation disrupt the natural flow and cause frustration.
*   **Generic Feedback:** Feedback is often limited to "correct" or "incorrect," lacking the specific, actionable detail needed to improve pronunciation.
*   **Unnatural Interaction:** Systems fail to handle natural conversational cues like pauses or interruptions, making the experience feel robotic and disengaging.
*   **Lack of Personalization:** Feedback is not tailored to the individual learner's proficiency level or specific, recurring errors.

Flowly will solve this by providing an always-available, patient, and highly responsive conversational partner that delivers expert-level pronunciation feedback in real-time.

---

### 3. Vision & Solution

Flowly aims to deliver the most fluid and pedagogically sound English speaking practice experience using cloud-first tools. The updated architecture includes:

* **Conversational Engine (Gemini Live API):** Google’s Gemini Live API will manage all real-time voice interactions including STT, TTS, turn-taking, and interruption handling with minimal latency and high conversational coherence.
* **Pronunciation Analysis (Azure):** Simultaneously, user speech is streamed to **Microsoft Azure’s Pronunciation Assessment** for granular, phoneme-level feedback on pronunciation, fluency, and prosody.
* **Pedagogical Intelligence (LLM-based core):** An LLM continues to orchestrate conversation flow and interpret Azure feedback into pedagogically sound, user-friendly guidance.

---

### 4. Target Audience & Personas

*   **Persona 1: The Beginner (Ananya)**
    *   **Profile:** A university student in a non-English speaking country, preparing for an English proficiency test (e.g., TOEFL, IELTS).
    *   **Needs:** To build foundational confidence in speaking, get precise correction on basic phoneme errors, and practice simple conversational scenarios.
    *   **Pain Points:** Fear of making mistakes in front of others; doesn't know *exactly* what she's pronouncing incorrectly.

*   **Persona 2: The Intermediate Improver (Marco)**
    *   **Profile:** A professional who uses English at work but wants to improve their fluency and sound more natural.
    *   **Needs:** To improve conversational flow, prosody (intonation and stress), and reduce a noticeable accent. Wants to practice more complex, unscripted conversations.
    *   **Pain Points:** His speech sounds "choppy" or "flat." He can't always keep up in fast-paced meetings.

---

### 5. Goals & Success Metrics

### 5. Goals & Success Metrics

| Goal                                   | Key Metric(s)                                                                                             | Target (V1)                                       |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Achieve "Gemini Live-like" Fluidity**  | End-to-end latency (user stops speaking to AI starts responding).                                           | < 600ms                                           |
|                                        | Successful interruption handling rate (AI successfully pauses and cedes turn).                            | > 95%                                             |
| **Deliver Effective Pedagogical Value**| Improvement in user's Azure Pronunciation Assessment scores (PronScore, Fluency, Accuracy) over 4 weeks.    | > 15% average improvement for active users.       |
|                                        | User engagement with feedback (e.g., re-trying a phrase after correction).                                 | > 70% of feedback prompts a user action.          |
| **Drive High User Engagement**         | Average session duration.                                                                                 | > 10 minutes                                      |
|                                        | User retention (Weekly Active Users / Monthly Active Users).                                              | > 40%                                             |
---

### 6. Feature Requirements

#### **Epic 1: Real-time Conversational Core (Gemini Live-based)**

* **REQ-001: Real-Time STT via Gemini Live API**
  The system must use Gemini Live's speech-to-text capabilities to transcribe speech with latency ≤ 500ms and continuous streaming support.

* **REQ-002: Natural Turn-Taking with Gemini Live**
  Gemini Live's in-built VAD and conversational engine must handle turn-taking naturally, accommodating hesitations and pauses typical of real human conversation.

* **REQ-003: Low-Latency TTS via Gemini Live**
  TTS responses must begin streaming audio output within 300ms of initial LLM response, ensuring smooth and timely voice replies.

* **REQ-004: Seamless Interruption Handling via Gemini Live**
  Gemini Live API must support dynamic interruption detection—pausing or canceling in-progress TTS when a user begins speaking and resuming dialogue based on updated input.

* **REQ-005: Voice Personalization**
  Use Gemini Live's available voice persona configurations to maintain a pleasant and consistent tutor voice. (Custom voice support to be considered in future versions based on Gemini API capabilities.)

---

#### **Epic 2: Pronunciation Assessment & Feedback Engine**
*   **REQ-006: Real-time Pronunciation Assessment:** The system must stream a duplicate of the user's raw audio to Azure Speech Service via the SDK for continuous, real-time assessment.
*   **REQ-007: Granular Data Capture:** The system must capture the full JSON output from Azure PA, including `AccuracyScore`, `FluencyScore`, `ProsodyScore`, `CompletenessScore`, `ErrorType`, and phoneme/word-level `Offset` and `Duration`.
*   **REQ-008: Multi-level Feedback Presentation:** The system must be capable of presenting feedback derived from phoneme, word, and full-sentence level analysis.
*   **REQ-009: Error-to-Feedback Mapping:** The system's LLM will use a predefined pedagogical framework to map specific Azure PA outputs to corrective feedback strategies, as outlined in the table below.

| Azure PA Output (Example)                                     | Pedagogical Interpretation                  | Feedback Strategy (by LLM)                               |
| ------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------- |
| Word: "countryside", AccuracyScore: 30, ErrorType: "Mispronunciation" | Mispronounced word, low accuracy on sounds. | Explicit Correction, Metalinguistic Feedback             |
| FluencyScore: 60 (overall)                                    | Poor flow, unnatural pauses.                | Metalinguistic Feedback, Targeted Practice (e.g., reading) |
| Phoneme: "th", AccuracyScore: 10 in "this"                    | Specific phoneme error.                     | Explicit Correction, Multimodal Feedback (e.g., diagram link) |
| Word: "apple", ErrorType: "Insertion" (e.g., "an apple")      | Extra word inserted.                        | Recast / Explicit Correction                             |

#### **Epic 3: Adaptive Pedagogical Intelligence (LLM-driven)**
*   **REQ-010: Contextual Feedback Generation:** The LLM must generate feedback that is relevant to the ongoing conversation, not just a clinical report of errors.
*   **REQ-011: Adaptive Feedback Strategy:** The system must maintain a dynamic learner state (e.g., mastery level). The LLM will adapt its feedback based on this state, providing more explicit feedback for beginners (Ananya) and more subtle, implicit feedback (recasts, hints) for intermediate learners (Marco).
*   **REQ-012: Dynamic Practice Suggestions:** Based on recurring errors identified by Azure PA, the LLM must be able to dynamically suggest targeted practice exercises (e.g., minimal pairs, repetition drills).
*   **REQ-013: Positive Reinforcement:** The LLM must be prompted to balance corrective feedback with specific praise to maintain a positive and motivating learning environment.

### 7. Non-Functional Requirements (NFRs)

* **NFR-001 (Performance):**
  End-to-end latency (user finishes speaking to system begins responding) must remain under 600ms using Gemini Live streaming pipeline and Azure PA in parallel.

* **NFR-002 (Architecture):**
  System architecture becomes **cloud-centric**, relying on Gemini Live API for conversational interaction and Azure PA for linguistic feedback. WebSockets will still be used for real-time communication among services.

* **NFR-003 (Scalability):**
  Serverless Gemini API and Azure services provide natural scalability; no dedicated GPU provisioning is needed for inference.

* **NFR-004 (Reliability):**
  The system must include failover fallback to resume conversation or delay gracefully if Azure PA becomes unavailable, with fallback to Gemini-only dialogue where necessary.

* **NFR-005 (Compatibility):**
  English `en-US` dialect support only (Azure PA limitation). Gemini Live’s support for multilingual input/output will be monitored for future expansion.

* **NFR-006 (Hardware):**
  No on-premise GPU requirements; client must support WebRTC and WebSocket for voice and text streaming to Gemini Live.

---

### 8. Out of Scope (for V1)

*   Support for languages other than English.
*   Official support and assessment for English dialects other than US-English (e.g., `en-GB`, `en-AU`).
*   A native mobile application (initial release will be a web-based client).
*   Comprehensive curriculum, lesson plans, and long-term progress dashboards.
*   Offline functionality.
*   User-uploaded voice cloning.

---

### 9. Dependencies & Assumptions

* **Dependency:** Access to Gemini Live API with voice capabilities (must support streaming STT, TTS, and full-duplex dialogue).
* **Dependency:** Microsoft Azure AI Speech Services for Pronunciation Assessment (with continuous assessment and JSON output).
* **Dependency:** High-quality, low-latency client-server connectivity to cloud APIs (Gemini and Azure).
* **Assumption:** Gemini Live API will continue to support sub-500ms TTS/STT latency with flexible turn-taking.
* **Assumption:** Gemini Live will allow access to timestamped transcript output, necessary for syncing with Azure’s phoneme feedback.

---

### 10. Open Questions

* What UI/UX design best merges Gemini Live conversation flow with Azure feedback without interrupting the user’s speaking rhythm?
* How do we visually or audibly present Azure PA's granular feedback in a user-friendly way mid-conversation?
* Can Gemini Live provide any real-time text/audio markers (e.g., emotion, hesitation) useful for adaptive pedagogy?
* What is the fallback logic if either Gemini Live or Azure PA is unavailable mid-session?
