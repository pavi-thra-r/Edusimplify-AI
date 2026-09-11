# 🎓 EduSimplify AI

## Personalized Course Content Simplification Agent

EduSimplify AI is an AI-powered educational application designed to transform complex academic content into simple, structured, and personalized learning material.

The application allows students to provide academic content through text or PDF documents and customize the generated explanation according to their **learning level, preferred language, and explanation style**.

---

## 📌 Problem Statement

### Course Content Simplification Agent

Educational materials can often contain complex terminology, technical explanations, and dense information that may be difficult for students with different learning backgrounds and proficiency levels.

EduSimplify AI addresses this challenge by analyzing academic content and reframing it into easier, structured explanations based on the learner's selected proficiency level.

The system aims to support more **personalized, accessible, and inclusive learning**.

---

# 🎯 Objectives

The main objectives of EduSimplify AI are:

- Simplify complex academic concepts.
- Adapt explanations according to learner proficiency.
- Support multilingual learning.
- Provide real-world analogies.
- Provide practical examples.
- Highlight important terminology.
- Generate examination-focused points.
- Create quick revision material.
- Generate MCQ-based quizzes.
- Support academic PDF documents.
- Provide downloadable learning notes.

---

# ✨ Key Features

## 📚 1. Text-Based Learning

Students can directly enter or paste academic content into the application.

The system analyzes the provided content and generates structured learning material.

---

## 📄 2. PDF-Based Learning

Students can upload academic PDF documents.

The application extracts the text from the PDF and processes the content to generate simplified learning material.

---

## 🎓 3. Personalized Learning Levels

The application provides three learning levels:

### Beginner

Designed for students who are new to the topic.

The explanation focuses on:

- Simple language
- Basic concepts
- Easy examples
- Real-world analogies

### Intermediate

Designed for students who have basic knowledge of the topic.

The explanation provides:

- Moderate technical detail
- Clear concepts
- Practical examples
- Important terminology

### Advanced

Designed for students who already have knowledge of the topic.

The explanation provides:

- More technical detail
- Deeper conceptual understanding
- Technical terminology
- Detailed examples

---

# 🌐 Multilingual Learning

EduSimplify AI supports multiple languages to make learning content more accessible.

Currently supported languages include:

- 🇬🇧 English
- 🇮🇳 Kannada
- 🇮🇳 Hindi
- 🇮🇳 Tamil
- 🇮🇳 Telugu

Students can select their preferred output language before generating the learning material.

---

# 📝 Explanation Styles

Students can choose the style in which the content should be explained.

### Simple and Clear

Focuses on easy-to-understand explanations.

### Detailed

Provides deeper explanations with additional conceptual information.

### Exam Preparation

Focuses on important points that can help students prepare for examinations.

---

# 🤖 AI-Generated Learning Material

EduSimplify AI generates structured learning material containing:

1. **Simple Explanation**
2. **Real-World Analogy**
3. **Key Concepts**
4. **Important Terminology**
5. **Practical Example**
6. **Exam Points**
7. **Quick Revision**
8. **5 MCQ Quiz with Answers**
9. **One-Line Summary**

This converts unstructured academic information into a more useful learning format.

---

# 🏗️ System Architecture

```text
                         STUDENT
                            │
                            ▼
                 ┌────────────────────┐
                 │   Academic Input   │
                 │                    │
                 │     Text / PDF     │
                 └─────────┬──────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   PDF Processing   │
                 │                    │
                 │  Text Extraction   │
                 └─────────┬──────────┘
                           │
                           ▼
              ┌──────────────────────────┐
              │   Learning Preferences   │
              │                          │
              │  • Learning Level        │
              │  • Language              │
              │  • Explanation Style     │
              └────────────┬─────────────┘
                           │
                           ▼
                 ┌────────────────────┐
                 │   AI Processing    │
                 │                    │
                 │ Content Analysis &  │
                 │ Simplification     │
                 └─────────┬──────────┘
                           │
                           ▼
             ┌─────────────────────────────┐
             │ Personalized Learning       │
             │ Material                    │
             │                             │
             │ • Explanation               │
             │ • Analogy                   │
             │ • Key Concepts              │
             │ • Terminology               │
             │ • Examples                  │
             │ • Exam Points               │
             │ • Quick Revision            │
             │ • MCQ Quiz                  │
             │ • Summary                   │
             └──────────────┬──────────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Downloadable Notes│
                  └───────────────────┘
