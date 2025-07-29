### **Development Roadmap: From MVP to Full-Featured Tutor**

This roadmap is structured to deliver the most critical user value first, creating a solid foundation to build upon.


// Half cascade model:
// const model = "gemini-2.5-flash-live-preview"
const model = "gemini-2.0-flash-live-001"

// Native audio output model:
// const model = "gemini-2.5-flash-preview-native-audio-dialog"

// Native audio output model:
//const model = "gemini-2.5-flash-exp-native-audio-dialog"

---

### **Phase 1: The Core Interaction MVP (Minimum Viable Product)**

**Goal:** Create a working application where a user can speak, see their words transcribed, and receive real-time, color-coded feedback on their pronunciation. This is the fundamental feedback loop.

| Priority | User Story (What the user wants) | Why (The value it provides) |
| :--- | :--- | :--- |
| **1** | **As a user, I want to speak naturally and have the AI respond with very low latency** | This establishes the core conversational engine (Gemini Live). Without this, there is no product. |
| **2** | **As a user, I want to see a real-time transcription of my speech in a sidebar** | This provides immediate confirmation that the system is hearing the user correctly and is the foundation for all visual feedback. |
| **3** | **As a user, I want the words in my transcript to be color-coded based on pronunciation accuracy as I speak** | This is the MVP's "killer feature." It delivers immediate, at-a-glance value and makes the tool instantly useful for identifying problem areas. |
| **4** | **As a user, I want to see the AI tutor's avatar on the screen** | Provides a necessary focal point for the interaction, even if it's not animated yet. It makes the app feel less like a faceless utility. |

**Outcome of Phase 1:** A functional "tech demo" that proves the core concept. A user can have a free-form conversation and see live color-coding on their spoken words.

---

### **Phase 2: Structuring the Learning Experience**

**Goal:** Transform the MVP from a free-form demo into a structured learning tool. The user can now choose *what* they want to practice, making the sessions more focused and goal-oriented.

| Priority | User Story (What the user wants) | Why (The value it provides) |
| :--- | :--- | :--- |
| **1** | **As a user, I want to see a simple welcome screen with clear options** | Creates a proper entry point to the application, guiding the user's journey from the start. |
| **2** | **As a user, I want to be able to choose from a list of conversation topics or a "free talk" mode** | This is a major step in pedagogical value. It allows users to target their practice to specific, real-world scenarios, dramatically increasing the app's utility. |
| **3** | **As a user, I want to see helpful conversation prompts on the whiteboard if I pause for too long** | Enhances the user experience by preventing "dead air" and helping learners who are unsure of what to say next, especially within a specific topic. |
| **4** | **As a user, I want to be able to interrupt the AI tutor while it's speaking** | This is a key quality-of-life improvement that makes the conversation feel significantly more natural and less robotic. |

**Outcome of Phase 2:** A true learning tool. Users can now select a lesson like "Ordering Coffee," get relevant prompts, and practice a specific scenario while still receiving the core color-coded feedback.

---

### **Phase 3: Unlocking Deep, Actionable Feedback**

**Goal:** Implement the "Professor's Notes" feature. This is where the application goes from showing the user *what* they did wrong to explaining *why* and *how* to fix it.

| Priority | User Story (What the user wants) | Why (The value it provides) |
| :--- | :--- | :--- |
| **1** | **As a user, I want to be able to click on a poorly pronounced (yellow or red) word in the transcript** | This provides the interaction mechanism to access deeper feedback. It makes the color-coded words interactive. |
| **2** | **When I click an error word, I want to see a "feedback card" on the main whiteboard** | This presents the detailed feedback in a focused, non-cluttered way, making it easy for the user to digest. |
| **3** | **On the feedback card, I want to read a simple, plain-language explanation of my error** | This is the brain of the feature. It translates complex Azure data into simple, actionable advice, which is the core teaching moment. |
| **4** | **On the feedback card, I want to be able to play back my own audio and the correct native audio for a word** | A powerful learning tool that enables users to self-diagnose by directly comparing their pronunciation with a native speaker's. |
| **5** | **As a user, I want the option to start a quick practice drill for a specific word or sound directly from the feedback card** | Closes the learning loop by immediately providing a tool to practice and correct the identified weakness. |

**Outcome of Phase 3:** A comprehensive tutoring system. The user can now fully understand their mistakes and is given the tools to actively correct them, completing the entire "Identify -> Understand -> Practice -> Improve" cycle.

---

### **Phase 4 & Beyond: Polish, Motivation, and Retention**

**Goal:** With the core product complete, these features focus on long-term user engagement, motivation, and creating a more polished and professional experience.

| Priority | User Story (What the user wants) | Why (The value it provides) |
| :--- | :--- | :--- |
| **1** | **As a user, I want to receive a summary at the end of each session that highlights my achievements and suggests future goals** | Provides a sense of accomplishment and a clear path forward, encouraging the user to return for another session. |
| **2** | **As a user, I want to view a simple dashboard with my historical progress on key metrics (e.g., accuracy, fluency)** | Gamifies the learning process and provides powerful motivation by visually showing the user that their hard work is paying off. |
| **3** | **As a user, I want the words spoken by the AI tutor to also appear in the transcript** | A useful feature for completeness, allowing users to review the entire conversation, including model phrases they might want to learn. |

This prioritized roadmap provides a clear and efficient path to building your AI English Tutor. It ensures that with each major phase, you deliver a significant and tangible increase in value to the end-user. Good luck with the development