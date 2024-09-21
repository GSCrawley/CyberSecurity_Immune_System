# Security_Guard

## Project Overview
Security_Guard is a cybersecurity threat intelligence system using AI agents and a Digital Genome structure. It aims to gather, analyze, and compile cybersecurity threat intelligence while being cost-effective during the development phase.

## Current Progress

1. Project Structure
   - Created a comprehensive file structure for the project, separating concerns into different modules (agents, managers, services, etc.).
   - This structure allows for better organization and scalability as the project grows.

2. Dependency Management
   - Set up `pyproject.toml` for managing project dependencies using Poetry.
   - Chose Poetry for its simplicity in managing virtual environments and dependencies.

3. Configuration Management
   - Created `config.py` using Pydantic's BaseSettings for configuration management.
   - This approach allows easy loading of environment variables and provides type checking for configuration values.

4. Cost-Conscious Approach
   - Shifted from using expensive LLM API calls to a more cost-effective approach using open-source models and traditional NLP techniques.
   - This decision was made to minimize token usage and associated costs during the initial development phase.

5. FastAPI Application Setup
   - Set up a basic FastAPI application in `main.py`.
   - Implemented CORS middleware for cross-origin requests.
   - Created placeholder routes for adding and retrieving threat intelligence.

6. Service Structure
   - Created placeholder files for OSINT and Analysis services.
   - These services will be implemented using cost-effective methods rather than relying on expensive LLM calls.

7. Database Integration
   - Prepared for Neo4j integration by setting up configuration variables.
   - Actual implementation of database operations is pending.

## Next Steps
- Implement OSINT gathering logic using web scraping and API calls to free threat intelligence platforms.
- Develop threat analysis logic using open-source NLP models and traditional techniques.
- Integrate Neo4j database for storing and retrieving threat intelligence data.
- Expand API endpoints to cover more functionality.
- Implement authentication and authorization for API endpoints.

## Why These Decisions Were Made
- The project structure and dependency management choices were made to ensure scalability and maintainability of the codebase.
- The shift to a cost-conscious approach allows for development and testing of core functionalities without incurring high API costs.
- FastAPI was chosen for its speed, ease of use, and built-in support for API documentation.
- The service-based architecture allows for easy expansion and modification of individual components without affecting the entire system.
- Neo4j was selected as the database due to its graph structure, which is well-suited for representing complex relationships in threat intelligence data.

This project is still in its early stages, with basic structures and placeholders in place. The focus is on building a solid foundation that can be easily expanded and optimized in the future.# CyberSecurity_Immune_System
