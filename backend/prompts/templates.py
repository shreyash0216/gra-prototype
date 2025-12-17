from typing import Dict, List, Any, Optional
import json

class PromptManager:
    def __init__(self):
        self.templates = {
            'default': self._default_template,
            'analytical': self._analytical_template,
            'creative': self._creative_template,
            'technical': self._technical_template,
            'summarization': self._summarization_template
        }
    
    def get_available_templates(self) -> List[str]:
        """Get list of available prompt templates"""
        return list(self.templates.keys())
    
    def generate_response(self, query: str, context: List[Dict[str, Any]], 
                         template_type: str = 'default', 
                         additional_context: Optional[str] = None) -> str:
        """Generate a response using the specified template"""
        if template_type not in self.templates:
            template_type = 'default'
        
        return self.templates[template_type](query, context, additional_context)
    
    def _format_context(self, context: List[Dict[str, Any]]) -> str:
        """Format retrieved context for inclusion in prompts"""
        if not context:
            return "No relevant context found."
        
        formatted_context = []
        for i, doc in enumerate(context, 1):
            content = doc.get('content', '')
            metadata = doc.get('metadata', {})
            source = metadata.get('source', 'unknown')
            
            formatted_context.append(f"[Context {i}] (Source: {source})\n{content}")
        
        return "\n\n".join(formatted_context)
    
    def _default_template(self, query: str, context: List[Dict[str, Any]], 
                         additional_context: Optional[str] = None) -> str:
        """Default response template"""
        formatted_context = self._format_context(context)
        
        prompt = f"""Based on the following context, please answer the user's question accurately and helpfully.

Context:
{formatted_context}

{f"Additional Context: {additional_context}" if additional_context else ""}

User Question: {query}

Please provide a clear, accurate response based on the available context. If the context doesn't contain enough information to fully answer the question, please indicate what information is missing."""

        # Simulate LLM response (in a real implementation, this would call an actual LLM)
        return self._simulate_llm_response(prompt, "default")
    
    def _analytical_template(self, query: str, context: List[Dict[str, Any]], 
                           additional_context: Optional[str] = None) -> str:
        """Analytical response template for data-driven queries"""
        formatted_context = self._format_context(context)
        
        prompt = f"""Analyze the following information and provide a structured, data-driven response to the user's question.

Context for Analysis:
{formatted_context}

{f"Additional Context: {additional_context}" if additional_context else ""}

Question to Analyze: {query}

Please provide:
1. Key findings from the available data
2. Relevant patterns or trends
3. Limitations of the current information
4. Actionable insights or recommendations"""

        return self._simulate_llm_response(prompt, "analytical")
    
    def _creative_template(self, query: str, context: List[Dict[str, Any]], 
                          additional_context: Optional[str] = None) -> str:
        """Creative response template for brainstorming and ideation"""
        formatted_context = self._format_context(context)
        
        prompt = f"""Using the provided context as inspiration, generate creative and innovative responses to the user's request.

Inspirational Context:
{formatted_context}

{f"Additional Context: {additional_context}" if additional_context else ""}

Creative Challenge: {query}

Please provide multiple creative approaches, considering:
- Novel combinations of existing ideas
- Alternative perspectives
- Innovative solutions
- Creative applications"""

        return self._simulate_llm_response(prompt, "creative")
    
    def _technical_template(self, query: str, context: List[Dict[str, Any]], 
                           additional_context: Optional[str] = None) -> str:
        """Technical response template for implementation details"""
        formatted_context = self._format_context(context)
        
        prompt = f"""Provide a detailed technical response based on the following documentation and context.

Technical Documentation:
{formatted_context}

{f"Additional Context: {additional_context}" if additional_context else ""}

Technical Query: {query}

Please include:
- Step-by-step implementation details
- Code examples where applicable
- Best practices and considerations
- Potential challenges and solutions
- Performance implications"""

        return self._simulate_llm_response(prompt, "technical")
    
    def _summarization_template(self, query: str, context: List[Dict[str, Any]], 
                               additional_context: Optional[str] = None) -> str:
        """Summarization template for condensing information"""
        formatted_context = self._format_context(context)
        
        prompt = f"""Summarize the following information in response to the user's request.

Information to Summarize:
{formatted_context}

{f"Additional Context: {additional_context}" if additional_context else ""}

Summarization Request: {query}

Please provide:
- Key points and main themes
- Important details and facts
- Concise overview
- Relevant conclusions"""

        return self._simulate_llm_response(prompt, "summarization")
    
    def _simulate_llm_response(self, prompt: str, template_type: str) -> str:
        """Simulate LLM response (replace with actual LLM call in production)"""
        # This is a placeholder - in a real implementation, you would call an actual LLM API
        responses = {
            "default": "Based on the provided context, I can help answer your question. This is a simulated response that would normally be generated by a language model using the formatted prompt and context.",
            "analytical": "Analysis shows several key patterns in the data. The main findings indicate... [This would be a detailed analytical response based on the context]",
            "creative": "Here are several creative approaches to consider: 1) Novel combination approach... 2) Alternative perspective... 3) Innovative solution... [Creative ideas would be generated here]",
            "technical": "Technical implementation details: Step 1: Initialize the system... Step 2: Configure parameters... [Detailed technical guidance would be provided]",
            "summarization": "Summary of key points: • Main theme 1... • Important detail 2... • Conclusion... [Concise summary would be generated]"
        }
        
        return responses.get(template_type, responses["default"])